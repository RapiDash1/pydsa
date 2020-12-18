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


if __name__ == "__main__":
    array = [num+1 for num in range(10)]
    print(jugglingAlgorithm(array, 2))