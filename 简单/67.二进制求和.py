"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。



示例 1：

输入:a = "11", b = "1"
输出："100"
示例 2：

输入：a = "1010", b = "1011"
输出："10101"


提示：

1 <= a.length, b.length <= 10^4
a 和 b 仅由字符 '0' 或 '1' 组成
字符串如果不是 "0" ，就不含前导零
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        思路：先确认两个字符串中较长的字符串，然后对较长的字符串进行遍历，从右到左进行遍历求和
        :param a:
        :param b:
        :return:
        """
        pass
        # if len(a) > len(b):
        #     maxList = list(a)
        #     minList = list(b)
        # else:
        #     maxList = list(b)
        #     minList = list(a)
        #
        # for i in range(-1,-len(maxList)-1,-1):
        #     # 1.判断minStr在该索引下是否含有元素
        #     if int(maxList[i]) > 1:
        #         if abs(i) >= len(maxList):
        #             maxList[i] = 0
        #             maxList = [1] + maxList
        #         else:
        #             print(i)
        #
        #             maxList[i-1] = int(maxList[i]) + 1
        #             maxList[i] = 0
        #     # 2.相同位置的元素进行相加
        #     if abs(i) < len(minList):
        #         maxList[i] = int(minList[i]) + int(maxList[i])
        #
        #         if int(maxList[i]) > 1:
        #             if abs(i) >= len(maxList):
        #                 maxList[i] = 0
        #                 maxList = [1] + maxList
        #             else:
        #                 maxList[i - 1] = int(maxList[i]) + 1
        #                 maxList[i] = 0

        return





if __name__ == '__main__':
    s = Solution()
    print(s.addBinary(a="1010", b="1011"))
    print(s.addBinary(a="11", b="1"))