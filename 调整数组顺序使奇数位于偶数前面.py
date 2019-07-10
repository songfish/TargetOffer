# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        result = []
        odd = []
        even = []
        for data in array:
            if data % 2 == 0:
                even.append(data)
            else:
                odd.append(data)
        result.extend(odd)
        result.extend(even)
        return result
        # return odd+even

    def reOrderArray1(self,array):
        if len(array) < 1:
            return
        elif len(array) == 1:
            return array

        front = 0
        rear = len(array) - 1
        while front <= rear:
            while array[front] & 0x1 == 1:
                front += 1
            while array[rear] & 0x1 == 0:
                rear -= 1
            array[front], array[rear] = array[rear], array[front]
        array[front], array[rear] = array[rear], array[front]
        return array


s = Solution()
result = s.reOrderArray1([1,2,3,4,5,6,7])
print(result)
