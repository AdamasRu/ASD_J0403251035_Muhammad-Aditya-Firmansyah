#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 2:  Implementasi Sederhana Algoritma Kruskal
#=========================================

# Daftar edge: (bobot, node1, node2)
edges = [
 (1, 'C', 'D'),
 (2, 'A', 'C'),
 (3, 'B', 'D'),
 (4, 'A', 'B'),
 (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

'''
JAWABAN ANALISIS:
1. Edge ('C', 'D') dengan bobot 1.
2. Karena Kruskal menggunakan prinsip greedy untuk meminimalkan total bobot MST.
3. Total bobot = 6.
4. Karena node-node tersebut sudah terhubung (untuk menghindari terbentuknya cycle).
'''