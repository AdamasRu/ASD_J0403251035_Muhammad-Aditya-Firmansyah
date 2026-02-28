#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Praktikum 5 : Latihan 3
#===================================================

def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index]
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


# =======================
# Diskusi dan Penjelasan
# =======================

# Tujuan Program:
# Fungsi cari_maks digunakan untuk mencari nilai maksimum
# dalam sebuah list secara rekursif

# Alur Program:
# 1. Fungsi mulai dari index = 0.
# 2. Fungsi akan memanggil dirinya sendiri dengan index + 1
#    sampai mencapai elemen terakhir
# 3. Setelah mencapai elemen terakhir, proses perbandingan
#    dilakukan saat fungsi kembali (backtracking).

# Ilustrasi Proses:
# cari_maks([3,7,2,9,5], 0)
# bandingkan 3 dengan hasil dari index 1
# bandingkan 7 dengan hasil dari index 2
# bandingkan 2 dengan hasil dari index 3
# bandingkan 9 dengan hasil dari index 4
# index 4 adalah elemen terakhir (5) = return 5
# bandingkan 9 dan 5 = return 9
# bandingkan 2 dan 9 = return 9
# bandingkan 7 dan 9 = return 9
# bandingkan 3 dan 9 = eturn 9

# Base Case:
# if index == len(data) - 1:
# = jika sudah sampai elemen terakhir, langsung kembalikan nilai elemen tersebut

# Recursive Call:
# maks_sisa = cari_maks(data, index + 1)
# Fungsi memanggil dirinya sendiri untuk mencari
# nilai maksimum dari sisa list setelah index saat ini
# Kemudian dibandingkan dengan elemen sekarang