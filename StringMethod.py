judul = "Belajar Python"

# method dan function string

# len = mengetahui jumlah banyak karakter
# Upper = membuat huruf menjadi kapital
# lower = membuat huruf menjadi kecil
# capitalize = membuat huruf paling awal menjadi kapita
# title = membuat huruf awal di tiap kata menjadi kapital
# replace = mengganti kata (case sensitif)
# in = mengecek kata (case sensitif) ,output true jika ada yang salah, false jika tidak ada yang sama

length = len(judul)  # function
kapital = judul.upper()  # method
kecil = judul.lower()
kapital_awal = judul.capitalize()
kapital_kata = judul.title()
mengganti = judul.replace("Python", "php")

kata = "Python"
cek = kata in judul

print(length)
print(kapital)
print(kecil)
print(kapital_awal)
print(kapital_kata)
print(mengganti)

print(cek)
