def Print1ToMaxOfNDigits(n):
    highlimit = 10 ** n
    result = []
    for i in range(1, highlimit):
        result.append(i)
    return result

def Print1ToMaxOfNDigits_2(n):
    if n <= 0:
        return
    number = ["0" for _ in range(n)]
    for i in range(10):
        number[0] = str(i) #这里应该是外层循环，就是遍历的是最高位数
        Print1ToMaxOfNDigitsRecursively(number, n, 0)


def Print1ToMaxOfNDigitsRecursively(number, l, index):
    # 已经遍历到最后一位数字，则打印出该数字
    if index == l - 1:
        printNumber(number)
        return
    # 否则继续深度优先遍历
    for i in range(10):
        number[index + 1] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, l, index + 1)


def printNumber(number):
    done = False
    while number[0] == "0" and len(number) > 1:
        number = number[1:]
    print("".join(number), end=" ")


result = Print1ToMaxOfNDigits_2(3)
print(result)