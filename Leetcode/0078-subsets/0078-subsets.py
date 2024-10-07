from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = None
        for i in range(n+1):
            if ans == None:
                ans = list(combinations(nums,i))
            else:
                ans += list(combinations(nums,i))
        return ans