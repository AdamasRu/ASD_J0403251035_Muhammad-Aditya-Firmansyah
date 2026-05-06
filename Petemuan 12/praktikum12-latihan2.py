#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Latihan 2: Implementasi Dijkstra 
#=========================================

import heapq 

# Weighted graph dengan bobot positif 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

def dijkstra(graph, start): 
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)] 

    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 

        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 

    return distances 


hasil = dijkstra(graph, 'A') 

print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance) 


# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4
# 2. Jarak terpendek dari A ke C adalah 2
# 3. Jarak terpendek dari A ke D adalah 3
# 4. Jarak A ke D lebih kecil melalui C karena A -> C -> D = 2 + 1 = 3,
#    sedangkan melalui B adalah A -> B -> D = 4 + 5 = 9, jadi jalur melalui C lebih efisien.
# 5. Fungsi priority_queue adalah untuk selalu mengambil node dengan jarak terkecil terlebih dahulu,
#    sehingga proses pencarian jalur terpendek menjadi lebih efisien.
# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini mengasumsikan bahwa
#    sekali jarak terpendek ditemukan, nilainya tidak akan berubah, padahal pada bobot negatif hal itu bisa terjadi.