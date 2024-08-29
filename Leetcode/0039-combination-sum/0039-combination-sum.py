import itertools
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def back(res):
            if sum(res) == target:
                answer.append(tuple(sorted(res)))
                return
            elif sum(res) > target:
                return
            else:
                for x in candidates:
                    res.append(x)
                    back(res)
                    res.pop()
        
        back([])
        
        return set(answer)
        
            