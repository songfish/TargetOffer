# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [0] * (rows * cols)
        count = self.movingCountCore(threshold,rows,cols,0,0,visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if 0 <= row < rows and 0 <= col < cols and self.getDigitSum(row)+self.getDigitSum(col) <= threshold and not visited[row*cols+col]:
            return True
        return False

    def getDigitSum(self,number):
        s = 0
        while (number > 0):
            s += number % 10
            number = number // 10
        return s

    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row*cols+col] = True
            count = 1 + self.movingCountCore(threshold, rows, cols, row, col-1, visited)\
                    + self.movingCountCore(threshold, rows, cols, row-1, col, visited)\
                    + self.movingCountCore(threshold, rows, cols, row, col+1, visited)\
                    + self.movingCountCore(threshold, rows, cols, row+1, col, visited)
        return count


s = Solution()
result = s.movingCount(5,10,10)
print(result)
