from networking.client import *

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
                


if __name__ == '__main__':
	main()
