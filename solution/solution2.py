from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        return self.merge(self.sortArray(left_half), self.sortArray(right_half))


    merge = lambda self, left, right: sorted(left + right)