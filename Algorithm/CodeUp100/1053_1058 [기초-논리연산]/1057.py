# 코드업 1057. [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기

# 입력

# 0 0

# 출력
# 1

a, b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)