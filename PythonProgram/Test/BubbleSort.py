def bubble_sort(arr):
    n=len(arr)
    for i in xrange(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
arr=[7,6,8,4,2,3,1,56,89,45,78]
print(bubble_sort(arr))
