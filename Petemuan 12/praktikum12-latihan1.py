#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 1: Weighted Graph dan Perhitungan Jalur 
#=========================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

# Menentukan jalur terpendek
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D") 


# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 4 + 5 = 9
# 2. Total bobot jalur A -> C -> D adalah 2 + 1 = 3
# 3. Jalur terpendek yang dipilih adalah A -> C -> D
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge karena yang dihitung adalah total bobot,
#    bukan banyaknya langkah. Meskipun jumlah edge sama atau bahkan lebih sedikit, jika bobotnya lebih besar,
#    maka jalur tersebut tetap bukan yang paling efisien.