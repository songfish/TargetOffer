# 数组中的重复数字
def duplicate(numbers):
    # write code here
    if numbers == []:
        return False
    count = dict()
    for i in numbers:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    if set(list(count.values())) == {1}:
        # print(set(count.values()))
        return False
    for value in count.values():
        if value > 1:
            print(value)
            return True


def duplicate2(numbers):
    length = len(numbers)
    for i in range(length):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                return True
            temp = numbers[i]
            numbers[i] = numbers[temp]
            numbers[temp] = temp


j = duplicate([2,1,3,0,4])
print(j)