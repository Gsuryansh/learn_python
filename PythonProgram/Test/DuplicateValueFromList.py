"""Program to remove duplicate value from the string"""
def remove_duplicate(arr):
    i=0
    l=len(arr)-1
    while i<l:
        j=i+1
        while j<l+1:
            if arr[i]==arr[j]:
                del arr[j]
                l=len(arr)-1
                j += 1
            else:
                j+=1
        print(i)
        i+=1
    return arr


arr=[1,1,1,1,1,1,1]
print(remove_duplicate(arr))

