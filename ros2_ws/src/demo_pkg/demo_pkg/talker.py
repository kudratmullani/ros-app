import rclpy
from rclpy.node import Node

class SimpleTalker(Node):
    def __init__(self):
        super().__init__('simple_talker')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello from ROS 2 Jazzy Docker!')

def main():
    rclpy.init()
    node = SimpleTalker()
    rclpy.spin(node)   # 👈 THIS MUST EXIST
    rclpy.shutdown()

if __name__ == '__main__':
    main()
