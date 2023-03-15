class NumMatrix:

    def __init__(self, matrix):
        m,n = len(matrix), len(matrix[0]) if matrix else 0
        self.prefix_sum = [ [0 for _ in range(n+1)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.prefix_sum[i][j+1] = self.prefix_sum[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        total = 0
        for m in range(row1, row2+1):
            total += self.prefix_sum[m][col2+1] - self.prefix_sum[m][col1]
        return total
