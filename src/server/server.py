import socket
import threading
import json
import time


class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.conn = connection
        self.addr = address
        self.pi_num = deserialize_data(
            self.conn.recv(4096))  # receive pi number from client, json deserialize, and store it
        self.start()

    # def run(self):
    #     while True:
    #         print('Client sent:', self.conn.recv(4096).decode())
    #         self.conn.send(b'Oi you sent something to me')

    def send_message(self, message):
        self.conn.send(message)

    def terminate(self):
        self.conn.close()


def start_server():
    host = "192.168.86.100"
    port = 8000
    clients = {}

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        print("Server started successfully.")

        sock.listen(7)
        print("Listening for connections.")

        while True:
            connection, address = sock.accept()
            client = ClientThread(connection, address)

            for i in range(10):  # wait up to 10 seconds for client to send its number upon connection
                if client.pi_num:
                    clients[client.pi_num] = client
                    break
                else:
                    time.sleep(1)
                    continue

            # print(clients)
            # clients.get('2').conn.sendall('hello'.encode())

            if not client.pi_num:  # terminate client connection if it doesn't send its number within 10 seconds
                client.terminate()
                print("terminated")


    except socket.error as err:
        print('Server failed: {}'.format(err))


def breakup_data(num_clients, data):
    pass


def create_message(pi_number, script_name, data=None):
    return [pi_number, script_name, data]


def serialize_data(data):
    return json.dumps(data).encode()


def deserialize_data(serialized_data):
    return json.loads(serialized_data)


if __name__ == '__main__':
    start_server()
