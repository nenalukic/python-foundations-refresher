# 🧩 Day 5 – Loading Data into Databases (SQL Integration for Data Engineers)

## 🎯 Goal

Today you'll complet the **“L” in ETL** — **Load** — by taking cleaned data from your ETL pipeline and storing it in a **relational database** (SQLite).
This makes your pipeline complete:

**Extract → Transform → Load**

---

## 🧱 What You'll Learn

| Concept                       | Description                                                              |
| ----------------------------- | ------------------------------------------------------------------------ |
| **ETL Workflow**              | Extract → Transform → Load — a foundational data engineering pattern     |
| **SQLite**                    | Lightweight, file-based SQL database — perfect for testing and pipelines |
| **`sqlite3` module**          | Python’s built-in way to connect and interact with SQLite databases      |
| **`pandas.to_sql()`**         | Automatically creates a SQL table and loads data from a DataFrame        |
| **`pandas.read_sql_query()`** | Runs SQL queries and returns the result as a DataFrame                   |
| **Timestamped files**         | Enable versioning of your data and easy pipeline automation              |
| **Dynamic file detection**    | The script now finds the newest cleaned CSV automatically                |

---


## Day 5 Script – `load_to_sqlite.py`

---

## 🧪 How to Run It

1. Make sure your virtual environment is active:

   ```bash
   source venv/bin/activate
   ```

2. Run the script:

   ```bash
   python3 day-5/load_to_sqlite.py
   ```

3. Expected output:

   ```
   🔍 Searching for cleaned CSV files in: day-4/output
   Found files: ['day-4/output/api_users_clean_20251023_153020.csv']
   📄 Using latest file: day-4/output/api_users_clean_20251023_153020.csv
   📂 Loading cleaned CSV data...
   ✅ Loaded 10 rows and 13 columns.
   🔌 Connected to SQLite database at: day-5/etl_data.db
   💾 Data successfully written to table 'api_users'.
   🔍 Running sample query...
      id            name              email            company_name
   0   1   Leanne Graham   Sincere@april.biz   Romaguera-Crona
   ...
   ✅ Database connection closed.
   ```

---

## 🧠 Key Takeaways

1. **You can load data directly from Pandas into SQL.**
2. **SQLite** is perfect for local testing but easily replaceable with PostgreSQL, MySQL, or Snowflake.
3. The **`.to_sql()`** method handles table creation and schema automatically.
4. Using **glob + timestamped files**, your ETL pipeline now adapts dynamically to new runs.
5. You’ve now built a **fully functional mini data pipeline** — the same structure used in real-world production systems.

---

## 🧰 Tools Used

| Tool      | Purpose                                    |
| --------- | ------------------------------------------ |
| `pandas`  | Data handling and CSV ↔ SQL transformation |
| `sqlite3` | Database connection and SQL operations     |
| `glob`    | Finding the latest CSV file dynamically    |
| `os`      | File management and timestamp access       |

---

## 🧩 Optional Extensions

Once you’re comfortable:

* **Replace SQLite with PostgreSQL** using `sqlalchemy` for real-world databases.
* Schedule this script daily with **cron**, **Airflow**, or **Prefect**.
* Create a second table (e.g. “companies”) and use **SQL joins** for relational modeling.

---

## 🏁 Summary

You’ve now:
✅ Completed the **entire ETL process**
✅ Built a **real pipeline** from raw API → clean CSV → SQL table
✅ Learned database fundamentals for Data Engineering
