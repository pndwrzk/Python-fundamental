# Exeption adalah cara untuk menghendle error
try:
    level = input("level kamu : ")
    level = int(level)
    level = level / 0
    print(level)
# erorr hendle secara general ,bisa digunakan di semua error
except:
    print("Terjadi kesalahan")
