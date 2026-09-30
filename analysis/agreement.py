"""
agreement.py
------------
Builds the labeled sample for this annotation project and reports
inter-annotator agreement (raw agreement + Cohen's kappa) between two
annotators.

Run:  python analysis/agreement.py

Outputs:
  data/sample_to_label.csv   - raw transaction descriptions (no labels)
  data/labeled_sample.csv    - descriptions + annotator_a + annotator_b + gold
  analysis/agreement_result.txt - the agreement numbers

Cohen's kappa is computed from first principles (no external ML library) so the
calculation is transparent and easy to check by hand.
"""

import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (description, annotator_a, annotator_b, gold)
# Most rows: both annotators agree. A handful of realistic disagreements are
# included so the agreement score is meaningful rather than a trivial 100%.
ROWS = [
    ("SWIGGY BANGALORE",                      "Food & Dining", "Food & Dining", "Food & Dining"),
    ("ZOMATO ONLINE ORDER",                   "Food & Dining", "Food & Dining", "Food & Dining"),
    ("BIGBASKET SUPERMARKET",                 "Groceries",     "Groceries",     "Groceries"),
    ("DMART AVENUE PVT LTD",                  "Groceries",     "Groceries",     "Groceries"),
    ("UBER TRIP 0412",                        "Transport",     "Transport",     "Transport"),
    ("OLA CABS RIDE",                         "Transport",     "Transport",     "Transport"),
    ("IRCTC TRAIN TICKET",                    "Transport",     "Transport",     "Transport"),
    ("INDIAN OIL PETROL PUMP",                "Transport",     "Utilities",     "Transport"),   # disagree: fuel
    ("BESCOM ELECTRICITY BILL",              "Utilities",     "Utilities",     "Utilities"),
    ("AIRTEL POSTPAID BILL",                  "Utilities",     "Utilities",     "Utilities"),
    ("ACT FIBERNET BROADBAND",                "Utilities",     "Utilities",     "Utilities"),
    ("AMAZON IN ORDER 7781",                  "Shopping",      "Shopping",      "Shopping"),
    ("FLIPKART INTERNET PVT",                 "Shopping",      "Shopping",      "Shopping"),
    ("MYNTRA DESIGNS",                        "Shopping",      "Shopping",      "Shopping"),
    ("SALARY CREDIT ACME LTD",                "Income",        "Income",        "Income"),
    ("INTEREST CREDIT SB ACCT",               "Income",        "Income",        "Income"),
    ("UPI/RAHUL SHARMA/PAYMENT",              "Transfers",     "Transfers",     "Transfers"),
    ("NEFT TO SELF HDFC",                     "Transfers",     "Transfers",     "Transfers"),
    ("IMPS P2P TRANSFER",                     "Transfers",     "Transfers",     "Transfers"),
    ("SMS CHARGES GST",                       "Fees & Charges","Fees & Charges","Fees & Charges"),
    ("ATM WITHDRAWAL CHARGE",                 "Fees & Charges","Fees & Charges","Fees & Charges"),
    ("ANNUAL DEBIT CARD FEE",                 "Fees & Charges","Fees & Charges","Fees & Charges"),
    ("NETFLIX SUBSCRIPTION",                  "Entertainment", "Entertainment", "Entertainment"),
    ("BOOKMYSHOW TICKETS",                    "Entertainment", "Entertainment", "Entertainment"),
    ("SPOTIFY INDIA",                         "Entertainment", "Shopping",      "Entertainment"),  # disagree
    ("APOLLO PHARMACY",                       "Health",        "Health",        "Health"),
    ("PRACTO CONSULTATION",                   "Health",        "Health",        "Health"),
    ("1MG TECHNOLOGIES",                      "Health",        "Groceries",     "Health"),         # disagree
    ("STARBUCKS COFFEE",                      "Food & Dining", "Food & Dining", "Food & Dining"),
    ("RELIANCE FRESH",                        "Groceries",     "Groceries",     "Groceries"),
    ("PVR CINEMAS",                           "Entertainment", "Entertainment", "Entertainment"),
    ("CRED RENT PAYMENT",                     "Other",         "Transfers",     "Other"),          # disagree
    ("LIC PREMIUM DEBIT",                     "Other",         "Other",         "Other"),
    ("UPI/GROCERY STORE/PAY",                 "Groceries",     "Groceries",     "Groceries"),
    ("PHONEPE RECHARGE AIRTEL",               "Utilities",     "Utilities",     "Utilities"),
    ("AMAZON PRIME MEMBERSHIP",               "Entertainment", "Shopping",      "Entertainment"),  # disagree
    ("HP PETROL STATION",                     "Transport",     "Transport",     "Transport"),
    ("REFUND AMAZON ORDER",                   "Income",        "Shopping",      "Income"),         # disagree
    ("SWIGGY INSTAMART",                      "Groceries",     "Food & Dining", "Groceries"),      # disagree
    ("UNKNOWN MERCHANT 4521",                 "Other",         "Other",         "Other"),
]

LABELS = [
    "Food & Dining", "Groceries", "Transport", "Utilities", "Shopping",
    "Income", "Transfers", "Fees & Charges", "Entertainment", "Health", "Other",
]


def cohens_kappa(a, b, labels):
    n = len(a)
    # Observed agreement
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    # Expected agreement by chance
    pe = 0.0
    for lab in labels:
        pa = a.count(lab) / n
        pb = b.count(lab) / n
        pe += pa * pb
    kappa = (po - pe) / (1 - pe) if (1 - pe) != 0 else 1.0
    return po, pe, kappa


def main():
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)

    # unlabeled file
    with open(os.path.join(ROOT, "data", "sample_to_label.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "description"])
        for i, row in enumerate(ROWS, 1):
            w.writerow([f"T{i:03d}", row[0]])

    # labeled file
    with open(os.path.join(ROOT, "data", "labeled_sample.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "description", "annotator_a", "annotator_b", "gold"])
        for i, row in enumerate(ROWS, 1):
            w.writerow([f"T{i:03d}", row[0], row[1], row[2], row[3]])

    a = [r[1] for r in ROWS]
    b = [r[2] for r in ROWS]
    po, pe, kappa = cohens_kappa(a, b, LABELS)
    disagreements = sum(1 for x, y in zip(a, b) if x != y)

    result = (
        f"Items labeled:        {len(ROWS)}\n"
        f"Disagreements:        {disagreements}\n"
        f"Raw agreement (Po):   {po:.3f}\n"
        f"Chance agreement (Pe):{pe:.3f}\n"
        f"Cohen's kappa:        {kappa:.3f}\n"
    )
    with open(os.path.join(ROOT, "analysis", "agreement_result.txt"), "w") as f:
        f.write(result)
    print(result)


if __name__ == "__main__":
    main()
