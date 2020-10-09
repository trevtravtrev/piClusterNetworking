import socket
import json
import time

import messages

class Client:
    def __init__(self, server_host, server_port):
        self.host = server_host
        self.port = server_port
        self.connected = False
        
        # get pi number in cluster. ***PI HOSTNAME MUST BE SET AS ONLY A NUMBER***
        self.pi_num = socket.gethostname()
        
        self.connect()
        self.client_handler()


    def connect(self):
        while True:
            try:
                # Connect to server
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                print("Successfully connected to server.")
                self.connected = True
                
                # Handshake with server (send pi number)
                message = messages.create_message("pi_num", self.pi_num)
                self.sock.sendall(message)
                break
            
            except Exception as e:
                self.connected = False
                print(f'connect error: {e}')
                
    def client_handler(self):
        while True:
            try:
                if self.connected:
                    data = self.sock.recv(4096)
                    
                    if data:
                        message = messages.deserialize_data(data)
                        print(f'Message received: {message}')
                        self.message_handler(message)
                
                    else:
                        self.connected = False
                else:
                    print("Client disconnected. Trying to reconnect...")
                    self.connect()
                    
            except Exception as e:
                print(f'client_handler error: {e}')
            
    def message_handler(self, message):
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
            
            
def main():
    c = Client("192.168.86.100", 8000)


if __name__ == '__main__':
    main()
