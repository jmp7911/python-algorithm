import itertools
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def back(i, res):
            if sum(res) == target:
                answer.append(tuple(res))
                return
            elif sum(res) > target:
                return
            else:
                for j in range(i, len(candidates)):
                    res.append(candidates[j])
                    back(j, res)
                    res.pop()
        
        back(0, [])
        
        return answer
        
            