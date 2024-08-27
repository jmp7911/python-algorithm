class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        ans = []
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (right - left) // 2
            if nums[mid] == target:
                for x in range(left, right):
                    if nums[x] == target:
                        ans.append(x)
                break
            elif nums[mid] > target:
                left = mid
            else:
                right = mid
        if len(ans) == 0:
            return [-1, -1]
        else:
            return [min(ans), max(ans)]