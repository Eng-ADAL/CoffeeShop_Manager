# ☕ CoffeeShop Manager CLI App for Café's ☕ 

## Contents

This repo contains:

* **Data files** in `data/`: `products.csv`, `couriers.csv`, `orders.csv`
* **Source code** in `source/`:

  * `main.py`, `products.py`, `couriers.py`, `orders.py`, `utils.py`
* **Unit tests** in `source/test/`
* **README.md**

---

## Project Background

A command-line interface (CLI) application developed during a Junior Data Engineering bootcamp. The app simulates a basic order management system for a small café, enabling management of products, couriers, and customer orders through intuitive, emoji-enhanced menus, with robust input validation and file-based persistence.

---

## Client Requirements

* 🧭 **Main Menu**: Provides entry point to Products, Couriers, and Orders menus
* 🛒 **Products Menu**: Create, view, update, delete products
* 🛵 **Couriers Menu**: Create, view, update, delete couriers
* 📦 **Orders Menu**: Create, view, update status, delete orders
* 📂 **Data Persistence** between sessions using CSV files
* 🧠 **Modular Design** across multiple `.py` modules

---

## Project Status
* **Done** CSV CRUD functions running app.
* **Planned** implemented (Dockerisation, Flask, Database integration, ID-based references)

---

## Tech Stack

* `Python 3.x`
* `CSV`, `JSON`
* CLI (command-line interface)
* `pytest` for unit testing
* `Git` for version control

---

## How to Run the App

**Recommendation:** using virtual environment

```bash
# Windows
py source/main.py

# macOS / Linux
python3 source/main.py
```

---

## 🧪 Unit Testing

This project includes a basic unit test suite using `pytest`.

Currently covered:

* Price validation logic (`valid_price`) in `utils.py`

Planned tests for:

* Phone number validation (`valid_uk_phone`)
* CSV read/write round-trip
* Data loaders (`load_*` functions)

**Running tests:**

```bash
pip install pytest # if not installed in your virtual environment

# Windows
py -m pytest -v -s 

# Linux / Mac
python3 -m pytest -v -s 
```

---

## Agile Development Log

### 1 Stage

* Built foundational menus for products (view, add, update, delete)
* Focused on Python fundamentals: lists, `input()`, `print()`, and control flow

### 2 Stage

* Introduced orders as dictionaries in a list
* Modularised code into `main.py`, `products.py`, `orders.py`, `utils.py`
* Added input validation and looping menus

### 3 Stage

* Added couriers menu and JSON/text file persistence using `pathlib`
* Continued refining menus and input handling
* Placeholder menus for order status/update features

### 4 Stage 

* Refactored persistence to CSV using `csv.DictReader`/`DictWriter`
* Completed full orders workflow: multi-item selection, courier assignment, total price calculation, timestamps
* Improved validation (`valid_uk_phone`, `valid_price`)

### 5 Stage (coming soon)
* Dockerisation on WSL


---

## 🆕 Additional Features

* Real-time total price calculator during order creation
* Timed waits and auto-continue prompts (`wot` function)
* Cross-platform clear screen functionality (`clr_scrn`)
* Timestamping orders with `timestamp()` utility


### ✅ **Core Learning Outcomes**

* Implemented **CSV-based data persistence** using `csv.DictReader` and `DictWriter`
* Managed **data loading and saving** with consistent structure (`read_csv`, `write_csv`, `load/save_*`)
* Completed full **CLI flow for orders**, with:

  * Multi-product selection
  * Courier assignment or \[Take Away] option
  * Phone/address validation with graceful fallback
* Deepened understanding of **reusable validation functions**, including `valid_uk_phone()`
* Enhanced **modular design** with all menus (`products`, `couriers`, `orders`) structured cleanly
* Learned to manage **data typing and formatting**, including float parsing, string manipulation, and list joins
* Strengthened **user interaction UX** with clear messages, emoji feedback, and retry logic

---

## 🚀 What I Implemented

### 🧾 Orders

* View all orders with formatted CLI table ✅
* Create new order:

  * Product selection loop with validation ✅
  * Optional courier assignment or \[Take Away] ✅
  * Automatic total price calculation ✅
  * Timestamp added to each order ✅
* Update order **status** (e.g. preparing, dispatched) with emojis ✅
* Delete order with confirmation ✅
* Order **full update** menu placeholder added ❌

### 🛵 Couriers

* Refined update courier logic:

  * Dual-name/phone update with validation ✅
  * Prevented accidental overwrites ✅
* Couriers stored as CSV with custom fields ✅
* Improved cancellation and retry flow ✅

### 📦 Products

* Previously complete; no major changes in Week 4 ✅
* Product list used during order creation ✅

### 📁 Data Handling

* Switched all persistence to text to **CSV format** ✅
* Added loader and saver functions for products, couriers, and orders ✅
* Handled type conversion (e.g. `float`, `int`, and `str`) from CSV ✅

---

## 🌟 What's Ahead:

| Feature                             | Reason            | Notes                                     |
| ----------------------------------- | ----------------- | ----------------------------------------- |
| Full order update (edit all fields) | Placeholder added | Planned or stretch                        |
| Export/import beyond CSV            | Not required      | Could explore SQLite/PostgreSQL in Week 5 |

---

## 🛠 Improvements Made 

* ✔ Moved phone validation into `utils.py` and reused across modules
* ✔ Implemented full **order status update** feature with choices
* ✔ Added better UI feedback for cancellations and invalid inputs
* ✔ Improved CLI formatting for all list outputs
* ✔ All menus now use consistent emoji-rich prompts

---
