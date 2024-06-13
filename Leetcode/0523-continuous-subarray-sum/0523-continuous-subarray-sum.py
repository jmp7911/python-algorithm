class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # modular 연산
        # 부분 합의 모듈러 값을 저장하여 같은 모듈러 값을 갖는 두 부분 배열이 있으면, 그 사이의 부분 배열의 합이 k의 배수임을 확인할 수 있다.
        N = len(nums)
        sum_map = {0:-1}
        prefix_sum = 0
        for i in range(N):
            prefix_sum = (prefix_sum + nums[i]) % k

            if prefix_sum in sum_map.keys():
                if i - sum_map[prefix_sum] > 1:
                    return True
            else:
                sum_map[prefix_sum] = i
        
        return False