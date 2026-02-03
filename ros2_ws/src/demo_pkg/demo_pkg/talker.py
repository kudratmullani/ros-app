import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleTalker(Node):
    def __init__(self):
        super().__init__('simple_talker')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = 'Hello from ROS 2 Jazzy Docker!'
        self.publisher.publish(msg)
        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    node = SimpleTalker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
