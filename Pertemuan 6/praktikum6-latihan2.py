#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Latihan 2
#============================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and ______________________: 
            data[j + 1] = data[j] 
            j -= 1 
         
        ______________________ 
     
    return data 
 
'''
Soal: 
1. Lengkapi kondisi agar menjadi sorting ascending. 
2. Ubah agar menjadi descending.

Jawaban:
1.  tambahkan data[j] > key untuk membandingkan apakah elemen sebelumnya lebih besar dari key
    Lalu setelah while loop selesai, baris yang kosong diisi dengan data[j + 1] = key untuk menempatkan key pada posisi yang benar.

2.  Ubah kondisi while menjadi data[j] < key yang sebelumnya data[j] > key sehingga elemen yang lebih kecil akan digeser ke kanan.
    Baris terakhir tetap diisi dengan data[j + 1] = key untuk menyisipkan key pada posisi yang benar
'''
