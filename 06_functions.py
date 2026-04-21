# 함수 예제 (def, Arguments, Return)

print("=== 1. 기본적인 함수 정의와 호출 ===")
# 함수는 특정 작업을 수행하는 코드의 모음입니다. 'def' 로 시작합니다.
def greet(name):
    # 건네받은 name 변수를 이용해 인사를 출력합니다.
    print(f"안녕하세요, {name}님!")

# 정의한 함수를 실제 사용할 때(호출) 데이터를 넘겨줍니다.
greet("개발자")
greet("파이썬")

print("\n=== 2. 반환값(Return)이 있는 함수 ===")
# 계산 결과를 밖으로 다시 돌려주는 함수입니다.
def add_numbers(a, b):
    result = a + b
    return result # 계산된 값을 반환합니다.

# 함수가 돌려준(return) 값을 변수(sum_val)에 저장하여 활용할 수 있습니다.
sum_val = add_numbers(10, 20)
print(f"10 + 20의 결과는 {sum_val}입니다.")

print("\n=== 3. 기본값(Default)을 가지는 매개변수 ===")
# 두 번째 매개변수 'msg'에 값을 주지 않으면 기본값인 "환영합니다!"를 사용합니다.
def welcome(user, msg="환영합니다!"):
    print(f"{user}님, {msg}")

welcome("철수")                # msg를 주지 않은 경우, 기본값 사용
welcome("영희", "또 오셨네요!") # msg를 직접 지정한 경우

print("\n=== 4. 여러 개의 인자를 받는 함수 (*args) ===")
# 매개변수 앞에 *를 붙이면 입력되는 개수와 상관없이 모든 값을 튜플(Tuple)로 묶어 받습니다.
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("1부터 3까지의 합:", sum_all(1, 2, 3))
print("여러 숫자의 합:", sum_all(10, 20, 30, 40, 50))
