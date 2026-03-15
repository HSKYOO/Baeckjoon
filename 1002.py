# 1002번: 터렛
# 입력 : x1, x2, r1, y1, y2, r2
# 사실상 r1, r2는 반지름, 

# 출력은 두 원의 교점을 구하는 것

# 해결방법
# 1. 두 원점 사이의 거리를 구한다
# 2. 반지름의 합과 원점 사이의 거리를 비교한다
# 3. 반지름의 합이 더 크다면 2개
#    원점 사이의 거리가 더 크면 0개
#    반지름의 합과 원점 사이의 거리가 같으면 1개

# 반례
# 1. 두 원이 완전히 일치할 때 -> 조건문 걸기
# 2. 원 안에 원이 있는 경우 (내포 or 내접)
# 3. 중심은 같지만 반지름이 다른 경우

# d = 두 점 사이의 거리
# r1, r2 = 입력 반지름

# 경우의 수
# short r = sh_r, long r = lg_r
# 0. x1 == x2 and y1 == y2 and r1 == r2 -> 무한 -> -1개
# 1. d > sh_r + lg_r -> 0개
# 2. d = sh_r + lg_r -> 1개

# 3. d < sh_r + lg_r -> 2개

# 4. d = lg_r - sh_r -> 1개
# 5. d < lg_r - sh_r -> 0개


tries = int(input())    # 반복 횟수
nlocation = []

for i in range(tries):

    short_r = 0 # r1, r2 중 가장 작은 반지름

    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dsq = (x1 - x2)^2 + (y1 - y2)^2     # 두점 사이 거리 제곱

    if(r1 <= r2):
        short_r = r1
    else:
        short_r = r2
    
    sqre_r = short_r^2   # 가장 작은 원의 반지름 제곱
    



