import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('node_b') 
        self.subscription = self.create_subscription(
            String,
            'hello_topic',        
            self.callback,          # 收到消息后的回调函数
            10)                

    def callback(self, msg):
        self.get_logger().info('学号：2024020803 姓名：李金凤') 

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
