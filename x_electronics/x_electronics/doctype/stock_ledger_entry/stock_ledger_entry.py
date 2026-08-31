# Copyright (c) 2026, Mark Namachanja and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class StockLedgerEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		item: DF.Link | None
		posting_date: DF.Date | None
		qty: DF.Float
		rate: DF.Float
		stock_entry: DF.Link | None
		warehouse: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Stock Ledger Entry"
