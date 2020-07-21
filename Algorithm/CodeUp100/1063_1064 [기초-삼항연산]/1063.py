# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기
# 문제 설명
# 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
# (단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.)

# 입력
# 두 정수가 공백을 두고 입력된다.
# (-2147483648 ~ 2147483647)

# 출력
# 큰 값이 10진수로 출력된다.

# 입력 예시
# 123 456

# 출력 예시
# 456

a,b=input().split()
x=int(a)
y=int(b)
print(x if x>y else y)

# 파이썬에서 삼항연산자는 if와 else를 사용해서 나타낸다.
# x가 y보다 클 때 x값을 출력하고 아니면 y를 출력한다는 의미이다.