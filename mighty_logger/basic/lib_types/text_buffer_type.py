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
	def __init__(self, env: EnvironmentType) -> None:
		self._text_buffer: list[str] = []
		self._environment: EnvironmentType = env

	@property
	def text_buffer(self) -> list:
		return self._text_buffer

	def __lt__(self, message: str) -> None:
		self.append(message)

	def __gt__(self, number_string: int) -> str:
		return self.pop(number_string)

	def __lshift__(self, name_file: str) -> None:
		self.load(name_file)

	def __rshift__(self, name_file: str) -> None:
		self.save(name_file, False)

	def append(self, message: str) -> None:
		raise NotImplementedError("Method append() is not implemented in the base class")

	def insert(self, number_string: int, message: str) -> None:
		raise NotImplementedError("Method insert() is not implemented in the base class")

	def replace(self, number_string: int, message: str) -> None:
		raise NotImplementedError("Method replace() is not implemented in the base class")

	def pop(self, number_string: int = -1) -> str:
		raise NotImplementedError("Method pop() is not implemented in the base class")

	def remove(self, number_string: int = -1) -> None:
		raise NotImplementedError("Method remove() is not implemented in the base class")

	def clear(self) -> None:
		raise NotImplementedError("Method clear() is not implemented in the base class")

	def save(self, name_file: str, clean: bool) -> None:
		raise NotImplementedError("Method save() is not implemented in the base class")

	def load(self, name_file: str) -> None:
		raise NotImplementedError("Method load() is not implemented in the base class")

	def input(self, input_text: str) -> str:
		raise NotImplementedError("Method input() is not implemented in the base class")

	def update_console(self) -> None:
		raise NotImplementedError("Method update_console() is not implemented in the base class")

	def update_entry(self) -> None:
		raise NotImplementedError("Method update_entry() is not implemented in the base class")
