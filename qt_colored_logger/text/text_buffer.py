"""
Module with implementation of text buffer.
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

from qt_colored_logger.basic.patterns import Singleton

class TextBufferBase(Singleton):
	def __init__(self):
		self._text_buffer: list[str] = []

	def __lshift__(self, other) -> None:
		"""
		Used to add a string to the end of the buffer.

		:param other: The line to be added
		"""
		self.append(f"{other}")

	def __rshift__(self, other) -> None:
		"""
		Used to save a buffer to the file.

		:param other: The name of the file where you want to save the buffer
		"""
		self.save(other)

	def append(self, message: str) -> None:
		pass

	def insert(self, number_string: int, message: str) -> None:
		pass

	def replace(self, number_string: int, message: str) -> None:
		pass

	def get_data(self) -> list:
		"""
		Returns a list of strings from a text buffer.

		:return: a list of text buffer lines
		"""
		return self._text_buffer

	def save(self, name_file: str = "buffer") -> None:
		pass

	def update_console(self) -> None:
		pass

class BasicTextBuffer(TextBufferBase):
	"""
	A class with a basic implementation of a simple text buffer. It is intended
	to be used in conjunction with HTML, but this is optional.
	"""

	def __init__(self):
		super().__init__()

	def append(self, message: str) -> None:
		"""
		Adds a string to the end of the text buffer.

		:param message: The string to be added to the buffer
		"""
		self._text_buffer.append(f"{message}")

	def insert(self, number_string: int, message: str) -> None:
		"""
		Adds a string to the middle of the text buffer at the specified position.

		:param number_string: Position (number) of the line to which you need to add a string
		:param message: The string to be placed on the position
		"""
		if number_string < len(self._text_buffer):
			self._text_buffer.insert(number_string, f"{message}")
		else:
			self._text_buffer.extend([""] * (number_string - len(self._text_buffer)))
			self.append(message)

	def replace(self, number_string: int, message: str) -> None:
		"""
		Replaces a specific string in a text buffer. If there is no such string, the method
		fills the list with empty strings up to the required position and *adds* the string.

		:param number_string: Position (number) of the string to be replaced (added)
		:param message: A string that will replace the previous one by position
		"""
		if number_string < len(self._text_buffer):
			self._text_buffer[number_string] = f"{message}"
		else:
			self._text_buffer.extend([""] * (number_string - len(self._text_buffer)))
			self.append(message)

	def save(self, name_file: str = "buffer") -> None:
		"""
		Saves the text of the buffer to a file.

		:param name_file: The name of the file where the buffer will be saved
		"""
		with open(name_file, "w") as text_buffer_file:
			text_buffer_file.write('\n'.join(self._text_buffer))

	def update_console(self) -> None:
		"""
		Refreshes the console, erasing output text and outputting an updated buffer.
		"""
		raise NotImplementedError("Method update_console() is not implemented in the base class.")

class TextBuffer(TextBufferBase):
	"""
	A class with an advanced implementation of the console text buffer. It is not necessary to use it
	only in the console, but almost all methods are reimplemented for more complex algorithms, taking
	into account the width of the console (number of characters per line) and use ANSI escape codes
	that are only found in the console.
	"""

	def __init__(self, console_width: int = 60):
		super().__init__()
		self._cursor_string: int = 0
		self._buffer_size: int = 0
		self.width = console_width

	def append(self, message: str) -> None:
		excess_console_string = len(re.sub(r"\033\[.*?m", "", message)) // self.width
		self._buffer_size += 1 + excess_console_string
		self._text_buffer.append(f"{message}")

	def insert(self, number_string: int, message: str):
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
		with open(name_file, "w") as text_buffer_file:
			if clean:
				for item in self._text_buffer:
					text_buffer_file.write("{}\n".format(re.sub(r"\033\[.*?m", "", item)))
			else:
				text_buffer_file.write('\n'.join(self._text_buffer))

	def update_console(self) -> None:
		"""
		Refreshes the console, erasing output text and outputting an updated buffer.
		"""
		# todo Translate to thread in a future update
		if self._cursor_string == 0:
			sys.stdout.write(f'\r\033[K')
		else:
			sys.stdout.write(f'\033[{self._cursor_string}A\r\033[J')
		sys.stdout.write('\n'.join(self._text_buffer))
		sys.stdout.flush()  # Clearing the output buffer so that the changes are displayed immediately
		self._cursor_string = self._buffer_size - 1
