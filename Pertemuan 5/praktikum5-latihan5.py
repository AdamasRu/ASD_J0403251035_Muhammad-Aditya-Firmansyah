#===================================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : TPL B2
#===================================================

#===================================================
#Praktikum 5 : Latihan 5
#===================================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)


# =======================
# Diskusi dan Penjelasan
# =======================

# Saat ini program mengizinkan angka yang sama muncul berulang
# Contoh hasil: 000, 011, 222, dll
# Karena setiap posisi selalu bisa memilih "0", "1", atau "2"
# tanpa memperhatikan apakah angka tersebut sudah dipakai sebelumnya

# Bagaimana mencegah angka yang sama muncul berulang?
# Kita harus memastikan angka yang dipilih belum ada di dalam string "hasil"
# sebelum melakukan rekursi,
# tambahkan pengecekan seperti:
# if angka not in hasil:
#     buat_pin(panjang, hasil + angka)
# Dengan cara ini:
# - Jika angka sudah pernah dipakai, tidak dipilih lagi
# - Setiap digit hanya muncul satu kali

# Jadi intinya:
# Tambahkan pengecekan agar angka yang dipilih
# tidak ada di dalam hasil sebelumnya