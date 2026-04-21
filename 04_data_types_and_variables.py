# 자료형과 변수 예제 (Data Types & Variables)

print("=== 1. 숫자형과 문자열 ===")
# 변수에 값을 할당합니다. 파이썬은 데이터 타입을 자동으로 인식합니다.
age = 25              # 정수 (int)
height = 175.5        # 실수 (float)
name = "파이썬"         # 문자열 (str)

print(f"이름: {name}, 나이: {age}, 키: {height}")

print("\n=== 2. 리스트(List) ===")
# 순서가 있고, 값을 변경할 수 있는 자료형입니다.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")    # 데이터 추가
fruits[0] = "kiwi"         # 0번째 위치의 데이터 변경
print(f"과일 리스트: {fruits}")
print(f"두 번째 과일: {fruits[1]}") # 인덱스는 0부터 시작합니다.

print("\n=== 3. 튜플(Tuple) ===")
# 순서가 있지만, 값을 변경할 수 없는(읽기 전용) 자료형입니다.
colors = ("red", "green", "blue")
# colors[0] = "yellow" # 튜플은 한 번 생성되면 변경불가라 이 주석을 풀면 에러가 납니다.
print(f"색상 튜플: {colors}")

print("\n=== 4. 세트(Set) ===")
# 순서가 없고, 중복된 값을 허용하지 않는 자료형입니다.
numbers = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"중복이 제거된 세트: {numbers}") # 출력: {1, 2, 3, 4, 5} -> 중복된 숫자는 한 번만 저장됩니다.
