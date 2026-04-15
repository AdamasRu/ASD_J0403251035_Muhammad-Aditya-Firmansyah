#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Latihan 1: Membuat Node Tree
#=========================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__ (self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#menampilkan 1st node
print("Data pada root:", root.data)
print("Data child kiri root:", root.left)
print("Data child kanan root:", root.right)

#Penjelasan : Code ini digunakan untuk membuat Node sebagai wadah untuk menampung data dalam struktur hirarki/binary tree