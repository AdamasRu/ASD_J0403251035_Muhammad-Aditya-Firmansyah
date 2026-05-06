#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Materi 1: Implementasi Dijkstra
#=========================================

import heapq 

graph = { 
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B dan C dengan bobot tertentu
    'B': {'D': 5},          # Node B terhubung ke D
    'C': {'D': 1},          # Node C terhubung ke D (jalur lebih murah)
    'D': {}                 # Node D tidak punya tetangga
} 

def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 

    # Jarak node awal = 0 
    distances[start] = 0 

    # Priority queue (menyimpan pasangan jarak dan node)
    pq = [(0, start)] 

    while pq: 
        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq) 

        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 

            # Hitung jarak baru ke tetangga
            distance = current_distance + weight 

            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 

                # Update jarak minimum
                distances[neighbor] = distance 

                # Masukkan ke priority queue untuk diproses
                heapq.heappush(pq, (distance, neighbor)) 

    # Mengembalikan hasil jarak terpendek dari node awal
    return distances 

hasil = dijkstra(graph, 'A') 
print(hasil) 


"""
Program ini menggunakan algoritma Dijkstra untuk mencari jarak terpendek
dari satu node ke semua node lain dalam sebuah graph berbobot.

Graph direpresentasikan sebagai dictionary, dan perhitungan dilakukan
menggunakan priority queue agar lebih efisien.

Dari node 'A', hasil akhirnya menunjukkan bahwa jalur tercepat ke 'D'
adalah melalui 'C', bukan melalui 'B', karena total bobotnya lebih kecil.
"""