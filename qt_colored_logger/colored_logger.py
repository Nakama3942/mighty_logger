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
from singleton import singleton

AnsiColorSet: dict = {}

@singleton
class AnsiColorSetInit:
	"""
	Initializes a color table and provides functionality to modify this table.
	Only one class object can be created!!!
	"""

	def __init__(self):
		"""
		Initializes the color table.
		Only one class object can be created!!!
		"""
		AnsiColorSet['TIME'] = AnsiForegroundColor('ORCHID')
		AnsiColorSet['USER'] = AnsiForegroundColor('MEDIUMORCHID')
		AnsiColorSet['STATUS'] = AnsiForegroundColor('ORANGE')
		AnsiColorSet['STATUS_MESSAGE'] = AnsiForegroundColor('DARKORANGE')
		AnsiColorSet['TYPE_DEBUG'] = AnsiForegroundColor('BURLYWOOD')
		AnsiColorSet['DEBUG_MESSAGE'] = AnsiForegroundColor('TAN')
		AnsiColorSet['TYPE_DEBUG_PERFORMANCE'] = AnsiForegroundColor('NAVAJOWHITE')
		AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'] = AnsiForegroundColor('WHEAT')
		AnsiColorSet['TYPE_PERFORMANCE'] = AnsiForegroundColor('BLANCHEDALMOND')
		AnsiColorSet['PERFORMANCE_MESSAGE'] = AnsiForegroundColor('BISQUE')
		AnsiColorSet['TYPE_EVENT'] = AnsiForegroundColor('MEDIUMSEAGREEN')
		AnsiColorSet['EVENT_MESSAGE'] = AnsiForegroundColor('SEAGREEN')
		AnsiColorSet['TYPE_AUDIT'] = AnsiForegroundColor('YELLOWGREEN')
		AnsiColorSet['AUDIT_MESSAGE'] = AnsiForegroundColor('OLIVEDRAB')
		AnsiColorSet['TYPE_METRICS'] = AnsiForegroundColor('OLIVE')
		AnsiColorSet['METRICS_MESSAGE'] = AnsiForegroundColor('DARKOLIVEGREEN')
		AnsiColorSet['TYPE_USER'] = AnsiForegroundColor('PALEGREEN')
		AnsiColorSet['USER_MESSAGE'] = AnsiForegroundColor('LIGHTGREEN')
		AnsiColorSet['TYPE_MESSAGE'] = AnsiForegroundColor('LIGHTSTEELBLUE')
		AnsiColorSet['MESSAGE_MESSAGE'] = AnsiForegroundColor('POWDERBLUE')
		AnsiColorSet['TYPE_INFO'] = AnsiForegroundColor('PALETURQUOISE')
		AnsiColorSet['INFO_MESSAGE'] = AnsiForegroundColor('LIGHTBLUE')
		AnsiColorSet['TYPE_NOTICE'] = AnsiForegroundColor('DEEPSKYBLUE')
		AnsiColorSet['NOTICE_MESSAGE'] = AnsiForegroundColor('DODGERBLUE')
		AnsiColorSet['TYPE_WARNING'] = AnsiForegroundColor('YELLOW')
		AnsiColorSet['WARNING_MESSAGE'] = AnsiForegroundColor('DARKYELLOW')
		AnsiColorSet['TYPE_ERROR'] = AnsiForegroundColor('FIREBRICK')
		AnsiColorSet['ERROR_MESSAGE'] = AnsiForegroundColor('DARKRED')
		AnsiColorSet['TYPE_CRITICAL'] = AnsiForegroundColor('DARKRED')
		AnsiColorSet['CRITICAL_MESSAGE'] = AnsiForegroundColor('MAROON')
		AnsiColorSet['TYPE_PROGRESS'] = AnsiForegroundColor('SKYBLUE')
		AnsiColorSet['PROGRESS_MESSAGE'] = AnsiForegroundColor('LIGHTSKYBLUE')
		AnsiColorSet['TYPE_SUCCESS'] = AnsiForegroundColor('GREEN')
		AnsiColorSet['SUCCESS_MESSAGE'] = AnsiForegroundColor('DARKGREEN')
		AnsiColorSet['TYPE_FAIL'] = AnsiForegroundColor('FIREBRICK')
		AnsiColorSet['FAIL_MESSAGE'] = AnsiForegroundColor('DARKRED')

	@staticmethod
	def setColor(logger_color_name: str, table_color_value: str):
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

		:param logger_color_name: Color name in logger color table
		:param table_color_value: Color value in logger color table
		"""
		from qt_colored_logger import ColorException
		if logger_color_name in AnsiColorSet:
			AnsiColorSet[logger_color_name] = AnsiForegroundColor(table_color_value)
		else:
			raise ColorException("This color is not in the dictionary")

@singleton
class Logger:
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
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_DEBUG']}@DEBUG - " if self.status_type else ""
		log += f"{AnsiColorSet['DEBUG_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_DEBUG_PERFORMANCE']}@DEBUG PERFORMANCE - " if self.status_type else ""
		log += f"{AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_PERFORMANCE']}@PERFORMANCE - " if self.status_type else ""
		log += f"{AnsiColorSet['PERFORMANCE_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_EVENT']}@EVENT - " if self.status_type else ""
		log += f"{AnsiColorSet['EVENT_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_AUDIT']}@AUDIT - " if self.status_type else ""
		log += f"{AnsiColorSet['AUDIT_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_METRICS']}@METRICS - " if self.status_type else ""
		log += f"{AnsiColorSet['METRICS_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_USER']}@USER - " if self.status_type else ""
		log += f"{AnsiColorSet['USER_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_MESSAGE']}@MESSAGE - " if self.status_type else ""
		log += f"{AnsiColorSet['MESSAGE_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_INFO']}@INFO - " if self.status_type else ""
		log += f"{AnsiColorSet['INFO_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_NOTICE']}@NOTICE - " if self.status_type else ""
		log += f"{AnsiColorSet['NOTICE_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_WARNING']}@WARNING - " if self.status_type else ""
		log += f"{AnsiColorSet['WARNING_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_ERROR']}!ERROR - " if self.status_type else ""
		log += f"{AnsiColorSet['ERROR_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_CRITICAL']}!!!@CRITICAL - " if self.status_type else ""
		log += f"{AnsiColorSet['CRITICAL_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		# log += f"{AnsiFormat['bold']['on']}" if bold else ""
		# log += f"{AnsiFormat['italic']['on']}" if italic else ""
		# log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		# log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		# log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		# log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		# log += f"{AnsiColorSet['TYPE_PROGRESS']}@PROGRESS - " if self.status_type else ""
		# log += f"{AnsiColorSet['PROGRESS_MESSAGE']}{message_text}" if self.message else ""
		# log += f"{AnsiFormat['reset']['on']}"
		# return log
		pass
		# Must run on a thread

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
		# Make transition to SUCCESS or FAIL

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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_SUCCESS']}@SUCCESS - " if self.status_type else ""
		log += f"{AnsiColorSet['SUCCESS_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
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
		log += f"{AnsiFormat['bold']['on']}" if bold else ""
		log += f"{AnsiFormat['italic']['on']}" if italic else ""
		log += f"{AnsiColorSet['TIME']}*{datetime.datetime.now()}\t" if self.time else ""
		log += f"{AnsiColorSet['USER']}${platform.node()}^{os.getlogin()}\t" if self.name else ""
		log += f"{AnsiColorSet['STATUS']}#STATUS: " if self.status else ""
		log += f"{AnsiColorSet['STATUS_MESSAGE']}{status_message_text}\t" if self.status_message else ""
		log += f"{AnsiColorSet['TYPE_FAIL']}@FAIL - " if self.status_type else ""
		log += f"{AnsiColorSet['FAIL_MESSAGE']}{message_text}" if self.message else ""
		log += f"{AnsiFormat['reset']['on']}"
		return log


# Test
if __name__ == "__main__":
	mod = AnsiColorSetInit()
	logger = Logger()
	print(logger.DEBUG("1", "2"))
	print(logger.DEBUG_PERFORMANCE("3", "4"))
	print(logger.PERFORMANCE("5", "6"))
	print(logger.EVENT("7", "8"))
	print(logger.AUDIT("9", "10"))
	print(logger.METRICS("11", "12"))
	print(logger.USER("13", "14"))
	print(logger.MESSAGE("15", "16"))
	print(logger.INFO("17", "18"))
	print(logger.NOTICE("19", "20"))
	print(logger.WARNING("21", "22"))
	print(logger.ERROR("23", "24"))
	print(logger.CRITICAL("25", "26"))
	# print(logger.START_PROCESS("27", "28"))
	print(logger.SUCCESS("29", "30"))
	print(logger.FAIL("31", "32"))
