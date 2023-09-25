import re

def isPhoneNumber(numstr):
    for i in range(len(numstr)):
        if i==3 or i==7:
            if numstr[i] != '-':
                return False
        else:
            if numstr[i].isdigit():
                continue
            else:
                return False
    return True

def isPhRegex(numstr):
    ph_pat = re.compile(r"\d{3}-\d{3}-\d{4}$")

    if ph_pat.match(numstr):
        return "It is a phone number"
    return False

numstr = input("Enter a phone no. : ")
ch=int(input("enter the choice 1 or 2: "))
if ch==1:

    print(isPhoneNumber(numstr))
if ch==2:

    print(isPhRegex(numstr))
