# 11866번: 요세푸스 문제 0
# N : 현재 사람 수 
# K : K 번째 사람 제거

# 핵심
# (현재 위치 + K - 1) % N = 현재 제거해야할 사람의 Index
# 지정된 Index의 element는 다른 array로 이동

n, k = map(int, input().split())
arr = []
marr = [] # 도착지 배열 arr -> marr
index = 0
josephusNumber = (index + k - 1) % n

# 1 부터 n 까지 순서대로 array에 넣기
for i in range(1, n + 1): # 1 ~ n까지
    arr.append(i)

while(1): # arr element 가 전부 없어질 때 까지
    target_number = arr.pop(josephusNumber)
    marr.append(target_number)
    if (len(arr) ==  0):
        break
    index = josephusNumber
    josephusNumber = (index + k - 1) % len(arr)

print("<", end="")
print(*marr, sep=", ",end="")
print(">")

# print(f"<{', '.join(map(str, marr))})