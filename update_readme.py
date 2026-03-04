import os

# 1. 파이썬 파일(.py) 개수 세기
# 현재 폴더(.)부터 하위 폴더까지 싹 뒤져서 .py 파일의 개수를 셉니다.
# update_readme.py 파일 자체는 개수에서 뺍니다.
solved_count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py') and file != 'update_readme.py':
            solved_count += 1

# 2. README.md 파일 읽어오기
with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 3. 새로운 내용으로 수정하기
# '현재까지 푼 문제 수:' 라는 글자가 있는 줄을 찾아서 숫자를 바꿔줍니다.
with open('README.md', 'w', encoding='utf-8') as f:
    for line in lines:
        if '- **현재까지 푼 문제 수:**' in line:
            f.write(f"- **현재까지 푼 문제 수:** {solved_count} 개\n")
        else:
            f.write(line)

print(f"README 업데이트 완료! 총 {solved_count}개의 파이썬 파일을 찾았습니다.")