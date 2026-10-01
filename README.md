# Annotation Guidelines Toolkit - Transaction Categorization

A complete, small data-annotation project: a **guidelines document**, a **hand-labeled sample dataset**, and an **inter-annotator agreement** check. It shows annotation from the side that matters most for quality - writing the rules that make labeling consistent, then measuring whether they worked.

The task: read a bank/UPI transaction description (e.g. `SWIGGY INSTAMART`, `BESCOM ELECTRICITY BILL`) and assign one of 11 spending categories. I chose this task because clean, consistently-labeled transaction data is exactly what fintech and finance annotation projects need, and it's a domain I know from years of bookkeeping.

## What's inside

| File | What it is |
|---|---|
| [`guidelines/annotation-guidelines.md`](guidelines/annotation-guidelines.md) | The label set, decision rules, and edge-case rulings annotators follow |
| [`data/sample_to_label.csv`](data/sample_to_label.csv) | 40 raw transaction descriptions, unlabeled |
| [`data/labeled_sample.csv`](data/labeled_sample.csv) | The same 40, labeled by two annotators plus a gold label |
| [`analysis/inter-annotator-agreement.md`](analysis/inter-annotator-agreement.md) | The agreement result and what it means |
| [`analysis/agreement.py`](analysis/agreement.py) | Builds the data and computes Cohen's kappa |
| [`CHANGELOG.md`](CHANGELOG.md) | How the guidelines tightened over three versions |

## Headline result

Two annotators applying v1.2 of the guidelines to 40 transactions reached **Cohen's kappa = 0.807** ("almost perfect"), with 7 disagreements - every one of which was a guideline gap that became a fixed edge-case ruling.

## The quality loop this demonstrates

```
write guidelines -> label independently -> measure agreement -> inspect disagreements -> tighten rules -> re-label
```

This is the core of reliable data labeling: the guidelines, not the annotators, are what you debug. Every disagreement is treated as a missing rule, not a mistake.

## Reproduce

```bash
python analysis/agreement.py
```

No external libraries - Cohen's kappa is computed from first principles so the math is easy to verify by hand.

---

*Independent practice project by Anuradha Rani. The transaction descriptions are synthetic examples; no real account data is used.*
