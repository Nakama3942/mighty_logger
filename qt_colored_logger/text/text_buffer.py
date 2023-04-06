import sys, time, re

from qt_colored_logger._basic import _Singleton

class TextBuffer(_Singleton):
	def __init__(self, delay: float = 0.0, console_width: int = 60):
		self._text_buffer: list[str] = []
		self._cursor_string: int = 0
		self._buffer_size: int = 0
		self.delay = delay
		self.width = console_width

	def append(self, message: str):
		self._text_buffer.append(f"{message}")
		console_string = len(re.sub(r"\033\[.*?m", "", message)) // self.width
		self._buffer_size = self._buffer_size + console_string + 1

	def replace(self, message: str, number_string: int):
		if number_string > self._cursor_string:
			count_new_string = (number_string - len(self._text_buffer))
			self._text_buffer.extend([""] * count_new_string)
			self._buffer_size = self._buffer_size + count_new_string
			self.append(message)
		else:
			old_console_string = len(re.sub(r"\033\[.*?m", "", self._text_buffer[number_string])) // self.width
			new_console_string = len(re.sub(r"\033\[.*?m", "", message)) // self.width
			self._buffer_size = self._buffer_size + new_console_string - old_console_string
			self._text_buffer[number_string] = f"{message}"

	def update_console(self):
		# Перевести в поток в будущем обновлении
		match self._cursor_string:
			case 0:
				sys.stdout.write(f'\r\033[K')
				sys.stdout.write('\n'.join(self._text_buffer))
			case _:
				sys.stdout.write(f'\033[{self._cursor_string}A\r\033[J')
				sys.stdout.write('\n'.join(self._text_buffer))
		sys.stdout.flush()  # Clearing the output buffer so that the changes are displayed immediately
		self._cursor_string = self._buffer_size - 1
		time.sleep(self.delay)

if __name__ == "__main__":
	buffer = TextBuffer(0.2)

	buffer.append("111")
	buffer.update_console()

	buffer.append("222")
	buffer.update_console()

	buffer.append("333")
	buffer.update_console()

	buffer.append("444")
	buffer.update_console()

	buffer.append("555")
	buffer.replace("15", 20)
	buffer.update_console()

	buffer.replace("9", 3)
	buffer.update_console()

	buffer.append("666")
	buffer.replace("8888", 1)
	buffer.update_console()

	buffer.append("777")
	buffer.update_console()

	buffer.append("888")
	buffer.replace("55", 5)
	buffer.update_console()

	buffer.append("999")
	buffer.replace("6969", 0)
	buffer.update_console()

	buffer.replace("88888888", 1)
	buffer.update_console()

	buffer.append("111111")
	buffer.update_console()

	buffer.append("121212")
	buffer.replace("10", 8)
	buffer.update_console()
