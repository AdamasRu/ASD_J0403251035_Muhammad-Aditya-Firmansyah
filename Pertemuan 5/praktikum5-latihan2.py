#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Praktikum 5 : Latihan 2
#===================================================

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)


# =======================
# Diskusi dan Penjelasan
# =======================

# Alur Eksekusi:
# countdown(3)
# → print "Masuk: 3"
# → countdown(2)
#    → print "Masuk: 2"
#    → countdown(1)
#       → print "Masuk: 1"
#       → countdown(0)
#          → print "Selesai"
#       → print "Keluar: 1"
#    → print "Keluar: 2"
# → print "Keluar: 3"

# Mengapa "Keluar" muncul terbalik?
# Karena rekursi menggunakan sistem stack (LIFO - Last In First Out)
# Setiap pemanggilan fungsi ditumpuk ke dalam call stack
# Saat mencapai base case (n == 0), fungsi mulai selesai dari pemanggilan terakhir terlebih dahulu

# Artinya:
# Yang terakhir masuk (countdown(1)) akan pertama kali keluar
# Maka urutan "Keluar" menjadi 1, 2, 3 (terbalik dari "Masuk")