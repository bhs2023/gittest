# 예외 처리 및 파일 다루기 예제

print("=== 1. 예외 처리 (try ~ except) ===")
# 코드를 실행하다가 에러(예외)가 발생했을 때, 프로그램이 멈추지 않고 대처할 수 있게 해줍니다.
try:
    num = 10
    zero = 0
    # 0으로 숫자를 나누면 ZeroDivisionError가 발생합니다.
    result = num / zero
    print(f"결과: {result}")
except ZeroDivisionError:
    # 에러가 발생했을 때 프로그램이 멈추는 대신 아래 문장을 실행합니다.
    print("!!! 에러 발생: 숫자를 0으로 나눌 수 없습니다 !!!")
except Exception as e:
    # 혹시 모를 다른 모든 에러를 잡아줍니다. e에는 에러 내용이 담깁니다.
    print(f"알 수 없는 에러가 발생했습니다: {e}")
finally:
    # 에러 발생 여부와 상관없이 무조건 마지막에 실행되는 구역입니다.
    print("계산 시도 작업이 완전히 종료되었습니다.")

print("\n=== 2. 파이썬으로 텍스트 파일 쓰기 및 읽기 ===")
file_path = "sample_test.txt"

# 1) 파일에 쓰기 모드('w': Write)로 엽니다. 파일이 없다면 새로 만듭니다.
# 'with' 문을 사용하면 들여쓰기가 끝날 때 파일이 자동으로 안전하게 닫힙니다. (file.close() 효과)
with open(file_path, "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬 파일 다루기 예제입니다!\n")
    f.write("이 파일은 코드를 통해 만들어졌습니다.\n")
print(f"{file_path} 파일에 내용을 성공적으로 썼습니다.")

# 2) 파일에서 내용 읽기 모드('r': Read)로 다시 엽니다.
print(f"\n[{file_path} 파일의 안쪽 내용을 읽어옵니다:]")
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read() # 파일 전체 내용을 한 번에 문자열 형태로 읽어들입니다.
    print(text)

# (코드 실행 후 왼쪽 파일 목록에 'sample_test.txt' 파일이 정말 생성됐는지 탭을 열어서 확인해보세요!)
