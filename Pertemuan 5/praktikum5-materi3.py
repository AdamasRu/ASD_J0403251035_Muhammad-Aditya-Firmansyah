#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Materi Rekursif : Menjumlahkan Elemen List
#===================================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0

    #recursive case
    return data[index] + jumlah_list(data, index+1)

print("===== Program Jumlah Data Lit =====")
print(jumlah_list([535,676,58,69,689,58,45,624,542,53,5765,8968,967,98,567,346,426,3567]))