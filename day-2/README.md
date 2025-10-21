# Day 2 – Working with Files, Data, and the OS

## 📚 Overview

On Day 2, we are focusing on **reading, writing, and managing data files** — one of the most common tasks for a Data Engineer.
We will explore how Python handles **text**, **CSV**, and **JSON** files, and how to automate file operations using **os** and **pathlib** modules.

---

## 🧠 Key Concepts

### 1. File I/O Basics

Read and write text files safely using `with open()` context managers.

💡 Always use `with open(...)` — it automatically closes files and prevents data loss.

---

### 2. Working with CSV Files

CSV files store tabular data.
We used Python’s built-in `csv` module for reading and writing.

---

### 3. Working with JSON Files

JSON is used for structured data (e.g., API responses, config files).

🧩 Difference between `json.dump()` and `json.dumps()`:

* `dump()` → writes to a **file**
* `dumps()` → returns a **string**

---

### 4. Working with the OS and File System

Use `os` and `pathlib` to automate directory operations.

---

### 5. Mini Project – Combine Multiple CSV Files

Combine all CSVs in a folder into a single dataset.

---

## ✅ Takeaways

1. Use `with open()` for safe file handling.
2. Understand when to use `csv` vs `json` for structured data.
3. Automate folder and file operations using `os` and `pathlib`.
4. Combine, clean, and transform multiple files programmatically.

