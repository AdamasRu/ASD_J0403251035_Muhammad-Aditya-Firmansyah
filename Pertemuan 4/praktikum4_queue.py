#=======================================================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#=======================================================================================

#=======================================================================================
#implementasi dasar: node pada linked list
#=======================================================================================

from codecs import ignore_errors


class Node:
    def __init__ (self, data): #konstruktor
        self.data = data #Menyimpan nilai / data
        self.next = None #Pointer untuk node selanjutnya

#Queue dengan 2 pointer : head dan tail
class QueueLL:
    def __init__(self):
        self.head = None #node paling depan
        self.tail = None #node paling belakang

    def is_empty(self):
        return self.head is None

    def enqueque(self, data):
        #MEnambah data di belakang (tail)
        nodeBaru = Node(data)

        #jika queue kosong, head dan tail menunjuk ke node yang sama
        if self.is_empty(): 
            self.head = nodeBaru
            self.tail = nodeBaru
            return
        
        #jika queue tidak kosong : tail lama menunjuk ke node yang baru
        self.tail.next = nodeBaru
        #tail pindah ke node baru
        self.tail = nodeBaru

    def dequeue(self):
        #menghapus data dari depan

        #1. ambil data yang paling depan
        data_terhapus = self.head.data

        #2. geser head ke node berikutnya
        self.head = self.head.next

        #3. Jika setelah geser head menjadi none, maka queue kosong
        #tail juga harus jadi none
        if self.head is None:
            self.tail = None

        return data_terhapus

    def tampilkan(self): #menampilkan isi queue dari head ke tail
        current = self.head
        print("Head", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None -> Tail")

#Instantiasi objek class QueueLL
Q = QueueLL()
Q.enqueque("A")
Q.enqueque("B")
Q.enqueque("C")
Q.enqueque("D")
Q.tampilkan()
Q.dequeue()
Q.tampilkan()