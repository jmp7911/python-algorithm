class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = []
        for x in nums:
            if x in answer:
                answer.remove(x)
            else:
                answer.append(x)
        return answer