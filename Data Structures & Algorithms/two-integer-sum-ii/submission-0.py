class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            if s < target:
                # Need a larger sum → move left pointer right
                left += 1
            else:
                # s > target → need a smaller sum → move right pointer left
                right -= 1

        return []   