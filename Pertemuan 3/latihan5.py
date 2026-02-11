# Node untuk single linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Tambah node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Tampilkan linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Balik linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev  

# ===========================
# MAIN PROGRAM
# ===========================

ll = LinkedList()

# Input dan masukkan data
elemen_str = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")
elemen_list = [int(x.strip()) for x in elemen_str.split(',')]
for val in elemen_list:
    ll.insert_at_end(val)

# Tampilkan sebelum dan sesudah dibalik
print("\nLinked List sebelum dibalik:")
ll.display()

ll.reverse()

print("\nLinked List setelah dibalik:")
ll.display()
