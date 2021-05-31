import socket

class Exit(Exception):
	pass

sock = socket.socket()
server = input('Введите сервер: ')  # Вводим команду localhost
port = input('Введите порт: ')  # Вводим порт 9090
print()

try:

	sock.connect((server, int(port)))

	# Сервер
	print(f"IP: {server}; Port: {port}")

	# Клиент
	host = sock.getsockname()
	print(f"Клиент IP: {host[0]}; Port: {host[1]}")

except ConnectionRefusedError as c:
	print(f"Ошибка {c}")
	exit()


while True:

	try:
		data = sock.recv(1024).decode("utf8")

		# отключение от сервера
		if len(data) == 0 or data.lower() == 'stop' or data.lower() == 'exit':
			raise Exception("Потрачено.")

	except ConnectionResetError as e:
		print(f"Ошибка {e}")
		sock.close()
		exit()

	except Exception as s:
		print(f"Ошибка {s}")
		sock.close()
		exit()

	print(f"\nСервер: {data}")


	try:
		promt = input("\nВведите комманду: ")
	except KeyboardInterrupt as k:
		print(f"Ошибка {k}")
		exit()


	try:
		result = sock.send(promt.encode())
		if not result:
			raise Exception("Данные не найдены")
	except Exception as e:
		print(f"Ошибка {e}")
		exit()


sock.close()
