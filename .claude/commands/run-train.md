# 学習実行

指定された設定ファイルを使って、顔認証モデルの学習を実行してください。

## 参照するもの

- `CLAUDE.md`
- 対象の `configs/*.yaml`
- `scripts/train.py`
- `src/facial_authentication/models.py`
- `src/facial_authentication/train_loop.py`
- `src/facial_authentication/datasets.py`

## 実行例

```bash
uv run python scripts/train.py --config configs/resnet18.yaml
```

## 確認事項
- uv を使って実行しているか
- GPUが利用可能か
- seedが固定されているか
- batch sizeがGPUメモリに対して妥当か
- 出力先が outputs/ 以下になっているか
- rawデータを直接変更していないか

## 学習後に確認すること
- checkpointが outputs/checkpoints/ に保存されているか
- logが outputs/logs/ に保存されているか
- metricsが outputs/metrics/ に保存されているか
- 使用したconfigが結果と対応付けられているか

## 出力する要約
- 実験名
- モデル名
- データセット
- 学習条件
- 最終epoch
- train loss
- validation accuracy
- 気になる点
- 次に行うべき評価