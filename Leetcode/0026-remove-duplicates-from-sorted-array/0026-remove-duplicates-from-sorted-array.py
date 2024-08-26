class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        be = nums[0]
        count = 0
        for x in nums[1:]:
            if x != be:
               count += 1
               nums[count] = x
               be = x
        

        return count + 1