#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J040325103
#Latihan 2: Membuat Binary Search Tree Sederhana
#=========================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__ (self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.right = Node("F")

#menampilkan isi node
print("Data pada root:", root.data)
print("child kiri root:", root.left.data)
print("child kanan root:", root.right.data)
print("child kiri dari B:", root.left.left.data)
print("child kanan dari B:", root.left.right.data)
print("child kanan dari C", root.right.right.data)

#Penjelasan:
#Code ini digunakan untuk menampilkan data-data yang ada pada binary tree menggunakan metode print()
#Node dibuat dengan cara memanggil class Node(), lalu dipanggil dengan print().