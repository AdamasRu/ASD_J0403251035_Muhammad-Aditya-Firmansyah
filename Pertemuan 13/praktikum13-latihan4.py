#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 4:  Studi Kasus: Jaringan Kabel Antar Gedung
#=========================================

import heapq

# 1. Representasi Weighted Graph
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# 2. Implementasi Algoritma Prim
def prim_jaringan(graph, start_node):
    visited = set([start_node])
    edges = []
    
    # Masukkan semua edge dari node awal ke priority queue (heap)
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))
    
    mst = []
    total_biaya = 0
    
    while edges:
        # Ambil edge dengan biaya (weight) terkecil
        weight, u, v = heapq.heappop(edges)
        
        # Jika gedung tujuan belum dikunjungi, tambahkan ke jaringan
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_biaya += weight
            
            # Tambahkan edge dari gedung yang baru dikunjungi ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_biaya

# Menjalankan algoritma mulai dari GedungA
hasil_mst, biaya_total = prim_jaringan(graph, 'GedungA')

# 3. Output Edge yang dipilih
print("--- Jaringan Kabel Internet Minimum ---")
for u, v, w in hasil_mst:
    print(f"Hubungkan {u} - {v} (Biaya: {w})")

# 4. Output Total Biaya Minimum
print("-" * 40)
print(f"Total Biaya Minimum Pemasangan: {biaya_total}")

'''
Jawaban Analisis:
1. Algoritma Prim (membangun jaringan secara bertahap dari satu titik fokus).
2. Edge yang dipilih: (GedungA - GedungC), (GedungC - GedungD), dan (GedungD - GedungB).
3. Total biaya minimum = 6.
4. Karena MST menjamin semua gedung terhubung dengan biaya paling rendah tanpa ada kabel yang mubazir/membentuk loop.
'''