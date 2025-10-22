# 🧱 Day 3 – Data Manipulation with Pandas

## 📚 Overview

On Day 3, we are focusing on **Pandas**, one of the most powerful Python libraries for data engineers.
You are going to learn how to **read**, **clean**, **transform**, **aggregate**, and **combine** structured datasets (CSV, JSON, etc.) using Pandas DataFrames.

---

## 🧠 Key Concepts

### 1. Creating DataFrames

✅ A **DataFrame** is like an in-memory table (similar to SQL or Excel).
Each column is a **Series** (like a single list with a label).

---

### 2. Reading Data from Files

---

### 3. Exploring and Selecting Data

```python
print(df.head())          # First 5 rows
print(df.info())          # column types
print(df.shape)           # (rows, columns)
print(df.columns)         # Column names
print(df[["month", "revenue"]])  # Select multiple columns
print(df[df["revenue"] > 6000])  # Filter rows
print(df.sort_values(by="revenue", ascending=False))  # Sort
```

---

### 4. Cleaning and Transforming Data

---

#### Handling Missing Values

---

#### Renaming Columns and Converting Types

---

### ⚙️ **Inplace Best Practices (Avoid FutureWarnings)**

| Situation                                | Safe? | Best Practice                |
| ---------------------------------------- | ----- | ---------------------------- |
| `df.rename(columns={...}, inplace=True)` | ✅     | OK – modifies full DataFrame |
| `df.fillna({...}, inplace=True)`         | ✅     | OK – full DataFrame          |
| `df["col"].fillna(x, inplace=True)`      | ⚠️    | Avoid – may modify a copy    |
| `df["col"] = df["col"].fillna(x)`        | ✅     | Best option                  |
| `df["col"] = df["col"].astype(int)`      | ✅     | Best option                  |

💡 **Rule:**
If you’re working on **a single column**, assign it back using `df["col"] = ...`.
Use `inplace=True` only when modifying the **entire DataFrame**.

---

### 5. Aggregations and Grouping

---

### 6. Joining and Merging

---

## 🧩 Mini Project – Sales Data Analysis

### Task

You have multiple CSV files in the `data/` folder:

```
sales_january.csv
sales_february.csv
sales_march.csv
```

Each contains:

```
day,revenue,expenses
1,200,150
2,220,140
3,180,160
```
---

### Your Steps

1. Load all CSVs into Pandas.
2. Combine them into one DataFrame.
3. Add a `month` column based on the file name.
4. Compute total and average **profit per month**.
5. Save the result to `cleaned_sales.csv`.

---

## ✅ Takeaways

1. Pandas = core skill for every Data Engineer.
2. Use DataFrames for efficient data exploration and transformation.
3. Handle missing data and conversions cleanly (avoid chained assignments).
4. Merge and aggregate datasets like SQL joins and GROUP BY.
5. Keep your code **clean, explicit, and future-proof**.
