#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Materi Rekursif : Kombinasi Biner
#===================================================


def biner(n, hasil=""):
    # Fungsi rekursif untuk membentuk kombinasi biner sepanjang n
    
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursi dengan menambahkan '0' ke string
    biner(n, hasil + "0")
    
    # Rekursi dengan menambahkan '1' ke string
    biner(n, hasil + "1")


# Memanggil fungsi untuk menghasilkan kombinasi biner 3 digit
biner(3)