# (+ - / *)
comand = ""

while comand != "exit":
    comand = input("perintah : ")

    if comand == "exit":
        break

    if comand != "+" and comand != "-" and comand != "*" and comand != "/":
        print("perintah tidak dikenali")
        continue
        # contine memaksa program untuk kembali ke looping, tanpa menjalan kode kode dibawahnya

    a = int(input("angka pertama : "))
    b = int(input("angka kedua : "))

    if comand == "+":
        hasil = a + b
    elif comand == "-":
        hasil = a - b
    elif comand == "*":
        hasil = a * b
    elif comand == "/":
        hasil = a/b

    print(f"hasil : {hasil}")

print("terima kasih sudah menggunakan aplikasi kami")
