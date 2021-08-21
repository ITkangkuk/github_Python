#dictionary 선언
dictionary={
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

print(dictionary)

print("name:" ,dictionary["name"])
print("type:",dictionary["type"])
print("ingredient:",dictionary["ingredient"])
print("origin:",dictionary["origin"])
print()

#값 변경
dictionary["name"]="8D 건조망고"
print("name:",dictionary["name"])

#dictionary  이름만 선언
dictionary={}
#요소 추가 이전
print("요소추가 이전:",dictionary)
#요소 추가
dictionary["name"]="새로운 이름"
dictionary["head"]="새로운 정신"
dictionary["body"]="새로운 몸"

print("요소 추가 후:",dictionary)

#dictionary 선언
dictionary={
    "name":"7D 건조 망고",
    "type":"당절임"
}

#요소 제거 전에 내용을 출력
print("요소 제거이전 :",dictionary)
#dicrionary요소를 제거
del dictionary["name"]
del dictionary["type"]
print("요소 제거 후:",dictionary)

dictionary={"name":"7D건조망고", "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

if "존재하지 않는 키"in dictionary:
    print(dictionary["존재하지 않는 키"])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

#존재하지 않는 키에 접근
value=dictionary.get("존재하지 않는 키")
print("값:",value)

#주소록을 저장할 빈 딕셔너리 생성
datas={}
cnt=0
#딕셔너리에서 사용할 키들을 튜플로 생성
#tuple은 불변한 순서가 있는 객체의 칩합, list 형과 비슷하지만 한번 생성되면 값을 변경할 수 없다.
key=("name","tel","address")

while True:
    #한사람의 주소록 정보를 입력받는다.
    name=input("이름:")
    tel=input("전화번호:")
    address=input("주소:")

    #입력받은 정보로 딕셔너리 생성
    d1={key[0]:name,key[1]:tel,key[2]:address}
    #주소록 지정할 딕셔너리 data에 키는 카운트 값으로 값은 d1으로 요소 추가

    datas[cnt]=d1
    cnt +=1
    #입력을 계속할 건지 물어본다 멈추려면 0입력
    cont=int(input("stop:0"))
    #0을 입력하면 break로 루프를 빠져나간다.
    if cont==0:
        break
    print("전체 출력")
    #datas의 키를 하나씩 꺼내 키에 대응하는 값을 출력
    for i in datas:
        print(datas[i])
    #datas에서 키가 1인 요소의 값은 {name:,tel:,address:}형태의 딕셔너리 datas[1]의 딕셔너리에서 키가 "tel"인 요소와 "address"인 요소의 값 수정
    datas[1]["tel"]="1234"
    datas[1]["address"]="경기도"

    print("키가 1번인 요소의 tel,address 수정 후")
    print(datas[1])