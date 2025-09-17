from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check(i):
            target = strs[0][i]
            for s in strs[1:]:
                if s[i] != target:
                    return False
            return True

        min_len = min(map(len, strs))
        for j in range(min_len):
            if not check(j):
                return strs[0][0:j]
        return strs[0][0:min_len]

