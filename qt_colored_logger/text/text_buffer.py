# ##########################   Qt_Colored-logger   ########################### #
# ---------------------------------------------------------------------------- #
#                                                                              #
# Copyright © 2023 Kalynovsky Valentin. All rights reserved.                   #
#                                                                              #
# Licensed under the Apache License, Version 2.0 (the "License");              #
# you may not use this file except in compliance with the License.             #
# You may obtain a copy of the License at                                      #
#                                                                              #
#     http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS,            #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.     #
# See the License for the specific language governing permissions and          #
# limitations under the License.                                               #
#                                                                              #
# ---------------------------------------------------------------------------- #
# ############################################################################ #

import sys, re

from qt_colored_logger.basic.patterns import Singleton

class BasicTextBuffer(Singleton):
	def __init__(self):
		self._text_buffer: list[str] = []

	def append(self, message: str):
		self._text_buffer.append(f"{message}")

	def replace(self, number_string: int, message: str):
		if number_string < len(self._text_buffer):
			self._text_buffer[number_string] = f"{message}"
		else:
			self._text_buffer.extend([""] * (number_string - len(self._text_buffer)))
			self.append(message)

	def get_data(self):
		return self._text_buffer

	def save(self, name_file: str = "buffer"):
		with open(name_file, "w") as text_buffer_file:
			text_buffer_file.write('\n'.join(self._text_buffer))

	def __lshift__(self, other):
		self.append(f"{other}")

	def __rshift__(self, other):
		self.save(other)

class TextBuffer(BasicTextBuffer):
	def __init__(self, console_width: int = 60):
		super().__init__()
		self._cursor_string: int = 0
		self._buffer_size: int = 0
		self.width = console_width

	def append(self, message: str):
		excess_console_string = len(re.sub(r"\033\[.*?m", "", message)) // self.width
		self._buffer_size += 1 + excess_console_string
		self._text_buffer.append(f"{message}")

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
