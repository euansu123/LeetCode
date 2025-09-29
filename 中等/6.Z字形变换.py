"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);


示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"


提示：

1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        思路：构造一个二维数组，输出二维数组第一行的值
        :param s:
        :param numRows:
        :return:
        """
        n, r = len(s), numRows #行
        t = 2 * (r - 1)  # 周期
        c = len(s)/2   # 列
        c = int(c) if int(c) == c else int(c) + 1

        if r == 1 or r >= len(s):
            return s

        # 构造二维数组
        arr = [[''] * c for _ in range(r)]

        x,y = 0, 0  # 记录行、列
        # 按照行进行遍历
        for i,ch in enumerate(s):
            arr[x][y] = ch

            if i % t < r - 1:
                x+=1
            else:
                x-=1
                y+=1

        # 依次读取列表，组成新的字符串
        newStr = "".join(ch for row in arr for ch in row if ch)
        return newStr

if __name__ == '__main__':
    s = Solution()
    # print(s.convert("PAYPALISHIRING", 3))
    # print(s.convert("PAYPALISHIRING", 4))
    # print(s.convert("PAYPALISHIRING", 5))
    print(s.convert("ABC", 2))


