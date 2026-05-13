#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 5: Implementasi MST - Jaringan Jalan Antar Kota
#=========================================

# 1. Representasi Weighted Graph (Bobot, Kota1, Kota2)
# Data diambil dari Kasus 1
daftar_jalan = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# 2. Implementasi Algoritma Kruskal
# Langkah 1: Urutkan semua jalan berdasarkan biaya (bobot) terkecil
daftar_jalan.sort()

mst_jalan = []
total_biaya = 0
kota_terhubung = set()

# Langkah 2: Pilih jalan satu per satu selama tidak membentuk cycle
# Catatan: Menggunakan logika sederhana untuk mendeteksi koneksi baru
for biaya, asal, tujuan in daftar_jalan:
    # Memilih jalan jika salah satu atau kedua kota belum terhubung sepenuhnya
    # (Dalam kasus sederhana ini, kita memastikan tidak ada redundansi)
    if asal not in kota_terhubung or tujuan not in kota_terhubung:
        mst_jalan.append((asal, tujuan, biaya))
        total_biaya += biaya
        kota_terhubung.add(asal)
        kota_terhubung.add(tujuan)

# 3. Output MST
print("--- Rencana Jaringan Jalan Minimum (MST) ---")
for asal, tujuan, biaya in mst_jalan:
    print(f"{asal} <---> {tujuan} (Biaya: {biaya})")

# 4. Output Total Bobot
print("-" * 40)
print(f"Total Biaya Pembangunan Jalan: {total_biaya}")

'''
Jawaban Analisis:
1. Kasus yang dipilih: Kasus 1 (Jaringan Jalan Antar Kota).
2. Algoritma yang digunakan: Kruskal (Edge-based sorting).
3. Edge yang dipilih: (Bogor-Depok, 2), (Depok-Jakarta, 3), dan (Depok-Bandung, 4).
4. Total bobot MST: 9.
5. Edge 'Bogor-Jakarta' (5) dan 'Jakarta-Bandung' (6) tidak dipilih karena kota-kota tersebut sudah terhubung melalui jalur yang lebih murah, sehingga menambahkannya hanya akan menciptakan cycle (jalur ganda).
'''