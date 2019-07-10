def minNumberInRotateArray(rotateArray):
    # write code here
    i = 0
    j = len(rotateArray) - 1
    mid = i
    while rotateArray[i] >= rotateArray[j]:
        if j - i == 1:
            mid = j
            break
        mid = (i + j) // 2
        if rotateArray[i] == rotateArray[mid] and rotateArray[i] == rotateArray[j]:
            return MinInOrder(rotateArray, i, j)
        if rotateArray[mid] >= rotateArray[j]:
            i = mid
        else:
            j = mid
    return rotateArray[mid]


def MinInOrder(array, start, end):
    result = array[0]
    for i in array[start: end+1]:
        if i < result:
            result = i
    return result


print(minNumberInRotateArray(rotateArray=[1,0,1,1,1]))
