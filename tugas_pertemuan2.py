# Dictionary utama buat nyimpen semua data barang
data_dict = {}


def load_data():
    """
    Ambil data stok barang dari file 'stok_barang.txt'
    lalu masukin ke dictionary data_dict.
    """
    with open("stok_barang.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # Biar nggak ada newline atau spasi aneh
            kodeBr, namaBr, stokBr = baris.split(",")  # Pisahin data pakai koma
            
            # Simpan data ke dictionary
            data_dict[kodeBr] = {
                "Nama": namaBr,
                "Stok": int(stokBr)  # Stok diubah ke angka
            }

    return data_dict


def daftar_barang():
    """
    Nampilin semua barang yang ada
    lengkap dengan stoknya dalam bentuk tabel.
    """
    if len(data_dict) == 0:
        print("Data Kosong")
        return

    print("\n==== STOK BARANG ====")
    print(f"{'Kode':<10} | {'Nama':<12} | {'Stok':>5}")
    print("-" * 32)

    # Loop data yang sudah diurutkan berdasarkan kode barang
    for kodeBr in sorted(data_dict):
        Nama = data_dict[kodeBr]["Nama"]
        Stok = data_dict[kodeBr]["Stok"]
        print(f"{kodeBr:<10} | {Nama:<12} | {Stok:>5}")


def cari_barang():
    """
    Cari barang berdasarkan kode barang
    lalu tampilkan datanya kalau ketemu.
    """
    barang_cari = input("Masukan Kode dari barang yang ingin dicari: ").strip()

    if barang_cari in data_dict:
        nama = data_dict[barang_cari]["Nama"]
        stok = data_dict[barang_cari]["Stok"]

        print("\n==== Data Barang Ditemukan ====")
        print(f"KODE : {barang_cari}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        print("\nBarang tidak ditemukan")


def update_stok():
    """
    Mengubah jumlah stok barang
    berdasarkan kode barang yang dimasukkan.
    """
    kode = input("Masukan kode barang yang akan diupdate: ").strip()

    # Kalau kode nggak ada, langsung batal
    if kode not in data_dict:
        print("Kode barang tidak ditemukan, update dibatalkan")
        return

    try:
        stok_baru = int(input("Masukkan stok baru: ").strip())
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan")
        return

    stok_lama = data_dict[kode]["Stok"]   # Simpan stok lama buat info
    data_dict[kode]["Stok"] = stok_baru   # Ganti stok dengan yang baru

    print(f"Update berhasil. Stok {kode} berubah dari {stok_lama} jadi {stok_baru}")


def simpan_file():
    """
    Menyimpan semua data yang ada di dictionary
    ke file 'stok_barang.txt'.
    """
    with open("stok_barang.txt", "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["Nama"]
            stok = data_dict[kode]["Stok"]

            # Tulis ke file dengan format: kode,nama,stok
            file.write(f"{kode},{nama},{stok}\n")

    print("\nData berhasil disimpan ke file")


def tambah_barang():
    """
    Nambahin barang baru ke dalam sistem.
    """
    kode = input("Masukkan kode barang baru: ").strip()

    # Cek dulu, jangan sampai kodenya dobel
    if kode in data_dict:
        print("Kode barang sudah ada. Tambah barang dibatalkan.")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        stok = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka. Tambah barang dibatalkan.")
        return

    # Masukkan barang baru ke dictionary
    data_dict[kode] = {
        "Nama": nama,
        "Stok": stok
    }

    print(f"Barang '{nama}' dengan kode {kode} berhasil ditambahkan")


# Load data dari file saat program pertama kali dijalankan
load_data()


# Loop utama program (menu)
while True:
    print("\n==== STOK BARANG KANTIN ====")
    print("Opsi Fitur")
    print("1. Daftar Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Simpan ke File")
    print("0. Keluar")

    try:
        A = int(input("Masukan Opsi Menu (1-5 dan 0): "))

        if A in [0, 1, 2, 3, 4, 5]:
            if A == 1:
                daftar_barang()
            elif A == 2:
                cari_barang()
            elif A == 3:
                tambah_barang()
            elif A == 4:
                update_stok()
            elif A == 5:
                simpan_file()
            elif A == 0:
                print("Program berakhir. Terima kasih 👍")
                break
        else:
            print("Menu tidak tersedia, silakan pilih menu yang benar\n")

    except ValueError:
        print("Input harus berupa angka!\n")
