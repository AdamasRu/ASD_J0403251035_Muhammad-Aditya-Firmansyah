#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Insertion Sort (Ascending)
#============================================

def insertion_sort(data):
    #loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri
        
        #geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data

angka = [1,6,9,3,5,7,2]
print("Hasil sorting: ", insertion_sort(angka))