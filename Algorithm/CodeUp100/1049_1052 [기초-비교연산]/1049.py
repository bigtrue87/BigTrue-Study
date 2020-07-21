# 코드업 1049. [기초-비교연산] 두 정수 입력받아 비교하기1

# - a가 b보다 크면 1을, a가 b보다 작거나 같으면 0을 출력

# 입력

# 9 1

# 출력
# 1

a, b = map(int, input().split())
if a > b:
    print(1)
else:
    print(0)