class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        bst, ben = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            st, en = intervals[i]

            if st >= bst and st <= ben:
                if en > ben:
                    ben = en
            else:
                ans.append([bst, ben])
                bst = st
                ben = en
        
        ans.append([bst, ben])
        return ans