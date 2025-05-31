# ERP UMKM - Aplikasi ERP berbasis Frappe Framework

Aplikasi ERP sederhana untuk pelaku UMKM, dikembangkan dengan Python dan Frappe Framework.

## Modul:
- Barang (Master produk)
- Penjualan & Laporan
- Pelanggan
- Pembelian

## Fitur:
- CRUD lengkap tiap modul
- Otomatisasi stok saat penjualan
- Laporan penjualan harian
- API Ready (REST API Frappe)

## Teknologi
- Frappe Framework v14
- Python
- MariaDB
- REST API













### Umkm

Erp untuk UMKM

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app umkm
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/umkm
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
