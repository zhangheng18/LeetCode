class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [ [0]*n for _ in range(n)]
        left2right, right2left = 0 , n-1
        top2bottom, bottom2top = 0, n -1
        
        idx = 1
        while idx <= n*n:
            # 左上到右上
            if top2bottom <= bottom2top:
                for i in range(left2right, right2left+1):
                    matrix[top2bottom][i] = idx
                    idx +=1
                top2bottom +=1
            
            # 右上到右下
            if left2right <= right2left:
                for i in range(top2bottom, bottom2top+1):
                    matrix[i][right2left] = idx
                    idx +=1
                right2left -=1

            # 右下到左下
            if top2bottom <=bottom2top:
                for i in range(right2left,left2right -1,-1):
                    matrix[bottom2top][i] = idx
                    idx +=1
                bottom2top -=1
           
            # 左下到左上
            if left2right <= right2left:
                for i in range(bottom2top,top2bottom-1,-1):
                    matrix[i][left2right] = idx
                    idx +=1
                left2right +=1
   
        return matrix
            