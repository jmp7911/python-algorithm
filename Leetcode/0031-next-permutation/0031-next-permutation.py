from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        flag = False
        for i in range(len(nums)-1,0,-1):
            be, af = nums[i-1], nums[i]
            
            if be >= af:
                stack.append(af)
            else:
                if len(stack) > 0:
                    stack.append(af)
                    m = min(list(filter(lambda x:x > be, stack)))
                    stack.remove(m)
                    stack.append(be)
                    
                    nums[i-1:] = [m] + sorted(stack)
                    
                else:
                    nums[i] = be
                    nums[i-1] = af

                flag = True
                break    
        if not flag:
            nums.sort()
        

                

