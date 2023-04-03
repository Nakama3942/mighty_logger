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

import datetime, platform, os, random

from qt_colored_logger.src import GetAnsiFormat

class _BasicLogger:
	def __init__(
			self,
			program_name: str,
			time: bool,
			status: bool,
			status_message: bool,
			status_type: bool,
			message: bool
	):
		"""
		Initializes and configures the log.

		:param time: Setting the time output
		:param name: Setting the name output
		:param status: Setting the status output
		:param status_message: Setting the status message output
		:param status_type: Setting the log type output
		:param message: Setting the log message output
		"""
		self._program_name = program_name
		self.time = time
		self.status = status
		self.status_message = status_message
		self.status_type = status_type
		self.message = message
		self._ID = random.randint(1000000, 9999999)

	def _initial(self, colors: list[str, str]):
		log = ""
		log += f"{colors[1]}"
		log += f"{colors[0]}-{self._program_name}?entry> "
		log += f"${platform.node()}^{os.getlogin()}"
		log += f"@{platform.system()}"
		log += f":{platform.version()}"
		log += f":{platform.architecture()[0]}"
		log += f":{platform.architecture()[1]}"
		log += f":{platform.machine()}"
		log += f"{GetAnsiFormat('reset/on')}"
		return log

	def _html_initial(self, colors: list[str, str]):
		log = ""
		log += f"<span style='background-color: #{colors[1]};'>"
		log += f"<span style='color: #{colors[0]};'>-{self._program_name}?entry> "
		log += f"${platform.node()}^{os.getlogin()}"
		log += f"@{platform.system()}"
		log += f":{platform.version()}"
		log += f":{platform.architecture()[0]}"
		log += f":{platform.architecture()[1]}"
		log += f":{platform.machine()}"
		log += f"</span></span>"
		return log

	def _assemble_entry(
			self,
			colors: list[str, str, str, str, str, str],
			status_message_text: str,
			message_type: str,
			message_text: str,
			bold: bool,
			italic: bool,
			invert: bool,
	):
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
		log = ""
		log += f"{GetAnsiFormat('bold/on')}" if bold else ""
		log += f"{GetAnsiFormat('italic/on')}" if italic else ""
		log += f"{GetAnsiFormat('invert/on')}" if invert else ""
		log += f"{colors[5]}"
		log += f"{colors[4]}-?entry> "
		log += f"{colors[0]}*{datetime.datetime.now()} " if self.time else ""
		log += f"{colors[1]}#STATUS: " if self.status else ""
		log += f"{colors[2]}{status_message_text} " if self.status_message else ""
		log += f"{colors[3]}{message_type} - " if self.status_type else ""
		log += f"{colors[4]}{message_text}" if self.message else ""
		log += f"{GetAnsiFormat('reset/on')}"
		return log

	def _assemble_html_entry(
			self,
			colors: list[str, str, str, str, str, str],
			status_message_text: str,
			message_type: str,
			message_text: str,
			bold: bool,
			italic: bool,
	):
		"""
		A method that assemble an entry into a string and returns it.
		Forms an HTML string.

		:param colors: 6 colors that the method uses to assemble the string
		:param status_message_text: Status message
		:param message_type: Entry type
		:param message_text: Entry message
		:param bold: Format the entry in bold
		:param italic: Format the entry in italic
		:return: the formed entry string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='background-color: #{colors[5]};'>"
		log += f"<span style='color: #{colors[4]};'>-?entry> </span>"
		log += f"<span style='color: #{colors[0]};'>*{datetime.datetime.now()} </span>" if self.time else ""
		log += f"<span style='color: #{colors[1]};'>#STATUS: </span>" if self.status else ""
		log += f"<span style='color: #{colors[2]};'>{status_message_text} </span>" if self.status_message else ""
		log += f"<span style='color: #{colors[3]};'>{message_type} - </span>" if self.status_type else ""
		log += f"<span style='color: #{colors[4]};'>{message_text}</span></span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log
