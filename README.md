# 🔐 PDF Password Brute Force Tool (Python)

Sebuah script Python sederhana untuk mencoba membuka file PDF terenkripsi menggunakan metode brute force berbasis wordlist.

> ⚠️ Tool ini dibuat untuk tujuan **edukasi dan pengujian keamanan pribadi**. Jangan gunakan untuk file atau sistem milik orang lain tanpa izin.

---

## 📂 Fitur

- Membuka file PDF yang dilindungi password
- Menggunakan wordlist eksternal untuk mencoba berbagai password
- Dibuat dengan `PyPDF2`
- Mudah dijalankan dan dimodifikasi

---

## 📦 Persyaratan

- Python 3.x
- Library: `PyPDF2`

### Install PyPDF2

```bash
pip install PyPDF2
```

## 🚀 Cara Penggunaan

1. **Siapkan file PDF yang diproteksi password**, misalnya: `dokumen.pdf`

2. **Buat file wordlist**, misalnya `wordlist.txt`, yang berisi daftar password yang akan dicoba

3. **Jalankan script Python**:

```bash
python brute_pdf.py
