import socket
import json


def start_client():
    host = "192.168.86.100"
    port = 8000

    pi_num = socket.gethostname()  # gets pi number in cluster. ****PI HOSTNAME MUST BE SET AS ONLY A NUMBER****

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        message = serialize_data(pi_num)
        sock.send(message)  # send json serialized pi number
        print("sent")

    except socket.error as err:
        print('Client failed: {}'.format(err))

    while True:
        print(sock.recv(4096))


def serialize_data(data):
    return json.dumps(data).encode()


def deserialize_data(serialized_data):
    return json.loads(serialized_data).decode()


if __name__ == '__main__':
    start_client()
