# Copyright (c) 2025, BEN and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from umkm.umkm.utils import kirim_notifikasi_telegram

class Penjualan(Document):
    def on_submit(self):
        frappe.msgprint("Memproses pengurangan stok...")
        for item in self.items:
            frappe.msgprint(f"Barang: {item.barang}, Qty: {item.qty}")
            barang = frappe.get_doc("Barang", item.barang)
            frappe.msgprint(f"Stok sebelum: {barang.stok}")
            if barang.stok < item.qty:
                frappe.throw(f"Stok tidak cukup untuk {barang.nama_barang} (sisa: {barang.stok})")
            # barang.flags.ignore_validate_update_after_submit = True
            barang.stok -= item.qty
            barang.save()
            frappe.msgprint(f"Stok sesudah: {barang.stok}")
            
            # Cek stok minimum dan kirim notifikasi untuk setiap barang
            if barang.stok < barang.stok_minimum:
                kirim_notifikasi_telegram(barang)

    def on_cancel(self):
        for item in self.items:
            barang = frappe.get_doc("Barang", item.barang)
            barang.stok += item.qty
            barang.save()
