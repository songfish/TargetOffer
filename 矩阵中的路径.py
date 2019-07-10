class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        visited = [0] * (rows * cols)
        pathlength = 0
        for row in range(rows):
            for col in range(cols):
                if self.haspathcore(matrix, rows, cols, row, col, path, pathlength, visited):
                    return True
        return False

    def haspathcore(self, matrix, rows, cols, row, col, path, pathlength, visited):
        if len(path) == pathlength:
            return True
        if row >= 0 and row < rows and col >=0 and col < cols and matrix[row * cols + col] == path[pathlength] and not visited[row * cols + col]:
        #matrix中有这个路径且在visited为0
            pathlength += 1
            visited[row * cols + col] = True
            hasPath = self.haspathcore(matrix, rows, cols, row, col-1, path, pathlength, visited) \
                      or self.haspathcore(matrix, rows, cols, row-1, col, path, pathlength, visited) \
                      or self.haspathcore(matrix, rows, cols, row, col+1, path, pathlength, visited) \
                      or self.haspathcore(matrix, rows, cols, row+1, col, path, pathlength, visited)
            if not hasPath:
                pathlength -= 1
                visited[row*cols + col] = False
            return hasPath


s = Solution()
ifTrue = s.hasPath("ABCESFCSADEE", 3, 4, "BCCED")
ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
print(ifTrue)
