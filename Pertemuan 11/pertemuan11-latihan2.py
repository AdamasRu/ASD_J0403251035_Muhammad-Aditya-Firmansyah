# ======================================================
# Nama : Muhammad Aditya Firmansyah
# NIM  : J0403251035
# ======================================================
# Studi Kasus DFS (Eksplorasi Jalur)
# ======================================================

# Graph berikut merepresentasikan jalur eksplorasi: 

graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': [] 
} 

# Gunakan algoritma DFS untuk menelusuri graph mulai dari node A.

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 
    
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 
    
visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited) 

'''
Pertanyaan Analisis 
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
Jawab: Hal ini dikarenakan mekanisme DFS yang mengandalkan struktur stack atau pemrosesan rekursif. 
Algoritma ini akan terus mengeksplorasi satu cabang hingga mencapai ujung (daun) sebelum melakukan 
backtracking untuk memeriksa cabang lain yang belum dikunjungi.

2. Apa yang terjadi jika urutan neighbor diubah?  
Jawab: Urutan penelusuran node akan ikut bergeser. Karena DFS memproses tetangga berdasarkan 
posisinya dalam daftar kedekatan (adjacency list), mengubah urutan list tersebut secara otomatis 
akan mengubah prioritas jalur yang diambil oleh algoritma.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
Jawab: Perbedaan utamanya terletak pada prioritas arah pencarian. DFS bergerak secara vertikal atau 
mendalam mengikuti satu rute hingga maksimal (contoh: A → B → D → E → C → F). 

Sebaliknya, BFS bergerak secara horizontal atau melebar dengan menyelesaikan satu level sebelum 
pindah ke level di bawahnya (contoh: A → B → C → D → E → F). Singkatnya, DFS memprioritaskan 
kedalaman rute, sementara BFS memprioritaskan cakupan luas pada tiap tingkatan.
'''