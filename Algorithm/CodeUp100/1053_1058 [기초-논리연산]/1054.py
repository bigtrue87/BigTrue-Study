# 코드업 1054. [기초-논리연산] 둘 다 참일 경우만 참 출력하기

# 입력

# 1 1

# 출력
# 1

a,b=input().split()

x=int(a)
y=int(b)
b1=bool(x)
b2=bool(y)
z=int(b1 and b2)

print(z)