# ======================================================
# Nama : Muhammad Aditya Firmansyah
# NIM  : J0403251035
# ======================================================
# Studi Kasus BFS (Jalur Terdekat Lokasi)
# ======================================================

from collections import deque 

# Sebuah graph digunakan untuk merepresentasikan hubungan antar lokasi sebagai berikut: 

graph = { 
'Rumah': ['Sekolah', 'Toko'], 
'Sekolah': ['Perpustakaan'], 
'Toko': ['Pasar'], 
'Perpustakaan': [], 
'Pasar': [] 
} 

# Graph tersebut menggambarkan jalur dari Rumah ke lokasi lain. 
# Gunakan algoritma BFS untuk menampilkan urutan kunjungan node dimulai dari Rumah.

def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 
    visited.add(start) 
    
    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 
        
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 
            
            
print("BFS dari Rumah:") 
bfs(graph, 'Rumah')


'''
Pertanyaan Analisis 
1. Node mana yang dikunjungi pertama?  
Jawab: Titik awal atau root node, yaitu "Rumah".

2. Mengapa BFS cocok untuk mencari jalur terdekat?  
Jawab: Hal ini dikarenakan BFS melakukan eksplorasi secara berlapis atau level demi level. 
Dengan mengunjungi seluruh node pada jarak terdekat sebelum melangkah ke ring berikutnya, 
algoritma ini menjamin bahwa jalur yang pertama kali ditemukan menuju suatu node adalah jalur terpendek.

3. Apa perbedaan urutan BFS jika struktur graph diubah? 
Jawab: Urutan eksekusi kunjungan akan berubah mengikuti modifikasi tersebut. Perubahan pada susunan 
tetangga di adjacency list akan menentukan node mana yang masuk ke dalam antrean (queue) terlebih dahulu. 

Karena BFS menerapkan prinsip First-In First-Out (FIFO), jika "Toko" diletakkan sebelum "Sekolah", 
maka "Toko" akan diproses lebih awal. Jadi, struktur data pendukung dan urutan input tetangga 
memegang peranan penting dalam hasil akhir penelusuran.
'''