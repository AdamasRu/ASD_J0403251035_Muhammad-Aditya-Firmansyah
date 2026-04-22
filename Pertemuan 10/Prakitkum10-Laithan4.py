#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J0403251035
#Latihan 4: Membuat BST Yang tidak seimbang
#=========================================

# Class Node untuk menyimpan data BST
from logging import root


class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
            print(root.data, end=" ")
            preorder(root.left)
            preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# -----------------------------
# Program utama
# -----------------------------
root = None
# Data dimasukkan berurutan naik
data_list = [10, 20, 30]
for data in data_list:
     root = insert(root, data)
print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root) #

#Penjelasan
'''
Program ini membuat sebuah Binary Search Tree (BST) yang tidak seimbang dengan memasukkan data secara berurutan naik (10, 20, 30).
Karena data dimasukkan dalam urutan naik, setiap node baru akan menjadi anak kanan dari node sebelumnya, 
sehingga membentuk struktur yang mirip dengan linked list. Fungsi preorder  digunakan untuk menampilkan urutan
data dalam BST, sementara fungsi tampil_struktur digunakan untuk menampilkan struktur tree secara visual, 
menunjukkan posisi setiap node (Root, L untuk kiri, R untuk kanan) dan levelnya dalam tree. Hasilnya akan menunjukkan 
bahwa semua node berada di sisi kanan, menciptakan sebuah BST yang tidak seimbang.   
'''