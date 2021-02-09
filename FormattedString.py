nama_depan = "Rizki"
nama_belakang = "Pandiwa"

# menggunakan concat
pesan = nama_depan + " [" + nama_belakang + "]"


# f adalah formatted string
print(pesan)

pesan = f"{nama_depan} [{nama_belakang}]"
print(pesan)

print("====================")
# menggabukan kan string dengan integer tanpa merubah tipe data pada variabel umur dari integer menjadi string
umur = 22
pesan = f"umur kamu {umur}"
print(pesan)
