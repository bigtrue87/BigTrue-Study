# 코드업 1058. [기초-논리연산] 둘 다 거짓일 경우에만 참 출력하기

# 입력

# 1 1

# 출력
# 0

a, b = map(int, input().split())
if a == 0 and b == 0:
    print(1)
else:
    print(0)
