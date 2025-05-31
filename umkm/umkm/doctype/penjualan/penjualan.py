# Copyright (c) 2025, BEN and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Penjualan(Document):
    def on_submit(self):
        for item in self.items:
            barang = frappe.get_doc("Barang", item.barang)
            if barang.stok < item.qty:
                frappe.throw(f"Stok tidak cukup untuk {barang.nama} (sisa: {barang.stok})")
            barang.stok -= item.qty
            barang.save()

    def on_cancel(self):
        for item in self.items:
            barang = frappe.get_doc("Barang", item.barang)
            barang.stok += item.qty
            barang.save()
