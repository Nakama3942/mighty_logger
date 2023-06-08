"""
Module with implementation of text buffers.
\n
Copyright © 2023 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys, re

from mighty_logger.basic.exceptions import ReCreationException
from mighty_logger.basic.patterns import Singleton
from mighty_logger.basic.text_buffer_type import TextBufferType

class BasicTextBuffer(Singleton, TextBufferType):
	"""
	A class with a basic implementation of a simple text buffer. It is intended
	to be used in conjunction with HTML, but this is optional.
	"""

	def __init__(self) -> None:
		if not hasattr(self, "_text_buffer"):
			super().__init__()
		else:
			raise ReCreationException("BasicTextBuffer class object already created")

	def append(self, message: str) -> None:
		self._text_buffer.append(f"{message}")

	def insert(self, number_string: int, message: str) -> None:
		if number_string < len(self._text_buffer):
			self._text_buffer.insert(number_string, f"{message}")
		else:
			self._text_buffer.extend([""] * (number_string - len(self._text_buffer)))
			self.append(message)

	def replace(self, number_string: int, message: str) -> None:
		if number_string < len(self._text_buffer):
			self._text_buffer[number_string] = f"{message}"
		else:
			self._text_buffer.extend([""] * (number_string - len(self._text_buffer)))
			self.append(message)

	def save(self, name_file: str = "buffer", clean: bool = True) -> None:
		with open(name_file, "w", encoding="utf-8") as text_buffer_file:
			if clean:
				text_buffer_file.write(self._text_buffer[0] + '\n' + '\n<br>'.join(self._text_buffer[1:]))
			else:
				text_buffer_file.write(self._text_buffer[0] + '\n' + '\n'.join(self._text_buffer[1:]))

	def update_console(self) -> None:
		super().update_console()

class TextBuffer(Singleton, TextBufferType):
	"""
	A class with an advanced implementation of the console text buffer. It is not necessary to use it
	only in the console, but almost all methods are reimplemented for more complex algorithms, taking
	into account the width of the console (number of characters per line) and use ANSI escape codes
	that are only found in the console.
	"""

	def __init__(self, console_width: int = 60) -> None:
		if not hasattr(self, "_text_buffer"):
			super().__init__()
			self._cursor_string: int = 0
			self._buffer_size: int = 0
			self.width = console_width
		else:
			raise ReCreationException("TextBuffer class object already created")

	def append(self, message: str) -> None:
		excess_console_string = len(re.sub(r"\033\[.*?m", "", message)) // self.width
		self._buffer_size += 1 + excess_console_string
		self._text_buffer.append(f"{message}")

	def insert(self, number_string: int, message: str) -> None:
		if number_string > self._cursor_string:
			count_empty_strings = (number_string - len(self._text_buffer))
			self._text_buffer.extend([""] * count_empty_strings)
			self._buffer_size += count_empty_strings
			self.append(message)
		else:
			excess_console_string = len(re.sub(r"\033\[.*?m", "", message)) // self.width
			self._buffer_size += 1 + excess_console_string
			self._text_buffer.insert(number_string, f"{message}")

	def replace(self, number_string: int, message: str) -> None:
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

	def save(self, name_file: str = "buffer", clean: bool = True) -> None:
		with open(name_file, "w", encoding="utf-8") as text_buffer_file:
			if clean:
				for item in self._text_buffer:
					text_buffer_file.write("{}\n".format(re.sub(r"\033\[.*?m", "", item)))
			else:
				text_buffer_file.write('\n'.join(self._text_buffer))

	def update_console(self) -> None:
		# todo Translate to thread in a future update
		if self._cursor_string == 0:
			sys.stdout.write(f'\r\033[K')
		else:
			sys.stdout.write(f'\033[{self._cursor_string}A\r\033[J')
		sys.stdout.write('\n'.join(self._text_buffer))
		sys.stdout.flush()  # Clearing the output buffer so that the changes are displayed immediately
		self._cursor_string = self._buffer_size - 1
