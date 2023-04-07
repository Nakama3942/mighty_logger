import sys, re

from qt_colored_logger._basic import _Singleton

class TextBuffer(_Singleton):
	def __init__(self, console_width: int = 60):
		self._text_buffer: list[str] = []
		self._cursor_string: int = 0
		self._buffer_size: int = 0
		self.width = console_width

	def append(self, message: str):
		self._text_buffer.append(f"{message}")
		excess_console_string = len(re.sub(r"\033\[.*?m", "", message)) // self.width
		self._buffer_size += 1 + excess_console_string

	def replace(self, number_string: int, message: str):
		if number_string > self._cursor_string:
			count_empty_strings = (number_string - len(self._text_buffer))
			self._text_buffer.extend([""] * count_empty_strings)
			self._buffer_size += count_empty_strings
			self.append(message)
		else:
			old_excess_console_strings = len(re.sub(r"\033\[.*?m", "", self._text_buffer[number_string])) // self.width
			new_excess_console_strings = len(re.sub(r"\033\[.*?m", "", message)) // self.width
			self._buffer_size += new_excess_console_strings - old_excess_console_strings
			self._text_buffer[number_string] = f"{message}"

	def save(self, name_file: str = "buffer", clean: bool = True):
		with open(name_file, "w") as text_buffer_file:
			if clean:
				for item in self._text_buffer:
					text_buffer_file.write("{}\n".format(re.sub(r"\033\[.*?m", "", item)))
			else:
				text_buffer_file.write('\n'.join(self._text_buffer))

	def update_console(self):
		# Перевести в поток в будущем обновлении
		if self._cursor_string == 0:
			sys.stdout.write(f'\r\033[K')
		else:
			sys.stdout.write(f'\033[{self._cursor_string}A\r\033[J')
		sys.stdout.write('\n'.join(self._text_buffer))
		sys.stdout.flush()  # Clearing the output buffer so that the changes are displayed immediately
		self._cursor_string = self._buffer_size - 1

	def __lshift__(self, other):
		self.append(f"{other}")

	def __rshift__(self, other):
		self.save(other)

# if __name__ == "__main__":
# 	buffer = TextBuffer()
#
# 	buffer.append("111")
# 	buffer.update_console()
#
# 	buffer.append("222")
# 	buffer.update_console()
#
# 	buffer.append("333")
# 	buffer.update_console()
#
# 	buffer.append("444")
# 	buffer.update_console()
#
# 	buffer.append("555")
# 	buffer.replace("15", 2)
# 	buffer.update_console()
#
# 	buffer.replace("9", 3)
# 	buffer.update_console()
#
# 	buffer.append("666")
# 	buffer.replace("8888", 1)
# 	buffer.update_console()
#
# 	buffer.append("777")
# 	buffer.update_console()
#
# 	buffer.append("888")
# 	buffer.replace("55", 5)
# 	buffer.update_console()
#
# 	buffer.append("999")
# 	buffer.replace("6969", 0)
# 	buffer.update_console()
#
# 	buffer.replace("88888888", 1)
# 	buffer.update_console()
#
# 	buffer.append("111111")
# 	buffer.update_console()
#
# 	buffer.append("121212")
# 	buffer.replace("10", 8)
# 	buffer.update_console()
#
# 	buffer.save()
