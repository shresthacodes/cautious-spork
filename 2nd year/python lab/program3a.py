# WAP that accepts the sentence and find the number of words, digits,uppercase letters & lowercase letters.
sen = input(">")
print("Given sentence:", sen)
words = sen.split()
n = len(words)
num = uc = lc = 0
print("Number of words is ", n)
for i in sen:
    if i.isdigit():
        num = num+1
    elif i.isupper():
        uc = uc+1
    elif i.islower():
        lc = lc+1

print("Number of digits is ", num)
print("Number of uppercase letters is ", uc)
print("Number of lowercase letters is ", lc)
