import json
from channels.generic.websocket import WebsocketConsumer

class OperacionConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        operation = text_data_json['operation']
        num1 = float(text_data_json['num1'])
        num2 = float(text_data_json['num2'])

        if operation == 'suma':
            resultado = num1 + num2
        elif operation == 'div':
            resultado = num1 / num2
        elif operation == 'resta':
            resultado = num1 - num2
        elif operation == 'multi':
            resultado = num1 * num2

        self.send(text_data=json.dumps({
            'message': resultado
        }))