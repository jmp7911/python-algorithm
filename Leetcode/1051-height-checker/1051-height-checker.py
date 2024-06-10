class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered = sorted(heights)
        count = 0
        for k, v in enumerate(heights):
            if heights[k] != ordered[k]:
                count += 1
        return count