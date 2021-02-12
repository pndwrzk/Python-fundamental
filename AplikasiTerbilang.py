# mentranslate angka menjadi kata

angka = input("Masukan angka : ")


angka_mapping = {
    "1": "satu",
    "2": "dua",
    "3": "tiga",
    "4": "empat",
    "5": "lima",
    "6": "enam",
    "7": "tujuh",
    "8": "delapan",
    "9": "sembilan",
    "10": "sepuluh",
}

output = ""

for a in angka:
    terbilang = angka_mapping.get(a, "invalid!")
    output = output + terbilang + " "

print(output)
