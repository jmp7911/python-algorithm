class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m == 0 and n == 0:
            return float(0)
        elif m == 1 and n == 0:
            return float(nums1[0])
        elif m == 0 and n == 1:
            return float(nums2[0])

        p1, p2 = 0, 0
        stack = []
        while p1 + p2 <= (m + n)//2:

            if p1 >= m:
                stack.append(nums2[p2])
                p2 += 1
            elif p2 >= n:
                stack.append(nums1[p1])
                p1 += 1
            else:
                if nums1[p1] <= nums2[p2]:
                    stack.append(nums1[p1])
                    p1 += 1
                else:
                    stack.append(nums2[p2])
                    p2 += 1

        
        if (m + n) % 2 == 0:
            answer = sum(stack[-2:]) / 2
        else:
            answer = stack[-1]
        return answer