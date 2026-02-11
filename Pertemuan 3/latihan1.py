# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Nilai tidak ditemukan.")
            return

        prev.next = temp.next
        print(f"Node dengan nilai {key} berhasil dihapus.")


# ==========================================================
# PROGRAM UTAMA
# ==========================================================

ll = LinkedList()

# Input data dari user
A = int(input("Masukan jumlah Data: "))

for i in range(A):
    data = int(input("Masukkan data: "))
    ll.insert_at_end(data)

print("\nLinked List awal:")
ll.display()

hapus = int(input("Masukkan nilai yang ingin dihapus: "))
ll.delete_node(hapus)

print("\nLinked List setelah penghapusan:")
ll.display()