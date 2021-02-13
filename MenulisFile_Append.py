# fungsi open
# parameter 1 = nama filenya
# parameter 2 =  mode

# mode mode :
# r = read = membaca file
# w = write = menulis ke sebuah file , jika file sudah ada isinya , maka isi tersebut akan di tiban
# a = append = menambahkan data ke dalam file
# r+ = user bisa baca dan bisa nulis

user = open("user.txt", "a")
# cara menbahkan text pada baris baru paling bawah
user.write("\nlink - link")

# mengetahui sebuah file bisa ditulis atau tidak , jika output true = bisa ,bisa tidaknya tegantung dengan mode yg digunakan
print(user.writable())

# jika sudah tidak digunakan maka file tutup gembali ,dengan cara di bawah ini
user.close()
