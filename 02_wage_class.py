# 주급 계산 예제 (클래스와 객체지향 활용)

# 직원의 정보를 담고 급여를 계산하는 Weekpay 클래스를 정의합니다.
class Weekpay:
    # __init__은 생성자 메서드로, 클래스로부터 객체가 만들어질 때 자동으로 실행됩니다.
    def __init__(self, name="", work_time=20, per_pay=10000):
        self.name = name            # 객체의 이름을 의미하는 인스턴스 변수
        self.work_time = work_time  # 객체의 근무 시간을 저장
        self.per_pay = per_pay      # 객체의 시급을 저장
        self.pay = 0                # 초기에 주급은 0원으로 설정해둡니다.
        self.process()              # 객체가 만들어지자마자 process() 메서드를 호출하여 즉시 주급을 계산합니다.

    # 주급을 계산하는 메서드(클래스 안에 있는 함수)입니다.
    def process(self):
        # 근무 시간과 시급을 곱하여 주급(self.pay)을 계산하고 저장합니다.
        self.pay = self.work_time * self.per_pay
        
    # 직원 정보를 화면에 출력해주는 메서드입니다.
    def display(self):
        # f-string을 활용해 정보들을 보기 좋게 출력합니다.
        print(f"이름: {self.name}, 근무시간: {self.work_time}시간, 시급: {self.per_pay:,}원, 주급: {self.pay:,}원")

# 여러 직원을 묶어서 관리하는 WeekPayManager 클래스를 정의합니다.
class WeekPayManager:
    # 객체 생성 시 직원들을 담을 빈 리스트를 만듭니다.
    def __init__(self):
        self.employee_list = []
        
    # 작성된 직원 객체(Weekpay)를 명단 리스트에 추가하는 메서드입니다.
    def add_employee(self, employee):
        self.employee_list.append(employee)
        
    # 명단에 있는 모든 직원의 정보를 화면에 출력하는 메서드입니다.
    def display_all(self):
        print("=== 직원 전체 주급 목록 ===")
        # 리스트에 담긴 직원 객체를 하나씩 꺼내어 각각의 display() 메서드를 호출합니다.
        for emp in self.employee_list:
            emp.display()

# 이 파이썬 파일이 프로그램의 시작점일 때만 아래 코드를 실행하라는 의미입니다.
if __name__ == "__main__":
    # 직원 관리자 객체를 하나 만듭니다.
    manager = WeekPayManager()
    
    # manager.add_employee()에 Weekpay로 생성한 객체를 바로 넘겨주어 명단에 추가시킵니다.
    manager.add_employee(Weekpay("홍길동", 40, 10000))
    manager.add_employee(Weekpay("임꺽정", 30, 20000))
    manager.add_employee(Weekpay("장길산", 20, 30000))
    
    # 모든 직원의 정보를 출력하라고 명령을 내립니다.
    manager.display_all()
