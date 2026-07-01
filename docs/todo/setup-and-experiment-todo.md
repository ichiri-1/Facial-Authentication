# 環境構築・データセット配置・実験準備 TODO

顔認証プロジェクト（CNN vs Vision Transformer）の次に行うべき作業を整理する。

## 基本方針（決定事項）

- **データセット**: まずは最小構成。normal=**LFW** を軸に、occluded=**MLFW**(LFWベース)、low_resolution=LFW画像の縮小→再拡大で人工生成。申請不要で早く回せることを優先。実データの遮蔽/低解像度(WebFace-OCC/SCface/TinyFace)は後の拡張候補。
- **検証プロトコル**: **verification (1:1ペア照合)** を主とする。埋め込みベースで cosine similarity を算出し、ROC-AUC / EER / TAR@FAR で normal/occluded/low_resolution の頑健性を比較。
- **モデル**: CNN(ResNet18/50) vs ViT(ViT-Tiny/Small, DeiT-Tiny)。timm の事前学習を利用し、公平比較のため入力サイズ・epoch・optimizer・lr・augmentation・分割を共通化。
- **ストレージ制約**: `/` は空きが逼迫。データ・モデル重み・出力・キャッシュはすべて `/storage` 配下（本プロジェクトは既に `/storage/nogi/ibunya/Facial-Authentication`）。

## 環境の現状

- `torch 2.6.0+cu124` / CUDA 12.4 / GPU 2枚（NVIDIA RTX A4500）認識OK、`.venv` 構築済み。
- `docs/agent/` の一部（data-catalog.md, analysis-workflow.md など）は汎用テンプレートのまま未記入。
- `src/facial_authentication/`、`configs/*.yaml`、`scripts/train.py`・`evaluate.py`・`prepare_dataset.py`・`make_robustness_sets.py` は未作成。

---

## フェーズ1: 基盤整備（コード骨格）

- [ ] 1-1. `src/facial_authentication/paths.py` 実装（`get_repo_root/data_dir/outputs_dir/ensure_parent_dir`）。後続スクリプトの依存。
- [ ] 1-2. `pyproject.toml` 整備（`[tool.ruff]`/`[tool.mypy]`/`[tool.pytest]` 設定と dev グループを `uv add --group dev` で追加）。
- [ ] 1-3. `docs/agent/data-catalog.md` を顔認証用に書き換え（Titanicテンプレを破棄し LFW/MLFW のパス・ライセンス・利用条件・被験者数を記載）。

## フェーズ2: データ配置（LFW軸・verification）

- [ ] 2-1. LFW 取得（`/storage` 配下の `data/raw/lfw/` に展開）。標準の pairs.txt（10-fold検証ペア）も取得。gitignore済み確認。
- [ ] 2-2. ライセンス確認（研究利用可否・レポート画像掲載可否を data-catalog.md に記録）。
- [ ] 2-3. 分割定義（verification前提で標準 pairs プロトコルを採用。学習用は人物単位で train/val を分離し、同一人物が train と test に跨がらないようにリーク防止）。

## フェーズ3: 前処理・条件生成

- [ ] 3-1. `prepare_dataset.py`（顔検出/アラインメント、または LFW-funneled/deepfunneled 利用）→ `data/processed/normal/`。
- [ ] 3-2. `make_robustness_sets.py`（test側のnormal画像から生成）
  - occluded: mask / sunglasses / random-rect / eye / mouth 遮蔽（MLFW併用検討）
  - low_resolution: downscale→upscale
  - → `data/processed/{occluded,low_resolution}/`

## フェーズ4: モデル・評価（埋め込みベース）

- [ ] 4-1. `configs/*.yaml`（resnet18/50, vit_tiny/small, deit_tiny）。入力サイズ・pretrained・epoch・optimizer・lr・batch・augmentation・分割を共通化（公平比較）。
- [ ] 4-2. `src/` モジュール（`datasets.py / models.py(timm) / transforms.py / train_loop.py / metrics.py / utils.py`）。埋め込み抽出 + cosine similarity を中核に。
- [ ] 4-3. `scripts/train.py`（分類 or metric-learning で学習、checkpoint→`outputs/checkpoints/`）。
- [ ] 4-4. `scripts/evaluate.py`（ペア照合で ROC-AUC / EER / TAR@FAR / cosine類似度分布 を条件別に算出→`outputs/metrics/`）。
- [ ] 4-5. `docs/agent/metrics-and-definitions.md` に上記指標の定義を記入。

## フェーズ5: 動作確認・品質

- [ ] 5-1. スモークテスト（1モデル×少数epoch×小サブセットで train→eval 貫通、GPU(A4500×2)・保存パス検証）。
- [ ] 5-2. `tests/` 追加（dataset shape / transform / EER・TAR@FAR 計算の単体テスト）。
- [ ] 5-3. 品質チェック（`bash scripts/run_quality_checks.sh` で ruff/mypy/pytest 通過）。

---

## 最優先の着手順（推奨）

1. 1-1 paths.py + 1-2 pyproject 整備（他すべての土台）
2. 2-1 LFW取得 + pairs（/storage配下）
3. 4-4 の評価指標コア（EER/TAR@FAR）を先に単体実装し、5-1 スモークまで最短で貫通させる
