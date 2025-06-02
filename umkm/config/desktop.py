from frappe import _

def get_data():
    return [
        {
            "module_name": "Umkm",
            "type": "module",
            "label": _("UMKM"),
            "icon": "octicon octicon-briefcase",
            "color": "blue",
            "link": "workspace/umkm"
        }
    ]
