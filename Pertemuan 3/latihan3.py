# Node untuk Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data    # simpan nilai node
        self.next = None    # pointer ke node berikutnya
        self.prev = None    # pointer ke node sebelumnya

# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None    # awalnya list kosong

    # Tambah node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:   # jika list kosong, node baru jadi head
            self.head = new_node
            return

        temp = self.head
        while temp.next:    # cari node terakhir
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp    # hubungkan node baru ke node sebelumnya

    # Tampilkan isi DLL
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")  # tampilkan node
            temp = temp.next
        print("None")  # akhir list

    # Cari node berdasarkan nilai
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:   # ketemu node
                return True
            temp = temp.next
        return False   # tidak ketemu

# ===========================
# MAIN PROGRAM
# ===========================

dll = DoublyLinkedList()

# Input elemen dari user
elemen_str = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")
elemen_list = [int(x.strip()) for x in elemen_str.split(',')]

# Masukkan setiap elemen ke linked list
for val in elemen_list:
    dll.insert_at_end(val)

# Tampilkan DLL
dll.display()

# Input nilai yang ingin dicari
cari = int(input("Masukkan elemen yang ingin dicari: "))

# Cari dan tampilkan hasil
if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")
