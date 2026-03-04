#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Insertion Sort dengan tracing
#============================================

def insertion_sort(data):

    #melihat data awal
    print("Data Awal: ", data)
    print("-" * 19)

    #loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        print("iterasi ke- ", i)
        print("Nilai Key =", key)
        print("Bagian Kiri (Terurut): ", data[:i])
        print("Bagian Kanan (Belum terurut): ", data[i:])
        
        #Geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan :", data)
        print("-" * 19)

    return data

angka = [1,6,9,3,5,7,2]
print("Hasil sorting: ", insertion_sort(angka))