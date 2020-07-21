# 코드업 1031. [기초-출력변환] 10진 정수 1개 입력받아 8진수로 출력하기

# 입력
# 10

# 출력
# 12

try:
  num = int(input());
  print(format(num, 'o'));
except Exception as e:
  print(e);



## 모범 답안
a=input()
n=int(a)
print('%o' % n) # '%포매팅 문자열' %변수