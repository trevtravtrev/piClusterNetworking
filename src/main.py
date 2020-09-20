import server
import protocol

s = server.Server("192.168.86.100", 8000)
num_clients = s.get_num_clients()