#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J0403251035
#Latihan 4: Traversal Inorder
#=========================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__ (self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi inorder : left > root > right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

#membuat tree
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal inorder
print("Hasil Traversal Preorder: ")
inorder(root)

#Penjelasan
'''
Codingan ini membuat binary tree sederhana menggunakan class Node
yang memiliki data serta anak kiri dan kanan, lalu menggunakan
fungsi inorder() untuk traversal dengan urutan kiri → root → kanan
secara rekursif. Tree disusun dari root "A" dengan anak "B" dan "C",
serta "D" dan "E" sebagai anak dari "B", sehingga menghasilkan output
traversal D, B, E, A, C.
'''