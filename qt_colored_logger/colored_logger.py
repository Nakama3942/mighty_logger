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

from qt_colored_logger._basic import _Singleton, _BasicLogger, ColorException
from qt_colored_logger.src import GetDefaultColor, AnsiColor, Dec2Ansi

AnsiColorSet: dict = {}

class AnsiColorSetInit(_Singleton):
	"""
	Initializes a color table and provides functionality to modify this table.
	Only one class object can be created!!!
	"""

	def __init__(self):
		"""
		Initializes the color table.
		Only one class object can be created!!!
		"""
		AnsiColorSet['TIME'] = AnsiColor(GetDefaultColor(8), "foreground")
		AnsiColorSet['USER'] = AnsiColor(GetDefaultColor(7), "foreground")
		AnsiColorSet['STATUS'] = AnsiColor(GetDefaultColor(4), "foreground")
		AnsiColorSet['STATUS_MESSAGE'] = AnsiColor(GetDefaultColor(3), "foreground")
		AnsiColorSet['TYPE_DEBUG'] = AnsiColor(GetDefaultColor(28), "foreground")
		AnsiColorSet['DEBUG_MESSAGE'] = AnsiColor(GetDefaultColor(27), "foreground")
		AnsiColorSet['DEBUG_BACKGROUND'] = None
		AnsiColorSet['TYPE_DEBUG_PERFORMANCE'] = AnsiColor(GetDefaultColor(30), "foreground")
		AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'] = AnsiColor(GetDefaultColor(29), "foreground")
		AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'] = None
		AnsiColorSet['TYPE_PERFORMANCE'] = AnsiColor(GetDefaultColor(32), "foreground")
		AnsiColorSet['PERFORMANCE_MESSAGE'] = AnsiColor(GetDefaultColor(31), "foreground")
		AnsiColorSet['PERFORMANCE_BACKGROUND'] = None
		AnsiColorSet['TYPE_EVENT'] = AnsiColor(GetDefaultColor(15), "foreground")
		AnsiColorSet['EVENT_MESSAGE'] = AnsiColor(GetDefaultColor(12), "foreground")
		AnsiColorSet['EVENT_BACKGROUND'] = None
		AnsiColorSet['TYPE_AUDIT'] = AnsiColor(GetDefaultColor(16), "foreground")
		AnsiColorSet['AUDIT_MESSAGE'] = AnsiColor(GetDefaultColor(14), "foreground")
		AnsiColorSet['AUDIT_BACKGROUND'] = None
		AnsiColorSet['TYPE_METRICS'] = AnsiColor(GetDefaultColor(13), "foreground")
		AnsiColorSet['METRICS_MESSAGE'] = AnsiColor(GetDefaultColor(11), "foreground")
		AnsiColorSet['METRICS_BACKGROUND'] = None
		AnsiColorSet['TYPE_USER'] = AnsiColor(GetDefaultColor(18), "foreground")
		AnsiColorSet['USER_MESSAGE'] = AnsiColor(GetDefaultColor(17), "foreground")
		AnsiColorSet['USER_BACKGROUND'] = None
		AnsiColorSet['TYPE_MESSAGE'] = AnsiColor(GetDefaultColor(21), "foreground")
		AnsiColorSet['MESSAGE_MESSAGE'] = AnsiColor(GetDefaultColor(23), "foreground")
		AnsiColorSet['MESSAGE_BACKGROUND'] = None
		AnsiColorSet['TYPE_INFO'] = AnsiColor(GetDefaultColor(24), "foreground")
		AnsiColorSet['INFO_MESSAGE'] = AnsiColor(GetDefaultColor(22), "foreground")
		AnsiColorSet['INFO_BACKGROUND'] = None
		AnsiColorSet['TYPE_NOTICE'] = AnsiColor(GetDefaultColor(26), "foreground")
		AnsiColorSet['NOTICE_MESSAGE'] = AnsiColor(GetDefaultColor(25), "foreground")
		AnsiColorSet['NOTICE_BACKGROUND'] = None
		AnsiColorSet['TYPE_WARNING'] = AnsiColor(GetDefaultColor(34), "foreground")
		AnsiColorSet['WARNING_MESSAGE'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['WARNING_BACKGROUND'] = AnsiColor(GetDefaultColor(6), "background")
		AnsiColorSet['TYPE_ERROR'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['ERROR_MESSAGE'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['ERROR_BACKGROUND'] = AnsiColor(GetDefaultColor(2), "background")
		AnsiColorSet['TYPE_CRITICAL'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['CRITICAL_MESSAGE'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['CRITICAL_BACKGROUND'] = AnsiColor(GetDefaultColor(0), "background")
		AnsiColorSet['TYPE_PROGRESS'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['PROGRESS_MESSAGE'] = AnsiColor(GetDefaultColor(34), "foreground")
		AnsiColorSet['PROGRESS_BACKGROUND'] = AnsiColor(GetDefaultColor(20), "background")
		AnsiColorSet['TYPE_SUCCESS'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['SUCCESS_MESSAGE'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['SUCCESS_BACKGROUND'] = AnsiColor(GetDefaultColor(9), "background")
		AnsiColorSet['TYPE_FAIL'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['FAIL_MESSAGE'] = AnsiColor(GetDefaultColor(33), "foreground")
		AnsiColorSet['FAIL_BACKGROUND'] = AnsiColor(GetDefaultColor(1), "background")

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
			AnsiColorSet[logger_color_name] = Dec2Ansi(color_value, "foreground")
		else:
			raise ColorException("This color is not in the dictionary")

class Logger(_Singleton, _BasicLogger):
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

	def DEBUG(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Debugging information logging:
		Can be used to record any information while debugging an application.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_DEBUG'],
				AnsiColorSet['DEBUG_MESSAGE'],
				AnsiColorSet['DEBUG_BACKGROUND'],
			], status_message_text, "@DEBUG", message_text, bold, italic, invert, background
		)

	def DEBUG_PERFORMANCE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Performance debugging information logging:
		Can be used to record the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_DEBUG_PERFORMANCE'],
				AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'],
				AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'],
			], status_message_text, "@DEBUG PERFORMANCE", message_text, bold, italic, invert, background
		)

	def PERFORMANCE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Performance information logging:
		Can be used to record the execution time of operations or
		other application performance information.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_PERFORMANCE'],
				AnsiColorSet['PERFORMANCE_MESSAGE'],
				AnsiColorSet['PERFORMANCE_BACKGROUND'],
			], status_message_text, "@PERFORMANCE", message_text, bold, italic, invert, background
		)

	def EVENT(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Event information logging:
		Can be used to track specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_EVENT'],
				AnsiColorSet['EVENT_MESSAGE'],
				AnsiColorSet['EVENT_BACKGROUND'],
			], status_message_text, "@EVENT", message_text, bold, italic, invert, background
		)

	def AUDIT(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Audit information logging:
		Can be used to track changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_AUDIT'],
				AnsiColorSet['AUDIT_MESSAGE'],
				AnsiColorSet['AUDIT_BACKGROUND'],
			], status_message_text, "@AUDIT", message_text, bold, italic, invert, background
		)

	def METRICS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Metrics information logging:
		Can be used to log metrics to track application performance and identify issues.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_METRICS'],
				AnsiColorSet['METRICS_MESSAGE'],
				AnsiColorSet['METRICS_BACKGROUND'],
			], status_message_text, "@METRICS", message_text, bold, italic, invert, background
		)

	def USER(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		User information logging:
		Can be used to add custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_USER'],
				AnsiColorSet['USER_MESSAGE'],
				AnsiColorSet['USER_BACKGROUND'],
			], status_message_text, "@USER", message_text, bold, italic, invert, background
		)

	def MESSAGE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_MESSAGE'],
				AnsiColorSet['MESSAGE_MESSAGE'],
				AnsiColorSet['MESSAGE_BACKGROUND'],
			], status_message_text, "@MESSAGE", message_text, bold, italic, invert, background
		)

	def INFO(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Default information logging:
		Can be used to display messages with specific content about the operation of the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_INFO'],
				AnsiColorSet['INFO_MESSAGE'],
				AnsiColorSet['INFO_BACKGROUND'],
			], status_message_text, "@INFO", message_text, bold, italic, invert, background
		)

	def NOTICE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_NOTICE'],
				AnsiColorSet['NOTICE_MESSAGE'],
				AnsiColorSet['NOTICE_BACKGROUND'],
			], status_message_text, "@NOTICE", message_text, bold, italic, invert, background
		)

	def WARNING(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
		"""
		Warning information logging:
		Can be used to display warnings that the program may work with unpredictable results.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_WARNING'],
				AnsiColorSet['WARNING_MESSAGE'],
				AnsiColorSet['WARNING_BACKGROUND'],
			], status_message_text, "@WARNING", message_text, bold, italic, invert, background
		)

	def ERROR(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
		"""
		Error information logging:
		Used to display errors and crashes in the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_ERROR'],
				AnsiColorSet['ERROR_MESSAGE'],
				AnsiColorSet['ERROR_BACKGROUND'],
			], status_message_text, "!ERROR", message_text, bold, italic, invert, background
		)

	def CRITICAL(self, status_message_text: str = "...", message_text: str = "...", bold: bool = True, italic: bool = False, invert: bool = False, background: bool = True) -> str:
		"""
		Critical error information logging:
		Used to display critical and unpredictable program failures.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_CRITICAL'],
				AnsiColorSet['CRITICAL_MESSAGE'],
				AnsiColorSet['CRITICAL_BACKGROUND'],
			], status_message_text, "!!!@CRITICAL", message_text, bold, italic, invert, background
		)

	def START_PROCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		# return self._assemble_entry(
		# 	[
		# 		AnsiColorSet['TIME'],
		# 		AnsiColorSet['USER'],
		# 		AnsiColorSet['STATUS'],
		# 		AnsiColorSet['STATUS_MESSAGE'],
		# 		AnsiColorSet['TYPE_PROGRESS'],
		# 		AnsiColorSet['PROGRESS_MESSAGE'],
		# 		AnsiColorSet['PROGRESS_BACKGROUND'],
		# 	], status_message_text, "@PROGRESS", message_text, bold, italic, invert, background
		# )
		pass
		# Must run on a thread

	def STOP_PROCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		pass
		# Make transition to SUCCESS or FAIL

	def SUCCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, background: bool = True) -> str:
		"""
		Success information logging:
		Used to display a message about the success of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_SUCCESS'],
				AnsiColorSet['SUCCESS_MESSAGE'],
				AnsiColorSet['SUCCESS_BACKGROUND'],
			], status_message_text, "@SUCCESS", message_text, bold, italic, invert, background
		)

	def FAIL(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, background: bool = True) -> str:
		"""
		Fail information logging:
		Used to display a message about the failed execution of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				AnsiColorSet['TIME'],
				AnsiColorSet['USER'],
				AnsiColorSet['STATUS'],
				AnsiColorSet['STATUS_MESSAGE'],
				AnsiColorSet['TYPE_FAIL'],
				AnsiColorSet['FAIL_MESSAGE'],
				AnsiColorSet['FAIL_BACKGROUND'],
			], status_message_text, "@FAIL", message_text, bold, italic, invert, background
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
	print(logger.FAIL(status_message_text="31", message_text="32", invert=True))

	logger.timeEnabled(False)
	print(logger.DEBUG("1", "2"))
