import socket
import threading

from . import messages


class Server:
    def __init__(self, host_ip, host_port):
        self.host = host_ip
        self.port = host_port
        self.connected = False
        self.clients = {}

        self.start_server()
        self.connection_handler()
                

    def start_server(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.bind((self.host, self.port))
                self.connected = True
                print("Server started successfully")
                break
                
            except Exception as e:
                self.connected = False
                print(f'start_server error: {e}')
                
                
    def connection_handler(self):
        while True:
            try:
                if self.connected:
                    self.sock.listen(7)
                    print("Listening for connections...")
                    
                    connection, address = self.sock.accept()
                    
                    client = ClientThread(self, connection, address)
                    client.start()                    
                    
                else:
                    print("Server not running. Restarting...")
                    self.start_server()

            except Exception as e:
                print(f'connection_handler error: {e}')
            
            
    def send_all(self, data):
        try:
            message = messages.serialize_data(data)
            
            for pi_num in self.clients:
                self.clients.get(pi_num).sendall(message)
                
            print(f'Message successfully sent to {len(self.clients)} client(s)')
            
        except Exception as e:
            print(f'send_all error: {e}')
            
            
    def message_handler(self, message):
        print("""
You must override the server "message_handler" function with your own custom message parser. 

For example:

    try:
        if "shutdown" in message:
            print("Shutting down in 5 seconds...")
            time.sleep(5)
            os.system("sudo shutdown -h now")

        elif "reboot" in message:
            print("Rebooting in 5 seconds...")
            time.sleep(5)
            os.system("sudo shutdown -r now")

        elif "test" in message:
            print(f'Test message received: {message.get("test")}')

        else:
            print("Error: function not found in keys.")

    except Exception as e:
        print(f'message_handler error: {e}')
""")


class ClientThread(threading.Thread):
    def __init__(self, serv, connection, address):
        threading.Thread.__init__(self)
        self.server = serv
        self.conn = connection
        self.addr = address
        self.pi_num = ""


    def run(self):
        self.get_pi_num()
        self.client_handler()
            
            
    def client_handler(self):
        while True:
            try:
                data = self.conn.recv(4096)

                if data:
                    message = messages.deserialize_data(data)
                    print(f'Message received: {message}')

                    self.server.message_handler(message)
                    
                else:
                    self.remove_client()
                    break
                    
            except Exception as e:
                print(f'client_handler error: {e}')
                    
        
    def get_pi_num(self):
        try:
            data = self.conn.recv(4096)

            if data:
                message = messages.deserialize_data(data)
                print(f'Message received: {message}')

                if "pi_num" in message:
                    self.pi_num = message.get('pi_num')
                    self.server.clients[self.pi_num] = self.conn
                    print(f'Pi {self.pi_num} connected.')
                    print(f'{len(self.server.clients)} client(s) connected')

                else:
                    print("Error: pi_num not found in message.")
                
        except Exception as e:
            print(f'get_pi_num error: {e}')


    def remove_client(self):
        try:
            print('Client disconnected. Removing from client list...')
            del self.server.clients[self.pi_num]
            print(f'{len(self.server.clients)} clients(s) connected')
        
        except Exception as e:
            print(f'remove_client error: {e}')
