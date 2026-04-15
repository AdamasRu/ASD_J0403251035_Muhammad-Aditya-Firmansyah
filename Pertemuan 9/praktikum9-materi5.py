#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J0403251035
#Latihan 5: Traversal Postorder
#=========================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__ (self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Membuat traversal postorder : Left > Right > Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
        

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
print("Hasil Traversal Postorder: ")
postorder(root)

#Penjelasan
'''
Codingan ini membuat binary tree sederhana dengan
class Node yang memiliki data serta anak kiri dan kanan,
lalu menggunakan fungsi postorder() untuk traversal dengan urutan 
kiri → kanan → root secara rekursif. Tree disusun dari root "A" dengan
anak "B" dan "C", serta "D" dan "E" di bawah "B", sehingga menghasilkan
output traversal D, E, B, C, A.
'''