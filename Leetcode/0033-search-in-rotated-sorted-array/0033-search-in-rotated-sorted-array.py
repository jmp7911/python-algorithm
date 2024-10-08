class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if abs(nums[l] - target) > abs(nums[r] - target):
                r -= 1
            else:
                l += 1
        
        return -1