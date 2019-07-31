def binarysearch(lst,key):
    low = 0
    high = len(lst) - 1
    while low <= high :
        mid = (low + high )// 2
        if lst[mid] == key:
            return mid
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

key = int(input("enter the key to be searched:"))
res = binarysearch([1,2,3,4,5,6,7],key)
if res == -1:
    print(f"{key} is not found")
else:
    print(f"{key} found at :{res}") 