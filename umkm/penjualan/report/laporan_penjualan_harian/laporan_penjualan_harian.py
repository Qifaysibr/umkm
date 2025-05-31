# Copyright (c) 2025, BEN and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate

def execute(filters=None):
    columns = [
        {"label": "Tanggal", "fieldname": "tanggal", "fieldtype": "Date", "width": 100},
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Data", "width": 200},
        {"label": "Total", "fieldname": "total", "fieldtype": "Currency", "width": 120},
    ]

    conditions = ""
    if filters and filters.get("tanggal"):
        conditions = f"WHERE penjualan.tanggal = '{filters.get('tanggal')}'"

    data = frappe.db.sql(f"""
        SELECT 
            tanggal, customer, total
        FROM `tabPenjualan` penjualan
        {conditions}
        ORDER BY tanggal DESC
    """, as_dict=True)

    return columns, data
