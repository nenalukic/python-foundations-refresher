# 🧩 Day 4 – Working with APIs, JSON Data & Building an ETL Pipeline

## 🎯 Goal

Learn how to fetch data from a REST API, store it as a CSV file, clean and flatten nested JSON data into a readable, structured table — and then automate the entire workflow into a real ETL pipeline.

---

## 🪄 What We Built

### 1. **`fetch_api_data.py`**

A script that:

* Fetches data from an open API (`https://jsonplaceholder.typicode.com/users`)
* Converts the JSON response into a Pandas DataFrame
* Saves it locally as `api_users.csv`

✅ *This created the raw dataset (with nested JSON columns like `address` and `company`).*

---

### 2. **`clean_api_data.py`**

A script that:

* Loads the raw `api_users.csv`
* Safely parses JSON-like strings using `ast.literal_eval()`
* Flattens nested fields with `pandas.json_normalize()`
* Prefixes nested columns to prevent naming conflicts
* Saves the clean, tabular result to `api_users_clean.csv`


✅ *This produced a flat, analysis-ready CSV with clear columns like:*

| id | name | username | email | address_city | address_zipcode | company_name | company_bs |
| -- | ---- | -------- | ----- | ------------ | --------------- | ------------ | ---------- |

---

## 💡 Key Takeaways (Part 1)

1. **APIs often return nested JSON** that must be flattened for analytics.
2. **`ast.literal_eval()`** safely converts Python-style dict strings back into dictionaries.
3. **`json_normalize()`** is a powerful Pandas function for expanding nested JSON fields.
4. **Prefixing columns** avoids name collisions (e.g. both `name` and `company.name`).
5. This workflow demonstrates a mini **ETL process**:

   * **Extract:** API request
   * **Transform:** Clean and flatten JSON
   * **Load:** Save clean CSV

---

# Advanced: Building a Real ETL Pipeline

## 🎯 Goal

Turn your previous API + cleaning scripts into a **real-world ETL pipeline** that automatically:

1. **Extracts** data from an API
2. **Transforms** (cleans & flattens) nested JSON with Pandas
3. **Loads** the clean dataset into a timestamped CSV for versioned storage

---

## 🧱 ETL Pipeline Script – `etl_api_users.py`

---

## 🧩 How It Works

| Step          | Function           | Description                                                    |
| ------------- | ------------------ | -------------------------------------------------------------- |
| **Extract**   | `extract_data()`   | Fetches data from the API endpoint and converts it to JSON     |
| **Transform** | `transform_data()` | Cleans and flattens nested JSON fields (`address`, `company`)  |
| **Load**      | `load_data()`      | Saves cleaned data into a timestamped CSV file under `/output` |

Each step is modular and reusable — a standard structure in real Data Engineering pipelines.

---

## 💾 Example Output

When you run:

```bash
(venv) ➜  day-4 git:(main) ✗ python3 etl_api_users.py
```

You’ll see:

```
📡 Fetching data from API...
🧹 Cleaning and transforming data...
💾 Data saved to: output/api_users_clean_20251023_153020.csv
✅ ETL pipeline completed successfully.
```

Each run produces a **new timestamped file**, allowing version tracking and historical data comparison.

---

## 🧠 Key Takeaways (Part 2)

1. **ETL Workflow** = Extract → Transform → Load — the backbone of every data pipeline.
2. **Modular Design** – Each function performs one job cleanly.
3. **Error Handling** – `response.raise_for_status()` ensures safe API calls.
4. **Data Flattening** – `pandas.json_normalize()` with prefixes keeps column names unique.
5. **Reproducibility** – Timestamped filenames make it easy to manage data versions.
6. **Real-World Readiness** – The script can be adapted for any API and scheduled automatically.

---

## 🧰 Tools & Libraries

| Library    | Purpose                          |
| ---------- | -------------------------------- |
| `requests` | Fetching data from REST APIs     |
| `pandas`   | Data cleaning and transformation |
| `ast`      | Safe parsing of non-JSON strings |
| `datetime` | Timestamping output files        |
| `os`       | File and directory management    |

