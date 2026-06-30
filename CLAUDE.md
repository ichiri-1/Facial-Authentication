# CLAUDE.md

このリポジトリは、**Python 3.11 / uv / PyTorch / CUDA 12.4** を用いた顔認証モデル比較プロジェクトです。

本プロジェクトでは、CNN系モデルとVision Transformer系モデルを用いて、顔認証における性能・精度・頑健性の違いを比較します。

詳細な作業手順は `.claude/skills/*/SKILL.md` に記述します。
プロジェクト固有の背景・実験設計・データセット方針・評価指標は `docs/agent/*` に記述します。

---

## Project Overview

本プロジェクトのテーマは以下です。

> CNNとVision Transformerによる顔認証性能の比較

具体的には、以下の条件でCNN系モデルとVision Transformer系モデルを比較します。

1. 顔が完全に見えている通常顔画像
2. マスク・サングラス・ランダム遮蔽などにより、顔の一部が隠れている画像
3. 遠距離または低解像度により、顔情報が劣化している画像

主な目的は、通常条件だけでなく、遮蔽や低解像度といった実利用に近い条件で、CNNとVision Transformerの認証精度や頑健性がどのように異なるかを調査することです。

余裕があれば、顔認証モデルが出力する特徴量ベクトルと、個人識別・プライバシー・セキュリティ上のリスクとの関係についても考察します。

---

## Hard Rules

以下のルールは常に適用してください。

* Pythonの依存関係管理には **uvのみ** を使用する。
* `pip`、`pip3`、`python -m pip`、`conda`、`poetry`、`pipenv`、`easy_install` は使用しない。
* rawデータ、顔画像データセット、認証情報、APIキー、トークン、個人識別情報をGitにコミットしない。
* `data/raw/` と `data/external/` は不変データとして扱い、直接変更・上書き・削除しない。
* 加工データは `data/interim/` または `data/processed/` に出力する。
* 顔画像は個人識別情報を含む可能性があるため、必要以上に読み込んだり表示したりしない。
* Claude Codeで顔画像そのものを不用意に読み取らない。
* 実験条件を変更する場合は、設定ファイルまたはドキュメントに明記する。
* 非自明な分析判断を行う前に、前提や仮定を説明する。
* データの意味やラベル定義が不明確な場合は、確認または保守的な仮定を置く。
* 変更は小さく、レビューしやすい単位で行う。
* レポート、説明文、コメント、ドキュメントは原則として日本語で記述する。
* コード、コマンド、ファイル名、設定キー、ライブラリ名は英語のまま扱う。

---

## Environment

想定する実行環境は以下です。

* Python: 3.11
* Package manager: uv
* GPU: CUDA 12.4
* Deep learning framework: PyTorch
* Main libraries:

  * torch
  * torchvision
  * timm
  * numpy
  * polars
  * scikit-learn
  * opencv-python
  * pillow
  * matplotlib
  * tqdm
  * pyyaml

---

## Package Management

依存関係管理には必ず `uv` を使用してください。

### 使用してよいコマンド

```bash
uv sync
uv add <package>
uv add --group dev <package>
uv run python <script>
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy src
```

### 使用禁止

```bash
pip install <package>
pip3 install <package>
python -m pip install <package>
conda install <package>
poetry add <package>
pipenv install <package>
```

---

## Common Commands

環境構築:

```bash
uv sync
```

CUDA確認:

```bash
uv run python scripts/check_cuda.py
```

テスト:

```bash
uv run pytest
```

リント:

```bash
uv run ruff check .
```

フォーマット:

```bash
uv run ruff format .
```

型チェック:

```bash
uv run mypy src
```

rawデータや秘密情報のコミットチェック:

```bash
uv run python scripts/check_no_raw_data_commit.py
uv run python scripts/check_no_sensitive_patterns.py
```

学習:

```bash
uv run python scripts/train.py --config configs/resnet18.yaml
```

評価:

```bash
uv run python scripts/evaluate.py --config configs/resnet18.yaml
```

---

## Repository Structure

想定するディレクトリ構成は以下です。

```text
.
├── CLAUDE.md
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .claude/
│   ├── settings.json
│   ├── settings.local.json
│   ├── commands/
│   │   ├── run-train.md
│   │   ├── run-eval.md
│   │   └── summarize-result.md
│   └── skills/
├── configs/
│   ├── resnet18.yaml
│   ├── resnet50.yaml
│   ├── vit_tiny.yaml
│   └── vit_small.yaml
├── docs/
│   └── agent/
│       ├── project-overview.md
│       ├── repository-structure.md
│       ├── data-catalog.md
│       ├── metrics-and-definitions.md
│       ├── analysis-workflow.md
│       ├── statistical-and-ml-guidelines.md
│       ├── validation-and-testing.md
│       ├── reporting-guidelines.md
│       ├── security-and-privacy.md
│       └── agent-behavior.md
├── data/
│   ├── raw/
│   ├── external/
│   ├── interim/
│   └── processed/
├── notebooks/
├── outputs/
│   ├── checkpoints/
│   ├── logs/
│   ├── metrics/
│   ├── figures/
│   ├── tables/
│   └── reports/
├── scripts/
│   ├── check_cuda.py
│   ├── prepare_dataset.py
│   ├── make_robustness_sets.py
│   ├── train.py
│   ├── evaluate.py
│   ├── check_no_raw_data_commit.py
│   └── check_no_sensitive_patterns.py
├── src/
│   └── facial_authentication/
│       ├── __init__.py
│       ├── datasets.py
│       ├── models.py
│       ├── train_loop.py
│       ├── metrics.py
│       ├── transforms.py
│       └── utils.py
└── tests/
```

---

## Data Safety

顔画像データは個人識別情報を含む可能性があるため、通常のデータ分析プロジェクトよりも慎重に扱ってください。

### 基本方針

* `data/raw/` と `data/external/` は不変データとして扱う。
* rawデータを直接変更しない。
* rawデータをGitにコミットしない。
* 顔画像を不用意にNotebookやログに出力しない。
* 画像例をレポートに掲載する場合は、利用規約やライセンスを確認する。
* データセットの利用条件を `docs/agent/data-catalog.md` に記録する。
* データセットの取得元、ライセンス、使用条件、前処理方法を記録する。

### データ保存先

* 生データ: `data/raw/`
* 外部配布データ: `data/external/`
* 中間加工データ: `data/interim/`
* 最終加工データ: `data/processed/`
* 実験結果: `outputs/`
* グラフ・図: `outputs/figures/`
* 評価指標: `outputs/metrics/`
* レポート: `outputs/reports/`

---

## Dataset Policy

使用するデータセットは、研究・教育目的で利用可能なオープンデータセットを基本とします。

候補データセットは以下です。

### 通常顔

* CelebA
* LFW
* CASIA-WebFace

### 遮蔽顔

* AR Face
* ROF
* RMFD
* MLFW
* WebFace-OCC

### 遠距離・低解像度顔

* SCface
* TinyFace
* QMUL-SurvFace

各データセットについて、以下を確認してください。

* 研究・教育目的で利用可能か
* 申請が必要か
* 再配布が禁止されていないか
* レポートへの画像掲載が可能か
* 個人識別情報として慎重に扱う必要があるか

---

## Experimental Design

基本実験は以下の流れで行います。

1. データセットの選定
2. データ利用条件の確認
3. 顔画像の前処理
4. 通常顔条件の作成
5. 遮蔽条件の作成
6. 低解像度・遠距離条件の作成
7. CNN系モデルの学習
8. Vision Transformer系モデルの学習
9. 通常顔での評価
10. 遮蔽顔での評価
11. 低解像度・遠距離顔での評価
12. 条件別の精度低下を比較
13. 結果を図表化
14. セキュリティ・プライバシー観点で考察

---

## Models

比較対象モデルは以下を基本とします。

### CNN

* ResNet18
* ResNet50

### Vision Transformer

* ViT-Tiny
* ViT-Small
* DeiT-Tiny

モデルを追加する場合は、比較の公平性を保つため、以下を確認してください。

* 入力画像サイズ
* 事前学習の有無
* 学習エポック数
* optimizer
* learning rate
* batch size
* data augmentation
* 評価指標
* 学習データと評価データの分割

---

## Evaluation Conditions

評価条件は以下の3つを基本とします。

### 1. normal

顔全体が見えている通常顔画像。
ベースライン条件として扱います。

### 2. occluded

顔の一部が隠れている画像。
以下のような条件を想定します。

* mask
* sunglasses
* random rectangle occlusion
* eye-region occlusion
* mouth-region occlusion

### 3. low_resolution

顔が遠くに写っている、または低解像度になっている画像。
実データセットが使用できない場合は、通常顔画像を縮小して再拡大することで人工的に作成します。

---

## Metrics

最初に使用する評価指標は以下です。

* Accuracy
* Top-1 Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

余裕があれば、顔認証らしい評価として以下も使用します。

* Cosine similarity
* ROC-AUC
* EER
* TAR@FAR
* FAR
* FRR

指標の定義は `docs/agent/metrics-and-definitions.md` に記述してください。

---

## Key Conventions

### Python

* 型ヒントを付ける。
* Google-style docstringを使用する。
* コメントは日本語で書く。
* ファイルパスは `pathlib.Path` を使用する。
* 絶対ローカルパスを書かない。
* 実験設定はYAMLで管理する。
* データセットパスをPythonコードに直接埋め込まない。

### DataFrame

* DataFrame操作では、原則として `polars` を優先する。
* 必要な場合のみ `pandas` を使用する。

### Visualization

* `plt.figure(...)` ではなく、`fig, ax = plt.subplots(...)` を使用する。
* 図は `outputs/figures/` に保存する。
* レポートで使えるように、軸ラベル・凡例・タイトルを明確にする。

### Documentation

* ドキュメントは日本語で書く。
* コード、コマンド、ファイルパス、設定キーは英語のままにする。
* 技術用語は無理に翻訳しない。
* 実験条件、前処理、評価指標、結果の解釈を明確に書く。

---

## File-Specific Guidelines

### Python files (`**/*.py`)

* `python-style` skillに従う。
* 型ヒントを付ける。
* Google-style docstringを使用する。
* コメントは日本語で書く。
* `pathlib.Path` を使用する。
* 不要な副作用を避ける。
* 学習、評価、データ前処理を分離する。

### Config files (`configs/**/*.yaml`)

* 実験条件を明示する。
* モデル名、データセット、入力サイズ、batch size、learning rate、epoch数を記述する。
* 出力先を明示する。
* 実験を再現できる情報を含める。

### Data files (`data/**`)

* `data/raw/` と `data/external/` の実データは変更・削除・コミットしない。
* `data/interim/` と `data/processed/` への書き出しは許可する。
* 大きなデータファイルはGitにコミットしない。
* `.gitkeep`、README、markdownなどの説明ファイルのみコミット可能とする。

### Notebooks (`**/*.ipynb`, `notebooks/**/*.md`)

* clean kernelから再実行できるようにする。
* 出力に秘密情報や大量の顔画像を残さない。
* 実験の一時確認に使い、最終的な処理は `scripts/` または `src/` に移す。

### Documentation (`README.md`, `docs/**/*.md`)

* 明確な日本語で書く。
* 実験目的、使用データ、評価指標、前処理、結果を記録する。
* コードスニペット、コマンド、ファイルパス、設定値は英語のまま扱う。

---

## Skill Routing

| Task                          | Skill                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 依存関係、テスト、リント、型チェック、Notebook実行 | [python-project-ops](.claude/skills/python-project-ops/SKILL.md)                                                      |
| データファイルの読み書き・移動               | [safe-data-handling](.claude/skills/safe-data-handling/SKILL.md) + [path-and-io](.claude/skills/path-and-io/SKILL.md) |
| Pythonコードの作成・レビュー             | [python-style](.claude/skills/python-style/SKILL.md)                                                                  |
| DataFrame操作                   | [dataframe-polars](.claude/skills/dataframe-polars/SKILL.md)                                                          |
| グラフ・可視化                       | [visualization](.claude/skills/visualization/SKILL.md)                                                                |
| Notebook作成・編集                 | [notebook-workflow](.claude/skills/notebook-workflow/SKILL.md)                                                        |
| 統計・機械学習・モデル評価                 | [statistical-ml-review](.claude/skills/statistical-ml-review/SKILL.md)                                                |
| 分析結果・レポート作成                   | [analysis-reporting](.claude/skills/analysis-reporting/SKILL.md)                                                      |
| ファイルパスとI/O                    | [path-and-io](.claude/skills/path-and-io/SKILL.md)                                                                    |

---

## Project Context

| Document                                                                        | Purpose                      |
| ------------------------------------------------------------------------------- | ---------------------------- |
| [project-overview.md](docs/agent/project-overview.md)                           | プロジェクトの目的とスコープ               |
| [repository-structure.md](docs/agent/repository-structure.md)                   | ディレクトリ構成                     |
| [data-catalog.md](docs/agent/data-catalog.md)                                   | データセット一覧、利用条件、前処理方針          |
| [metrics-and-definitions.md](docs/agent/metrics-and-definitions.md)             | 評価指標の定義                      |
| [analysis-workflow.md](docs/agent/analysis-workflow.md)                         | 実験・分析ワークフロー                  |
| [statistical-and-ml-guidelines.md](docs/agent/statistical-and-ml-guidelines.md) | 統計・MLガイドライン                  |
| [validation-and-testing.md](docs/agent/validation-and-testing.md)               | テスト・検証方針                     |
| [reporting-guidelines.md](docs/agent/reporting-guidelines.md)                   | レポート作成方針                     |
| [security-and-privacy.md](docs/agent/security-and-privacy.md)                   | 顔認証・特徴量ベクトルに関するセキュリティとプライバシー |
| [agent-behavior.md](docs/agent/agent-behavior.md)                               | Claude Codeの行動指針             |

---

## Report Direction

最終レポートでは、以下の観点を中心にまとめます。

* CNNとVision Transformerの通常顔に対する性能差
* 遮蔽条件での性能低下
* 遠距離・低解像度条件での性能低下
* CNNとVision Transformerの頑健性の違い
* 特徴量ベクトルと個人識別に関するセキュリティ・プライバシー上の考察
* 実験上の制約
* 今後の課題

---

## References

* Marcos Rodrigo, Carlos Cuevas, and Narciso García, “Comprehensive comparison between vision transformers and convolutional neural networks for face recognition tasks,” Scientific Reports, 14, 21392, 2024.

---

## Skills

@.claude/skills/python-project-ops/SKILL.md
@.claude/skills/python-style/SKILL.md
@.claude/skills/dataframe-polars/SKILL.md
@.claude/skills/path-and-io/SKILL.md
@.claude/skills/safe-data-handling/SKILL.md
@.claude/skills/notebook-workflow/SKILL.md
@.claude/skills/statistical-ml-review/SKILL.md
@.claude/skills/visualization/SKILL.md
@.claude/skills/analysis-reporting/SKILL.md
