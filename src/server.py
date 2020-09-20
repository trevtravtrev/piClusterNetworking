import socket
import threading
import messages
import json
import time


class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connected = True
        self.conn = connection
        self.addr = address
        self.pi_num = messages.deserialize_data(self.conn.recv(4096))  # receive pi # from client
        self.message = None
        self.start()

    def run(self):
        while True:
            self.message = messages.deserialize_data(self.conn.recv(4096))

            if not self.message:
                self.connected = False

    def send_to_client(self, message):
        self.conn.send(message)

    def terminate(self):
        self.conn.close()


class Server:
    def __init__(self, host_ip, host_port):
        self.host = host_ip
        self.port = host_port
        self.clients = {}

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.host, self.port))
            print("Server started successfully")

            self.sock.listen(7)
            print("Listening for connections...")

            while True:
                connection, address = self.sock.accept()
                print("A client is attempting to connect...")
                client = ClientThread(connection, address)

                for i in range(10):  # wait up to 10 seconds for client to send its pi number upon connection
                    if client.pi_num:
                        self.clients[client.pi_num] = client
                        print('Pi #{} successfully connected'.format(client.pi_num))
                        break
                    else:
                        time.sleep(1)
                        continue

                if not client.pi_num:  # terminate client connection if it doesn't send its number within 10 seconds
                    client.terminate()
                    print('Client ({} {}) terminated.'.format(client.conn, client.addr))


        except socket.error as err:
            print('Error: {}'.format(err))

    def get_num_clients(self):
        return len(self.clients)

    def send_message_all(self, message, is_split=True):
        """
        :param message: Input split message (type: list, dict, str, tuple obtained by split_list(), split(dict),
        split(sting), split(tuple)) or input a non-split message to send same message to all pis (type: list, dict,
        str, tuple, int)
        :param is_split: True if data is different split data to be split across all pis for distributed processing,
        False if data is same single message to be sent to all pis
        :return:
        """
        if is_split:
            if self.clients:
                if isinstance(message, list):
                    index = 0
                    for key in self.clients:
                        client = self.clients.get(key)
                        serialized_message = messages.serialize_data(message[index])  # serialize data
                        client.send_to_client(serialized_message)
                        index += 1

                elif isinstance(message, dict):
                    pass

                else:
                    print("Error: invalid data input")

            else:
                print("Error: 'clients' dictionary is empty.")

        else:
            if self.clients:
                for key in self.clients:
                    client = self.clients.get(key)
                    serialized_message = messages.serialize_data(message)
                    client.send_to_client(serialized_message)

    def send_message(self, client_num, data):
        pass
