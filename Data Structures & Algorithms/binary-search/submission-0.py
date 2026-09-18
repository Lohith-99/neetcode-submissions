class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                # Target must be in the right half
                l = m + 1
            else:
                # Target must be in the left half
                r = m - 1

        return -1