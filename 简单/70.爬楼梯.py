"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶


提示：

1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        考察1和2的组合模式有多少种
        :param n:
        :return:
        """
        p, q, r = 1, 1, 0
        if n == 1:
            return q
        for i in range(2, n + 1):
            r = p + q
            p = q
            q = r

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))