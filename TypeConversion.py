# Type Conversion adalah mengubah suatu tipe data dari tipe ke satu ke tipe yang lain

tahun = input("tahun lahir : ")
print(type(tahun))
# inputan dari user selalu dianggap string

# mengubah variabel tahun menjadi tipe data integer dari tipe data string
tahun = int(tahun)
print(type(tahun))
umur = 2021 - tahun
print(umur)
# mengubah variabel umur menjadi tipe data string dari tipe data integer
print("umur kamu " + str(umur))
