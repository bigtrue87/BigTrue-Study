# 코드업 1045 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기

# 입력
# 10 3

# 출력
# 13
# 7
# 30
# 3
# 1
# 3.33

a, b = map(int, input().split(' '))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(('%0.2f' % (a/b)))