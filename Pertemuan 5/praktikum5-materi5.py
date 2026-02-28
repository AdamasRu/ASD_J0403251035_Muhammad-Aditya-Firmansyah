#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Materi Rekursif : Kombinasi Biner dengan batas "1"
#===================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi rekursif untuk membentuk kombinasi biner
    # dengan pembatasan jumlah angka '1'
    
    # Pruning: jika jumlah_1 sudah melewati batas, hentikan rekursi
    if jumlah_1 > batas:
        return
    
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursi dengan menambahkan '0' (jumlah_1 tetap)
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Rekursi dengan menambahkan '1' (jumlah_1 bertambah 1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Memanggil fungsi untuk kombinasi 4 digit
# dengan maksimal 2 angka '1'
biner_batas(4, 2)