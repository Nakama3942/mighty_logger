# ##########################   Qt_Сolored-logger   ########################### #
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

# The idea is taken here:
# https://github.com/Nakama3942/WiretappingScanner/commit/da5e0e71681b9e1462d5bba5438fc8b1fde8142e

import datetime, platform, os, random

ColorPickerQ = {
	# https://ru.wikipedia.org/wiki/HTML-%D1%86%D0%B2%D0%B5%D1%82%D0%B0
	'FIREBRICK': '#b22222',
	'DARKRED': '#8b0000',
	'ORANGE': '#ffa500',
	'DARKORANGE': '#ff8c00',
	'YELLOW': '#ffff00',
	'DARKYELLOW': '#ffcc00',
	'MEDIUMSPRINGGREEN': '#00fa9a',
	'SPRINGGREEN': '#00ff7f',
	'MEDIUMSEAGREEN': '#3cb371',
	'SEAGREEN': '#2e8b57',
	'FORESTGREEN': '#228b22',  # -
	'GREEN': '#008000',
	'DARKGREEN': '#006400',
	'YELLOWGREEN': '#9acd32',
	'OLIVEDRAB': '#6b8e23',
	'OLIVE': '#808000',
	'DARKOLIVEGREEN': '#556b2f',
	'AQUAMARINE': '#7fffd4',
	'TURQUOISE': '#40e0d0',
	'SKYBLUE': '#87ceeb',
	'LIGHTSKYBLUE': '#87cefa',
	'BLUE': '#0000ff',
	'MEDIUMBLUE': '#0000cd',
	'DARKBLUE': '#00008b',
	'NAVY': '#000080',
	'BLUEVIOLET': '#8a2be2',
	'DARKVIOLET': '#9400d3',
	'GAINSBORO': '#dcdcdc',
	'LIGHTGREY': '#d3d3d3',
	'SILVER': '#c0c0c0',
	'DARKGREY': '#a9a9a9',
	'GREY': '#808080',
	'DIMGREY': '#696969',
}

class PickerModifierQ:
	def __init__(self):
		pass

	def setHexColor(self, color_name: str, hex_color_value: str):
		ColorPickerQ[color_name] = hex_color_value

	def setColor(self, color_name: str, red: int, green: int, blue: int):
		ColorPickerQ[color_name] = f'#{hex(red)}{hex(green)}{hex(blue)}'

class LoggerQ:
	"""
	The LoggerQ class is a class that implements the functionality
	of logging the work of software in different directions.
	It has a color output of information, settings for the operation of the log.
	Implements the output of the following information:
	1) Record creation time;
	2) Recording device;
	3) Record status;
	4) Recording status message;
	5) Record type;
	6) Write message.
	Implements the output of the following types of records:
	1)  `DEBUG`
	2)  `DEBUG_PERFORMANCE`
	3)  `PERFORMANCE`
	4)  `EVENT`
	5)  `AUDIT`
	6)  `METRICS`
	7)  `USER`
	8)  `MESSAGE`
	9)  `INFO`
	10) `NOTICE`
	11) `WARNING`
	12) `ERROR`
	13) `CRITICAL`
	14) `PROGRESS`
	15) `SUCCESS`
	16) `FAIL`
	"""
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
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['GREY']};'>@DEBUG -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DIMGREY']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def DEBUG_PERFORMANCE(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Performance debugging information logging:
		Can be used to record the execution time of operations or other
		performance information whilethe application is being debugged.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['SILVER']};'>@DEBUG PERFORMANCE -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKGREY']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def PERFORMANCE(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Performance information logging:
		Can be used to record the execution time of operations or
		other application performance information.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['GAINSBORO']};'>@PERFORMANCE -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['LIGHTGREY']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def EVENT(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Event information logging:
		Can be used to track specific events in the application,
		such as button presses ormouse cursor movements.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['MEDIUMSEAGREEN']};'>@EVENT -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['SEAGREEN']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def AUDIT(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Audit information logging:
		Can be used to track changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['YELLOWGREEN']};'>@AUDIT -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['OLIVEDRAB']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def METRICS(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Metrics information logging:
		Can be used to log metrics to track application performance and identify issues.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['OLIVE']};'>@METRICS -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKOLIVEGREEN']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def USER(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		User information logging:
		Can be used to add custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['MEDIUMSPRINGGREEN']};'>@USER -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['SPRINGGREEN']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def MESSAGE(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['BLUE']};'>@MESSAGE -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['MEDIUMBLUE']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def INFO(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Default information logging:
		Can be used to display messages with specific content about the operation of the program.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['AQUAMARINE']};'>@INFO -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['TURQUOISE']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def NOTICE(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['DARKBLUE']};'>@NOTICE -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['NAVY']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def WARNING(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Warning information logging:
		Can be used to display warnings that the program may work with unpredictable results.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['YELLOW']};'>@WARNING -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKYELLOW']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def ERROR(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Error information logging:
		Used to display errors and crashes in the program.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>!ERROR -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def CRITICAL(self, status_message_text: str = "", message_text: str = "", bold: bool = True, italic: bool = False) -> str:
		"""
		Critical error information logging:
		Used to display critical and unpredictable program failures.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>!!!@CRITICAL -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def START_PROCESS(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Stub.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		# log = ""
		# log += f"<b>" if bold else ""
		# log += f"<i>" if italic else ""
		# log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		# log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		# log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		# log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		# log += f"<span style='color: {ColorPickerQ['SKYBLUE']};'>@PROGRESS -</span>\t" if self.status_type else ""
		# log += f"<span style='color: {ColorPickerQ['LIGHTSKYBLUE']};'>{message_text}</span>" if self.message else ""
		# log += f"</i>" if italic else ""
		# log += f"</b>" if bold else ""
		# return log
		pass
		# Должен выполняться в потоке

	def STOP_PROCESS(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Stub.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		pass
		# Сделать переход в SUCCESS или FAIL

	def SUCCESS(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = True) -> str:
		"""
		Success information logging:
		Used to display a message about the success of the process.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['GREEN']};'>@SUCCESS -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKGREEN']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def FAIL(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = True) -> str:
		"""
		Fail information logging:
		Used to display a message about the failed execution of the process.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['BLUEVIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>@FAIL -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log


# if __name__ == '__main__':
# 	logger = Logger()
# 	print(logger.DEBUG("1"))
# 	print(logger.INFO("2"))
# 	print(logger.WARNING("3"))
# 	print(logger.ERROR("4"))
# 	print(logger.CRITICAL("5"))
#
# 	loggerMod = PickerModifier()
# 	loggerMod.setHexColor('RED', '#151719')
# 	loggerMod.setColor('DARKRED', 50, 80, 149)
#
# 	print(logger.CRITICAL("6"))
