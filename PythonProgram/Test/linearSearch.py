def linearSearch(arr,element):
    for i in xrange(len(arr)):
        if arr[i]==element:
            return i
    return -1
arr=[1,2,3,2,33,43,23,45,67,87,65,12,567]
element=1
index=linearSearch(arr,element)
if index== -1:
    print("Element not found")
else:
    print("Element found %d" %(index))


"""Time complexity of this algorithm is o(n)"""