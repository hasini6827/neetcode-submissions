class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                current_sum = nums[i] + nums[j]
                if current_sum == target:
                    return [i, j]
        return [-1, -1]

        