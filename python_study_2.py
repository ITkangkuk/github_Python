#3 if문
score=int(input("점수를 입력하시오"))
if score>=60:
    print("합격")
else:
    print("불합격")

num=int(input("점수를 입력하시오"))
if num%2==0:
    print("짝수")
else:
    print("홀수")

score=int(input("점수를 입력하시오"))

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
print("성적처리 완료")

#while
i=1
while i<=5:
     print(i,"hello")
     i+=1
print("while 밖")

#for
for i in range(0,3):
    print(i)

sum=0
for i in range(1,101):
    sum+=i
print("sum",sum)

for i in [2,5,1,3,4]:
    print(i)

a=[1,2,3,4,5]
for i in a:
    print(i)

str='abcdef'
for i in str:
    print(i)

dan=int(input("단수를 입력하시오:"))
for i in range(1,10):
    print(dan,"*",i,"=",dan*i)

list=[1,2,3,4,5]
num=int(input("1~5사이의 숫자를 입력하시오"))
if num in list:
    print(list.index(num),"위치에 있다.")
else:
    print("없다.")

#이메일 여러개를 저장할 리스트 생성
emails=[]

while True:
    #이메일 중복 여부를 체크할 변수
    check=False
    #등록할 이메일을 입력 받아 변수 email에 저장
    email=input("등록한 이메일 입력:")

    #리스트 처음부터 끝까지 입력받은 이메일과 같은지 비교(중복체크)
    for i in emails:
        if i==email:
            print("중복된 이메일")
            check=True
            break
    if check==True:
        continue

    emails.append(email)

    cont=int(input("반복을 멈추려면 0을 입력"))
    if cont==0:
        break

print("등록된 이메일 목록")
for i in email:
    print(i)

print("이메일 등록 확인")
search_email=input("검색할 이메일 입력")
if search_email in emails:
    print(emails.index(search_email),"번째로 등록되었습니다.")
else:
    print("등록되지 않은 이메일")

print("이메일 수정")
edit_email=input("수정할 이메일 입력")

if edit_email in emails:
    new_email=input("새로운 이메일 입력")
    idx=emails.index(edit_email)
    emails[idx]=new_email
else:
    print("등록된 이메일이 없다.")
    print("등록된 이메일 목록")
    for i in emails:
        print("i=",i)

print("이메일 삭제")
del_email=input("삭제할 이메일을 입력하시오")
if del_email in emails:
    idx=emails.index(del_email)
    del_email=emails.pop(idx)
    print(del_email,"삭제되었습니다.")
else:
    print("등록되지 않은 이메일")

print("등록된 이메일 목록")
for i in emails:
    print(i)