// Copyright (c) 2025, BEN and contributors
// For license information, please see license.txt

frappe.query_reports["Laporan Penjualan Harian"] = {
  "filters": [
    {
      fieldname: "tanggal",
      label: "Tanggal",
      fieldtype: "Date",
      default: frappe.datetime.get_today()
    }
  ]
};
