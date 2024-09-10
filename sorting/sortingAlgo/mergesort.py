def mergesort(mylist):
    n = len(mylist)
    if n>1:
        list1 = mylist[n//2:]
        list2 = mylist[:n//2]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)

def merge(list1, list2, mylist):
    i1 = 0
    i2 = 0
    while i1 + i2 < len(mylist):
        if i1 == len(list1):
            mylist[i1+i2]=list2[i2]
            i2 +=1
        elif i2 == len(list2):
            mylist[i1+i2]=list1[i1]
            i1+=1
        elif list1[i1]>list2[i2]:
            mylist[i1+i2]=list2[i2]
            i2 +=1
        else:
            mylist[i1+i2]=list1[i1]
            i1+=1

