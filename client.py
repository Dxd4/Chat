import socket, threading

def send():
	while True:
		msg = input("\nMe > ")
		cli_sock.send(msg.encode())

def receive():
	while True:
		sen_name = cli_sock.recv(1024)
		data = cli_sock.recv(1024)
		print(f"\n{sen_name.decode()} > {data.decode()}\n")

if __name__ == "__main__":
	cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	HOST = input("Ip address: ")
	PORT = int(input("Port: "))
	cli_sock.connect((HOST, PORT))	 
	print('Connected to chat')
	uname = input("Nickname: ")
	cli_sock.send(uname.encode())

	thread_send = threading.Thread(target = send)
	thread_send.start()

	thread_receive = threading.Thread(target = receive)
	thread_receive.start()