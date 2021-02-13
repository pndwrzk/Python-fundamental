import random

# hasilnya bisa jadi bukan integeer
print(random.random())


# hasilnya integer dengan parameter 1 = batas angak bawa, parameter 2 = batas angka atas
for Index in range(6):
    # mencetak 6 kali angka random
    print(random.randint(10, 30))


print("=================")
users = ["rizki", "pandiwa", "agung", "bimo", "oco", "elang", "mustopa"]
# memilih user secara random
batas_bawah = 0
batas_atas = len(users) - 1
random_int = random.randint(batas_bawah, batas_atas)
winner = users[random_int]
print(winner)

# diatas adalah cara muter muter
# dibawah cara lebih mudah
print("=================")
winner1 = random.choice(users)
print(winner1)
