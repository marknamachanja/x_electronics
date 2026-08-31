# X Electronics - Warehouse Management System

A custom Frappe application designed to manage warehouse inventory, handle stock transactions, and maintain a stateless stock ledger using moving average valuation. This project was developed as an interview assignment.

## Core Architecture

* **Master Data:** Custom `Item` and `Warehouse` DocTypes configured for tree structures.
* **Transactional Data:** 
  * `Stock Entry` (Submittable): Handles `Receipt`, `Consume`, and `Transfer` transactions.
  * `Stock Ledger Entry` (Submittable): A stateless ledger where records are created dynamically upon Stock Entry submission.
* **Backend Logic:** Python controller hooks calculate moving average valuation rates purely via SQL on the fly, eliminating the need for stored cumulative totals.
* **Automated Testing:** Includes Python unit tests (`test_stock_entry.py`) to verify ledger creation and data validation.

## Reports

Built with raw SQL utilizing Window Functions for real-time aggregation:
1. **Stock Balance:** Displays real-time inventory balances and valuation rates per warehouse.
2. **Stock Ledger:** Displays cumulative quantities and running balances ordered by posting date.

---

## Screenshots

### 1. Master Data (Items & Warehouses)
*Item List View*
![Item List](screenshots/item_list.png)

*Warehouse List*
![Warehouse List](screenshots/warehouse_list.png)

### 2. Transactions
*Stock Entry Form (Receipt)*
![Stock Entry Form](screenshots/stock_entry_form.png)

*Stock Entry List*
![Stock Entry List](screenshots/stock_list.png)

*Stock Ledger Entry List*
![Stock Ledger Entry](screenshots/stock_ledger_entry.png)

### 3. Analytics & Reporting
*Stock Balance Report (Stateless Valuation)*
![Stock Balance](screenshots/stock_balance.png)

---
*Developed by Mark Simiyu Namachanja*
