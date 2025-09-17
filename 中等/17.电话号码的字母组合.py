"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。





示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]


提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

"""

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return list()

        def makeCombinations(index:int,combinations:List[str])  -> List[str]:

            digit = digits[index]
            combination = combinations

            combinations = []
            for letter in keyboard[digit]:
                _combination = [item + letter for item in combination ]
                combinations.extend(_combination)

            if index < len(digits) - 1:
                return makeCombinations(index+1,combinations)
            else:
                return combinations


        digit = digits[0]
        combinations = [item for item in keyboard[digit]]

        if len(digits) == 1:
            return combinations

        return makeCombinations(1, combinations)





if __name__ == '__main__':
    s = Solution()
    r = s.letterCombinations("234")
    print(r)