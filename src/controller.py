import socket
import json

import messages

class Client:
	def __init__(self, server_host, server_port):
		self.host = server_host
		self.port = server_port
		self.connected = False
		
		# get pi number in cluster. ***PI HOSTNAME MUST BE SET AS ONLY A NUMBER***
		# pi_num 0 is known as the controller pi by the server
		self.pi_num = 0
		
		self.connect()
		self.controller()

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
                
	def controller(self):
		while True:
			try:
				if self.connected:
					choice = int(input("1 Shutdown\n2 Reboot\n3 Test\nEnter Number: "))
					
					if choice == 1:
						message = messages.create_message("shutdown")
						self.sock.sendall(message)
					
					elif choice == 2:
						message = messages.create_message("reboot")
						self.sock.sendall(message)
						
					elif choice == 3:
						message = messages.create_message("test")
						self.sock.sendall(message)
						
					else:
						print("Invalid input. Try again...")
						continue
						
					print("Message sent to server")
					
				else:
					print("Client disconnected. Trying to reconnect...")
					self.connect()
				
			except Exception as e:
				print(f'controller error: {e}')
				self.connected = False


if __name__ == '__main__':
    c = Client("192.168.86.100", 8000)
