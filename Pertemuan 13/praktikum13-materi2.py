#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Materi 2: Algoritma Prim
#=========================================

import heapq

# Representasi graph berbentuk adjacency list
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk edge
    edges = []

    # Memasukkan semua edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot MST
    total_weight = 0

    # Selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Tandai node sebagai dikunjungi
            visited.add(v)

            # Tambahkan edge ke MST
            mst.append((u, v, weight))

            # Tambahkan bobot ke total
            total_weight += weight

            # Masukkan edge baru dari node tersebut
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight


# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)