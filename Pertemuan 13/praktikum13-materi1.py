#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Materi 1: Implementasi Dijkstra
#=========================================

# Daftar edge dalam format:
# (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan hasil Minimum Spanning Tree (MST)
mst = []

# Menyimpan total bobot MST
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Proses memilih edge
for weight, u, v in edges:

    # Edge dipilih jika tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total
        total_weight += weight

        # Menandai node sebagai sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)