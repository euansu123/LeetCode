"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 如果非空，则仅由小写英文字母组成
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firststr = strs[0]
        for i in range(len(firststr)):
            for j in range(1, len(strs)):
                # 判断长度，然后判断是否相等，任何一条不满足，直接return
                if i > len(strs[j]) -1 or strs[j][i] != firststr[i]:
                    return firststr[:i] if i >= 1 else ""

        return firststr

if __name__ == '__main__':
    # s = Solution()
    # r = s.longestCommonPrefix(["flower","flow","flight"])
    # print(r)
    # r = s.longestCommonPrefix(["dog","racecar","car"])
    # print(r)
    # r = s.longestCommonPrefix(["ab", "a"])
    # print(r)
    strs = ["flower","flow","flight"]
    print(map(len, strs))
    for item in map(len, strs):
        print(item)
    min_len = min(map(len, strs))
    print(min_len)