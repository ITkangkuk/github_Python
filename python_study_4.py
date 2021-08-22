def gugudan(dan):
    """구구단 한단 출력 함수
    dan이 출력할 단수"""
    for i in range(1,10):
        print(dan,"*",i,"=",dan*i)

def main():
    dan=int(input("출력할 단수를 입력하시오:"))
    gugudan(dan)

main()

def print_3_times():
    print("one")
    print("two")
    print("three")

print_3_times()

#range 1부터 시작 10보다 하나 적은 9까지

def add(a,b):
    """더하기 함수"""
    return a+b

def sub(a,b):
    """뺴기 함수"""
    return a-b

def multi(a,b):
    """곱하기기 함수"""
    return a*b

def dev(a,b):
    """나누기 함수"""
    if b==0:
        print("0으로 나눌 수 없다")
        return None
    else:
        return a/b

def main():
    """메인 함수"""
    #메인의 시작이 프로그램의 시작점이고 main 이 끝나면 프로그램의 끝
    op=""
    num1=0
    num2=0
    result=0

    num1=int(input("숫자1를 입력하세요"))
    num2=int(input("숫자2을 입력하세요"))
    op=input("연산자를 입력하시오")

    if op in "+":
        result=add(num1,num2)
    elif op in "-":
        result=sub(num1,num2)
    elif op in "*":
        result=multi(num1,num2)
    elif op in "/":
        result=dev(num1,num2)
    else:
        print("정확한 연산자를 입력하세요")
        return

    print(num1,op,num2,"=",result)

main()


def addPrint(a,b):
    result=a+b
    print(a,"+",b,"=",result)

def main():
    addPrint(1,2)
    addPrint(2.234, 5.6)
    addPrint("abc","def")
    addPrint([1,2],[3,4])

main()

#함수에서 변경하더라도 호출한 쪽에는 전혀 영향이 없다.
#immutable타입: int,bool,float,complex,tuple,frozen,set
#변경이 가능한 타입의 값이라면 그 메모리에 저장된 값을 함수에서 변경하면 호출한 쪽에서도 값이 변경된다.
#mutable 타입:list,set,dictionary

def f1():
    print("f1()함수 호출")
def f2():
    print("f2()함수 호출")
def f3():
    print("f3()함수 호출")

def main1():
    num=int(input("0~2사이의 숫자를 입력하시오"))

    if num==0:
        f1()
    elif num==1:
        f2()
    elif num==2:
        f3()
    else:
        print("잘못입력")

def main2():
    list1=[f1,f2,f3]
    num=int(input("0~2사이의 숫자를 입력하시오"))

    if num<0 or num>2:
        print("잘못된 입력")
        return
    else:
        list1[num]()

main1()
main2()

names=[]

def getName(name):
    if name in names:
        return names.index(name)

def add():
    name=input("이름입력")
    ch=getName(name)
    if ch==None:
        names.append(name)