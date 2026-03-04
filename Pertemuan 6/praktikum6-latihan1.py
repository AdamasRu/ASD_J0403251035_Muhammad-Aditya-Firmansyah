#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Latihan 1
#============================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data 
 
'''
Soal
1. Mengapa perulangan dimulai dari indeks 1? 
2. Apa fungsi variabel key? 
3. Mengapa digunakan while, bukan for? 
4. Operasi apa yang terjadi di dalam while? 

Jawaban
1.  Perulangan dimulai dari indeks 1 karena elemen pada indeks 0 dianggap sudah terurut

2.  berfungsi untuk menyimpan nilai elemen yang sedang diproses agar nilainya tidak hilang 
    saat terjadi pergeseran elemen, lalu nantinya ditempatkan pada posisi yang tepat.

3.  Pakai while karena jumlah pergeseran elemen tidak diketahui sejak awal dan bergantung pada kondisi tertentu

4.  Didalam while terjadi proses membandingkan elemen dengan key
    menggeser elemen yang lebih besar ke kanan, serta mengurangi indeks untuk 
    mengecek elemen sebelumnya hingga ditemukan posisi yang sesuai.
'''