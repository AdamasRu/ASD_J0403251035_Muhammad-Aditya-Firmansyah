#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 1: Graph III: Spanning Tree
#=========================================

# Daftar edge graph berdasarkan image_4a3713.png
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
# Menghubungkan semua node (A, B, C, D) tanpa cycle
spanning_tree = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

'''
Jawaban Analisis:
1. Graph awal memiliki cycle dan lebih banyak edge, sedangkan spanning tree menghubungkan semua node tanpa cycle.
2. Agar jalur antar node tidak redundan (berlebih) sesuai definisi pohon (graf asiklik).
3. Karena hanya menggunakan jumlah edge minimal (n - 1) untuk menghubungkan n buah node.
'''