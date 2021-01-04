# [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]

def pivot(array):
    low = 0
    high = len(array)-1

    while low < high:
        mid = (low+high)//2
        if array[mid] <= array[mid+1]:
            if array[mid] < array[0]:
                high = mid
            else:
                low = mid
        else:
            return mid

def binarySearch(array, element):
    low = 0
    high = len(array)-1

    if array[low] == element:
        return low

    if array[high] == element:
        return high

    while low < high:
        mid = (low+high)//2

        if array[mid] > element:
            high = mid
        elif array[mid] < element:
            low = mid
        else:
            return mid

    return low


def search(array, element):
    pivotPos = pivot(array)
    if element < array[pivotPos]:
        if element >= array[0]:
            return binarySearch(array[:pivotPos], element)
        else:
            return binarySearch(array[pivotPos+1:], element)+(pivotPos+1)
    return pivotPos


if __name__ == "__main__":
    print(search([5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 3))