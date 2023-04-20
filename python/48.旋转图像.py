class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 对角线翻转
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 水平翻转
        for row in matrix:
            start, end  = 0, n-1
            while start < end:
                row[start],row[end] = row[end],row[start]
                start+=1
                end-=1
