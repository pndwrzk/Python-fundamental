message = input(">>> : ")

emoji_mapping = {
    ":)": "😊",
    ":(": "🥺",
    ":D": "😂"
}

# memecah kalimat menjadi sebuah 1 kata 1 kata  dalam array
words = message.split(" ")

output = ""

for w in words:
    output = output + emoji_mapping.get(w, w) + " "

print(output)
