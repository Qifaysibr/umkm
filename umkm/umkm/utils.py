import frappe
import requests

def kirim_notifikasi_telegram(barang):
    bot_token = frappe.db.get_single_value("Telegram Settings", "bot_token")
    chat_id = frappe.db.get_single_value("Telegram Settings", "chat_id")

    message = (
        f"⚠️ Stok barang menipis!\n\n"
        f"Barang: {barang.nama_barang}\n"
        f"Stok: {barang.stok}\n"
        f"Minimum: {barang.stok_minimum}"
    )

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        requests.post(url, data={"chat_id": chat_id, "text": message}, timeout=5)
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Telegram Notification Error")
