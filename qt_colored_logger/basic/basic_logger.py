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

from qt_colored_logger.src import GetAnsi

class BasicLogger:
	def __init__(
			self,
			time: bool = True,
			name: bool = True,
			status: bool = True,
			status_message: bool = True,
			status_type: bool = True,
			message: bool = True
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
		self.time = time
		self.name = name
		self.status = status
		self.status_message = status_message
		self.status_type = status_type
		self.message = message
		self._ID = random.randint(1000000, 9999999)

	def timeEnabled(self, enabled: bool):
		"""
		Sets the output of the date-time at the time the log is written.

		:param enabled: Output state
		"""
		self.time = enabled

	def nameEnabled(self, enabled: bool):
		"""
		Sets the output of the computer-user at the time the log is written.

		:param enabled: Output state
		"""
		self.name = enabled

	def statusEnabled(self, enabled: bool):
		"""
		Sets the output of the status at the time the log is written.

		:param enabled: Output state
		"""
		self.status = enabled

	def status_messageEnabled(self, enabled: bool):
		"""
		Sets the output of the status message at the time the log is written.

		:param enabled: Output state
		"""
		self.status_message = enabled

	def status_typeEnabled(self, enabled: bool):
		"""
		Sets the output of the log type at the time the log is written.

		:param enabled: Output state
		"""
		self.status_type = enabled

	def messageEnabled(self, enabled: bool):
		"""
		Sets the output of the log message at the time the log is written.

		:param enabled: Output state
		"""
		self.message = enabled

	def _assemble_entry(
			self,
			colors: list[str, str, str, str, str, str],
			status_message_text: str,
			message_type: str,
			message_text: str,
			bold: bool,
			italic: bool
	):
		"""
		A method that assemble an entry into a string and returns it.
		Forms a console string.

		:param colors: 6 colors that the method uses to assemble the string
		:param status_message_text: Status message
		:param message_type: Entry type
		:param message_text: Entry message
		:param bold: Format the entry in bold
		:param italic: Format the entry in italic
		:return: the formed entry string
		"""
		log = ""
		log += f"{GetAnsi()['bold']['on']}" if bold else ""
		log += f"{GetAnsi()['italic']['on']}" if italic else ""
		log += f"{colors[0]}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{colors[1]}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{colors[2]}#STATUS: " if self.status else ""
		log += f"{colors[3]}{status_message_text}\t" if self.status_message else ""
		log += f"{colors[4]}{message_type} - " if self.status_type else ""
		log += f"{colors[5]}{message_text}" if self.message else ""
		log += f"{GetAnsi()['reset']['on']}"
		return log

	def _assemble_html_entry(
			self,
			colors: list[str, str, str, str, str, str],
			status_message_text: str,
			message_type: str,
			message_text: str,
			bold: bool,
			italic: bool
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
		log += f"<span style='color: #{colors[0]};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{colors[1]};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{colors[2]};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{colors[3]};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{colors[4]};'>{message_type} - </span> " if self.status_type else ""
		log += f"<span style='color: #{colors[5]};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log
