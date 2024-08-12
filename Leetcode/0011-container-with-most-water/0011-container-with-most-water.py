import numpy
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # volum = min(x, y) * (y - x)
        answer = -1
        left, right = 0, len(height) - 1
        
        while left < right:
            volum = min(height[left], height[right]) * (right - left)
            answer = max(volum, answer)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return answer