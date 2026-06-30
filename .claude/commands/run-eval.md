# 評価実行

学習済みモデルを用いて、通常顔・遮蔽顔・低解像度顔の条件別評価を実行してください。

## 参照するもの

- `CLAUDE.md`
- 対象の `configs/*.yaml`
- `scripts/evaluate.py`
- `src/facial_authentication/metrics.py`
- `docs/agent/metrics-and-definitions.md`

## 実行例

```bash
uv run python scripts/evaluate.py --config configs/resnet18.yaml
```

## 評価条件

以下を分けて評価してください。

1. 通常顔
2. 遮蔽顔
3. 遠距離または低解像度顔

## 評価指標

まずは以下を確認してください。

- Accuracy
- Top-1 Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

余裕があれば以下も確認してください。

- Cosine similarity
- ROC-AUC
- EER
- TAR@FAR

## 出力する要約
- 使用したモデル
- 使用したcheckpoint
- 通常顔での精度
- 遮蔽顔での精度
- 低解像度顔での精度
- 通常顔からの精度低下率
- CNNとViTの比較に使えそうな観察