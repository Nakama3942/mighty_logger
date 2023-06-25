"""
A module with an implementation of the base (parent) logger class.
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

import datetime, platform, os, random

from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.basic.patterns import Singleton
from mighty_logger.src.ansi_format import GetAnsiFormat
from mighty_logger.src.environments import LogEnvironments

class BasicLogger(Singleton):
	def __init__(
		self,
		program_name: str,
		env: EnvironmentType
	) -> None:
		self._ID: int = random.randint(1000000, 9999999)
		self._program_name: str = program_name
		self._environment: EnvironmentType = env
		self._settings: dict = {}

	def _initialized_data(
		self,
		colors: list[str, str],
	) -> str:
		"""
		A method that assemble an entry of system initialized data.

		:param colors: Color string list of initialized data
		:return: a string with initialized data
		"""
		match self._environment.environment_name:
			case LogEnvironments.CONSOLE.environment_name:
				return (
					f"{colors[1]}" +
					f"{colors[0]}-{self._program_name}?entry> " +
					f"${platform.node()}:{os.getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}" +
					f"{GetAnsiFormat('reset/on')}"
				)
			case LogEnvironments.PLAIN_CONSOLE.environment_name:
				return (
					f"-{self._program_name}?entry> " +
					f"${platform.node()}:{os.getlogin()}" +
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
					f"${platform.node()}:{os.getlogin()}" +
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
					f"${platform.node()}:{os.getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}" +
					f"</span></span>"
				)
			case LogEnvironments.PLAIN.environment_name:
				return (
					f"-{self._program_name}?entry> " +
					f"${platform.node()}:{os.getlogin()}" +
					f":{platform.system()}" +
					f":{platform.version()}" +
					":{}:{}".format(*platform.architecture()) +
					f":{platform.machine()}"
				)

	def _assemble_entry(
		self,
		colors: list[str, str, str, str, str, str],
		animation: str,
		icon: str,
		status_message_text: str,
		message_type: str,
		message_text: str,
		local_settings: dict
	) -> str:
		"""
		A method that assemble an entry into a string and returns it.

		:param colors: 6 colors that the method uses to assemble the string
		:param animation: Animation of entry
		:param icon: Type icon
		:param status_message_text: Status message
		:param message_type: Entry type
		:param message_text: Entry message
		:param local_settings: Settings for the string of the current entry
		:return: the formed entry string
		"""
		bold = local_settings['bold'] if 'bold' in local_settings else self._settings['global_bold_font']
		italic = local_settings['italic'] if 'italic' in local_settings else self._settings['global_italic_font']
		invert = local_settings['invert'] if 'invert' in local_settings else self._settings['global_invert_font']
		time_entry = local_settings['time_local_entry'] if 'time_local_entry' in local_settings else self._settings['time_global_entry']
		status_entry = local_settings['status_local_entry'] if 'status_local_entry' in local_settings else self._settings['status_global_entry']
		status_message_entry = local_settings['status_message_local_entry'] if 'status_message_local_entry' in local_settings else self._settings['status_message_global_entry']
		status_type_entry = local_settings['status_type_local_entry'] if 'status_type_local_entry' in local_settings else self._settings['status_type_global_entry']
		message_entry = local_settings['message_local_entry'] if 'message_local_entry' in local_settings else self._settings['message_global_entry']

		match self._environment.environment_name:
			case LogEnvironments.CONSOLE.environment_name:
				return (
					(f"{GetAnsiFormat('bold/on')}" if bold else "") +
					(f"{GetAnsiFormat('italic/on')}" if italic else "") +
					(f"{GetAnsiFormat('invert/on')}" if invert else "") +
					f"{colors[5]}" +
					f"{colors[4]}-?entry> {animation} " +
					(f"{colors[0]}*{datetime.datetime.now()} " if time_entry else "") +
					f"{icon} " +
					(f"{colors[1]}#STATUS: " if status_entry else "") +
					(f"{colors[2]}{status_message_text} " if status_message_entry else "") +
					(f"{colors[3]}{message_type} - " if status_type_entry else "") +
					(f"{colors[4]}{message_text}" if message_entry else "") +
					f"{GetAnsiFormat('reset/on')}"
				)
			case LogEnvironments.PLAIN_CONSOLE.environment_name:
				return (
					f"-?entry> {animation} " +
					(f"*{datetime.datetime.now()} " if time_entry else "") +
					f"{icon} " +
					(f"#STATUS: " if status_entry else "") +
					(f"{status_message_text} " if status_message_entry else "") +
					(f"{message_type} - " if status_type_entry else "") +
					(f"{message_text}" if message_entry else "")
				)
			case LogEnvironments.HTML.environment_name:
				return (
					(f"<b>" if bold else "") +
					(f"<i>" if italic else "") +
					f"<span style='background-color: #{colors[5]};'>" +
					f"<span style='color: #{colors[4]};'>-?entry> {animation} </span>" +
					(f"<span style='color: #{colors[0]};'>*{datetime.datetime.now()} </span>" if time_entry else "") +
					f"{icon} " +
					(f"<span style='color: #{colors[1]};'>#STATUS: </span>" if status_entry else "") +
					(f"<span style='color: #{colors[2]};'>{status_message_text} </span>" if status_message_entry else "") +
					(f"<span style='color: #{colors[3]};'>{message_type} - </span>" if status_type_entry else "") +
					(f"<span style='color: #{colors[4]};'>{message_text}</span></span>" if message_entry else "") +
					(f"</i>" if italic else "") +
					(f"</b>" if bold else "")
				)
			case LogEnvironments.MARKDOWN.environment_name:
				return (
						(f"<b>" if bold else "") +
						(f"<i>" if italic else "") +
						f"<span style='background-color: #{colors[5]};'>" +
						f"<span style='color: #{colors[4]};'>-?entry> {animation} </span>" +
						(f"<span style='color: #{colors[0]};'>*{datetime.datetime.now()} </span>" if time_entry else "") +
						f"{icon} " +
						(f"<span style='color: #{colors[1]};'>#STATUS: </span>" if status_entry else "") +
						(f"<span style='color: #{colors[2]};'>{status_message_text} </span>" if status_message_entry else "") +
						(f"<span style='color: #{colors[3]};'>{message_type} - </span>" if status_type_entry else "") +
						(f"<span style='color: #{colors[4]};'>{message_text}</span></span>" if message_entry else "") +
						(f"</i>" if italic else "") +
						(f"</b>" if bold else "")
				)
			case LogEnvironments.PLAIN.environment_name:
				return (
					f"-?entry> {animation} " +
					(f"*{datetime.datetime.now()} " if time_entry else "") +
					f"{icon} " +
					(f"#STATUS: " if status_entry else "") +
					(f"{status_message_text} " if status_message_entry else "") +
					(f"{message_type} - " if status_type_entry else "") +
					(f"{message_text}" if message_entry else "")
				)
