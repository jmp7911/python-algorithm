class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # insertion sort
        '''
        i = 1
        n = len(nums)
        while i < n:
            if nums[i-1] <= nums[i]:
                i += 1
            else:
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
                i -= 1
            if i == 0:
                i = 1
        '''
        # bubble sort
        n = len(nums)
        for _ in range(n):
            for i in range(1, n):
                if nums[i-1] > nums[i]:
                    temp = nums[i-1]
                    nums[i-1] = nums[i]
                    nums[i] = temp
                    