"""
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

from mighty_logger.basic.lib_types.environment_type import EnvironmentType

class TextBufferType:
	"""
	The data type that characterizes the Text Buffer.

	.. versionadded:: 0.0.0
	"""

	def __init__(self, env: EnvironmentType) -> None:
		self._text_buffer: list[str] = []
		self._environment: EnvironmentType = env

	def __lshift__(self, message: str) -> None:
		"""
		Used to add a string to the end of the Text Buffer.

		.. versionadded:: 0.0.0

		:param message: The string to be added
		:type message: str
		"""
		self.append(message)

	def __rshift__(self, name: str) -> None:
		"""
		Used to save a Text Buffer to the file.

		.. versionadded:: 0.0.0

		:param name: The name of the file where you want to save the Text Buffer
		:type name: str
		"""
		self.save(name, True)

	def get_data(self) -> list:
		"""
		Returns a list of strings from a Text Buffer.

		.. versionadded:: 0.0.0

		:return: A list of Text Buffer strings
		:rtype: list
		"""
		return self._text_buffer

	def append(self, message: str) -> None:
		"""
		Adds a string to the end of the Text Buffer.

		.. versionadded:: 0.0.0

		:param message: The string to be added to the Text Buffer
		:type message: str
		:raises NotImplementedError: Method append() is not implemented in the base class
		"""
		raise NotImplementedError("Method append() is not implemented in the base class")

	def insert(self, number_string: int, message: str) -> None:
		"""
		Adds a string to the middle of the Text Buffer at the specified position.

		.. versionadded:: 0.0.0

		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str
		:raises NotImplementedError: Method insert() is not implemented in the base class
		"""
		raise NotImplementedError("Method insert() is not implemented in the base class")

	def replace(self, number_string: int, message: str) -> None:
		"""
		Replaces a specific string in a Text Buffer. If there is no such string, the method
		fills the list with empty strings up to the required position and *adds* the string.

		.. versionadded:: 0.0.0

		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str
		:raises NotImplementedError: Method replace() is not implemented in the base class
		"""
		raise NotImplementedError("Method replace() is not implemented in the base class")

	def pop(self, number_string: int = -1) -> str:
		"""
		Removes and returns the specified string from the Text Buffer.

		.. versionadded:: 0.0.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str
		:raises NotImplementedError: Method pop() is not implemented in the base class
		"""
		raise NotImplementedError("Method pop() is not implemented in the base class")

	def remove(self, number_string: int = -1) -> None:
		"""
		Deletes without returning the specified string from the Text Buffer.

		.. versionadded:: 0.0.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:raises NotImplementedError: Method remove() is not implemented in the base class
		"""
		raise NotImplementedError("Method remove() is not implemented in the base class")

	def clear(self) -> None:
		"""
		Clears the entire Text Buffer, making it empty.

		.. versionadded:: 0.0.0

		:raises NotImplementedError: Method clear() is not implemented in the base class
		"""
		raise NotImplementedError("Method clear() is not implemented in the base class")

	def save(self, name_file: str, clean: bool) -> None:
		"""
		Saves the text of the Text Buffer to a file.

		.. versionadded:: 0.0.0

		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool
		:raises NotImplementedError: Method save() is not implemented in the base class
		"""
		raise NotImplementedError("Method save() is not implemented in the base class")

	def load(self, name_file: str) -> None:
		"""
		Loads the text of the Text Buffer from a file.

		.. versionadded:: 0.0.0

		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str
		:raises NotImplementedError: Method load() is not implemented in the base class
		"""
		raise NotImplementedError("Method load() is not implemented in the base class")

	def input(self, input_text: str) -> str:
		"""
		A wrapper method for the standard Python input() that prepares
		the Text Buffer before using this function, and performs certain actions after,
		so that the Text Buffer can continue to function normally.

		.. versionadded:: 0.0.0

		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str
		:raises NotImplementedError: Method input() is not implemented in the base class
		"""
		raise NotImplementedError("Method input() is not implemented in the base class")

	def update_console(self) -> None:
		"""
		Refreshes the console, erasing output text and outputting an updated buffer.

		.. versionadded:: 0.0.0

		:raises NotImplementedError: Method append() is not implemented in the base class
		"""
		raise NotImplementedError("Method update_console() is not implemented in the base class")

	def update_entry(self) -> None:
		"""
		Rewrites the last line of output after updating the last line of the buffer.
		Used (mostly) by the Progress bar (that is Progress string).

		.. versionadded:: 0.0.0

		:raises NotImplementedError: Method append() is not implemented in the base class
		"""
		raise NotImplementedError("Method update_entry() is not implemented in the base class")

# todo написать функцию, которая только дописывает последнюю строку