import frappe
from frappe.model.document import Document

class StockEntry(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        amended_from: DF.Link | None
        item: DF.Link
        posting_date: DF.Date | None
        qty: DF.Float
        rate: DF.Float
        source_warehouse: DF.Link | None
        target_warehouse: DF.Link | None
        type: DF.Literal["Receipt", "Consume", "Transfer"]
    # end: auto-generated types

    def on_submit(self):
        if self.type in ['Receipt', 'Transfer']:
            # Incoming stock uses the rate provided on the form
            self.create_sle(self.target_warehouse, self.qty, self.rate)
            
        if self.type in ['Consume', 'Transfer']:
            # Outgoing stock ignores the form rate and calculates moving average
            outgoing_rate = self.get_moving_average_rate(self.item)
            self.create_sle(self.source_warehouse, -self.qty, outgoing_rate)

    def on_cancel(self):
        # Find and cancel any linked Stock Ledger Entries
        sles = frappe.get_all("Stock Ledger Entry", filters={"stock_entry": self.name})
        for sle in sles:
            doc = frappe.get_doc("Stock Ledger Entry", sle.name)
            doc.cancel()

    def create_sle(self, warehouse, qty, rate):
        sle = frappe.get_doc({
            "doctype": "Stock Ledger Entry",
            "item": self.item,
            "warehouse": warehouse,
            "qty": qty,
            "rate": rate,
            "stock_entry": self.name,
            "posting_date": self.posting_date or frappe.utils.today()
        })
        sle.insert(ignore_permissions=True)
        sle.submit()

    def get_moving_average_rate(self, item):
        # The stateless single SQL query valuation (Weighted Average of Receipts)
        sql = """
            SELECT COALESCE(SUM(qty * rate) / NULLIF(SUM(qty), 0), 0)
            FROM `tabStock Ledger Entry`
            WHERE item = %s AND qty > 0 AND docstatus = 1
        """
        result = frappe.db.sql(sql, (item,))
        return result[0][0] if result else 0