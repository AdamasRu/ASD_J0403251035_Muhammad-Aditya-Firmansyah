#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Kelas: TPL B2
#Materi 2: Implementasi Dijkstra
#=========================================

def bellman_ford(graph, start): 
    # Menyimpan jarak minimum ke setiap node
    distances = {node: float('inf') for node in graph} 
    
    # Jarak node awal = 0
    distances[start] = 0 
    
    # Relaksasi berulang (sebanyak jumlah node - 1)
    for _ in range(len(graph) - 1): 
        
        # Iterasi setiap node dalam graph
        for node in graph: 
            
            # Periksa semua tetangga dari node
            for neighbor, weight in graph[node].items(): 
                
                # Jika ditemukan jarak yang lebih kecil
                if distances[node] + weight < distances[neighbor]: 
                    
                    # Update jarak minimum
                    distances[neighbor] = distances[node] + weight 
    
    # Mengembalikan hasil jarak terpendek
    return distances 


# Contoh graph
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

# Menjalankan algoritma
hasil = bellman_ford(graph, 'A') 

# Menampilkan hasil
print(hasil)


"""
Program ini menggunakan algoritma Bellman-Ford untuk mencari jarak
terpendek dari satu node ke semua node lainnya dalam graph berbobot.

Berbeda dengan Dijkstra, algoritma ini tetap bisa bekerja walaupun
terdapat bobot negatif (selama tidak ada siklus negatif).

Pada contoh ini, hasil menunjukkan jarak terpendek dari node 'A',
di mana jalur tercepat ke 'D' adalah melalui 'C' dengan total bobot lebih kecil.
"""