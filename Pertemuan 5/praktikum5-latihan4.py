#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Praktikum 5 : Latihan 4
#===================================================

def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)


# =======================
# Diskusi dan Penjelasan
# =======================

# Tujuan Program:
# Fungsi ini menghasilkan semua kombinasi sepanjang n
# menggunakan dua pilihan karakter: "A" dan "B".

# Bagaimana jumlah kombinasi dihasilkan?
# Setiap langkah rekursi memiliki 2 pilihan:
# Tambah "A"
# Tambah "B"
# Pada setiap posisi terdapat 2 kemungkinan
# Jika panjang kombinasi adalah n, maka total kombinasi yang terbentuk adalah: 2^n (2 pangkat n)
# Contoh untuk n = 2:
# Posisi 1 > 2 pilihan (A/B)
# Posisi 2 > 2 pilihan (A/B)
# Total kombinasi = 2 × 2 = 4

# Hasil yang dicetak:
# AA
# AB
# BA
# BB