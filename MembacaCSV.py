# file CSV adalah file yang isinya dipisah dengan tanda koma
import csv

user = open("user.csv", "r")
# delimiter adalah = pemisah nya
user_csv = csv.reader(user, delimiter=",")
for row in user_csv:
    print(f"nama : {row[0]} , Username: {row[1]} , role : {row[2]}")
user.close()
