def merge(left_half,right_half, count):
    if left_half[0]>right_half[0]:
        count[0]+=1
        return left_half
    elif right_half[0]>left_half[0]:
        count[0]+=1
        return right_half
    return left_half



def merge_sort(arr, left, right,count):
    if(left >= right):
        # base case
        return [arr[left]] # or return [arr[right]]
    mid=(left+right)//2
    left_half = merge_sort(arr, left, mid,count) # recursively we extracted the left sorted half
    right_half = merge_sort(arr, mid+1, right,count) # recursively we extracted the right sorted half
    output=merge(left_half, right_half,count) # merged both the halfs
    return output
n=[int(x) for x in input().split()]
count=[0]
merge_sort(n,0,len(n)-1,count)
print(count[0])