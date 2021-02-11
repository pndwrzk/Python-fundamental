angka = [1, 2, 3, 4, 5, 6, 7, 8]

angka_max = max(angka)
print(angka_max)
print("==============")

angka.sort()
# index -1 adalah elemen paling akhir
angka_max = angka[-1]
print(angka_max)
print("==============")


angka_max = angka[0]
for a in angka:
    if a > angka_max:
        angka_max = a
print(angka_max)
