#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Materi Rekursif : Faktorial
#===================================================

def faktorial(n):
    #base case
    if n == 0:
        return 1

    #recursive case
    return n * faktorial(n-1) #n-1 * n-2.............

print("=== Program Faktorial ===")
i = int(input("Masukan Angka Faktorial : "))
print(f"Hasil Faktorial : {faktorial(i)}")