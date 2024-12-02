# Easy Fibonacci Series

n = int(input("How many Fibonacci numbers do you want? "))

a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b
