#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Materi Rekursif : Call Stack
#Tracing bilangan (masuk-keluar)
#input 3 = 3 2 1 | 1 2 3
#===================================================

def hitung(n):

    #base case
    if n == 0:
        print("selesai")
        return

    print("Masuk:", n)
    hitung(n-1) #recursive case
    print("Keluar", n)

print("===== Program Tracing =====")
hitung(3)