#praktikum 2: konsep adt dan file handling (studi kasus)
#latihan 1: Membuat fungsi load data

nama_file = "data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {}
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
        
            #simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {       #key
                "nama": nama,         #value
                "nilai": int(nilai)   #value
            }

    return data_dict

#manggil fungsi baca_data_mahasiswa
buku_data = baca_data_mahasiswa(nama_file)
#print("jumlah data terbaca", len(buku_data))


#latihan 2: membuat fungsi menampilkan data
def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("Data Kosong")
        return 
    
    #membuat header tabel
    print("\n==== Data Mahasiswa ====")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32)

    for nim in sorted(data_dict):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

#memanggil fungsi menampilkan data
#tampilkan_data(buku_data)

#latihan 3: Membuat fungsi mencari data
def cari_data(data_dict):
    #mencari data mahasiswa berdasarlan NIM
    nim_cari = input("Masukan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")

    else:
        print("\nData tidak ditemukan")

#cari_data(buku_data)

#Latihan 4:membuat fungsi update nilai
def update_nilai(data_dict):
    nim = input("Masukan NIM mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buku_data)

#Latihan 5 : Membuat fungsi menyimpan perubahan data ke file

def simpan_data(nama_file,data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file,buku_data)
#print("Data Berhasil Disimpan")

#latihan 6: Membuat menu
def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("\n=== MENU DATA MAHASISWA===")
    print("1. Tampilkan semua dAta")
    print("2. Cari data MahasiswA berdasarkan NIM")
    print("3. Update Nilai Mahasiswa")
    print("4. Simpan data ke file")
    print("0. Keluar")

    pilihan = input("Pilihan menu: ").strip()

    if pilihan == "1":
        tampilkan_data(buku_data)

    elif pilihan == "2":
        cari_data(buku_data)

    elif pilihan == "3":
        update_nilai(buku_data)

    elif pilihan == "4":
        simpan_data(nama_file, buku_data)
        print("Data berhasil disimpan")

    elif pilihan == "0":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid, coba lagi")

if __name__ == "__main__":
    main()        