def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Contoh penggunaan
n = int(input("Masukkan nilai n untuk pola: "))
print_pattern(n)
10