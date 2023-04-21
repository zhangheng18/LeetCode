class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        m, n = len(matrix), len(matrix[0])

        top2bottom, bottom2top = 0, m-1
        left2right, right2left = 0,n-1

        while len(res) < m*n:
            # 左上->右上
            if top2bottom <= bottom2top:
                # 包含right2left
                for i in range(left2right, right2left+1):
                    res.append( matrix[top2bottom][i])
                # 上边界
                top2bottom +=1

            # 右上->右下
            if left2right <= right2left:
                for i in range(  top2bottom, bottom2top+1):
                    res.append( matrix[i][right2left])
                #右边界
                right2left -=1

            # 右下->左下
            if top2bottom <= bottom2top:
                #包含 left2right
                for i in range(right2left, left2right-1,-1):
                    res.append( matrix[bottom2top][i])
                #下边界
                bottom2top -=1

            #左下-> 左上
            if left2right <= right2left:
                for i in range(bottom2top, top2bottom -1,-1):
                    res.append(matrix[i][left2right])
                # 左边界
                left2right +=1

        return res