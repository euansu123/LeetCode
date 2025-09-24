"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。



示例 1：

输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为 5。
示例 2：

输入：s = "   fly me   to   the moon  "
输出：4
解释：最后一个单词是“moon”，长度为 4。
示例 3：

输入：s = "luffy is still joyboy"
输出：6
解释：最后一个单词是长度为 6 的“joyboy”。


提示：

1 <= s.length <= 10^4
s 仅有英文字母和空格 ' ' 组成
s 中至少存在一个单词
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif s[i] == ' ' and length != 0:
                break
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord('Hello World'))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord('luffy is still joyboy'))