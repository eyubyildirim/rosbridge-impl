import time, roslibpy, threading

global client
client = roslibpy.Ros(host='localhost', port=9090)
client.run()


def send_message(linearX, angularZ):
    global client

    talker = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist')

    twist = roslibpy.Message({
        'linear': {
            'x': linearX,
            'y': 0.0,
            'z': 0.0
        },
        'angular': {
            'x': 0.0,
            'y': 0.0,
            'z': angularZ
        },
    })
    talker.publish(twist)

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


t2 = threading.Thread(target=receive_message, args=())

t2.start()

