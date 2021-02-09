# operatorprecedence = operasi yang akan didahulukan

# pengapitan tanda kurung didahulukan  terlebih dahulu dari perpangkatan
# perpangkatankan akan didahulukan dari perkalian atau pembagian
# perkalian atau pembagian akan didahulukan dari pada penjumlahan atau pengurangan

hitung = 2 + 10 * 5 ** (2 + 6)
# 2 + 6 dihitung dahulu
# hasil penjumlahan dipangkatkan dengan 5
# hasil perpangkatan * 10
# hasil perkalian + 2
print(hitung)
