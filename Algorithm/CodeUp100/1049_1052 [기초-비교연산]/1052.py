# 코드업 1052. [기초-비교연산] 두 정수 입력받아 비교하기4

# - a와 b가 다른 경우 1을, 그렇지 않은 경우 0을 출력

# 입력

# 0 1

# 출력
# 1

a, b = map(int, input().split())
if a != b:
    print(1)
else:
    print(0)