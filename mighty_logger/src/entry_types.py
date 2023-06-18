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

from mighty_logger.text.icon_set import IconSetType

class EntryType:
	def __init__(
		self,
		type_name: str,
		time_color: str,
		status_color: str,
		status_message_color: str,
		type_color: str,
		message_color: str,
		background_color: str,
		icon: list
	) -> None:
		self.__type_name: str = type_name
		self.__time_color: str = time_color
		self.__status_color: str = status_color
		self.__status_message_color: str = status_message_color
		self.__type_color: str = type_color
		self.__message_color: str = message_color
		self.__background_color: str = background_color
		self.__icon: list = icon

	@property
	def type_name(self) -> str:
		return self.__type_name

	@property
	def time_color(self) -> str:
		return self.__time_color

	@property
	def status_color(self) -> str:
		return self.__status_color

	@property
	def status_message_color(self) -> str:
		return self.__status_message_color

	@property
	def type_color(self) -> str:
		return self.__type_color

	@property
	def message_color(self) -> str:
		return self.__message_color

	@property
	def background_color(self) -> str:
		return self.__background_color

	@property
	def icon(self) -> list:
		return self.__icon

class EntryTypes:
	debug = EntryType(
		"%DEBUG",
		"DEBUG_TIME",
		"DEBUG_STATUS",
		"DEBUG_STATUS_MESSAGE",
		"TYPE_DEBUG",
		"DEBUG_MESSAGE",
		"DEBUG_BACKGROUND",
		['🐛', '🐞', '🚧', '🔬']
	)
	debug_performance = EntryType(
		"%DEBUG PERFORMANCE",
		"DEBUG_PERFORMANCE_TIME",
		"DEBUG_PERFORMANCE_STATUS",
		"DEBUG_PERFORMANCE_STATUS_MESSAGE",
		"TYPE_DEBUG_PERFORMANCE",
		"DEBUG_PERFORMANCE_MESSAGE",
		"DEBUG_PERFORMANCE_BACKGROUND",
		['⏱️', '⌛️', '🔍', '📈']
	)
