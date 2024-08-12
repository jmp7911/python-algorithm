class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        times = 1
        answer = ''
        while num > 0:
            remainer = num % 10
            num //=  10
            
            if remainer == 4:
                answer = symbols[times] + symbols[times * 5] + answer
            elif remainer == 9:
                answer = symbols[times] + symbols[times * 10] + answer
            elif remainer > 5:
                answer = symbols[times * 5] + symbols[times] * (remainer - 5) + answer
            else:
                if remainer * times in symbols:
                    answer = symbols[remainer * times] + answer
                else:
                    answer = symbols[times] * remainer + answer

            times *= 10
        return answer
    