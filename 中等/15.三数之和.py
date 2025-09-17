"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:

    # 超出时间限制
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 三数之和为0
        results = []
        sorted_nums = sorted(nums)
        length = len(sorted_nums)

        for first in range(length - 2):
            if first > 0 and sorted_nums[first] == sorted_nums[first - 1]:
                continue

            target = -sorted_nums[first]
            thrid = length - 1
            for second in range(first + 1, length - 1):
                if second > first + 1 and sorted_nums[second] == sorted_nums[second - 1]:
                    continue

                while thrid > second and sorted_nums[second] + sorted_nums[thrid] > target:
                    thrid -= 1

                if thrid == second:
                    break

                if sorted_nums[second] + sorted_nums[thrid] == target:
                    results.append([sorted_nums[first], sorted_nums[second], sorted_nums[thrid]])

        return results

    def threeSumNew(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            # c 对应的指针初始化指向数组的最右侧
            thrid = n - 1
            target = -nums[first]
            print(target)
            # 枚举b
            for second in range(first + 1, n):
                # 需要和上一次枚举的值不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 指针的左侧
                while second < thrid and nums[second] + nums[thrid] > target:
                    thrid -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c了，可以退出循环
                if second == thrid:
                    break
                if nums[second] + nums[thrid] == target:
                    ans.append([nums[first], nums[second], nums[thrid]])

        return ans


if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([-1,0,1,2,-1,-4])
    print(r)

    r = s.threeSum([0,0,0])
    print(r)

    r = s.threeSum([1,2,-2,-1])
    print(r)

    # r = s.threeSumNew([-1,0,1,2,-1,-4])
    # print(r)