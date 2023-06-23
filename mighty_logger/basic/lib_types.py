"""
...
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

class EnvironmentType:
	def __init__(self, environment_name: str, environment_code: int) -> None:
		self.__environment_name: str = environment_name
		self.__environment_code: int = environment_code

	@property
	def environment_name(self) -> str:
		return self.__environment_name

	@property
	def environment_code(self) -> int:
		return self.__environment_code

class EntryType:
	def __init__(
		self,
		*,
		type_name: str,
		time_color: tuple,
		status_color: tuple,
		status_message_color: tuple,
		type_color: tuple,
		message_color: tuple,
		background_color: tuple,
		icon: tuple
	) -> None:
		self.__type_name: str = type_name
		self.__time_color: tuple = time_color
		self.__status_color: tuple = status_color
		self.__status_message_color: tuple = status_message_color
		self.__type_color: tuple = type_color
		self.__message_color: tuple = message_color
		self.__background_color: tuple = background_color
		self.__icon: tuple = icon

	@property
	def type_name(self) -> str:
		return self.__type_name

	@property
	def time_color(self) -> tuple:
		return self.__time_color

	@property
	def status_color(self) -> tuple:
		return self.__status_color

	@property
	def status_message_color(self) -> tuple:
		return self.__status_message_color

	@property
	def type_color(self) -> tuple:
		return self.__type_color

	@property
	def message_color(self) -> tuple:
		return self.__message_color

	@property
	def background_color(self) -> tuple:
		return self.__background_color

	@property
	def icon(self) -> tuple:
		return self.__icon

class StatusMessageType:
	"""
	Wrapper class for status message.
	"""
	def __init__(self, message: str):
		self.__current_status_message: str = message

	@property
	def current_status_message(self) -> str:
		return self.__current_status_message

class BasicAnimationType:
	"""
	Basic wrapper class for animations type.
	"""
	def __init__(self, animation: list):
		self.__animation: list = animation

	@property
	def animation(self) -> list:
		return self.__animation

class IndefiniteAnimationType(BasicAnimationType):
	"""
	Wrapper class for indefinite animations type.
	"""
	...

class DefiniteAnimationType(BasicAnimationType):
	"""
	Wrapper class for definite animations type.
	"""
	...
