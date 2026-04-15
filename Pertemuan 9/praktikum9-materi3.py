#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J0403251035
#Latihan 3: Membuat Traversal preorder
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

#membuat tree
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal preorder
print("Hasil Traversal Preorder: ")
preorder(root)

#penjelasan
'''
Codingan ini membuat binary tree sederhana menggunakan class Node
yang memiliki data serta anak kiri dan kanan, lalu menggunakan
fungsi preorder() untuk traversal dengan urutan root → kiri → kanan
secara rekursif. Tree disusun dari root "A" dengan anak "B" dan "C",
serta "D" dan "E" sebagai anak dari "B", sehingga menghasilkan output
traversal A, B, D, E, C.
'''