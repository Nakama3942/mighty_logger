import sys, time

from qt_colored_logger._basic import _Singleton

class TextBuffer(_Singleton):
	def __init__(self, delay: float = 0.0):
		self._text_buffer: list[str] = []
		self._cursor_string: int = 0
		self._buffer_size: int = 0
		self.delay = delay

	def append(self, message: str):
		self._text_buffer.append(message)
		self._buffer_size = len(self._text_buffer)

	def replace(self, message: str, number_string: int):
		try:
			self._text_buffer[number_string] = message
		except IndexError:
			while len(self._text_buffer) != number_string:
				self.append("")
			self.append(message)

	def update_console(self):
		match self._buffer_size:
			case 1:
				pass
			case 2:
				sys.stdout.write(f'\r\033[K')
			case _:
				# todo оптимизировать, так как если строка не вмещается в
				# длинну экрана - фактическое количество строк увеличивается
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
	buffer.replace("15", 2)
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
