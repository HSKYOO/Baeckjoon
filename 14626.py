# ISBN
# 알고리즘
# 1. input을 array에 배치
# 2. array에서 (짝수 1 홀수 3)을 곱함

broken_isbn = input()

answer = -1 # 자연수 제외 수 -> 0일 가능성도 있으므로


for repeat in range(10):    # "*" 부분을 answer 라는 변수 대신 처음부터 0 부터 9까지 적용하며 테스트 -> 테스트 통과시 answer로 대입 및 출력

    array_isbn = [] # array 초기화(매 반복시) 
    sum = 0         # 총합 초기화

    for i in broken_isbn:
        # print(broken_isbn[i])
        if (i == '*'):  # * 만나면 answer라는 변수로 치환
            array_isbn.append(repeat)
        else:
            array_isbn.append(int(i))   # 여기까진 정상적으로 작동함


    for j in range(len(array_isbn)):
        if (j % 2 == 1):            # 이외에 홀수 array에는 (x3) 
            array_isbn[j] *= 3

    for k in array_isbn: # 각 array에 element 합치기
        sum += k

    if(sum % 10 == 0):
        answer = repeat
        break
    
if(answer != -1):
    print(answer)
else:
    print("no answer")
