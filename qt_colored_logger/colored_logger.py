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
from qt_colored_logger.src import AnsiColor, Dec2Ansi

class Logger(_Singleton, _BasicLogger):
	"""
	The Logger class is a class that implements the functionality
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
			*,
			program_name: str = "Unknown",
			time: bool = True,
			name: bool = True,
			status: bool = True,
			status_message: bool = True,
			status_type: bool = True,
			message: bool = True
	):
		super().__init__(program_name, time, name, status, status_message, status_type, message)
		self.__AnsiColorSet: dict = {}
		self._ansi_color_set_init()

	def _ansi_color_set_init(self):
		"""
		Sets the colors of the logger.
		"""
		# DEBUG colors
		self.__AnsiColorSet['DEBUG_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['DEBUG_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['DEBUG_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['DEBUG_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_DEBUG'] = AnsiColor('BURLYWOOD', "foreground")
		self.__AnsiColorSet['DEBUG_MESSAGE'] = AnsiColor('TAN', "foreground")
		self.__AnsiColorSet['DEBUG_BACKGROUND'] = ""
		# DEBUG_PERFORMANCE colors
		self.__AnsiColorSet['DEBUG_PERFORMANCE_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['DEBUG_PERFORMANCE_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_DEBUG_PERFORMANCE'] = AnsiColor('NAVAJOWHITE', "foreground")
		self.__AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'] = AnsiColor('WHEAT', "foreground")
		self.__AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'] = ""
		# PERFORMANCE colors
		self.__AnsiColorSet['PERFORMANCE_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['PERFORMANCE_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['PERFORMANCE_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['PERFORMANCE_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_PERFORMANCE'] = AnsiColor('BLANCHEDALMOND', "foreground")
		self.__AnsiColorSet['PERFORMANCE_MESSAGE'] = AnsiColor('BISQUE', "foreground")
		self.__AnsiColorSet['PERFORMANCE_BACKGROUND'] = ""
		# EVENT colors
		self.__AnsiColorSet['EVENT_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['EVENT_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['EVENT_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['EVENT_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_EVENT'] = AnsiColor('MEDIUMSEAGREEN', "foreground")
		self.__AnsiColorSet['EVENT_MESSAGE'] = AnsiColor('SEAGREEN', "foreground")
		self.__AnsiColorSet['EVENT_BACKGROUND'] = ""
		# AUDIT colors
		self.__AnsiColorSet['AUDIT_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['AUDIT_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['AUDIT_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['AUDIT_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_AUDIT'] = AnsiColor('YELLOWGREEN', "foreground")
		self.__AnsiColorSet['AUDIT_MESSAGE'] = AnsiColor('OLIVEDRAB', "foreground")
		self.__AnsiColorSet['AUDIT_BACKGROUND'] = ""
		# METRICS colors
		self.__AnsiColorSet['METRICS_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['METRICS_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['METRICS_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['METRICS_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_METRICS'] = AnsiColor('OLIVE', "foreground")
		self.__AnsiColorSet['METRICS_MESSAGE'] = AnsiColor('DARKOLIVEGREEN', "foreground")
		self.__AnsiColorSet['METRICS_BACKGROUND'] = ""
		# USER colors
		self.__AnsiColorSet['USER_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['USER_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['USER_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['USER_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_USER'] = AnsiColor('PALEGREEN', "foreground")
		self.__AnsiColorSet['USER_MESSAGE'] = AnsiColor('LIGHTGREEN', "foreground")
		self.__AnsiColorSet['USER_BACKGROUND'] = ""
		# MESSAGE colors
		self.__AnsiColorSet['MESSAGE_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['MESSAGE_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['MESSAGE_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['MESSAGE_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_MESSAGE'] = AnsiColor('LIGHTSTEELBLUE', "foreground")
		self.__AnsiColorSet['MESSAGE_MESSAGE'] = AnsiColor('POWDERBLUE', "foreground")
		self.__AnsiColorSet['MESSAGE_BACKGROUND'] = ""
		# INFO colors
		self.__AnsiColorSet['INFO_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['INFO_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['INFO_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['INFO_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_INFO'] = AnsiColor('PALETURQUOISE', "foreground")
		self.__AnsiColorSet['INFO_MESSAGE'] = AnsiColor('LIGHTBLUE', "foreground")
		self.__AnsiColorSet['INFO_BACKGROUND'] = ""
		# NOTICE colors
		self.__AnsiColorSet['NOTICE_TIME'] = AnsiColor('ORCHID', "foreground")
		self.__AnsiColorSet['NOTICE_USER'] = AnsiColor('MEDIUMORCHID', "foreground")
		self.__AnsiColorSet['NOTICE_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['NOTICE_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_NOTICE'] = AnsiColor('DEEPSKYBLUE', "foreground")
		self.__AnsiColorSet['NOTICE_MESSAGE'] = AnsiColor('DODGERBLUE', "foreground")
		self.__AnsiColorSet['NOTICE_BACKGROUND'] = ""
		# WARNING colors
		self.__AnsiColorSet['WARNING_TIME'] = AnsiColor('DARKMAGENTA', "foreground")
		self.__AnsiColorSet['WARNING_USER'] = AnsiColor('PURPLE', "foreground")
		self.__AnsiColorSet['WARNING_STATUS'] = AnsiColor('DARKRED', "foreground")
		self.__AnsiColorSet['WARNING_STATUS_MESSAGE'] = AnsiColor('MAROON', "foreground")
		self.__AnsiColorSet['TYPE_WARNING'] = AnsiColor('NAVY', "foreground")
		self.__AnsiColorSet['WARNING_MESSAGE'] = AnsiColor('MIDNIGHTBLUE', "foreground")
		self.__AnsiColorSet['WARNING_BACKGROUND'] = AnsiColor('DARKYELLOW', "background")
		# ERROR colors
		self.__AnsiColorSet['ERROR_TIME'] = AnsiColor('PLUM', "foreground")
		self.__AnsiColorSet['ERROR_USER'] = AnsiColor('VIOLET', "foreground")
		self.__AnsiColorSet['ERROR_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['ERROR_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_ERROR'] = AnsiColor('GAINSBORO', "foreground")
		self.__AnsiColorSet['ERROR_MESSAGE'] = AnsiColor('LIGHTGRAY', "foreground")
		self.__AnsiColorSet['ERROR_BACKGROUND'] = AnsiColor('DARKRED', "background")
		# CRITICAL colors
		self.__AnsiColorSet['CRITICAL_TIME'] = AnsiColor('PLUM', "foreground")
		self.__AnsiColorSet['CRITICAL_USER'] = AnsiColor('VIOLET', "foreground")
		self.__AnsiColorSet['CRITICAL_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['CRITICAL_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_CRITICAL'] = AnsiColor('DARKSALMON', "foreground")
		self.__AnsiColorSet['CRITICAL_MESSAGE'] = AnsiColor('LIGHTSALMON', "foreground")
		self.__AnsiColorSet['CRITICAL_BACKGROUND'] = AnsiColor('MAROON', "background")
		# PROGRESS colors
		self.__AnsiColorSet['PROGRESS_TIME'] = AnsiColor('PURPLE', "foreground")
		self.__AnsiColorSet['PROGRESS_USER'] = AnsiColor('INDIGO', "foreground")
		self.__AnsiColorSet['PROGRESS_STATUS'] = AnsiColor('DARKRED', "foreground")
		self.__AnsiColorSet['PROGRESS_STATUS_MESSAGE'] = AnsiColor('MAROON', "foreground")
		self.__AnsiColorSet['TYPE_PROGRESS'] = AnsiColor('NAVY', "foreground")
		self.__AnsiColorSet['PROGRESS_MESSAGE'] = AnsiColor('MIDNIGHTBLUE', "foreground")
		self.__AnsiColorSet['PROGRESS_BACKGROUND'] = AnsiColor('SKYBLUE', "background")
		# SUCCESS colors
		self.__AnsiColorSet['SUCCESS_TIME'] = AnsiColor('LAVENDERBLUSH', "foreground")
		self.__AnsiColorSet['SUCCESS_USER'] = AnsiColor('MISTYROSE', "foreground")
		self.__AnsiColorSet['SUCCESS_STATUS'] = AnsiColor('KHAKI', "foreground")
		self.__AnsiColorSet['SUCCESS_STATUS_MESSAGE'] = AnsiColor('DARKKHAKI', "foreground")
		self.__AnsiColorSet['TYPE_SUCCESS'] = AnsiColor('PALEGREEN', "foreground")
		self.__AnsiColorSet['SUCCESS_MESSAGE'] = AnsiColor('LIGHTGREEN', "foreground")
		self.__AnsiColorSet['SUCCESS_BACKGROUND'] = AnsiColor('DARKGREEN', "background")
		# FAIL colors
		self.__AnsiColorSet['FAIL_TIME'] = AnsiColor('LAVENDERBLUSH', "foreground")
		self.__AnsiColorSet['FAIL_USER'] = AnsiColor('MISTYROSE', "foreground")
		self.__AnsiColorSet['FAIL_STATUS'] = AnsiColor('ORANGE', "foreground")
		self.__AnsiColorSet['FAIL_STATUS_MESSAGE'] = AnsiColor('DARKORANGE', "foreground")
		self.__AnsiColorSet['TYPE_FAIL'] = AnsiColor('YELLOW', "foreground")
		self.__AnsiColorSet['FAIL_MESSAGE'] = AnsiColor('DARKYELLOW', "foreground")
		self.__AnsiColorSet['FAIL_BACKGROUND'] = AnsiColor('DARKRED', "background")

	def set_color(self, logger_color_name: str, color_value: list[int, int, int]):
		"""
		A method that sets the ANSI escape code color code in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys: see README.md/Data/"Logger Color Chart"

		:param logger_color_name: Color name in logger color table
		:param color_value: Color value in RGB
		"""
		if logger_color_name in AnsiColorSet:
			self.__AnsiColorSet[logger_color_name] = Dec2Ansi(color_value, "foreground")
		else:
			raise ColorException("This color is not in the dictionary")

	def DEBUG(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['DEBUG_TIME'],
				self.__AnsiColorSet['DEBUG_USER'],
				self.__AnsiColorSet['DEBUG_STATUS'],
				self.__AnsiColorSet['DEBUG_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_DEBUG'],
				self.__AnsiColorSet['DEBUG_MESSAGE'],
				self.__AnsiColorSet['DEBUG_BACKGROUND'],
			], status_message_text, "%DEBUG", message_text, bold, italic, invert, background
		)

	def DEBUG_PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['DEBUG_PERFORMANCE_TIME'],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_USER'],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS'],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_DEBUG_PERFORMANCE'],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'],
			], status_message_text, "%DEBUG PERFORMANCE", message_text, bold, italic, invert, background
		)

	def PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['PERFORMANCE_TIME'],
				self.__AnsiColorSet['PERFORMANCE_USER'],
				self.__AnsiColorSet['PERFORMANCE_STATUS'],
				self.__AnsiColorSet['PERFORMANCE_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_PERFORMANCE'],
				self.__AnsiColorSet['PERFORMANCE_MESSAGE'],
				self.__AnsiColorSet['PERFORMANCE_BACKGROUND'],
			], status_message_text, "%PERFORMANCE", message_text, bold, italic, invert, background
		)

	def EVENT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['EVENT_TIME'],
				self.__AnsiColorSet['EVENT_USER'],
				self.__AnsiColorSet['EVENT_STATUS'],
				self.__AnsiColorSet['EVENT_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_EVENT'],
				self.__AnsiColorSet['EVENT_MESSAGE'],
				self.__AnsiColorSet['EVENT_BACKGROUND'],
			], status_message_text, "~EVENT", message_text, bold, italic, invert, background
		)

	def AUDIT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['AUDIT_TIME'],
				self.__AnsiColorSet['AUDIT_USER'],
				self.__AnsiColorSet['AUDIT_STATUS'],
				self.__AnsiColorSet['AUDIT_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_AUDIT'],
				self.__AnsiColorSet['AUDIT_MESSAGE'],
				self.__AnsiColorSet['AUDIT_BACKGROUND'],
			], status_message_text, "~AUDIT", message_text, bold, italic, invert, background
		)

	def METRICS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['METRICS_TIME'],
				self.__AnsiColorSet['METRICS_USER'],
				self.__AnsiColorSet['METRICS_STATUS'],
				self.__AnsiColorSet['METRICS_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_METRICS'],
				self.__AnsiColorSet['METRICS_MESSAGE'],
				self.__AnsiColorSet['METRICS_BACKGROUND'],
			], status_message_text, "~METRICS", message_text, bold, italic, invert, background
		)

	def USER(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['USER_TIME'],
				self.__AnsiColorSet['USER_USER'],
				self.__AnsiColorSet['USER_STATUS'],
				self.__AnsiColorSet['USER_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_USER'],
				self.__AnsiColorSet['USER_MESSAGE'],
				self.__AnsiColorSet['USER_BACKGROUND'],
			], status_message_text, "~USER", message_text, bold, italic, invert, background
		)

	def MESSAGE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['MESSAGE_TIME'],
				self.__AnsiColorSet['MESSAGE_USER'],
				self.__AnsiColorSet['MESSAGE_STATUS'],
				self.__AnsiColorSet['MESSAGE_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_MESSAGE'],
				self.__AnsiColorSet['MESSAGE_MESSAGE'],
				self.__AnsiColorSet['MESSAGE_BACKGROUND'],
			], status_message_text, "@MESSAGE", message_text, bold, italic, invert, background
		)

	def INFO(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['INFO_TIME'],
				self.__AnsiColorSet['INFO_USER'],
				self.__AnsiColorSet['INFO_STATUS'],
				self.__AnsiColorSet['INFO_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_INFO'],
				self.__AnsiColorSet['INFO_MESSAGE'],
				self.__AnsiColorSet['INFO_BACKGROUND'],
			], status_message_text, "@INFO", message_text, bold, italic, invert, background
		)

	def NOTICE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = False) -> str:
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
				self.__AnsiColorSet['NOTICE_TIME'],
				self.__AnsiColorSet['NOTICE_USER'],
				self.__AnsiColorSet['NOTICE_STATUS'],
				self.__AnsiColorSet['NOTICE_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_NOTICE'],
				self.__AnsiColorSet['NOTICE_MESSAGE'],
				self.__AnsiColorSet['NOTICE_BACKGROUND'],
			], status_message_text, "@NOTICE", message_text, bold, italic, invert, background
		)

	def WARNING(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
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
				self.__AnsiColorSet['WARNING_TIME'],
				self.__AnsiColorSet['WARNING_USER'],
				self.__AnsiColorSet['WARNING_STATUS'],
				self.__AnsiColorSet['WARNING_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_WARNING'],
				self.__AnsiColorSet['WARNING_MESSAGE'],
				self.__AnsiColorSet['WARNING_BACKGROUND'],
			], status_message_text, "!WARNING", message_text, bold, italic, invert, background
		)

	def ERROR(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
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
				self.__AnsiColorSet['ERROR_TIME'],
				self.__AnsiColorSet['ERROR_USER'],
				self.__AnsiColorSet['ERROR_STATUS'],
				self.__AnsiColorSet['ERROR_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_ERROR'],
				self.__AnsiColorSet['ERROR_MESSAGE'],
				self.__AnsiColorSet['ERROR_BACKGROUND'],
			], status_message_text, "!!ERROR", message_text, bold, italic, invert, background
		)

	def CRITICAL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = True, italic: bool = False, invert: bool = False, background: bool = True) -> str:
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
				self.__AnsiColorSet['CRITICAL_TIME'],
				self.__AnsiColorSet['CRITICAL_USER'],
				self.__AnsiColorSet['CRITICAL_STATUS'],
				self.__AnsiColorSet['CRITICAL_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_CRITICAL'],
				self.__AnsiColorSet['CRITICAL_MESSAGE'],
				self.__AnsiColorSet['CRITICAL_BACKGROUND'],
			], status_message_text, "!!!@CRITICAL", message_text, bold, italic, invert, background
		)

	def START_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
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
		return self._assemble_entry(
			[
				self.__AnsiColorSet['PROGRESS_TIME'],
				self.__AnsiColorSet['PROGRESS_USER'],
				self.__AnsiColorSet['PROGRESS_STATUS'],
				self.__AnsiColorSet['PROGRESS_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_PROGRESS'],
				self.__AnsiColorSet['PROGRESS_MESSAGE'],
				self.__AnsiColorSet['PROGRESS_BACKGROUND'],
			], status_message_text, "&PROGRESS [****......]", message_text, bold, italic, invert, background
		)
		pass
		# Must run on a thread

	def STOP_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, background: bool = True) -> str:
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

	def SUCCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, background: bool = True) -> str:
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
				self.__AnsiColorSet['SUCCESS_TIME'],
				self.__AnsiColorSet['SUCCESS_USER'],
				self.__AnsiColorSet['SUCCESS_STATUS'],
				self.__AnsiColorSet['SUCCESS_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_SUCCESS'],
				self.__AnsiColorSet['SUCCESS_MESSAGE'],
				self.__AnsiColorSet['SUCCESS_BACKGROUND'],
			], status_message_text, "&SUCCESS", message_text, bold, italic, invert, background
		)

	def FAIL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, background: bool = True) -> str:
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
				self.__AnsiColorSet['FAIL_TIME'],
				self.__AnsiColorSet['FAIL_USER'],
				self.__AnsiColorSet['FAIL_STATUS'],
				self.__AnsiColorSet['FAIL_STATUS_MESSAGE'],
				self.__AnsiColorSet['TYPE_FAIL'],
				self.__AnsiColorSet['FAIL_MESSAGE'],
				self.__AnsiColorSet['FAIL_BACKGROUND'],
			], status_message_text, "&FAIL", message_text, bold, italic, invert, background
		)


# Test
if __name__ == "__main__":
	logger = Logger(program_name="WiretappingScaner")
	print(logger.DEBUG(status_message_text="1", message_text="2"))
	print(logger.DEBUG_PERFORMANCE(status_message_text="3", message_text="4"))
	print(logger.PERFORMANCE(status_message_text="5", message_text="6"))
	print(logger.EVENT(status_message_text="7", message_text="8"))
	print(logger.AUDIT(status_message_text="9", message_text="10"))
	print(logger.METRICS(status_message_text="11", message_text="12"))
	print(logger.USER(status_message_text="13", message_text="14"))
	print(logger.MESSAGE(status_message_text="15", message_text="16"))
	print(logger.INFO(status_message_text="17", message_text="18"))
	print(logger.NOTICE(status_message_text="19", message_text="20"))
	print(logger.WARNING(status_message_text="21", message_text="22"))
	print(logger.ERROR(status_message_text="23", message_text="24"))
	print(logger.CRITICAL(status_message_text="25", message_text="26"))
	print(logger.START_PROCESS(status_message_text="27", message_text="28"))
	print(logger.SUCCESS(status_message_text="29", message_text="30"))
	print(logger.FAIL(status_message_text="31", message_text="32"))
	# print(logger.FAIL(status_message_text="33", message_text="34", invert=True))

	# logger.timeEnabled(False)
	# print(logger.DEBUG(status_message_text="1", message_text="2"))
