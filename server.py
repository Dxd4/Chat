import socket, threading, time

def accept_client(messages):
	while True:
		cli_sock, cli_add = ser_sock.accept()
		uname = cli_sock.recv(1024)
		CONNECTION_LIST.append((uname, cli_sock))
		print(f"{uname.decode()} is connected")
		thread_client = threading.Thread(target = broadcast_usr, args=[uname, cli_sock, messages])
		thread_client.start()

def broadcast_usr(uname, cli_sock, messages):
	while True:
		try:
			data = cli_sock.recv(1024)
			if data:
				print(f"{uname.decode()} > {data.decode()}")
				messages += (f"\n{uname.decode()} > {data.decode()}")
				b_usr(cli_sock, uname, data)
		except Exception as x:
			print(x.message)
			break

def b_usr(cs_sock, sen_name, msg):
	for client in CONNECTION_LIST:
		if client[1] != cs_sock:
			client[1].send(sen_name)
			client[1].send(msg)


if __name__ == "__main__":	
	messages = ""
	CONNECTION_LIST = []
	ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	HOST = "localhost"
	PORT = 2288
	ser_sock.bind((HOST, PORT))
	ser_sock.listen(1)
	print('Chat server started on port : ' + str(PORT))
	thread_ac = threading.Thread(target = accept_client(messages))
	thread_ac.start()