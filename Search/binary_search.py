myList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targetValue = 5

def binarySearch(arr, target):
    n=len(arr)
    left =0
    right = n-1
    while left < right:
        middle = (left + right) //2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else: 
            right = middle - 1
    return middle


if __name__ == "__main__":
    result = binarySearch(myList, targetValue)
    print(result)
