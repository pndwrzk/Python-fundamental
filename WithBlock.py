# with = memastikan file yang dibuka untuk ditutup kembali (auto tutup file jika developer lupa ,atau pun terdapat error saat di tengah proses)

# file CSV adalah file yang isinya dipisah dengan tanda koma
import csv

with open("user.csv", "r") as user:
    # delimiter adalah = pemisah nya
    user_csv = csv.reader(user, delimiter=",")
    for row in user_csv:
        print(f"nama : {row[0]} , Username: {row[1]} , role : {row[2]}")
