# 코드업 1064. [기초-비교연산] 정수 3개 입력받아 가장 작은 수 출력하기

# 입력

# 3 -1 5

# 출력
# -1

a, b, c= map(int,input().split())
num = (a if a<b else b)
print(num if num<c else c)