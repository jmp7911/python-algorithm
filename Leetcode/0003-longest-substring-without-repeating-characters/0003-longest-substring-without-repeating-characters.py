class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ""
        answer = 0
        for x in s:
            if sub_string.find(x) != -1:
                sub_string = sub_string[sub_string.find(x)+1:]
            sub_string += x
            answer = max(answer, len(sub_string))
            # print(x, sub_string)
        return answer