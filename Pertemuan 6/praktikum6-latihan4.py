#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Latihan 4
#============================================

def merge_sort(data): 
    if len(data) <= 1: 
        return data 
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 
     
    return merge(left_sorted, right_sorted) 

'''
Soal: 
1. Apa yang dimaksud dengan base case? 
2. Mengapa fungsi memanggil dirinya sendiri? 
3. Apa tujuan fungsi merge()? 

Jawaban:
1.  Base case adalah kondisi penghentian rekursi
    contoh pada code diatas, base casenya adalah saat panjang data kurang dari atau sama dengan 1
2.  Fungsi memanggil dirinya sendiri karena merge sort menggunakan konsep rekursi untuk membagi data menjadi bagian yang lebih kecil.
3.  Tujuan fungsi merge() adalah menggabungkan dua bagian data yang sudah terurut menjadi satu list yang terurut kembali secara keseluruhan
'''