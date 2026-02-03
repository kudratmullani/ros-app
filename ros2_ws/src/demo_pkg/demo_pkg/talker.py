import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
import time

class SimpleTalker(Node):
    def __init__(self):
        super().__init__('simple_talker')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello from ROS 2 Jazzy Docker!')

def main():
    rclpy.init()
    node = SimpleTalker()

    try:
        rclpy.spin(node)
    except ExternalShutdownException:
        node.get_logger().info('ROS shutdown requested (CI/Docker stop)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
