# Annotation Guidelines: Transaction Category Labeling

**Task:** Read a bank/UPI transaction description and assign exactly one category.

**Version:** 1.2 (see [`../CHANGELOG.md`](../CHANGELOG.md))

These guidelines exist so that two different annotators, reading the same transaction, land on the same label. Where the raw text is ambiguous, the **decision rules** and **edge cases** below decide the answer — an annotator should never have to guess.

---

## 1. The label set

Assign **one and only one** of these 11 categories:

| Label | Use it for |
|---|---|
| **Food & Dining** | Restaurants, cafés, food-delivery of prepared meals (Swiggy, Zomato, Starbucks) |
| **Groceries** | Supermarkets, grocery delivery, daily provisions (BigBasket, DMart, Reliance Fresh, Swiggy Instamart) |
| **Transport** | Ride-hailing, fuel, public transport, train/flight tickets (Uber, Ola, petrol pumps, IRCTC) |
| **Utilities** | Electricity, water, gas, mobile, broadband, DTH bills and recharges |
| **Shopping** | General retail and e-commerce for goods (Amazon, Flipkart, Myntra) |
| **Income** | Money received: salary, interest, refunds, cashback credited in |
| **Transfers** | Person-to-person or self transfers with no goods/service (UPI to a person, NEFT to self, IMPS) |
| **Fees & Charges** | Bank fees, card fees, ATM charges, penalty/GST charges levied by the bank |
| **Entertainment** | Streaming, movies, events, subscriptions for media (Netflix, PVR, BookMyShow, Spotify) |
| **Health** | Pharmacies, clinics, diagnostics, doctor consultations (Apollo, Practo, 1mg) |
| **Other** | Anything that fits none of the above, or cannot be identified |

---

## 2. General decision rules

Apply these in order:

1. **Identify the merchant first.** The merchant name usually decides the category, even if other words are present. "AMAZON PRIME MEMBERSHIP" is Amazon, but the *thing bought* (Prime = streaming) decides it — see Rule 3.
2. **Categorise by what was bought, not who sold it,** when a merchant sells across categories. Amazon selling a book → Shopping; Amazon Prime video subscription → Entertainment.
3. **Direction matters.** Money *in* (credits) is almost always **Income** or **Transfers**, never Shopping/Groceries. A "REFUND" is money coming back in → **Income**.
4. **A transfer has no goods or service.** If money moves to a person or to your own account with nothing purchased, it's **Transfers**. If it pays for something, use the specific category.
5. **Bank-levied costs are Fees & Charges,** even when the word "GST" appears (e.g. "SMS CHARGES GST").
6. **If two categories genuinely fit, use the more specific one.** Health beats Groceries for a pharmacy; Groceries beats Food & Dining for instant-grocery delivery.
7. **Only use "Other" as a last resort** — when the merchant is unidentifiable or the transaction fits no category.

---

## 3. Edge cases (these were real disagreements — follow the ruling)

These cases caused annotators to split. The ruling is now fixed so future labeling is consistent.

| Transaction | Tempting wrong label | Correct label | Ruling |
|---|---|---|---|
| `INDIAN OIL PETROL PUMP`, `HP PETROL STATION` | Utilities | **Transport** | Fuel is a transport cost, not a household utility. Utilities = billed home services only. |
| `SWIGGY INSTAMART` | Food & Dining | **Groceries** | Instamart delivers groceries, not prepared meals. Only Swiggy/Zomato *restaurant* orders are Food & Dining. |
| `SPOTIFY INDIA`, `AMAZON PRIME MEMBERSHIP` | Shopping | **Entertainment** | Media subscriptions are Entertainment, even when billed by a retailer. |
| `1MG TECHNOLOGIES` | Groceries / Shopping | **Health** | 1mg is a pharmacy/health platform. Health beats general Shopping. |
| `REFUND AMAZON ORDER` | Shopping | **Income** | It's money coming back *in*. Direction beats merchant. |
| `CRED RENT PAYMENT` | Transfers | **Other** | Rent isn't in the label set and isn't a plain person-to-person transfer; use Other. |

---

## 4. Worked examples

- `BESCOM ELECTRICITY BILL` → **Utilities** (home service, billed).
- `UPI/RAHUL SHARMA/PAYMENT` → **Transfers** (paid to a person, no goods).
- `STARBUCKS COFFEE` → **Food & Dining** (prepared food/drink).
- `SALARY CREDIT ACME LTD` → **Income** (money in, salary).
- `ANNUAL DEBIT CARD FEE` → **Fees & Charges** (bank-levied cost).
- `UNKNOWN MERCHANT 4521` → **Other** (unidentifiable).

---

## 5. When you're still unsure

If, after applying all rules, a transaction still fits two categories equally, pick the one **earlier** in this priority order and flag the item for review:

**Income → Transfers → Fees & Charges → Health → Utilities → Transport → Groceries → Food & Dining → Entertainment → Shopping → Other**

Flagging (rather than silently guessing) is how the guidelines improve — every flagged item is a candidate for a new edge-case ruling in the next version.
