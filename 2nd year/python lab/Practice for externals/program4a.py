def merge(nlist):
    print("Unsorted list:",nlist)
    if len(nlist)>1:
        mid=len(nlist)//2

        llist=nlist[:mid]
        rlist = nlist[mid:]
        merge(llist)
        merge(rlist)
        i=j=k=0
        while i<len(llist) and j<len(rlist):
            if llist[i]<rlist[j]:
                nlist[k]=llist[i]
                i=i+1
            else:
                nlist[k]=rlist[j]
                j=j+1
            k=k+1

        while i<len(llist):
            nlist[k]=llist[i]
            i=i+1
            k=k+1
        while j<len(rlist):
            nlist[k]=rlist[j]
            j=j+1
            k=k+1
    print("merging",nlist)


n=input("enter the numbers with spaces:")
nlist=[int(num) for num in n.split()]
merge(nlist)
print(nlist)