def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# Contoh penggunaan
n = int(input("Masukkan nilai n untuk deret Fibonacci: "))
fibonacci(n)
