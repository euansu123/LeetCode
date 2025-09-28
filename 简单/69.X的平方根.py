"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。



示例 1：

输入：x = 4
输出：2
示例 2：

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。


提示：

0 <= x <= 231 - 1
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        寻找最大的整数，使得i*i<=x
        :param x:
        :return:
        """
        result = 0
        for i in range(1, x+1):
            if i * i <= x:
                result = i
            else:
                break

        return result

if __name__=='__main__':
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(3))
    print(s.mySqrt(8))
    print(s.mySqrt(0))
    print(s.mySqrt(2))