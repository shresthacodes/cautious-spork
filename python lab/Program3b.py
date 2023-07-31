# WAP to find the string similarity between two given strings
import difflib


def similarity(str1, str2):
    count = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    return count.ratio()


str1 = input(">")
str2 = input(">")
print(similarity(str1, str2))
