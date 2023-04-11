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

from mighty_logger.basic.patterns import Singleton
from mighty_logger.src.ansi_format import GetAnsiFormat
from mighty_logger.src.log_environment import LogEnvironments

# todo Сделать работу с настройками в отдельном словаре.

class BasicLogger(Singleton):
	def __init__(
			self,
			program_name: str,
			time: bool,
			status: bool,
			status_message: bool,
			status_type: bool,
			entry_message: bool
	):
		"""
		Initializes and configures the log.

		:param program_name: Installing the program name output
		:param time: Setting the time output
		:param name: Setting the name output
		:param status: Setting the status output
		:param status_message: Setting the status message output
		:param status_type: Setting the log type output
		:param entry_message: Setting the log message output
		"""
		self._program_name = program_name
		self.time = time
		self.status = status
		self.status_message = status_message
		self.status_type = status_type
		self.entry_message = entry_message
		self._ID = random.randint(1000000, 9999999)
		self._pc_name = platform.node()
		self._user_name = os.getlogin()
		self._system_name = platform.system()
		self._system_version = platform.version()
		self._system_architecture = platform.architecture()
		self._pc_machine = platform.machine()

	def _initialized_data(
			self,
			colors: list[str, str],
			env: str
	) -> str:
		"""
		A method that assemble an entry of system initialized data.
		Forms a console string.

		:param colors: Color string list of initialized data
		:return: a string with initialized data
		"""
		if env == LogEnvironments.HTML:
			return (
					f"<span style='background-color: #{colors[1]};'>" +
					f"<span style='color: #{colors[0]};'>-{self._program_name}?entry> " +
					f"${self._pc_name}^{self._user_name}" +
					f"@{self._system_name}" +
					f":{self._system_version}" +
					f":{self._system_architecture[0]}" +
					f":{self._system_architecture[1]}" +
					f":{self._pc_machine}</span></span><br>"
			)
		else:
			return (
					f"{colors[1]}" +
					f"{colors[0]}-{self._program_name}?entry> " +
					f"${self._pc_name}^{self._user_name}" +
					f"@{self._system_name}" +
					f":{self._system_version}" +
					f":{self._system_architecture[0]}" +
					f":{self._system_architecture[1]}" +
					f":{self._pc_machine}{GetAnsiFormat('reset/on')}"
			)

	def _assemble_entry(
			self,
			colors: list[str, str, str, str, str, str],
			status_message_text: str,
			message_type: str,
			message_text: str,
			bold: bool,
			italic: bool,
			invert: bool,
			env: str
	) -> str:
		"""
		A method that assemble an entry into a string and returns it.
		Forms a console string.

		:param colors: 7 colors that the method uses to assemble the string
		:param status_message_text: Status message
		:param message_type: Entry type
		:param message_text: Entry message
		:param bold: Format the entry in bold
		:param italic: Format the entry in italic
		:param invert: invert the colors in format the entry
		:return: the formed entry string
		"""
		if env == LogEnvironments.HTML:
			return (
					(f"<b>" if bold else "") +
					(f"<i>" if italic else "") +
					f"<span style='background-color: #{colors[5]};'>" +
					f"<span style='color: #{colors[4]};'>-?entry> </span>" +
					(f"<span style='color: #{colors[0]};'>*{datetime.datetime.now()} </span>" if self.time else "") +
					(f"<span style='color: #{colors[1]};'>#STATUS: </span>" if self.status else "") +
					(f"<span style='color: #{colors[2]};'>{status_message_text} </span>" if self.status_message else "") +
					(f"<span style='color: #{colors[3]};'>{message_type} - </span>" if self.status_type else "") +
					(f"<span style='color: #{colors[4]};'>{message_text}</span></span>" if self.message else "") +
					(f"</i>" if italic else "") +
					(f"</b>" if bold else "") + "<br>"
			)
		else:
			return (
					(f"{GetAnsiFormat('bold/on')}" if bold else "") +
					(f"{GetAnsiFormat('italic/on')}" if italic else "") +
					(f"{GetAnsiFormat('invert/on')}" if invert else "") +
					f"{colors[5]}" +
					f"{colors[4]}-?entry> " +
					(f"{colors[0]}*{datetime.datetime.now()} " if self.time else "") +
					(f"{colors[1]}#STATUS: " if self.status else "") +
					(f"{colors[2]}{status_message_text} " if self.status_message else "") +
					(f"{colors[3]}{message_type} - " if self.status_type else "") +
					(f"{colors[4]}{message_text}" if self.message else "") +
					f"{GetAnsiFormat('reset/on')}"
			)
