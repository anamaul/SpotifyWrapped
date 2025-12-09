import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- KONFIGURASI ---
FILE_NAME = 'Streaming_History_Audio_2025_2.json' # sesuaikan dengan nama file JSON Anda

# 1. Load Data
try:
    df = pd.read_json(FILE_NAME)
except ValueError:
    print(f"File {FILE_NAME} tidak ditemukan. Pastikan file JSON ada di folder yang sama.")
    exit()

# 2. Data Cleaning & Preparation
df['endTime'] = pd.to_datetime(df['ts'])
df['minutesPlayed'] = df['ms_played'] / 60000

# 3. Analisis: Top 10 Artis
top_artists_time = df.groupby('master_metadata_album_artist_name')['minutesPlayed'].sum().sort_values(ascending=False).head(10)
print("=== Top 10 Artis (Durasi Dengar) ===")
print(top_artists_time)
print("\n")

# 4. Analisis Waktu (Pagi/Siang/Sore/Malam)
analysis_time = df['endTime'].dt.hour
morning = analysis_time[(analysis_time >= 5) & (analysis_time < 12)].count()
afternoon = analysis_time[(analysis_time >= 12) & (analysis_time < 17)].count()
evening = analysis_time[(analysis_time >= 17) & (analysis_time < 21)].count()
night = analysis_time[(analysis_time >= 21) | (analysis_time < 5)].count()

print("=== Kebiasaan Waktu Mendengar ===")
print(f"Pagi (05-12): {morning}")
print(f"Siang (12-17): {afternoon}")
print(f"Sore  (17-21): {evening}")
print(f"Malam (21-05): {night}")
print("\n")

# 5. Top Lagu (Repeat)
print("=== Top 10 Lagu Sering Putar ===")
toptracks = df['master_metadata_track_name'].value_counts().head(10)
print(toptracks)
print("\n")

# 6. Skipped Tracks Analysis (< 10 detik)
skip_tracks = df[df['ms_played'] < 10000]
skip_track_counts = skip_tracks['master_metadata_track_name'].value_counts().head(10)
print("=== Top 10 Lagu Sering Di-Skip (< 10 detik) ===")
print(skip_track_counts)

# 7. Visualisasi
plt.figure(figsize=(10, 6))
# PERBAIKAN WARNING SEABORN DISINI:
sns.barplot(
    x=top_artists_time.values, 
    y=top_artists_time.index, 
    hue=top_artists_time.index, 
    legend=False, 
    palette="Greens_r"
)
plt.title('Top 10 Artis Favorit Saya')
plt.xlabel('Total Menit Didengar')
plt.tight_layout() # Agar tulisan tidak terpotong
plt.show()