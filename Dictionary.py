# Dictionary adalah sebuah struktur data yang bisa menyimpan data dalam bentuk key/kunci dan value

user = {
    "nama": "Rizki Pandiwa",
    "umur": 21,
    "is_admin": True
}

# mengambil data nama
nama = user["nama"]
print(nama)
print("==========")

# menghidari error jika mengases data yang keynya tidak terdaftar
# parameter 1 pada method get adalah key yang ingin dicari
# parameter 2 pada method get adalah outpot apabila key yang dicari tidak ada
# apabila parameter 2 tidak ada maka , output menjadi none
username = user.get("username", "username tidak ada")
print(username)
print("==========")


# menambahkan key baru
user["hobi"] = "traveling"
print(user)
print("==========")

# mengganti value
user["umur"] = 19
print(user)
print("==========")
