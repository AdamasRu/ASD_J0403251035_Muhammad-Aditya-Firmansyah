#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Tugas Hands-On : Sistem Antrian Bengkel Motor
#===================================================

# Class Node merepresentasikan satu pelanggan dalam antrian
class Node:
    def __init__(self, no, nama, servis):
        self.no = no            # Nomor antrian pelanggan
        self.nama = nama        # Nama pelanggan
        self.servis = servis    # Jenis servis
        self.next = None        # Pointer ke node berikutnya


# Class QueueBengkel mengelola antrian berbasis Linked List
class QueueBengkel:
    def __init__(self):
        self.front = None   # Pointer ke pelanggan terdepan (FIFO)
        self.rear = None    # Pointer ke pelanggan terakhir

    # Method untuk menambahkan pelanggan ke antrian (enqueue)
    def enqueue(self, no, nama, servis):
        baru = Node(no, nama, servis)  # Membuat node baru
        
        # Jika antrian kosong
        if self.rear is None:
            self.front = self.rear = baru
        else:
            # Hubungkan node terakhir ke node baru
            self.rear.next = baru
            self.rear = baru
        
        print("Pelanggan berhasil ditambahkan ke antrian.")

    # Method untuk melayani pelanggan terdepan (dequeue)
    def dequeue(self):
        # Jika antrian kosong
        if self.front is None:
            print("Antrian kosong. Tidak ada pelanggan untuk dilayani.")
            return
        
        # Simpan data pelanggan terdepan
        layani = self.front
        
        # Geser front ke node berikutnya
        self.front = self.front.next
        
        # Jika setelah dequeue antrian menjadi kosong
        if self.front is None:
            self.rear = None
        
        print("Melayani Pelanggan:")
        print(f"No Antrian : {layani.no}")
        print(f"Nama       : {layani.nama}")
        print(f"Servis     : {layani.servis}")

    # Method untuk menampilkan seluruh antrian (traversal)
    def tampilkan(self):
        # Jika antrian kosong
        if self.front is None:
            print("Antrian masih kosong.")
            return
        
        print("\nDaftar Antrian Pelanggan:")
        current = self.front   # Mulai dari node terdepan
        
        # Traversal hingga node terakhir
        while current:
            print("--------------------------")
            print(f"No Antrian : {current.no}")
            print(f"Nama       : {current.nama}")
            print(f"Servis     : {current.servis}")
            current = current.next


# Fungsi utama program
def main():
    q = QueueBengkel()
    
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)
        
        elif pilih == "2":
            q.dequeue()
        
        elif pilih == "3":
            q.tampilkan()
        
        elif pilih == "4":
            print("Program selesai. Terima kasih.")
            break
        
        else:
            print("Pilihan tidak valid")


# Menjalankan program
if __name__ == "__main__":
    main()