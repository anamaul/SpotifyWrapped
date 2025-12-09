# 🎵 Spotify Personal Data Analysis

Project data analysis sederhana menggunakan Python untuk menganalisis kebiasaan mendengarkan musik di Spotify berdasarkan data _Extended Streaming History_.

## 📊 Fitur Analisis

Program ini mengolah data JSON dari Spotify untuk menghasilkan _insight_:

1.  **Top 10 Artis** berdasarkan total durasi mendengarkan (menit).
2.  **Analisis Waktu**: Kapan waktu tersering mendengarkan musik (Pagi, Siang, Sore, atau Malam).
3.  **Top Lagu (Repeat)**: Lagu yang paling sering diputar berulang-ulang.
4.  **Skipped Tracks**: Lagu yang sering dilewati (diputar kurang dari 10 detik).
5.  **Visualisasi Data**: Grafik batang untuk 10 artis teratas.

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Pandas** (Pembersihan dan manipulasi data)
- **Matplotlib & Seaborn** (Visualisasi data)

## 🚀 Cara Menjalankan

1.  **Clone Repository**

    ```bash
    git clone https://github.com/anamaul/SpotifyWrapped.git
    cd SpotifyWrapped
    ```

2.  **Install Library**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Siapkan Data**

    - Request data pribadi Anda di [Spotify Privacy Settings](https://www.spotify.com/account/privacy/).
    - Pilih "Extended streaming history".
    - Download file JSON dan letakkan di folder project.
    - Ubah nama file di `Main.py` (variabel `FILE_NAME`) sesuai nama file JSON Anda.

4.  **Jalankan Program**
    ```bash
    python Main.py
    ```

## 🔒 Privasi

Repository ini **tidak menyertakan** file dataset (`.json`) karena mengandung data pribadi (IP Address, Device Info).

---

**Author:** [Muhammad Maulana Adrian]
