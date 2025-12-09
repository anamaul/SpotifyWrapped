import pandas as pd #import pandas untuk manipulasi data
import matplotlib.pyplot as plt #import matplotlib untuk visualisasi data
import seaborn as sns #import seaborn untuk visualisasi data yang lebih menarik

# --- KONFIGURASI ---
FILE_NAME = 'Streaming_History_Audio_20##.json' # sesuaikan dengan nama file JSON Anda

# 1. Load Data
try: # Membaca file JSON
    df = pd.read_json(FILE_NAME)
except ValueError:
    print(f"File {FILE_NAME} tidak ditemukan. Pastikan file JSON ada di folder yang sama.")
    exit()

# 2. Data Cleaning & Preparation
df['endTime'] = pd.to_datetime(df['ts']) # konversi kolom 'ts' ke datetime
df['minutesPlayed'] = df['ms_played'] / 60000 # konversi milidetik ke menit

# 3. Analisis: Top 10 Artis
top_artists_time = df.groupby('master_metadata_album_artist_name')['minutesPlayed'].sum().sort_values(ascending=False).head(10) # mengelompokkan berdasarkan artis dan menjumlahkan durasi dengar
print("=== Top 10 Artis (Durasi Dengar) ===")
print(top_artists_time)
print("\n")

# 4. Analisis Waktu (Pagi/Siang/Sore/Malam)
analysis_time = df['endTime'].dt.hour # ekstrak jam dari waktu dengar
morning = analysis_time[(analysis_time >= 5) & (analysis_time < 12)].count() # hitung jumlah dengar di pagi hari(jam 5 - 12 disini termasuk pagi, bisa diubah tergantung anda)
afternoon = analysis_time[(analysis_time >= 12) & (analysis_time < 17)].count() # hitung jumlah dengar di siang hari (jam 12 - 17 termasuk siang, bisa diubah tergantung anda)
evening = analysis_time[(analysis_time >= 17) & (analysis_time < 21)].count() # hitung jumlah dengar di sore hari (jam 17 - 21 termasuk sore, bisa diubah tergantung anda)
night = analysis_time[(analysis_time >= 21) | (analysis_time < 5)].count() # hitung jumlah dengar di malam hari (jam 21 - 5 termasuk malam, bisa diubah tergantung anda)

print("=== Kebiasaan Waktu Mendengar ===")
print(f"Pagi (05-12): {morning}")
print(f"Siang (12-17): {afternoon}")
print(f"Sore  (17-21): {evening}")
print(f"Malam (21-05): {night}")
print("\n")

# 5. Top Lagu (Repeat)
print("=== Top 10 Lagu Sering Putar ===")
toptracks = df['master_metadata_track_name'].value_counts().head(10) # menghitung lagu yang paling sering diputar
print(toptracks)
print("\n")

# 6. Skipped Tracks Analysis (< 10 detik)
skip_tracks = df[df['ms_played'] < 10000] # filter lagu yang diputar kurang dari 10 detik
skip_track_counts = skip_tracks['master_metadata_track_name'].value_counts().head(10) # hitung lagu yang paling sering di-skip
print("=== Top 10 Lagu Sering Di-Skip (< 10 detik) ===")
print(skip_track_counts)
print("\n")

# 7. Visualisasi (Versi Upgrade)
# Set tema visual agar background lebih bersih
sns.set_theme(style="white", context="talk")  #tema 'talk' untuk presentasi

plt.figure(figsize=(12, 7)) # Canvas

# Membuat Bar Plot
ax = sns.barplot(
    x=top_artists_time.values, 
    y=top_artists_time.index, 
    hue=top_artists_time.index, 
    legend=False, 
    palette="rocket" # Coba ganti: 'viridis', 'magma', 'mako', atau 'coolwarm' tergantung selera Anda
)

# Menambahkan Judul & Label
plt.title('🎧 Top 10 Artis Favorit Saya', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Total Durasi (Menit)', fontsize=12, color='gray')
plt.ylabel('') # Hilangkan label Y 

# FITUR KEREN: Menambahkan angka menit di ujung setiap bar
# fmt='%.0f' artinya bulatkan angka (tidak ada koma)
ax.bar_label(ax.containers[0], fmt='%.0f menit', padding=5, fontsize=10, color='black')

# Merapikan garis pinggir (Hapus garis atas, kanan, dan kiri)
sns.despine(left=True, bottom=True)

# Memastikan layout pas
plt.tight_layout()
plt.show()