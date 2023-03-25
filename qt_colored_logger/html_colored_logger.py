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

HtmlColorSet: dict = {}

class HtmlColorSetInitQ:
	"""
	Initializes a color table and provides functionality to modify this table.
	Only one class object can be created!!!
	"""
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		"""
		Initializes the color table.
		Only one class object can be created!!!
		"""
		from qt_colored_logger import HexColor
		HtmlColorSet['TIME'] = HexColor('ORCHID')
		HtmlColorSet['USER'] = HexColor('MEDIUMORCHID')
		HtmlColorSet['STATUS'] = HexColor('ORANGE')
		HtmlColorSet['STATUS_MESSAGE'] = HexColor('DARKORANGE')
		HtmlColorSet['TYPE_DEBUG'] = HexColor('DIMGRAY')
		HtmlColorSet['DEBUG_MESSAGE'] = HexColor('DARKGRAY')
		HtmlColorSet['TYPE_DEBUG_PERFORMANCE'] = HexColor('SILVER')
		HtmlColorSet['DEBUG_PERFORMANCE_MESSAGE'] = HexColor('GRAY')
		HtmlColorSet['TYPE_PERFORMANCE'] = HexColor('GAINSBORO')
		HtmlColorSet['PERFORMANCE_MESSAGE'] = HexColor('LIGHTGRAY')
		HtmlColorSet['TYPE_EVENT'] = HexColor('MEDIUMSEAGREEN')
		HtmlColorSet['EVENT_MESSAGE'] = HexColor('SEAGREEN')
		HtmlColorSet['TYPE_AUDIT'] = HexColor('YELLOWGREEN')
		HtmlColorSet['AUDIT_MESSAGE'] = HexColor('OLIVEDRAB')
		HtmlColorSet['TYPE_METRICS'] = HexColor('OLIVE')
		HtmlColorSet['METRICS_MESSAGE'] = HexColor('DARKOLIVEGREEN')
		HtmlColorSet['TYPE_USER'] = HexColor('PALEGREEN')
		HtmlColorSet['USER_MESSAGE'] = HexColor('LIGHTGREEN')
		HtmlColorSet['TYPE_MESSAGE'] = HexColor('LIGHTSTEELBLUE')
		HtmlColorSet['MESSAGE_MESSAGE'] = HexColor('POWDERBLUE')
		HtmlColorSet['TYPE_INFO'] = HexColor('PALETURQUOISE')
		HtmlColorSet['INFO_MESSAGE'] = HexColor('LIGHTBLUE')
		HtmlColorSet['TYPE_NOTICE'] = HexColor('DEEPSKYBLUE')
		HtmlColorSet['NOTICE_MESSAGE'] = HexColor('DODGERBLUE')
		HtmlColorSet['TYPE_WARNING'] = HexColor('YELLOW')
		HtmlColorSet['WARNING_MESSAGE'] = HexColor('DARKYELLOW')
		HtmlColorSet['TYPE_ERROR'] = HexColor('FIREBRICK')
		HtmlColorSet['ERROR_MESSAGE'] = HexColor('DARKRED')
		HtmlColorSet['TYPE_CRITICAL'] = HexColor('DARKRED')
		HtmlColorSet['CRITICAL_MESSAGE'] = HexColor('MAROON')
		HtmlColorSet['TYPE_PROGRESS'] = HexColor('SKYBLUE')
		HtmlColorSet['PROGRESS_MESSAGE'] = HexColor('LIGHTSKYBLUE')
		HtmlColorSet['TYPE_SUCCESS'] = HexColor('GREEN')
		HtmlColorSet['SUCCESS_MESSAGE'] = HexColor('DARKGREEN')
		HtmlColorSet['TYPE_FAIL'] = HexColor('FIREBRICK')
		HtmlColorSet['FAIL_MESSAGE'] = HexColor('DARKRED')

	@staticmethod
	def setHexColor(color_name: str, hex_color_value: str):
		"""
		A method that sets the hexadecimal color code in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys:
		`TIME, USER, STATUS, STATUS_MESSAGE, TYPE_DEBUG, DEBUG_MESSAGE, TYPE_DEBUG_PERFORMANCE,
		DEBUG_PERFORMANCE_MESSAGE, TYPE_PERFORMANCE, PERFORMANCE_MESSAGE, TYPE_EVENT, EVENT_MESSAGE,
		TYPE_AUDIT, AUDIT_MESSAGE, TYPE_METRICS, METRICS_MESSAGE, TYPE_USER, USER_MESSAGE,
		TYPE_MESSAGE, MESSAGE_MESSAGE, TYPE_INFO, INFO_MESSAGE, TYPE_NOTICE, NOTICE_MESSAGE,
		TYPE_WARNING, WARNING_MESSAGE, TYPE_ERROR, ERROR_MESSAGE, TYPE_CRITICAL, CRITICAL_MESSAGE,
		TYPE_PROGRESS, PROGRESS_MESSAGE, TYPE_SUCCESS, SUCCESS_MESSAGE, TYPE_FAIL, FAIL_MESSAGE.`

		:param color_name: Color name in logger color table
		:param hex_color_value: Color value in logger color table
		"""
		from qt_colored_logger import ColorException
		if color_name in HtmlColorSet:
			HtmlColorSet[color_name] = hex_color_value
		else:
			raise ColorException("This color is not in the dictionary")

	@staticmethod
	def setColor(color_name: str, red: int, green: int, blue: int):
		"""A method that converts the digital values of red, green, and blue
		in a color to a hexadecimal color code and sets it to the logger's color table.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys:
		`TIME, USER, STATUS, STATUS_MESSAGE, TYPE_DEBUG, DEBUG_MESSAGE, TYPE_DEBUG_PERFORMANCE,
		DEBUG_PERFORMANCE_MESSAGE, TYPE_PERFORMANCE, PERFORMANCE_MESSAGE, TYPE_EVENT, EVENT_MESSAGE,
		TYPE_AUDIT, AUDIT_MESSAGE, TYPE_METRICS, METRICS_MESSAGE, TYPE_USER, USER_MESSAGE,
		TYPE_MESSAGE, MESSAGE_MESSAGE, TYPE_INFO, INFO_MESSAGE, TYPE_NOTICE, NOTICE_MESSAGE,
		TYPE_WARNING, WARNING_MESSAGE, TYPE_ERROR, ERROR_MESSAGE, TYPE_CRITICAL, CRITICAL_MESSAGE,
		TYPE_PROGRESS, PROGRESS_MESSAGE, TYPE_SUCCESS, SUCCESS_MESSAGE, TYPE_FAIL, FAIL_MESSAGE.`

		:param color_name: Color name in logger color table
		:param red: Red color value in logger color table
		:param green: Green color value in logger color table
		:param blue: Blue color value in logger color table
		"""
		from qt_colored_logger import ColorException
		if color_name in HtmlColorSet:
			HtmlColorSet[color_name] = f'#{hex(red)}{hex(green)}{hex(blue)}'
		else:
			raise ColorException("This color is not in the dictionary")

class LoggerQ:
	"""
	The LoggerQ class is a class that implements the functionality
	of logging the work of software in different directions.
	It has a color output of information, settings for the operation of the log.
	Only one class object can be created!!!
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
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

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
		Only one class object can be created!!!

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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_DEBUG']};'>@DEBUG -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['DEBUG_MESSAGE']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def DEBUG_PERFORMANCE(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Performance debugging information logging:
		Can be used to record the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_DEBUG_PERFORMANCE']};'>@DEBUG PERFORMANCE -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['DEBUG_PERFORMANCE_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_PERFORMANCE']};'>@PERFORMANCE -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['PERFORMANCE_MESSAGE']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def EVENT(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		"""
		Event information logging:
		Can be used to track specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message_text: log status message
		:param message_text: log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_EVENT']};'>@EVENT -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['EVENT_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_AUDIT']};'>@AUDIT -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['AUDIT_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_METRICS']};'>@METRICS -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['METRICS_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_USER']};'>@USER -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['USER_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_MESSAGE']};'>@MESSAGE -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['MESSAGE_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_INFO']};'>@INFO -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['INFO_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_NOTICE']};'>@NOTICE -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['NOTICE_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_WARNING']};'>@WARNING -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['WARNING_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_ERROR']};'>!ERROR -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['ERROR_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_CRITICAL']};'>!!!@CRITICAL -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['CRITICAL_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		# log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		# log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		# log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		# log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		# log += f"<span style='color: #{HtmlColorSet['TYPE_PROGRESS']};'>@PROGRESS -</span> " if self.status_type else ""
		# log += f"<span style='color: #{HtmlColorSet['PROGRESS_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_SUCCESS']};'>@SUCCESS -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['SUCCESS_MESSAGE']};'>{message_text}</span>" if self.message else ""
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
		log += f"<span style='color: #{HtmlColorSet['TIME']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: #{HtmlColorSet['USER']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS']};'>#STATUS:</span> " if self.status else ""
		log += f"<span style='color: #{HtmlColorSet['STATUS_MESSAGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: #{HtmlColorSet['TYPE_FAIL']};'>@FAIL -</span> " if self.status_type else ""
		log += f"<span style='color: #{HtmlColorSet['FAIL_MESSAGE']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log


# Test
if __name__ == "__main__":
	mod = HtmlColorSetInitQ()
	log = LoggerQ()
	print(log.DEBUG("1", "2"))
	print(log.DEBUG_PERFORMANCE("3", "4"))
	print(log.PERFORMANCE("5", "6"))
	print(log.EVENT("7", "8"))
	print(log.AUDIT("9", "10"))
	print(log.METRICS("11", "12"))
	print(log.USER("13", "14"))
	print(log.MESSAGE("15", "16"))
	print(log.INFO("17", "18"))
	print(log.NOTICE("19", "20"))
	print(log.WARNING("21", "22"))
	print(log.ERROR("23", "24"))
	print(log.CRITICAL("25", "26"))
	# print(log.START_PROCESS("27", "28"))
	print(log.SUCCESS("29", "30"))
	print(log.FAIL("31", "32"))

	print(len(HtmlColorSet))
	mod.setColor("TIME", 100, 200, 255)
	print(len(HtmlColorSet))
