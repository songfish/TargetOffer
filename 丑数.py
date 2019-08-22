class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == None and len(index) <= 0:
            return 0

        uglyNumbers = [1]*index
        nextIndex = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while nextIndex < index:
            minVal = min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, uglyNumbers[index5]*5)
            uglyNumbers[nextIndex] = minVal

            while uglyNumbers[index2]*2 <= uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3]*3 <= uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5]*5 <= uglyNumbers[nextIndex]:
                index5 += 1
            nextIndex += 1

        return uglyNumbers[-1]

s = Solution()
print(s.GetUglyNumber_Solution(11))


