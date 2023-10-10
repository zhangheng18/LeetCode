class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 左下
        x1, y1 = float('inf'), float('inf')
        # 右上
        x2, y2 = float('-inf'), float('-inf')

        # 顶点
        points = set()

        # 实际面积
        actual_area = 0
        for xi, yi, ai, bi in rectangles:
            # 获取期望矩形的 左下右上 左边
            x1, y1 = min(xi, x1), min(yi, y1)
            x2, y2 = max(ai, x2), max(bi, y2)

            actual_area += (ai - xi) * (bi - yi)

            # 小矩形的4个顶点
            p1, p2 = (xi, bi), (ai, bi)
            p3, p4 = (ai, yi), (xi, yi)
            # 留下顶点 （奇数）
            for p in (p1, p2, p3, p4):
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)

        # 判断期望矩形面积与实际矩形是否相同
        expect_area = (x2 - x1) * (y2 - y1)
        if actual_area != expect_area:
            return False

        # 多余4个顶点
        if len(points) != 4:
            return False
        # 左上
        if (x1, y2) not in points:
            return False
        # 右上
        if (x2, y2) not in points:
            return False
        # 右下:
        if (x2, y1) not in points:
            return False
        # 左下
        if (x1, y1) not in points:
            return False

        # 面积符合 顶点符合
        return True
