# 백준 5073번: 삼각형과 세 변
# 1. 입력받기
# 2. 삽입 정렬
# 2.5 invalid 확인 -> arr[0] + arr[1] < arr[2] 이면 invalid
# 3. 변 길이 비교 arr[0] 과 [1] / arr[1] 과 [2]
# 4. 같은 길이 count 결과에 따른 결과 저장 -> result[]
# 5. 000 입력시 result[] 출력

result = []

while(1):
    triside = []
    sub = 0
    count_same = 0
    a, b, c = map(int, input().split())

    if(a == 0 and b == 0 and c == 0):
        break
    
    triside.append(a)
    triside.append(b)
    triside.append(c)

    
    # insertion sort 
    for i in range(3):
        key = triside[i]
        j = i - 1

        while j >= 0 and triside[j] > key:
            triside[j + 1] = triside[j]
            j -= 1

        triside[j + 1] = key


    if(triside[0] + triside[1] <= triside[2]):
        result.append("Invalid")
        continue

    # 비교
    if(triside[0] == triside[1]):
        count_same += 1
    
    if(triside[1] == triside[2]):
        count_same += 1

    if(count_same == 0):
        result.append("Scalene")
    elif(count_same == 1):
        result.append("Isosceles")
    elif(count_same == 2):
        result.append("Equilateral")

for k in result:
    print(k)
