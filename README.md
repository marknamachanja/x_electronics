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
*Developed by Mark Simiyu Namachanja*
