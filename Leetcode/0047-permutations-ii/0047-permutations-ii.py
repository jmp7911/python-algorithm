from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(map(lambda x:tuple(x), permutations(nums)))