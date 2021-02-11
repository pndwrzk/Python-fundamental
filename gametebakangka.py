mencoba = 0
angka_rahasia = 4
batas = 3

while mencoba < batas:
    inputnumber = input("masukan angka : ")
    inputnumber = int(inputnumber)

    if inputnumber == angka_rahasia:
        print("====================")
        print("selamat kamu menang")
        break
        # break memaksa program untuk berhenti
    elif mencoba == 2 and inputnumber != angka_rahasia:
        print("====================")
        print("kamu kalah")

    mencoba += 1
