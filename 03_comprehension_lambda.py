# 컴프리헨션(Comprehension)과 람다(Lambda) 예제

print("=== 1. 리스트 컴프리헨션 ===")
# 영어 단어들이 담겨있는 원본 리스트입니다.
wordList = ["apple", "banana", "kiwi", "melon", "fig"]

# 리스트 컴프리헨션: 기존 리스트를 바탕으로 새로운 리스트를 간단하게(한 줄로) 만드는 파이썬의 강력한 문법입니다.
# 해석: wordList에서 단어(w)를 하나씩 꺼내는데, 만약 그 단어의 길이가 5 이상(len(w) >= 5)이라면, 대문자로 바꿔서(w.upper()) 새로운 리스트에 담아라!
upper_words = [w.upper() for w in wordList if len(w) >= 5]
print("원본 단어 리스트:", wordList)
print("길이가 5 이상인 단어 (대문자):", upper_words)
print("-" * 30)

print("=== 2. 람다 함수 (익명 함수) ===")
# 람다(lambda)는 이름이 없는 아주 간결한 함수를 만들 때 사용합니다.
# "lambda 매개변수: 반환할 식" 형태로 작성합니다.
# 리스트 안에 함수 자체를 변수처럼 저장해두는 기법입니다.
fucList = [
    lambda x, y : x + y, # 더하기 기능을 하는 람다함수 (인덱스 0번 위치)
    lambda x, y : x - y, # 빼기 기능을 하는 람다함수 (인덱스 1번 위치)
    lambda x, y : x * y, # 곱하기 기능을 하는 람다함수 (인덱스 2번 위치)
    lambda x, y : x / y  # 나누기 기능을 하는 람다함수 (인덱스 3번 위치)
]

a = 10
b = 5

print(f"{a} 와 {b} 의 연산 결과:")
# 리스트에서 함수를 꺼낸 뒤(예: fucList[0]), 소괄호를 붙여 매개변수 a, b를 넘겨주며 람다 함수를 실행시킵니다.
print(f"더하기: {fucList[0](a, b)}")
print(f"빼기: {fucList[1](a, b)}")
print(f"곱하기: {fucList[2](a, b)}")
print(f"나누기: {fucList[3](a, b)}")
print("-" * 30)

print("=== 3. List 함수와 Filter, Lambda의 조합 ===")
# 1부터 10까지 숫자가 담긴 리스트입니다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(함수, 반복가능한자료형) 함수는 자료형의 데이터를 하나씩 '함수'에 넣었을 때 참(True)인 성분만 걸러냅니다.
# 여기서는 람다 함수 'lambda x: x % 2 == 0' (2로 나눴을 때 나머지가 0인지 확인)이 필터 조건으로 쓰였습니다.
# 마지막으로 filter 결과를 눈으로 볼 수 있게 list()로 감싸서 리스트 형태로 변환합니다.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("1부터 10까지 숫자 리스트:", numbers)
print("짝수 필터링 결과:", even_numbers)
