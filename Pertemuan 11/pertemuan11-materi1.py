# ======================================================
# Nama : Muhammad Aditya Firmansyah
# NIM  : J0403251035
#===============================================
# Implemantasi Dasar Graph
#===============================================

graph = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','D'],
    'D': ['B','C']
}


for node in graph:
    print(node, "->", graph[node])