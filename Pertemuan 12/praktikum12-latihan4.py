#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
#Algoritma: Dijkstra 
#=========================================

import heapq 

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
    'Perpustakaan': {'Lab': 3}, 
    'Kantin': {'Lab': 4, 'Aula': 7}, 
    'Lab': {'Aula': 1}, 
    'Aula': {} 
} 

def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
    
    # Jarak awal = 0 
    distances[start] = 0 
    
    # Priority queue 
    priority_queue = [(0, start)] 
    
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        
        # Lewati jika jarak lebih besar dari yang sudah tercatat
        if current_distance > distances[current_node]: 
            continue 
        
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
            
            # Update jika lebih kecil 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    
    return distances 


hasil = dijkstra(graph, 'Gerbang') 

print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit") 


# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin (2 menit)
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit
#    (Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7)
# 3. Tidak, jalur langsung tidak selalu menghasilkan jarak paling kecil.
#    Contohnya, dari Kantin ke Aula langsung butuh 7 menit, tetapi lewat Lab
#    hanya 4 + 1 = 5 menit, jadi lebih cepat lewat jalur lain.
# 4. Dijkstra cocok digunakan karena semua bobot bernilai positif dan kita ingin
#    mencari jalur tercepat (minimum) dari satu titik ke semua lokasi lain secara efisien.