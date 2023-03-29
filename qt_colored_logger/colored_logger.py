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

from qt_colored_logger.basic.patterns import Singleton
from qt_colored_logger.basic import BasicLogger
from qt_colored_logger.basic import ColorException
from qt_colored_logger.src import GetDefaultColorScheme, AnsiForegroundColor, Dec2Ansi

AnsiColorSet: dict = {}

class AnsiColorSetInit(Singleton):
	"""
	Initializes a color table and provides functionality to modify this table.
	Only one class object can be created!!!
	"""

	def __init__(self):
		"""
		Initializes the color table.
		Only one class object can be created!!!
		"""
		AnsiColorSet['TIME'] = AnsiForegroundColor(GetDefaultColorScheme()[0])
		AnsiColorSet['USER'] = AnsiForegroundColor(GetDefaultColorScheme()[1])
		AnsiColorSet['STATUS'] = AnsiForegroundColor(GetDefaultColorScheme()[2])
		AnsiColorSet['STATUS_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[3])
		AnsiColorSet['TYPE_DEBUG'] = AnsiForegroundColor(GetDefaultColorScheme()[4])
		AnsiColorSet['DEBUG_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[5])
		AnsiColorSet['TYPE_DEBUG_PERFORMANCE'] = AnsiForegroundColor(GetDefaultColorScheme()[6])
		AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[7])
		AnsiColorSet['TYPE_PERFORMANCE'] = AnsiForegroundColor(GetDefaultColorScheme()[8])
		AnsiColorSet['PERFORMANCE_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[9])
		AnsiColorSet['TYPE_EVENT'] = AnsiForegroundColor(GetDefaultColorScheme()[10])
		AnsiColorSet['EVENT_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[11])
		AnsiColorSet['TYPE_AUDIT'] = AnsiForegroundColor(GetDefaultColorScheme()[12])
		AnsiColorSet['AUDIT_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[13])
		AnsiColorSet['TYPE_METRICS'] = AnsiForegroundColor(GetDefaultColorScheme()[14])
		AnsiColorSet['METRICS_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[15])
		AnsiColorSet['TYPE_USER'] = AnsiForegroundColor(GetDefaultColorScheme()[16])
		AnsiColorSet['USER_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[17])
		AnsiColorSet['TYPE_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[18])
		AnsiColorSet['MESSAGE_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[19])
		AnsiColorSet['TYPE_INFO'] = AnsiForegroundColor(GetDefaultColorScheme()[20])
		AnsiColorSet['INFO_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[21])
		AnsiColorSet['TYPE_NOTICE'] = AnsiForegroundColor(GetDefaultColorScheme()[22])
		AnsiColorSet['NOTICE_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[23])
		AnsiColorSet['TYPE_WARNING'] = AnsiForegroundColor(GetDefaultColorScheme()[24])
		AnsiColorSet['WARNING_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[25])
		AnsiColorSet['TYPE_ERROR'] = AnsiForegroundColor(GetDefaultColorScheme()[26])
		AnsiColorSet['ERROR_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[27])
		AnsiColorSet['TYPE_CRITICAL'] = AnsiForegroundColor(GetDefaultColorScheme()[27])
		AnsiColorSet['CRITICAL_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[28])
		AnsiColorSet['TYPE_PROGRESS'] = AnsiForegroundColor(GetDefaultColorScheme()[29])
		AnsiColorSet['PROGRESS_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[30])
		AnsiColorSet['TYPE_SUCCESS'] = AnsiForegroundColor(GetDefaultColorScheme()[31])
		AnsiColorSet['SUCCESS_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[32])
		AnsiColorSet['TYPE_FAIL'] = AnsiForegroundColor(GetDefaultColorScheme()[26])
		AnsiColorSet['FAIL_MESSAGE'] = AnsiForegroundColor(GetDefaultColorScheme()[27])

	@staticmethod
	def setColor(logger_color_name: str, color_value: list[int, int, int]):
		"""
		A method that sets the ANSI escape code color code in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys:
		`TIME, USER, STATUS, STATUS_MESSAGE, TYPE_DEBUG, DEBUG_MESSAGE, TYPE_DEBUG_PERFORMANCE,
		DEBUG_PERFORMANCE_MESSAGE, TYPE_PERFORMANCE, PERFORMANCE_MESSAGE, TYPE_EVENT, EVENT_MESSAGE,
		TYPE_AUDIT, AUDIT_MESSAGE, TYPE_METRICS, METRICS_MESSAGE, TYPE_USER, USER_MESSAGE,
		TYPE_MESSAGE, MESSAGE_MESSAGE, TYPE_INFO, INFO_MESSAGE, TYPE_NOTICE, NOTICE_MESSAGE,
		TYPE_WARNING, WARNING_MESSAGE, TYPE_ERROR, ERROR_MESSAGE, TYPE_CRITICAL, CRITICAL_MESSAGE,
		TYPE_PROGRESS, PROGRESS_MESSAGE, TYPE_SUCCESS, SUCCESS_MESSAGE, TYPE_FAIL, FAIL_MESSAGE.`

		:param logger_color_name: Color name in logger color table
		:param color_value: Color value in RGB
		"""
		if logger_color_name in AnsiColorSet:
			AnsiColorSet[logger_color_name] = Dec2Ansi(color_value)
		else:
			raise ColorException("This color is not in the dictionary")

class Logger(Singleton, BasicLogger):
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

	def DEBUG(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Debugging information logging:
		Can be used to record any information while debugging an application.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_DEBUG'],
				AnsiColorSet['DEBUG_MESSAGE']
			], status_message_text, "@DEBUG", message_text, bold, italic
		)

	def DEBUG_PERFORMANCE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Performance debugging information logging:
		Can be used to record the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_DEBUG_PERFORMANCE'],
				AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE']
			], status_message_text, "@DEBUG PERFORMANCE", message_text, bold, italic
		)

	def PERFORMANCE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Performance information logging:
		Can be used to record the execution time of operations or
		other application performance information.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_PERFORMANCE'],
				AnsiColorSet['PERFORMANCE_MESSAGE']
			], status_message_text, "@PERFORMANCE", message_text, bold, italic
		)

	def EVENT(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Event information logging:
		Can be used to track specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_EVENT'],
				AnsiColorSet['EVENT_MESSAGE']
			], status_message_text, "@EVENT", message_text, bold, italic
		)

	def AUDIT(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Audit information logging:
		Can be used to track changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_AUDIT'],
				AnsiColorSet['AUDIT_MESSAGE']
			], status_message_text, "@AUDIT", message_text, bold, italic
		)

	def METRICS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Metrics information logging:
		Can be used to log metrics to track application performance and identify issues.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_METRICS'],
				AnsiColorSet['METRICS_MESSAGE']
			], status_message_text, "@METRICS", message_text, bold, italic
		)

	def USER(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		User information logging:
		Can be used to add custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_USER'],
				AnsiColorSet['USER_MESSAGE']
			], status_message_text, "@USER", message_text, bold, italic
		)

	def MESSAGE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_MESSAGE'],
				AnsiColorSet['MESSAGE_MESSAGE']
			], status_message_text, "@MESSAGE", message_text, bold, italic
		)

	def INFO(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Default information logging:
		Can be used to display messages with specific content about the operation of the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_INFO'],
				AnsiColorSet['INFO_MESSAGE']
			], status_message_text, "@INFO", message_text, bold, italic
		)

	def NOTICE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_NOTICE'],
				AnsiColorSet['NOTICE_MESSAGE']
			], status_message_text, "@NOTICE", message_text, bold, italic
		)

	def WARNING(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Warning information logging:
		Can be used to display warnings that the program may work with unpredictable results.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_WARNING'],
				AnsiColorSet['WARNING_MESSAGE']
			], status_message_text, "@WARNING", message_text, bold, italic
		)

	def ERROR(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Error information logging:
		Used to display errors and crashes in the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_ERROR'],
				AnsiColorSet['ERROR_MESSAGE']
			], status_message_text, "!ERROR", message_text, bold, italic
		)

	def CRITICAL(self, status_message_text: str = "...", message_text: str = "...", bold: bool = True, italic: bool = False) -> str:
		"""
		Critical error information logging:
		Used to display critical and unpredictable program failures.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_CRITICAL'],
				AnsiColorSet['CRITICAL_MESSAGE']
			], status_message_text, "!!!@CRITICAL", message_text, bold, italic
		)

	def START_PROCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
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

	def STOP_PROCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		pass
		# Make transition to SUCCESS or FAIL

	def SUCCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True) -> str:
		"""
		Success information logging:
		Used to display a message about the success of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_SUCCESS'],
				AnsiColorSet['SUCCESS_MESSAGE']
			], status_message_text, "@SUCCESS", message_text, bold, italic
		)

	def FAIL(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True) -> str:
		"""
		Fail information logging:
		Used to display a message about the failed execution of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_FAIL'],
				AnsiColorSet['FAIL_MESSAGE']
			], status_message_text, "@FAIL", message_text, bold, italic
		)


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

	logger.timeEnabled(False)
	print(logger.DEBUG("1", "2"))
