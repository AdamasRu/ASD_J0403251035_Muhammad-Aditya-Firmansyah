#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J0403251035
#Latihan 5: Struktur Organisasi Perusahaan
#=========================================


#Class node digunakan untuk dasar dari tree

class Node:
    def __init__ (self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder : Root > Left > Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#Membuat tree struktur Organisasi
root = Node("Direktur")

#Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#Child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

#menjalankan traversal preorder
print("Struktur Organisasi Preorder: ")
preorder(root)

#Penjelasan
'''
Codingan ini membuat struktur binary tree sederhana
untuk struktur organisasi menggunakan class Node yang
memiliki data serta anak kiri dan kanan, lalu menggunakan fungsi
preorder() untuk traversal dengan urutan root → kiri → kanan secara
rekursif. Tree disusun sebagai struktur organisasi dengan "Direktur"
sebagai root, "Manajer A" dan "Manajer B" sebagai anaknya, serta
beberapa staff di bawahnya, sehingga menghasilkan output traversal:
Direktur, Manajer A, Staff 1, Staff 2, Manajer B, Staff 3.
'''