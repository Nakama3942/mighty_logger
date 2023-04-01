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

# The idea is taken here:
# https://github.com/Nakama3942/WiretappingScanner/commit/da5e0e71681b9e1462d5bba5438fc8b1fde8142e

from qt_colored_logger._basic import _Singleton, _BasicLogger, ColorException
from qt_colored_logger.src import GetDefaultColor, HexColor, Dec2Hex

HtmlColorSet: dict = {}

class HtmlColorSetInitQ(_Singleton):
	"""
	Initializes a color table and provides functionality to modify this table.
	Only one class object can be created!!!
	"""

	def __init__(self):
		"""
		Initializes the color table.
		Only one class object can be created!!!
		"""
		HtmlColorSet['TIME'] = HexColor(GetDefaultColor(8))
		HtmlColorSet['USER'] = HexColor(GetDefaultColor(7))
		HtmlColorSet['STATUS'] = HexColor(GetDefaultColor(4))
		HtmlColorSet['STATUS_MESSAGE'] = HexColor(GetDefaultColor(3))
		HtmlColorSet['TYPE_DEBUG'] = HexColor(GetDefaultColor(28))
		HtmlColorSet['DEBUG_MESSAGE'] = HexColor(GetDefaultColor(27))
		HtmlColorSet['TYPE_DEBUG_PERFORMANCE'] = HexColor(GetDefaultColor(30))
		HtmlColorSet['DEBUG_PERFORMANCE_MESSAGE'] = HexColor(GetDefaultColor(29))
		HtmlColorSet['TYPE_PERFORMANCE'] = HexColor(GetDefaultColor(32))
		HtmlColorSet['PERFORMANCE_MESSAGE'] = HexColor(GetDefaultColor(31))
		HtmlColorSet['TYPE_EVENT'] = HexColor(GetDefaultColor(15))
		HtmlColorSet['EVENT_MESSAGE'] = HexColor(GetDefaultColor(12))
		HtmlColorSet['TYPE_AUDIT'] = HexColor(GetDefaultColor(16))
		HtmlColorSet['AUDIT_MESSAGE'] = HexColor(GetDefaultColor(14))
		HtmlColorSet['TYPE_METRICS'] = HexColor(GetDefaultColor(13))
		HtmlColorSet['METRICS_MESSAGE'] = HexColor(GetDefaultColor(11))
		HtmlColorSet['TYPE_USER'] = HexColor(GetDefaultColor(18))
		HtmlColorSet['USER_MESSAGE'] = HexColor(GetDefaultColor(17))
		HtmlColorSet['TYPE_MESSAGE'] = HexColor(GetDefaultColor(21))
		HtmlColorSet['MESSAGE_MESSAGE'] = HexColor(GetDefaultColor(23))
		HtmlColorSet['TYPE_INFO'] = HexColor(GetDefaultColor(24))
		HtmlColorSet['INFO_MESSAGE'] = HexColor(GetDefaultColor(22))
		HtmlColorSet['TYPE_NOTICE'] = HexColor(GetDefaultColor(26))
		HtmlColorSet['NOTICE_MESSAGE'] = HexColor(GetDefaultColor(25))
		HtmlColorSet['TYPE_WARNING'] = HexColor(GetDefaultColor(5))
		HtmlColorSet['WARNING_MESSAGE'] = HexColor(GetDefaultColor(6))
		HtmlColorSet['TYPE_ERROR'] = HexColor(GetDefaultColor(2))
		HtmlColorSet['ERROR_MESSAGE'] = HexColor(GetDefaultColor(1))
		HtmlColorSet['TYPE_CRITICAL'] = HexColor(GetDefaultColor(1))
		HtmlColorSet['CRITICAL_MESSAGE'] = HexColor(GetDefaultColor(0))
		HtmlColorSet['TYPE_PROGRESS'] = HexColor(GetDefaultColor(19))
		HtmlColorSet['PROGRESS_MESSAGE'] = HexColor(GetDefaultColor(20))
		HtmlColorSet['TYPE_SUCCESS'] = HexColor(GetDefaultColor(10))
		HtmlColorSet['SUCCESS_MESSAGE'] = HexColor(GetDefaultColor(9))
		HtmlColorSet['TYPE_FAIL'] = HexColor(GetDefaultColor(2))
		HtmlColorSet['FAIL_MESSAGE'] = HexColor(GetDefaultColor(1))

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
		:param hex_color_value: Hexadecimal color value in logger color table
		"""
		if color_name in HtmlColorSet:
			HtmlColorSet[color_name] = hex_color_value
		else:
			raise ColorException("This color is not in the dictionary")

	@staticmethod
	def setColor(color_name: str, color_value: list[int, int, int]):
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
		:param color_value: Color value in RGB
		"""
		if color_name in HtmlColorSet:
			HtmlColorSet[color_name] = Dec2Hex(color_value)
		else:
			raise ColorException("This color is not in the dictionary")

class LoggerQ(_Singleton, _BasicLogger):
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
	6) Recording message.
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_DEBUG'],
				HtmlColorSet['DEBUG_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_DEBUG_PERFORMANCE'],
				HtmlColorSet['DEBUG_PERFORMANCE_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_PERFORMANCE'],
				HtmlColorSet['PERFORMANCE_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_EVENT'],
				HtmlColorSet['EVENT_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_AUDIT'],
				HtmlColorSet['AUDIT_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_METRICS'],
				HtmlColorSet['METRICS_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_USER'],
				HtmlColorSet['USER_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_MESSAGE'],
				HtmlColorSet['MESSAGE_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_INFO'],
				HtmlColorSet['INFO_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_NOTICE'],
				HtmlColorSet['NOTICE_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_WARNING'],
				HtmlColorSet['WARNING_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_ERROR'],
				HtmlColorSet['ERROR_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_CRITICAL'],
				HtmlColorSet['CRITICAL_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_SUCCESS'],
				HtmlColorSet['SUCCESS_MESSAGE']
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
		return self._assemble_html_entry(
			[
				HtmlColorSet['TIME'],
				HtmlColorSet['USER'],
				HtmlColorSet['STATUS'],
				HtmlColorSet['STATUS_MESSAGE'],
				HtmlColorSet['TYPE_FAIL'],
				HtmlColorSet['FAIL_MESSAGE']
			], status_message_text, "@FAIL", message_text, bold, italic
		)


# Test
if __name__ == "__main__":
	mod = HtmlColorSetInitQ()
	logger = LoggerQ(status_message=False)
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

	# logger2 = LoggerQ()
	# print(logger.ID)
	# print(logger2.ID)
	# logger.ID = 10
	# print(logger.ID)
	# print(logger2.ID)

	print(len(HtmlColorSet))
	mod.setColor("TIME", [100, 200, 255])
	print(len(HtmlColorSet))

	# print(logger.DEBUG(message_text="Debug data"))
	# print(logger.DEBUG(message_text="Debug data", bold=True))
	# print(logger.DEBUG(message_text="Debug data", italic=True))
	# print(logger.DEBUG(message_text="Debug data", bold=True, italic=True))
	#
	# print(logger.NOTICE(message_text="Debug data"))
	# mod.setColor("NOTICE_MESSAGE", 127, 255, 0)
	# print(logger.NOTICE(message_text="Debug data"))
