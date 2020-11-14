from roslibpy import Message

class Message(Message):

    def __init__(self, values=None):
        self.message = {}
        if values is not None:
            self.update(values)