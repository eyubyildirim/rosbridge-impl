from geometry_msgs.msg import Twist, Vector3
import time, roslibpy, threading
import geometry_msgs.msg

global client
client = roslibpy.Ros(host='localhost', port=9090)
client.run()


def send_message():
    global client
    count = 1

    talker = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist')

    time.sleep(2)

    while client.is_connected:
        twist = roslibpy.Message({
            'linear': {
                'x': 1.0,
                'y': 0.0,
                'z': 0.0
            },
            'angular': {
                'x': 0.0,
                'y': 0.0,
                'z': 1.0
            },
        })
        talker.publish(twist)
        time.sleep(1)

    talker.unadvertise()


def receive_message():
    global client

    listener = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist')
    listener.subscribe(lambda message: print('Heard talking: ', message['angular'], message['linear']))

    try:
        while client.is_connected:
            pass
    except KeyboardInterrupt:
        client.terminate()


t1 = threading.Thread(target=send_message, args=())
t2 = threading.Thread(target=receive_message, args=())

t2.start()
t1.start()
