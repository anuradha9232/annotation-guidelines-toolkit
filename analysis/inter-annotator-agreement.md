# Inter-Annotator Agreement

Before trusting a labeled dataset, you check whether two annotators applying the same guidelines actually agree. If they don't, the guidelines are ambiguous - not the annotators. This is the quality-assurance step that separates a reliable dataset from a noisy one.

## Results on this sample

Computed by [`agreement.py`](agreement.py) over the 40 items in [`../data/labeled_sample.csv`](../data/labeled_sample.csv):

| Metric | Value |
|---|---|
| Items labeled | 40 |
| Disagreements | 7 |
| Raw agreement (Po) | 0.825 |
| Chance agreement (Pe) | 0.093 |
| **Cohen's kappa (kappa)** | **0.807** |

## Why kappa, not just "82.5% agreed"

Raw agreement overstates quality, because some agreement happens by luck. Cohen's kappa corrects for chance:

```
kappa = (Po - Pe) / (1 - Pe)
```

- **Po** = the share of items both annotators labeled the same (0.825).
- **Pe** = the agreement you'd expect if both were guessing with each label's frequency (0.093).

A kappa of **0.807** falls in the "substantial to almost-perfect" band - good enough to trust, with a small set of edge cases worth tightening.

| kappa range | Interpretation |
|---|---|
| < 0.20 | Poor |
| 0.21-0.40 | Fair |
| 0.41-0.60 | Moderate |
| 0.61-0.80 | Substantial |
| 0.81-1.00 | Almost perfect |

## What the 7 disagreements tell us

Every disagreement in this sample was a **guideline gap, not a careless error** - for example fuel (Transport vs Utilities), instant grocery delivery (Groceries vs Food & Dining), and media subscriptions (Entertainment vs Shopping). Each one became a fixed ruling in Section 3 of the [guidelines](../guidelines/annotation-guidelines.md). That is the loop: measure agreement -> inspect disagreements -> tighten the guidelines -> re-label. A second round with the updated rules would push kappa higher.

## Reproduce

```bash
python analysis/agreement.py
```
