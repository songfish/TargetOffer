# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # if matrix == 0 or rows <= 0 or columns <= 0:
        #     return
        rows = len(matrix)
        columns = len(matrix[0])
        result = []
        def PrintMatrixInCircle(start):
            endX = columns - 1 - start
            endY = rows - 1 - start
            for i in range(start, endX + 1):
                result.append(matrix[start][i])
            if start < endY:
                for i in range(start + 1, endY + 1):
                    result.append(matrix[i][endX])
            if start < endY:
                for i in range(endX - 1, start - 1, -1):
                    result.append(matrix[endY][i])
            if start < endX and start < endY - 1:
                for i in range(endY - 1, start, -1):
                    result.append(matrix[i][start])

        start = 0
        while columns > start * 2 and rows > start * 2:
            PrintMatrixInCircle(start)
            start += 1
        return result


s = Solution()
# print(s.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
# print(s.printMatrix([[1]]))
print(s.printMatrix([[1],[2],[3],[4],[5]]))
# print(s.printMatrix([[1,2,3,4,5]]))