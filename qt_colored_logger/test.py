import sys, time

class Logger:
    def __init__(self):
        self.text_buffer = []

    def log(self, message):
        self.text_buffer.append(message)

class ConsoleLogger:
	def __init__(self, logger):
		super().__init__()
		self.logger = logger

	def update_console(self):
		if len(self.logger.text_buffer) == 2:
			sys.stdout.write(f'\r\033[J')
		else:
			sys.stdout.write(f'\033[{len(self.logger.text_buffer) - 2}A\r\033[J')
		sys.stdout.write('\n'.join(self.logger.text_buffer))  # Заменяем содержимое строки в консоли
		sys.stdout.flush()  # Очищаем буфер вывода, чтобы изменения сразу отобразились

if __name__ == "__main__":
	logger = Logger()
	console_logger = ConsoleLogger(logger)

	logger.log("111")
	console_logger.update_console()

	time.sleep(1)

	logger.log("222")
	console_logger.update_console()

	time.sleep(1)

	logger.log("333")
	console_logger.update_console()

	time.sleep(1)

	logger.log("444")
	console_logger.update_console()

	time.sleep(1)

	logger.log("555")
	console_logger.update_console()
	logger.text_buffer[2] = "15"

	time.sleep(1)

	logger.log("666")
	console_logger.update_console()

	time.sleep(1)

	logger.log("777")
	console_logger.update_console()
