# Aplikasi Analisis Sentimen Shopee

Aplikasi web Django ini melakukan analisis sentimen pada ulasan produk dari Shopee, sebuah marketplace online populer. Aplikasi ini memungkinkan pengguna untuk memasukkan URL produk Shopee, mengambil ulasan produk, dan menganalisis sentimen dari ulasan tersebut untuk memberikan wawasan apakah produk tersebut layak untuk dibeli atau tidak.

## Teknologi yang Digunakan

- **Django**: Kerangka kerja web yang digunakan untuk membangun aplikasi.
- **scikit-learn**: Digunakan untuk analisis sentimen dengan menggunakan vektorisasi TF-IDF dan klasifikasi K-Nearest Neighbors (KNN).
- **Requests**: Perpustakaan untuk membuat permintaan HTTP untuk mengambil ulasan produk dari API Shopee.
- **Python Regular Expressions (regex)**: Untuk validasi URL dan pra-pemrosesan teks.
- **pickle**: Perpustakaan serialisasi yang digunakan untuk memuat model analisis sentimen yang telah dilatih dan vektorisasi.

## Prasyarat

- Python 3.x terpasang di sistem Anda.
- Kerangka kerja Django terpasang (`pip install django`).
- Perpustakaan Python yang dibutuhkan terpasang (`pip install scikit-learn requests emoji`).

## Pengaturan dan Penggunaan

1. Klona repositori ke mesin lokal Anda:

    ```
    git clone https://github.com/bagusdwsn/Shopeefies.git
    ```

2. Buka direktori proyek:

    ```
    cd Shopeefies
    ```

3. Jalankan server pengembangan Django:

    ```
    python manage.py runserver
    ```

4. Akses aplikasi web di peramban Anda di `http://localhost:8000`.

5. Masukkan URL produk Shopee yang valid dalam kolom input dan klik tombol "Prediksi" untuk menganalisis sentimen ulasannya.

## Alur Kerja Aplikasi

1. **Halaman Beranda**: Setelah mengakses aplikasi, pengguna akan disajikan dengan halaman beranda yang berisi kolom input untuk memasukkan URL produk Shopee.

2. **Analisis Sentimen**: Setelah mengirimkan URL produk yang valid, aplikasi akan mengambil ulasan menggunakan API Shopee dan melakukan analisis sentimen pada ulasan tersebut.

3. **Halaman Hasil**: Pengguna akan diarahkan ke halaman hasil di mana mereka dapat melihat hasil analisis sentimen, termasuk sentimen dari setiap ulasan dan keputusan keseluruhan (apakah membeli produk atau tidak) berdasarkan persentase sentimen.
