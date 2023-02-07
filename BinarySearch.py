import math
#  O(log(n)) time | O(1) space
def Binary_search(arr,targetNum):
    if len(arr) < 1:
        return None
    idxL,idxR = 0 , len(arr) - 1
    while idxL <= idxR:
        idxM = math.floor((idxL + idxR)/2)
        if arr[idxM] == targetNum:
            return True
        if arr[idxM] < targetNum:
            idxL = idxM + 1
        else:
            idxR = idxM - 1
    return False


list1 = [1,3,4,6,5,63,34,6376,36,342,24,5,-3536,464,234,999999,-999999]
list1.sort()
print(Binary_search(list1,-8))
    