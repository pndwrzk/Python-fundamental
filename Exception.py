# Exeption adalah cara untuk menghendle error
try:
    level = input("level kamu : ")
    level = int(level)
    level = level / 0
    print(level)
except ZeroDivisionError:
    print("Error tidak bisa di bagi 0")
except ValueError:
    # jika program error menjalankan ini
    print("yang kamu masukkan itu bukan angka")
#
