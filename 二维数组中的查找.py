# 二维数组中的查找
def Find(target, array):
    row = len(array)
    column = len(array[0])
    for i in range(column):
        # print('i={}'.format(i))
        for j in range(row):
            # print('j={}'.format(j))
            if array[i][j] == target:
                return True
            else:
                j += 1
        i += 1
    return False


def Find2(target, array):
    row = len(array)
    column = len(array[0])
    i = 0
    j = column - 1
    while i < row and j >= 0:
        if array[i][j] == target:
            return True
        elif array[i][j] > target:
            j -= 1
        else:
            i += 1
    return False

def Find3(target, array):
    row = len(array)
    column = len(array[0])
    i = row - 1
    j = 0
    while i >=0 and j < column:
        if array[i][j] == target:
            return True
        elif array[i][j] < target:
            j += 1
        else:
            i -= 1
    return False
f = Find3(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
print(f)
