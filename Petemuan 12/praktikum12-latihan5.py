#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 5: Studi Kasus dengan Program Shortest Path
#=========================================

import heapq

# Representasi graph berbobot (dalam satuan jarak/waktu)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},   # Dari Bogor ke Jakarta & Depok
    'Depok': {'Jakarta': 2, 'Bandung': 6}, # Dari Depok ke Jakarta & Bandung
    'Jakarta': {'Bandung': 7},             # Dari Jakarta ke Bandung
    'Bandung': {}                          # Bandung tidak punya tetangga
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak ke node awal = 0
    distances[start] = 0
    
    # Priority queue untuk memilih node dengan jarak terkecil
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Lewati jika sudah ada jarak yang lebih kecil
        if current_distance > distances[current_node]:
            continue
        
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jarak lebih pendek, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


# Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma
hasil = dijkstra(graph, start_node)

# Menampilkan hasil
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")


# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor
# 2. Node dengan jarak paling kecil dari node awal (selain dirinya sendiri) adalah Depok (2)
# 3. Node dengan jarak paling besar dari node awal adalah Bandung (8)
# 4. Cara kerja Dijkstra pada kasus ini:
#    - Dimulai dari Bogor dengan jarak 0
#    - Kemudian mengecek tetangga terdekat (Depok = 2, Jakarta = 5)
#    - Dari Depok, ditemukan jalur lebih cepat ke Jakarta (2 + 2 = 4)
#    - Lalu dihitung ke Bandung melalui jalur tercepat (Depok → Bandung = 2 + 6 = 8)
#    - Algoritma selalu memilih node dengan jarak terkecil terlebih dahulu
#      hingga semua node mendapatkan jarak minimum