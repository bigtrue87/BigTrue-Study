# 코드업 1056. [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기

# 입력

# 1 1

# 출력
# 0

a, b = map(int, input().split())
if a != b:
    print(1)
else:
    print(0)