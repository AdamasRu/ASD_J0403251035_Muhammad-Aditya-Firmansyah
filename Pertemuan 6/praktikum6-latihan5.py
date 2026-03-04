#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Latihan 5
#============================================

def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
     
    while i < len(left) and j < len(right): 
        if __________________________: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
     
    result.extend(left[i:]) 
    result.extend(right[j:]) 
     
    return result 

'''
Soal: 
1. Lengkapi kondisi agar menjadi ascending. 
2. Jelaskan fungsi result.extend(). 

Jawaban:
1.  Kondisi pada bagian if diisi dengan left[i] <= right[j]
2.  Fungsi result.extend() digunakan untuk menambahkan sisa elemen yang belum diproses dari salah satu list, baik left maupun right
    agar jika ada data sisa di salah satu sisi yang bisa langsung ditambah tanpa perlu dibandingin, bisa langsung ditambah
'''