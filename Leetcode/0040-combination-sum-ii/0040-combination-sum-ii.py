class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        if sum(candidates) == target:
            return [candidates]
        elif sum(candidates) < target:
            return ans
        def back(i, res):
            if sum(res) == target:
                if tuple(sorted(res)) not in ans:
                    ans.append(tuple(sorted(res)))
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] + sum(res) <= target:
                    res.append(candidates[j])
                    back(j + 1, res)
                    res.pop()
        back(0, [])

        return ans