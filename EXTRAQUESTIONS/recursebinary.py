#recursive binary search

def binarysearch(lst,low,high,key):
    while low <= high :
        mid = (low + high )// 2
        if lst[mid] == key:
            return mid
        elif key > lst[mid]:
            return binarysearch(lst,mid+1,high,key)
        else:
            return(lst,low,mid - 1,key)
    return -1

key = int(input("enter the key to be searched:"))
res = binarysearch([1,2,3,4,5,6,7],0,7,key)
if res == -1:
    print(f"{key} is not found")
else:
    print(f"{key} found at :{res}") 