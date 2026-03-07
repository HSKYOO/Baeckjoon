# ISBN
# 알고리즘
# 1. input을 array에 배치
# 2. array에서 (짝수 1 홀수 3)을 곱함
# 3. '*' 부분은 for 반복문으로 1

broken_isbn = input("ISBN: ")
array_isbn = []
answer = 0
sum = 0

for i in broken_isbn:
    # print(broken_isbn[i])
    if (i == '*'):  # * 만나면 answer라는 변수로 치환
        array_isbn.append(answer)
    else:
        array_isbn.append(int(i))


for j in range(len(array_isbn)):
    
    if (j % 2 == 1):            # 이외에 홀수 array에는 (x3)
        array_isbn[j] *= 3

for k in range(len(array_isbn)): # 각 array에 element 합치기
    sum += array_isbn[k]

answer = (10 - (sum % 10)) % 10

print(answer)
