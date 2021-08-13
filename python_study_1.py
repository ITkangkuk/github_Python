print("Hello Python")

#2
print("commit")
a=True
print(a)

b=False
print("b의 타입=",type(b))
print(b)

if a:
    print("a는 참이다.")

#파이썬은 들여쓰기가 중요
a=10
b=6
c=a+b
print(a,"+",b,"=",c)

c=a-b
print(a,"-",b,"=",c)

c=a*b
print(a,"*",b,"=",c)

c=a**b
print(a,"**",b,"=",c)

a=12
print("a의 타입",type(a))
print("a=",a)

a=5
b=8
if a>0 and b<10:
    print("a는 0보다 크고 b는 10보다 작다.")
if a>10 and b<10:
    print("a는 10보다 크고 b는 10보다 작다.")
#if 문 구조 살짝 바뀐 것

name="abc"
age=12

if name=="aaa" or age==12:
    print("name이 aaa이거나 age가 12이다.")

if not name=="abc":
    print("name이 abc가 아니다")

#in 문자열, 리스트, 튜플에 지정한 값이 있으면 true 없으면 false를 반환
#not in 문자열 리스트 투플에 지정한 값이 없으면 true, 있으면 false를 반환
if name in "abc":
    print("in 문자열?")

a=[1,2,3,4]
b="apple"

print("a=",a)
print("b=",b)
print()

print("3 in a:",3 in a)
print("a in b:","a"in b)
