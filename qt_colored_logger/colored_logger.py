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
from qt_colored_logger import AnsiFormat, AnsiForegroundColor

class HtmlColorSetInit:
	pass

class Logger:
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

		:param time: setting the time output
		:param name: setting the name output
		:param status: setting the status output
		:param status_message: setting the status message output
		:param status_type: setting the log type output
		:param message: setting the log message output
		"""
		self.time = time
		self.name = name
		self.status = status
		self.status_message = status_message
		self.status_type = status_type
		self.message = message
		self.ID = random.randint(1000000, 9999999)

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

	def DEBUG(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Debugging information logging:
		Can be used to record any information while debugging an application.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiForegroundColor('ORCHID')}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiForegroundColor('MEDIUMORCHID')}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiForegroundColor('ORANGE')}#STATUS: " if self.status else ""
		log += f"{AnsiForegroundColor('DARKORANGE')}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiForegroundColor('BURLYWOOD')}@DEBUG - " if self.status_type else ""
		log += f"{AnsiForegroundColor('TAN')}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
		return log


# Test
if __name__ == "__main__":
	# mod = HtmlColorSetInitQ()
	logger = Logger()
	print(logger.DEBUG("1", "2"))
