import rclpy
from rclpy.node import Node

# ROS 2에서는 프로그램을 'Node'라고 부릅니다.
# Node 클래스를 상속받아 나만의 노드를 만듭니다.
class MyMinimalNode(Node):
    def __init__(self):
        # 노드 이름을 'basic_tutorial_node'로 설정합니다.
        super().__init__('basic_tutorial_node')
        
        # 1초마다 한 번씩 실행될 타이머를 설정합니다.
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        # 터미널에 로그를 출력합니다.
        self.get_logger().info(f'안녕하세요! ROS 2 노드가 {self.count}초째 실행 중입니다.')
        self.count += 1

def main(args=None):
    # rclpy를 초기화합니다.
    rclpy.init(args=args)
    
    # 노드 객체를 생성합니다.
    node = MyMinimalNode()
    
    try:
        # 노드가 계속 돌면서 콜백(timer_callback)을 수행하도록 합니다.
        # 실행 중에 Control + C를 누르면 중단됩니다.
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('사용자에 의해 노드가 종료되었습니다.')
    finally:
        # 노드와 rclpy를 안전하게 종료합니다.
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
