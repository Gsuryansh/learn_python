"""def ArrayRotation(arr,d):
    temp=[]
    temp=arr[d:]+arr[:d]
    return temp
a=[1,2,3,4,5,6,7,8,9]
rotation_by=5
rotated_array=ArrayRotation(a,rotation_by)
print(rotated_array)
"""

"""def ArrayRotation(arr,d):

    for x in xrange(d):
        arr=LeftRotation(arr)
    return arr

def LeftRotation(arr):
    temp=arr[0]
    for i in range (len(arr)-1):
        arr[i]=arr[i+1]
    arr[i+1]=temp
    return arr
a=[1,2,3,4,5,6,7,8,9]
d=5
print(ArrayRotation(a,d))"""

"""In the above program we have rotated the array by one element at a time"""


