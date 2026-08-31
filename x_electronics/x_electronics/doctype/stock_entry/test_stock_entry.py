import frappe
from frappe.tests.utils import FrappeTestCase

class TestStockEntry(FrappeTestCase):
    def setUp(self):
        if not frappe.db.exists("Item", "Test Laptop"):
            frappe.get_doc({"doctype": "Item", "item_code": "Test Laptop", "item_name": "Test Laptop"}).insert()
        
        if not frappe.db.exists("Warehouse", "Store - Base"):
            frappe.get_doc({"doctype": "Warehouse", "warehouse_name": "Store - Base", "is_group": 0}).insert()
            
    def test_receipt_creates_sle(self):
        se = frappe.get_doc({
            "doctype": "Stock Entry",
            "type": "Receipt",
            "item": "Test Laptop",
            "target_warehouse": "Store - Base",
            "qty": 10,
            "rate": 1000,
            "posting_date": frappe.utils.today()
        }).insert()
        se.submit()
        
        sles = frappe.get_all("Stock Ledger Entry", filters={"stock_entry": se.name}, fields=["qty", "rate"])
        self.assertEqual(len(sles), 1)
        self.assertEqual(sles[0].qty, 10)
        self.assertEqual(sles[0].rate, 1000)