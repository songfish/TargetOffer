def cut(length):  # 动态规划
    l = [0,1,2,3]
    if length == 0:
        return 0
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    for i in range(4, length+1):
        max = 0
        for j in range(1, i//2 + 1):
            product = l[j] * l[i-j]
            if max < product:
                max = product
        l.append(max)
    max = l[length]
    return max


def cut_1(length): # 贪婪算法
    if length == 0:
        return 0
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 3
    timesof3 = length // 3
    if length - timesof3 * 3 == 1:
        timesof3 -= 1
    timesof2 = (length - timesof3 * 3) // 2
    return (3 ** timesof3) * (2 ** timesof2)


def cut_2(length): # 贪婪算法
    if length == 0:
        return 0
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 3
    if length % 3 == 1: # 如果余数是1，那么就是把1个3和1并起来分成2*2
        num = length // 3 - 1
        return 3 ** num * 4
    if length % 3 == 2:
        num = length // 3
        return 3 ** num * 2
    return 3 ** (length // 3)   # 其他的情况，即余数为0


result = cut_2(8)
print(result)
