angka = [1, 2, 3, 4, 5]
print(angka)

# append = menambahkan elemen ke dalam array
angka.append(6)
print(angka)
print("=======")

# insert = menambahkan elemen ke dalam array dengan mengatur index arraynya
# parameter 1 =index yang ingin di isi
# parameter 2 = objek yg ingin dimasukkan
angka.insert(2, 11)
print(angka)
print("=======")

# pop = mengapus elemen
# parameter = index yang akan di apus
angka.pop(0)
print(angka)
print("=======")

# remove = mengapus elemen
# parameter = objek yang akan di apus
angka.remove(4)
print(angka)
print("=======")

angka.sort()
print(angka)
