import socket
import json


class Client:
    def __init__(self):
        self.host = "192.168.86.100"
        self.port = 8000
    
        self.pi_num = socket.gethostname()  # gets pi number in cluster. ***PI HOSTNAME MUST BE SET AS ONLY A NUMBER***

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
    
        except socket.error as err:
            print('Client failed: {}'.format(err))

        message = serialize_data(self.pi_num)
        self.sock.send(message)  # send json serialized pi number
    
        while True:
            print(self.sock.recv(4096))

    def send_message(self):
        pass



def serialize_data(data):
    return json.dumps(data).encode()


def deserialize_data(serialized_data):
    return json.loads(serialized_data).decode()


if __name__ == '__main__':
    start_client()
