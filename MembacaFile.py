# fungsi open
# parameter 1 = nama filenya
# parameter 2 =  mode

# mode mode :
# r = read = membaca file
# w = write = menulis ke sebuah file , jika file sudah ada isinya , maka isi tersebut akan di tiban
# a = append = menambahkan data ke dalam file
# r+ = user bisa baca dan bisa nulis

user = open("user.txt", "r")

# print(user.read())  # mencetak semua isi dalam file
# user.readable()  #mengetahui sebuah file bisa dibaca atau tidak , jika output true = bisa ,bisa tidaknya tegantung dengan mode yg digunakan


print("==========================")
# print(user.readline())  # mencetak baris perbaris = baris pertama
# print(user.readline())  # baris kedua
# print(user.readline())  # baris ketiga
print("==========================")

index = 1
user = user.readlines()  # mengembalikan sebuah list / array
for u in user:
    print(f"no:{index} - {u}")
    index += 1

# jika sudah tidak digunakan maka file tutup gembali ,dengan cara di bawah ini
user.close()
