# Importing binascii module
import binascii

def solution(data):
    answer = ''
    for i, str in enumerate(data):
        binaryCode = ''
        for j, chr in enumerate(str):
            if chr == '+':
                binaryCode += '1'
            elif chr == '-':
                binaryCode += '0'
        Ascii = int(binaryCode, 2)
        answer += Ascii.to_bytes((Ascii.bit_length() + 7) // 8, 'big').decode()
    return answer

solution([' + - - + - + - ', ' + + + - + - + ', ' + + - + + + - '])