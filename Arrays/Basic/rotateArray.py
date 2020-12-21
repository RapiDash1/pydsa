# Example - 
# array - [1, 2, 3, 4, 5]
# rotated array - [4, 5, 1, 2, 3]

def rotateArray(array, shiftBy):
    shiftBy %= len(array) 
    return array[shiftBy:] + array[:shiftBy]


def jugglingAlgorithm(array, shift):
    arrayLen = len(array)
    shift %= len(array)
    arrayGcd = gcd(shift, arrayLen)

    for pos in range(arrayGcd):
        initElementValue = array[pos]
        elementPos = pos
        while True:
            nextElementPos = elementPos + shift
            if nextElementPos >= arrayLen:
                nextElementPos = nextElementPos - arrayLen
            if nextElementPos == pos:
                break
            array[elementPos] = array[nextElementPos]
            elementPos = nextElementPos
        array[elementPos] = initElementValue
    
    return array


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(a, a%b)


def reverse(array, low, high):
    a = low
    b = high

    while a < b:
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1


def reversalAlgorithm(array, shift):
    shift %= len(array)
    reverse(array, 0, len(array)-1)
    reverse(array, len(array)-shift, len(array)-1)
    reverse(array, 0, len(array)-1-shift)
    return array


def cyclicRotate(array):
    initElement = array[0]

    for pos in range(len(array)-1):
        array[pos] = array[pos+1]
    
    array[-1] = initElement

    return array


if __name__ == "__main__":
    array = [num+1 for num in range(10)]
    print(cyclicRotate(array))