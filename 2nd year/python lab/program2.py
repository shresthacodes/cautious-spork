# Program to find the sum of fibonacci series

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter value of n: "))
if n < 1:
    print("Number should be greater than 0")

else:
    print(fibonacci(n))

# Convert binary to decimal, octal to hexadecimal
n = str(input("Enter value of binary : "))
def btd(n):
    dec = int(n, 2)
    print("Decimal Value is : ", dec)

num = str(input("Enter value of Octal : "))
def oth(n):
    hexa = hex(int(n, 8))
    print("Hexadecimal Value is : ", hexa.replace("0x", ""))
if all(char in '01' for char in n):
    btd(n)
else:
    print("input not valid")
if all(char in '01234567' for char in n):
    oth(n)
else:
    print("input not valid")