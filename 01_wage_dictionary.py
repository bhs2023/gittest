# 주급 계산 예제 (딕셔너리와 리스트 활용)

# personList라는 이름의 리스트를 생성합니다. 
# 리스트 내부에는 각각의 직원 정보를 담은 딕셔너리(dict) 데이터가 들어있습니다.
personList = [
    {"name": "홍길동", "work_time": 40, "per_pay": 10000}, # 이름, 일한 시간, 시급을 키(key)와 값(value) 쌍으로 저장합니다.
    {"name": "임꺽정", "work_time": 30, "per_pay": 20000},
    {"name": "장길산", "work_time": 20, "per_pay": 30000}
]

# 새로운 직원 추가
# 리스트의 append() 메서드를 사용하여 새로운 딕셔너리 데이터를 리스트 맨 끝에 추가합니다.
personList.append({"name": "이몽룡", "work_time": 35, "per_pay": 15000})

# 급여 계산 및 출력
print("=== 주급 계산 결과 ===")

# for 반복문을 통해 personList 리스트 안의 딕셔너리를 하나씩 꺼내어 'worker' 변수에 담고 반복합니다.
for worker in personList:
    # 급여 계산: 일한 시간 * 시급
    # 기존 딕셔너리에 'pay'라는 새로운 키를 만들고 계산 결과를 값으로 저장합니다.
    worker['pay'] = worker['work_time'] * worker['per_pay']
    
    # f-string(f"문자열")을 사용하여 문자열과 변수의 값을 보기 좋게 조립하여 출력합니다.
    print(f"이름: {worker['name']}")
    print(f"근무 시간: {worker['work_time']}시간")
    print(f"시급: {worker['per_pay']:,}원")  # {변수:,} 형태는 숫자에 1,000단위 콤마를 찍어줍니다.
    print(f"주급: {worker['pay']:,}원")
    print("-" * 20) # 구분선을 넣기 위해 "-" 문자열을 20번 반복해서 출력합니다.
