#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Praktikum 5 : Latihan 1
#===================================================

def pangkat(a, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return a * pangkat(a, n - 1)

print(pangkat(2, 4))  # Output: 16


# =======================
# Diskusi dan Penjelasan
# =======================

# Alur Program:
# 1. Fungsi pangkat(a, n) digunakan untuk menghitung a^n (a pangkat n).
# 2. Saat dipanggil pangkat(2, 4), fungsi akan memanggil dirinya sendiri
#    dengan nilai n yang terus berkurang sampai mencapai 0.
# 3. Proses perhitungannya menjadi:
#    pangkat(2,4)
#    = 2 * pangkat(2,3)
#    = 2 * (2 * pangkat(2,2))
#    = 2 * (2 * (2 * pangkat(2,1)))
#    = 2 * (2 * (2 * (2 * pangkat(2,0))))
#    = 2 * 2 * 2 * 2 * 1
#    = 16

# Base Case:
# if n == 0: return 1
# Artinya jika pangkat sudah 0, fungsi berhenti dan mengembalikan 1

# Recursive Call:
# return a * pangkat(a, n - 1)
# Fungsi memanggil dirinya sendiri dengan nilai n dikurangi 1
# Setiap pemanggilan akan mengalikan a sampai mencapai base case