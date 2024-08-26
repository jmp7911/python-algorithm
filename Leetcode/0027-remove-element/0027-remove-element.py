class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        inplace = []
        count = 0
        for i, x in enumerate(nums):
            if x == val:
                inplace.append(i)
            else:
                count += 1
                if len(inplace) > 0:
                    idx = inplace.pop(0)
                    nums[idx] = x
                    inplace.append(i)
        return count
        