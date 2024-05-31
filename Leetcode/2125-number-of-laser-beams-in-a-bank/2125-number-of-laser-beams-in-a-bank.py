class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        up_floor_device, answer = 0, 0
        for row in bank:
            device = row.count('1')
            if not device:
                continue
            else:
                answer += up_floor_device * device
                up_floor_device = device
        return answer
