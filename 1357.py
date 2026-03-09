# 1357번: 뒤집힌 덧셈
# 문제 -> 일의 자리가 0이면 뒤집으면 단위가 달라짐
# 일단 입력 받음

# Rev()
# 100자리 -> hundred = n / 100 
# 10자리 -> (n - hundred * 100) / 10
# 1자리 -> one = n % 10

def Rev(n):
    
    arr = []    # 단위 보관 (반복문 용)
    reverse = 0
    i = 0

    while(n != 0):
        arr.append(n % 10) 
        n = n // 10 
        i += 1

    for j in arr:
        reverse += j
        reverse *= 10
    
    reverse //= 10

    return reverse

a, b = map(int, input().split())

first_add = Rev(a) + Rev(b)

second_add = Rev(first_add)

print(second_add)

