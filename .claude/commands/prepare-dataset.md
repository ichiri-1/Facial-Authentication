# データセット準備

顔認証実験に使うデータセットの準備方針を検討し、必要な前処理コードを作成してください。

## 参照するもの

- `CLAUDE.md`
- `docs/agent/data-catalog.md`
- `docs/agent/security-and-privacy.md`
- `scripts/prepare_dataset.py`
- `src/facial_authentication/datasets.py`
- `src/facial_authentication/transforms.py`

## やること

1. データセットの利用条件を確認する。
2. rawデータは直接変更しない。
3. 加工結果は `data/interim/` または `data/processed/` に保存する。
4. 学習・検証・テスト分割を再現可能にする。
5. 通常顔・遮蔽顔・低解像度顔の条件を区別できるようにする。
6. 処理内容をログまたはREADMEに残す。

## 禁止事項

- `data/raw/` と `data/external/` の実データを変更しない。
- 顔画像を大量にNotebookやログに出力しない。
- データセット本体をGitに追加しない。
- 利用規約が不明なデータセットを前提にしない。

## 出力する要約

- 使用したデータセット
- 入力ディレクトリ
- 出力ディレクトリ
- 作成した分割
- 各条件の画像数
- 注意点