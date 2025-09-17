"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。



示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
示例 2：

输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。

 提示：
（1）3 <= nums.length <= 1000
（2）-1000 <= nums[i] <= 1000
（3）-104 <= target <= 104
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        需要考虑正负数的情况，如果是负数，会出现正数 + 负数的情况
        """
        sum_result = nums[0] + nums[1] + nums[2]
        # 1.判断列表的长度，如果等于三直接返回结果
        if len(nums) == 3:
            return sum(nums)
        # 2.对列表从小到大进行排序
        sorted_nums = sorted(nums)
        # 3.遍历一个元素，寻找剩余两个元素
        for i in range(0, len(sorted_nums)-2):
            left = i + 1
            right = len(sorted_nums) - 1
            while left != right:
                tmp = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if abs(tmp - target) < abs(sum_result - target):
                    sum_result = tmp

                if tmp > target:
                    right -= 1
                else:
                    left += 1

            # if abs(sum(sorted_nums[i:i+3]) - target) < abs_min__result:
            #     abs_min__result = abs(sum(sorted_nums[i:i+3]) - target)
            #     min_result = sum(sorted_nums[i:i+3])
            # else:
            #     break

        return sum_result


if __name__ == '__main__':
    S = Solution()
    # r = S.threeSumClosest(nums=[-1,2,1,-4], target=1)
    #
    # r2 = S.threeSumClosest(nums=[1,1,1,1], target=-100)
    #
    # r3 = S.threeSumClosest(nums=[10,20,30,40,50,60,70,80,90], target=0)

    r4 = S.threeSumClosest(nums=[4,0,5,-5,3,3,0,-4,-5], target=-2)
    print(r4)
