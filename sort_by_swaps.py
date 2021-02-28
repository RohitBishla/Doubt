n=int(input())
A=[int(x) for x in input().split()]
number_of_swap=0

for i in range(len(A)): 
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j
            jth=j
              
    # Swap the found minimum element with  
    # the first element 
    if min_idx!=i:
        A[i], A[min_idx],number_of_swap = A[min_idx], A[i],number_of_swap+1
        ith=i
print(number_of_swap)
print(ith,jth)

def sort(a,count,b):
    
    for i in range(len(a)):
        swapped = False
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                count+=1
                c = len(b)
                b.append(j)
                   
                swapped = True
        if not swapped :
            print(count)
            print(*b)
            return

    return 


n = int(input())
a = [int(x) for x in input().split()]
sort(a,0,[])
# 
# i=0
# mid=n//2
# while i<mid:
#     j=n-1
#     that_number_at_i=li[i]
#     while j>mid:
#         if that_number_at_i>li[j]:
#             number_of_swap+=1
#             learn_i=i
#             learn_j=j
#             li[i],li[j]=li[j],li[i]
#         j-=1
#     i+=1
# print(number_of_swap)
# print(learn_i,learn_j)
# print(li)