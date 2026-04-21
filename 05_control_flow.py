# 제어문 예제 (조건문과 반복문)

print("=== 1. if 조건문 ===")
score = 85

# 조건에 따라 실행할 코드를 분기합니다. 들여쓰기(Indent)가 매우 중요합니다!
if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
else:
    print("C학점 이하입니다.")

print("\n=== 2. for 반복문 ===")
# 리스트와 같은 자료형의 원소를 처음부터 끝까지 하나씩 꺼내어 반복합니다.
print("과일 목록 출력:")
fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(f"- {fruit}")

# range(시작, 끝, 간격) 함수를 이용한 반복
print("1부터 5까지 더하기:")
total = 0
for i in range(1, 6): # 1부터 5까지 (6은 포함되지 않음)
    total += i        # total = total + i 와 같은 수식입니다.
print(f"총합: {total}")

print("\n=== 3. while 반복문 ===")
# 조건이 참(True)인 동안 계속해서 반복합니다.
count = 5
while count > 0:
    print(f"카운트 다운: {count}")
    count -= 1 # count를 1씩 감소시킵니다.
print("발사!")

print("\n=== 4. break와 continue ===")
# break: 반복문을 즉시 탈출합니다.
# continue: 아래 코드를 무시하고 다음 반복으로 넘어갑니다.
for num in range(1, 10):
    if num % 2 == 0:
        continue # 짝수면 무시하고 다음 숫자로 넘어감
    if num > 7:
        break    # 7보다 크면 반복문을 완전히 멈춤
    print(f"조건을 통과한 홀수: {num}")
