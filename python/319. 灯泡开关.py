import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        电灯一开始都是关闭的，所以某一盏灯最后如果是点亮的，必然要被按奇数次开关

        假设只有 6 盏灯，而且我们只看第 6 盏灯。需要进行 6 轮操作对吧，对于第 6 盏灯，会被按下几次开关呢？这不难得出，第 1 轮会被按，第 2 轮，第 3 轮，第 6 轮都会被按。
        为什么第 1、2、3、6 轮会被按呢？因为 6=1*6=2*3。一般情况下，因子都是成对出现的，也就是说开关被按的次数一般是偶数次。
        但是有特殊情况，比如说总共有 16 盏灯，那么第 16 盏灯会被按几次?
        16 = 1*16 = 2*8 = 4*4
        其中因子 4 重复出现，所以第 16 盏灯会被按 5 次，奇数次
        就假设现在总共有 16 盏灯，我们求 16 的平方根，等于 4，这就说明最后会有 4 盏灯亮着，
            它们分别是第 1*1=1 盏、第 2*2=4 盏、第 3*3=9 盏和第 4*4=16 盏。
        """
        return int(math.sqrt(n))
