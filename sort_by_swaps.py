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