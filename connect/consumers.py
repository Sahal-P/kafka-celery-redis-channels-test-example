import json

from channels.generic.websocket import WebsocketConsumer


class TestConsumer(WebsocketConsumer):
    def connect(self):
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        self.room_name = "test_consumer"  
        self.room_group_name = "test_consumer_group"  
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))