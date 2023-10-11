def merge_list(list1: list[int], list2: list[int] ) -> list[int]:
    newList = list1 + list2
    x = all(isinstance(x, int) for x in newList)
    if x == False:
        raise ValueError("All values in the list should be Interger")
    else:  
        newList = mergeSort(newList)
        return newList

'''
I would use Merge Sort Algorithm for quick and more stable sorting for long unsorted liat
In average, time-complexity for this sorting algorithm is O(nlogn)
'''
def mergeSort(a: list[int]):
    if len(a) <= 1 :
        return
    
    mid = len(a)//2
    
    left = a[:mid]
    right = a[mid:] 
    
        
    mergeSort(left)
    mergeSort(right)
    
    merge(left,right,a)
    return a


def merge(left: list[int], right: list[int], a: list[int]):
    leftIndex = 0
    rightIndex = 0
    j = 0 # next open position in a
    m = len(left)
    n = len(right)
    
    while leftIndex < m and rightIndex < n:
        if left[leftIndex] <= right[rightIndex]:
            a[j] = left[leftIndex]
            leftIndex += 1
        else:
            a[j] = right[rightIndex]
            rightIndex += 1
        j += 1
        
    while leftIndex < m:
        a[j] = left[leftIndex]
        j += 1
        leftIndex += 1
        
    while rightIndex < n:
        a[j] = right[rightIndex]
        j += 1
        rightIndex += 1

