n,m=map(int,input().split())
li=[int(x) for x in input().split()]

li.sort()

while m!=n:
    # Checking difference between first element and second last element, and second element with last element
    # Than remove one element from list from which difference is maximum untile length of list is equal to n. 
    if li[m-2]-li[0]>li[m-1]-li[1]:
        li.pop(0)
        m-=1
    else:
        li.pop(m-1)
        m-=1
print(li[m-1]-li[0])
