# jika sebuah fungsi memiliki paramater ,maka pada saat memanggil paramaternya tidak boleh kosong


def hallo(nama):
    # hasil parameter seperti variable biasa
    # nama = "Pandiwa"

    print(f"Hallo {nama}")


# memanggil function hallo dengan isi para meter "Pandiwa"
# jika kita memanggil sebuah fungsi diharuskan memperhatikan urutan parameternya,karna penempatan penulisan parameternya mempengaruhi variable yang menerima
hallo("Pandiwa")
print("=========")
hallo("Rizki")
