class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # [4,5,0,-2,-3,1] , k = 5
        # [4] -> 4
        # [4,5] -> 4
        # [4,5,0] -> 4
        # [4,5,0,-2] -> 2
        # [4,5,0,-2,-3] -> 4
        # [4,5,0,-2,-3,1] -> 0
        answer = 0
        N = len(nums)
        sum_map = [0 for _ in range(k)]
        prefix_sum = 0
        for i in range(N):
            prefix_sum = (prefix_sum + nums[i]) % k

            if sum_map[prefix_sum] > 0:
                answer += sum_map[prefix_sum]
            
            sum_map[prefix_sum] += 1
        
        return answer + sum_map[0]