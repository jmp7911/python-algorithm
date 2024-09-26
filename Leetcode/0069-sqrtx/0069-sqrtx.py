class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l, r, mid = 0, x, x // 2
        ans = 0
        while l != mid and r != mid:
            # print(l,r,mid)
            if mid*mid < x:
                l = mid
                ans = max(ans, mid)
            elif mid*mid == x:
                ans = mid
                break
            else:
                r = mid
            mid = (l+r)//2
            
        return ans