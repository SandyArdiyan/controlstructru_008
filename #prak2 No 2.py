#prak2 No 2
def bilangan_terbesar(a, b, c):
    return max(a, b, c)

a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
c = float(input("Masukkan bilangan ketiga: "))

print("Bilangan terbesar adala:",bilangan_terbesar(a, b, c))