angka = (1, 2, 3)

# contoh bukan cara unpack
x = angka[0]
y = angka[1]
z = angka[2]

print(x, y, z)

print("=============")

# unpack adalah cara mudah untuk memasukan elemen tuple kedalam sebuah variabel , seperti dalam contoh diatas

# contoh menggunakan cara unpack
a, b, c = angka
print(a, b, c)

print("=============")

# cara mengambil 1 elemen saja dari tuple
# _ = dipython dianggap variable yg tidak akan digunakan
_, d, _ = angka
print(d)


# ATAU
print("=============")

m, *n = angka
print(m)
