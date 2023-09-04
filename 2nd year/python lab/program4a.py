# Insertion sort and merge sort


l = input("Enter the list of numbers: ")
ls = [int(num) for num in l.split()]
print("Unsorted array:", ls)
# for insertionsort


def insertionsort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i-1

        while j >= 0 and key < ls[j]:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = key
    print("Sorted list ", ls)


# Mergesort

def mergesort(ls):
    print(ls)
    print(" ")
    # dividing left and right part of the list
    if len(ls) > 1:
        mid = len(ls)//2
        llist = ls[:mid]
        mergesort(llist)
        rlist = ls[mid:]

        mergesort(rlist)
        i = j = k = 0
        while i < len(llist) and j < len(rlist):
            if llist[i] < rlist[j]:
                ls[k] = llist[i]
                i += 1
                k += 1
            else:
                ls[k] = rlist[j]
                j += 1
                k += 1

        while i < len(llist):
            ls[k] = llist[i]
            i += 1
            k += 1

        while j < len(rlist):
            ls[k] = rlist[j]
            j += 1
            k += 1
    print("Sorted list:\n", ls)


a = int(input("Enter the choice 1: insertion sort and 2: mergesort: "))
if a == 1:
    insertionsort(ls)
elif a == 2:
    mergesort(ls)
