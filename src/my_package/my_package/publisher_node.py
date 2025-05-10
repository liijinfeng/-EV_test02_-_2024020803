import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('node_a') 
        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)
        self.timer = self.create_timer(1, self.timer_callback)  # 每1秒触发一次回调函数

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, ROS2!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'发布：{msg.data}') 

def main(args=None):
    rclpy.init(args=args)  
    node = PublisherNode()  
    rclpy.spin(node)      
    node.destroy_node()   
    rclpy.shutdown()   

if __name__ == '__main__':
    main()
