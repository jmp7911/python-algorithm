class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        near = far = 0
        
        while near < len(nums) - 1:
            farthest = 0
            
            for i in range(near, far + 1):
                if i + nums[i] < len(nums) - 1:
                    farthest = max(farthest, i + nums[i])
                else:
                    return True
            
            near = far + 1
            far = farthest

        
        return False