from networking.client import *

<<<<<<< HEAD
class ControllerClient(Client):
	def __init__(self, server_host, server_port, client_name):
		super().__init__(server_host, server_port, client_name)
		
	def client_handler(self):
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

def main():
	c = ControllerClient("192.168.86.100", 8000, "Controller")
	
=======
def main():
	client = Client("192.168.86.100", 8000)
	
	while True:
		try:
			if client.connected:
				choice = int(input("1 Shutdown\n2 Reboot\n3 Test\nEnter Number: "))
				
				if choice == 1:
					message = messages.create_message("shutdown")
					client.sock.sendall(message)
				
				elif choice == 2:
					message = messages.create_message("reboot")
					client.sock.sendall(message)
					
				elif choice == 3:
					message = messages.create_message("test")
					client.sock.sendall(message)
					
				else:
					print("Invalid input. Try again...")
					continue
					
				print("Message sent to server")
				
			else:
				print("Client disconnected. Trying to reconnect...")
				client.connect()
			
		except Exception as e:
			print(f'controller error: {e}')
			client.connected = False
                

>>>>>>> 5c352f3ad909e4552e1a5ad74958f681fa8a03a1

if __name__ == '__main__':
	main()
