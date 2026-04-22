#=========================================
#Nama: Muhammad Aditya Firmansyah
#NIM : J0403251035
#Latihan 1: BST
#=========================================

class Node:
    def __init__(self, data): #untuk membuat node baru
        self.data = data
        self.left = None
        self.right = None

def insert(root, data): #fungsi untuk memasukkan data ke dalam BST
    if root is None:
        return Node(data)

    if data < root.data: #jika data yang dimasukkan lebih kecil dari data pada node saat ini, maka akan masuk ke subtree kiri
        if root.left is None: 
            root.left = insert(root.left, data) 
        elif data > root.data:
            root.right = insert(root.right, data)
        return root

#Mengisi data BST
root = None
data_list = [50, 30, 70, 20, 40, 50, 80]

for data in data_list: #mengisi data ke dalam BST dengan memanggil fungsi insert() untuk setiap elemen dalam data_list
    root = insert(root, data)

print("BST berhasil dibuat")

#=========================================
#Latihan 2: Traversal Inorder
#=========================================

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print ("hasil Inornder:")
inorder(root)

#=========================================
#Latihan 3: Search di BST
#=========================================

def search(root,key): #fungsi untuk mencari data dalam BST dengan membandingkan nilai yang dicari dengan nilai pada node saat ini, dan kemudian memutuskan apakah akan mencari di subtree kiri atau kanan
    if root is None: #jika node saat ini adalah None, maka data tidak ditemukan dalam BST, sehingga fungsi akan mengembalikan False
        return False
    
    if root.data ==key: #jika nilai pada node saat ini sama dengan nilai yang dicari, maka data ditemukan dalam BST, sehingga fungsi akan mengembalikan True
        return True
    
    if key < root.data: #jika nilai yang dicari lebih kecil dari nilai pada node saat ini, maka fungsi akan mencari di subtree kiri dengan memanggil dirinya sendiri secara rekursif dengan parameter root.left
        return search(root.left,key)    
    else: #jika nilai yang dicari lebih besar dari nilai pada node saat ini, maka fungsi akan mencari di subtree kanan dengan memanggil dirinya sendiri secara rekursif dengan parameter root.right
        return search(root.right,key) 
    
#uji pencarian
key = 40

if search(root,key):
    print("Data Ditemukan")
else:
    print("Data Tidak Ditemukan")

#Penjelasan
'''
Program di atas merupakan implementasi dari Binary Search Tree (BST) dalam bahasa Python.
BST adalah struktur data pohon biner yang memiliki sifat khusus, yaitu setiap node memiliki nilai yang lebih kecil dari
nilai pada node induknya di subtree kiri, dan nilai yang lebih besar di subtree kanan.

Pada program ini, terdapat tiga bagian utama yaitu:
1. BST = Bagian ini mendefinisikan kelas Node untuk merepresentasikan setiap node dalam BST, dan fungsi insert() untuk memasukkan data ke dalam BST sesuai dengan aturan yang berlaku.
2. Traversal Inorder = Bagian ini mendefinisikan fungsi inorder() untuk melakukan traversal terhadap BST secara inorder.
3. Search di BST = Bagian ini mendefinisikan fungsi search() untuk mencari data dalam BST.

Program ini secara singkat itu untuk mengisi BST dengan data, melakukan traversal inorder untuk menampilkan data dalam urutan yang benar, 
dan melakukan pencarian untuk memeriksa apakah suatu nilai ada dalam BST atau tidak.
'''