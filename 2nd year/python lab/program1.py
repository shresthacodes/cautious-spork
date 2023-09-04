# WAP to find the best of two average test marks out of 3 test marks accepted from the user
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
tl = a+b+c
min = min(a, b, c)
b_a = tl-min
avg = b_a/2
print("Best of two average test marks out of 3 test marks is: ", avg)
