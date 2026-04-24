# 1012번: 유기농 배추
# 묶음의 왼쪽 상단만 count 할 것
# 탐색: 1 발견시 오른쪽 1칸 아래 1칸 조사 1 있으면 이동 후 탐색 지속
# 탐색이 끝난 후 기존 위치를 제외한 탐색 했던 칸 0으로 바꿈
# 지정된 횟수까지 반복 후 count 출력

repeat = int(input())       # 반복횟수
count = 0

for i in repeat:
    m, n, k = map(int, input().split())     # m : 가로길이 // n : 세로길이 // k : 배추가 심어져있는 위치의 갯수
    arr = [[0 for _ in range(m)] for _ in range(n)]     # 배열 0 으로 초기화

    for j in k:         # 배추 갯수만큼 repeat
        x, y = map(int, input().split())
        arr[[x], y] = 1                     # (x, y) = 1
    
    # 탐색
def search(arr):
    
    # 배열을 순서대로 돌아가며 1 을 탐색 -> 발견시 아래, 왼쪽 search
    for i in arr:
        if(i == 1):
            count += 1
            i = 12
            i += 5
            
