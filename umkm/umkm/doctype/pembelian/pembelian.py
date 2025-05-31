# Copyright (c) 2025, BEN and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Pembelian(Document):
    def on_submit(self):
        for item in self.items:
            barang = frappe.get_doc("Barang", item.barang)
            barang.stok += item.qty
            barang.save()

    def on_cancel(self):
        for item in self.items:
            barang = frappe.get_doc("Barang", item.barang)
            barang.stok -= item.qty
            barang.save()

