import socket
import datetime
from system import System


def save_log(text):


	log = open("logs.txt", "a")  #Запись логов



	now = datetime.datetime.now() 
	log.write('<<' + str(now) + '>> ' + text + '\n')

	log.close()


system = System("")


sock = socket.socket()
print('Запуск сервера!')
save_log('Запуск сервера!')


port = input('Введите порт: ')  #Порт 9090
sock.bind(('', int(port)))


while True:

	sock.listen(1)
	print(f"Слушаем порт ({port})")
	save_log(f"Слушаем порт ({port})")


	try:
		conn, addr = sock.accept()
	except KeyboardInterrupt as k:
		print(f"Ошибка {k}")
		save_log(f"Ошибка {k}")
		exit()

	print(f"Подключение к {addr}")
	save_log(f"Подключение к {addr[0]}:{addr[1]}")

	print()

	message = "Введите домашнюю директорию"
	conn.send(message.encode())
	print(f"Домашнаяя директория: {message}")

	while True:

		try:
			message = ""
			data = conn.recv(1024).decode("utf8")

		except ConnectionResetError as e:
			print(f"Ошибка {e}")
			save_log(f"Ошибка {e}")
			exit()

		except KeyboardInterrupt as k:
			print(f"Ошибка {k}")
			save_log(f"Ошибка {k}")
			exit()


		if data == "" or data == "exit":
			print(f"Клиент отключен")
			save_log(f"Клиент отключен")
			break

		elif data == "stop":
			break

		elif system.way != "":
			message = system.main(data)



		if system.way == "":
			message = system.setWay(data)
			save_log(message)


		print(f"Корневая папка: {data}\n")
		save_log(f"Корневая папка: {data}")


		conn.send(message.encode())
		print(f"Отправка: {message}")
		save_log(f"Отправка: {message}")

	if data == "stop":
		break

print('Закрытое соединение.')
save_log('Закрытое соединение.')
conn.close()
