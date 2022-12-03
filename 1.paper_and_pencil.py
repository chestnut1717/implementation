######################
#
# Paper and Pencil Binary Decimal Multiplication
# with Python
# compatible with binary, decimal and hexadecimal
#
######################


# convert binary number
def converter(cond, A, B):
    if cond == 1:
        # clear zero bit at left side
        return A.lstrip("0"), B.lstrip("0")
    if cond == 2:
        return bin(int(A))[2:], bin(int(B))[2:]
    elif cond == 3:
        return bin(int("0x"+A, 16))[2:], bin(int("0x"+B, 16))[2:]

def get_max_length(str_num):
    return len(str_num)

# 곱셈 결과 및 숫자 라인 출력하는 함수
def print_line(maxLength, line, end='\n'):
    print("{0}{1}".format( " " * (maxLength - len(line)), line), end=end)

def paper_pencil_mul(A, B):

    # 승수를 LSB부터 하나씩 곱함
    bit_save = []
    cnt = 0
    result = 0
    
    for b in reversed(B):
        # bit 곱셈 저장하는 출력용 str
        tmp_str = ""

        for a in A:
            # 하나씩 더해줌
            tmp_result = int(a) * int(b)
            tmp_str += str(tmp_result)

        result += int('0b' + tmp_str, 2) * (2 ** cnt)
        bit_save.append(tmp_str)
        cnt += 1
    
    result_str = bin(result)[2:]
    
    # 출력
    maxLength = get_max_length(result_str)
    print_line(maxLength, A)
    print_line(maxLength, B, end='\r')
    print('X')
    print("-" * maxLength)
    
    ## 각 승수 한 자리와 피승수 AND 연산 결과 출력
    i = 0
    while i < cnt:
    
        print_line(maxLength - i, bit_save[i])
        i += 1
    

    ## 곱셈 결과 출력
    print("-" * maxLength)
    print_line(maxLength, bin(result)[2:])
    print(maxLength, i)
        
condition = int(input("1) 2진수 / 2) 10진수 3) 16진수 : "))

A = input('첫번째 수를 입력하세요: ')
B = input('두번째 수를 입력하세요: ')

a, b = converter(condition, A, B)
paper_pencil_mul(a, b)

real = bin(int(a, 2) * int(b, 2))
print(real[2:])
