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

from random import randint
import platform
from os import getlogin
from datetime import datetime

from mighty_logger.basic.lib_types.entry_type import EntryType
from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.basic.exceptions import MessageException
from mighty_logger.basic.singleton import Singleton
from mighty_logger.src.environments import LogEnvironments
from mighty_logger.src.ansi_format import GetAnsiFormat

class BasicLogger(Singleton):
	def __init__(
		self,
		program_name: str,
		env: EnvironmentType
	) -> None:
		self._ID: int = randint(1000000, 9999999)
		self._program_name: str = program_name
		self._environment: EnvironmentType = env
		self._settings: dict = {}

	def _initialized_data(
		self,
		colors: list[str, str]
	) -> str:
		match self._environment.environment_name:
			case LogEnvironments.CONSOLE.environment_name:
				return (
					f"{colors[1]}" +
					f"{colors[0]}-{self._program_name}?entry> " +
					f"${platform.node()}:{getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}" +
					f"{GetAnsiFormat('reset/on')}"
				)
			case LogEnvironments.PLAIN_CONSOLE.environment_name:
				return (
					f"-{self._program_name}?entry> " +
					f"${platform.node()}:{getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}" +
					f"{GetAnsiFormat('reset/on')}"
				)
			case LogEnvironments.HTML.environment_name:
				return (
					f"<span style='background-color: #{colors[1]};'>" +
					f"<span style='color: #{colors[0]};'>-{self._program_name}?entry> " +
					f"${platform.node()}:{getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}" +
					f"</span></span>"
				)
			case LogEnvironments.MARKDOWN.environment_name:
				return (
					f"<span style='background-color: #{colors[1]};'>" +
					f"<span style='color: #{colors[0]};'>-{self._program_name}?entry> " +
					f"${platform.node()}:{getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}" +
					f"</span></span>"
				)
			case LogEnvironments.PLAIN.environment_name:
				return (
					f"-{self._program_name}?entry> " +
					f"${platform.node()}:{getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}"
				)

	def _assemble_entry(
		self,
		entry_type: EntryType,
		icon_set: int,
		animation: str,
		message_text: str,
		local_settings: dict
	) -> str:
		if len(message_text) < 10:
			raise MessageException("Message is too short (less than 10 characters)")

		bold = local_settings['bold'] if 'bold' in local_settings else self._settings['global_bold_font']
		italic = local_settings['italic'] if 'italic' in local_settings else self._settings['global_italic_font']
		invert = local_settings['invert'] if 'invert' in local_settings else self._settings['global_invert_font']
		background = local_settings['background'] if 'background' in local_settings else self._settings['global_background']

		match self._environment.environment_name:
			case LogEnvironments.CONSOLE.environment_name:
				return (
					(f"{GetAnsiFormat('bold/on')}" if bold else "") +
					(f"{GetAnsiFormat('italic/on')}" if italic else "") +
					(f"{GetAnsiFormat('invert/on')}" if invert else "") +
					f"{entry_type.background_color[self._environment.environment_code][background]}" +
					f"{entry_type.message_color[self._environment.environment_code][background]}-?entry> {animation} " +
					f"{entry_type.time_color[self._environment.environment_code][background]}*{datetime.now()} " +
					f"{entry_type.icon[icon_set]} " +
					f"{entry_type.status_color[self._environment.environment_code][background]}#STATUS: " +
					f"{entry_type.type_color[self._environment.environment_code][background]}{entry_type.type_category}{entry_type.type_name} - " +
					f"{entry_type.message_color[self._environment.environment_code][background]}{message_text}" +
					f"{GetAnsiFormat('reset/on')}"
				)
			case LogEnvironments.PLAIN_CONSOLE.environment_name:
				return (
					f"-?entry> {animation} " +
					f"*{datetime.now()} " +
					f"{entry_type.icon[icon_set]} " +
					f"#STATUS: " +
					f"{entry_type.type_category}{entry_type.type_name} - " +
					f"{message_text}"
				)
			case LogEnvironments.HTML.environment_name:
				return (
					(f"<b>" if bold else "") +
					(f"<i>" if italic else "") +
					f"<span style='background-color: #{entry_type.background_color[self._environment.environment_code][background]};'>" +
					f"<span style='color: #{entry_type.message_color[self._environment.environment_code][background]};'>-?entry> {animation} </span>" +
					f"<span style='color: #{entry_type.time_color[self._environment.environment_code][background]};'>*{datetime.now()} </span>" +
					f"{entry_type.icon[icon_set]} " +
					f"<span style='color: #{entry_type.status_color[self._environment.environment_code][background]};'>#STATUS: </span>" +
					f"<span style='color: #{entry_type.type_color[self._environment.environment_code][background]};'>{entry_type.type_category}{entry_type.type_name} - </span>" +
					f"<span style='color: #{entry_type.message_color[self._environment.environment_code][background]};'>{message_text}</span></span>" +
					(f"</i>" if italic else "") +
					(f"</b>" if bold else "")
				)
			case LogEnvironments.MARKDOWN.environment_name:
				return (
					(f"<b>" if bold else "") +
					(f"<i>" if italic else "") +
					f"<span style='background-color: #{entry_type.background_color[self._environment.environment_code][background]};'>" +
					f"<span style='color: #{entry_type.message_color[self._environment.environment_code][background]};'>-?entry> {animation} </span>" +
					f"<span style='color: #{entry_type.time_color[self._environment.environment_code][background]};'>*{datetime.now()} </span>" +
					f"{entry_type.icon[icon_set]} " +
					f"<span style='color: #{entry_type.status_color[self._environment.environment_code][background]};'>#STATUS: </span>" +
					f"<span style='color: #{entry_type.type_color[self._environment.environment_code][background]};'>{entry_type.type_category}{entry_type.type_name} - </span>" +
					f"<span style='color: #{entry_type.message_color[self._environment.environment_code][background]};'>{message_text}</span></span>" +
					(f"</i>" if italic else "") +
					(f"</b>" if bold else "")
				)
			case LogEnvironments.PLAIN.environment_name:
				return (
					f"-?entry> {animation} " +
					f"*{datetime.now()} " +
					f"{entry_type.icon[icon_set]} " +
					f"#STATUS: " +
					f"{entry_type.type_category}{entry_type.type_name} - " +
					f"{message_text}"
				)
