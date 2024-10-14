def print_odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")

# Contoh penggunaan
n = int(input("Masukkan nilai n untuk bilangan ganjil: "))
print_odd_numbers(n)
2