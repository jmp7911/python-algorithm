class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 10**4+1
        cnt = [0 for _ in range(n+1)]
        for i, x in enumerate(nums):
            cnt[x] += 1
            if cnt[x] >= 3:
                nums[i] = 10**4 + 1
                cnt[x] = 2

        nums.sort()
        return sum(cnt)