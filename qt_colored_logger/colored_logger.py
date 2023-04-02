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
			global_background: bool = False,
			time: bool = True,
			name: bool = True,
			status: bool = True,
			status_message: bool = True,
			status_type: bool = True,
			message: bool = True
	):
		super().__init__(program_name, time, name, status, status_message, status_type, message)
		self.global_background = global_background
		self.__AnsiColorSet: dict = {}
		self._ansi_color_set_init()
		print(self._initial_log())

	def _ansi_color_set_init(self):
		"""
		Sets the colors of the logger.
		"""
		self.__AnsiColorSet['INITIAL_COLOR'] = [AnsiColor('GOLD', "foreground"), AnsiColor('INDIGO', "foreground")]
		self.__AnsiColorSet['INITIAL_BACKGROUND'] = ["", AnsiColor('GOLD', "background")]
		# DEBUG colors
		self.__AnsiColorSet['DEBUG_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['DEBUG_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['DEBUG_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_DEBUG'] = [AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['DEBUG_MESSAGE'] = [AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['DEBUG_BACKGROUND'] = ["", AnsiColor('TAN', "background")]
		# DEBUG_PERFORMANCE colors
		self.__AnsiColorSet['DEBUG_PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_DEBUG_PERFORMANCE'] = [AnsiColor('NAVAJOWHITE', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'] = [AnsiColor('WHEAT', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'] = ["", AnsiColor('WHEAT', "background")]
		# PERFORMANCE colors
		self.__AnsiColorSet['PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_PERFORMANCE'] = [AnsiColor('BLANCHEDALMOND', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['PERFORMANCE_MESSAGE'] = [AnsiColor('BISQUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['PERFORMANCE_BACKGROUND'] = ["", AnsiColor('BISQUE', "background")]
		# EVENT colors
		self.__AnsiColorSet['EVENT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['EVENT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['EVENT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_EVENT'] = [AnsiColor('GREENYELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['EVENT_MESSAGE'] = [AnsiColor('YELLOWGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['EVENT_BACKGROUND'] = ["", AnsiColor('YELLOWGREEN', "background")]
		# AUDIT colors
		self.__AnsiColorSet['AUDIT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['AUDIT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['AUDIT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_AUDIT'] = [AnsiColor('MEDIUMSPRINGGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['AUDIT_MESSAGE'] = [AnsiColor('SPRINGGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['AUDIT_BACKGROUND'] = ["", AnsiColor('SPRINGGREEN', "background")]
		# METRICS colors
		self.__AnsiColorSet['METRICS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['METRICS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['METRICS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_METRICS'] = [AnsiColor('PALEGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['METRICS_MESSAGE'] = [AnsiColor('LIGHTGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['METRICS_BACKGROUND'] = ["", AnsiColor('LIGHTGREEN', "background")]
		# USER colors
		self.__AnsiColorSet['USER_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['USER_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['USER_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_USER'] = [AnsiColor('CHARTREUSE', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['USER_MESSAGE'] = [AnsiColor('LAWNGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['USER_BACKGROUND'] = ["", AnsiColor('LAWNGREEN', "background")]
		# MESSAGE colors
		self.__AnsiColorSet['MESSAGE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['MESSAGE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['MESSAGE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_MESSAGE'] = [AnsiColor('PALETURQUOISE', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['MESSAGE_MESSAGE'] = [AnsiColor('POWDERBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['MESSAGE_BACKGROUND'] = ["", AnsiColor('POWDERBLUE', "background")]
		# INFO colors
		self.__AnsiColorSet['INFO_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['INFO_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['INFO_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_INFO'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['INFO_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['INFO_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
		# NOTICE colors
		self.__AnsiColorSet['NOTICE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['NOTICE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['NOTICE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_NOTICE'] = [AnsiColor('LIGHTBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['NOTICE_MESSAGE'] = [AnsiColor('LIGHTSTEELBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['NOTICE_BACKGROUND'] = ["", AnsiColor('LIGHTSTEELBLUE', "background")]
		# WARNING colors
		self.__AnsiColorSet['WARNING_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self.__AnsiColorSet['WARNING_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['WARNING_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_WARNING'] = [AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['WARNING_MESSAGE'] = [AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['WARNING_BACKGROUND'] = ["", AnsiColor('DARKYELLOW', "background")]
		# ERROR colors
		self.__AnsiColorSet['ERROR_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
		self.__AnsiColorSet['ERROR_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
		self.__AnsiColorSet['ERROR_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
		self.__AnsiColorSet['TYPE_ERROR'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('GAINSBORO', "foreground")]
		self.__AnsiColorSet['ERROR_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTGRAY', "foreground")]
		self.__AnsiColorSet['ERROR_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]
		# CRITICAL colors
		self.__AnsiColorSet['CRITICAL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
		self.__AnsiColorSet['CRITICAL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
		self.__AnsiColorSet['CRITICAL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
		self.__AnsiColorSet['TYPE_CRITICAL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('DARKSALMON', "foreground")]
		self.__AnsiColorSet['CRITICAL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTSALMON', "foreground")]
		self.__AnsiColorSet['CRITICAL_BACKGROUND'] = ["", AnsiColor('MAROON', "background")]
		# PROGRESS colors
		self.__AnsiColorSet['PROGRESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")]
		self.__AnsiColorSet['PROGRESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self.__AnsiColorSet['PROGRESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self.__AnsiColorSet['TYPE_PROGRESS'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
		self.__AnsiColorSet['PROGRESS_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self.__AnsiColorSet['PROGRESS_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
		# SUCCESS colors
		self.__AnsiColorSet['SUCCESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
		self.__AnsiColorSet['SUCCESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
		self.__AnsiColorSet['SUCCESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
		self.__AnsiColorSet['TYPE_SUCCESS'] = [AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
		self.__AnsiColorSet['SUCCESS_MESSAGE'] = [AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
		self.__AnsiColorSet['SUCCESS_BACKGROUND'] = ["", AnsiColor('DARKGREEN', "background")]
		# FAIL colors
		self.__AnsiColorSet['FAIL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
		self.__AnsiColorSet['FAIL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
		self.__AnsiColorSet['FAIL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
		self.__AnsiColorSet['TYPE_FAIL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")]
		self.__AnsiColorSet['FAIL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")]
		self.__AnsiColorSet['FAIL_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]

	def _initial_log(self):
		return self._initial(
			[
				self.__AnsiColorSet['INITIAL_COLOR'][self.global_background],
				self.__AnsiColorSet['INITIAL_BACKGROUND'][self.global_background]
			], self.global_background
		)

	def set_color(self, logger_color_name: str, color_value: list[int, int, int], foreground: bool = True, background: bool = False):
		"""
		A method that sets the ANSI escape code color code in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys: see README.md/Data/"Logger Color Chart".

		todo описать, как работают флаги foreground и background

		:param logger_color_name: Color name in logger color table
		:param color_value: Color value in RGB
		:param foreground: Change foreground text color with/without background?
		:param background: Change background color?
		"""
		if logger_color_name in self.__AnsiColorSet:
			if background and not foreground:
				self.__AnsiColorSet[logger_color_name][1] = Dec2Ansi(color_value, "background")
			elif background and foreground:
				self.__AnsiColorSet[logger_color_name][1] = Dec2Ansi(color_value, "foreground")
			else:
				self.__AnsiColorSet[logger_color_name][0] = Dec2Ansi(color_value, "foreground")
		else:
			raise ColorException("This color is not in the dictionary")

	def DEBUG(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Debugging information logging:
		Can be used to record any information while debugging an application.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['DEBUG_TIME'][background],
				self.__AnsiColorSet['DEBUG_STATUS'][background],
				self.__AnsiColorSet['DEBUG_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_DEBUG'][background],
				self.__AnsiColorSet['DEBUG_MESSAGE'][background],
				self.__AnsiColorSet['DEBUG_BACKGROUND'][background],
			], status_message_text, "%DEBUG", message_text, bold, italic, invert, background
		)

	def DEBUG_PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Performance debugging information logging:
		Can be used to record the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['DEBUG_PERFORMANCE_TIME'][background],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS'][background],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_DEBUG_PERFORMANCE'][background],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'][background],
				self.__AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%DEBUG PERFORMANCE", message_text, bold, italic, invert, background
		)

	def PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Performance information logging:
		Can be used to record the execution time of operations or
		other application performance information.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['PERFORMANCE_TIME'][background],
				self.__AnsiColorSet['PERFORMANCE_STATUS'][background],
				self.__AnsiColorSet['PERFORMANCE_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_PERFORMANCE'][background],
				self.__AnsiColorSet['PERFORMANCE_MESSAGE'][background],
				self.__AnsiColorSet['PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%PERFORMANCE", message_text, bold, italic, invert, background
		)

	def EVENT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Event information logging:
		Can be used to track specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['EVENT_TIME'][background],
				self.__AnsiColorSet['EVENT_STATUS'][background],
				self.__AnsiColorSet['EVENT_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_EVENT'][background],
				self.__AnsiColorSet['EVENT_MESSAGE'][background],
				self.__AnsiColorSet['EVENT_BACKGROUND'][background],
			], status_message_text, "~EVENT", message_text, bold, italic, invert, background
		)

	def AUDIT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Audit information logging:
		Can be used to track changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['AUDIT_TIME'][background],
				self.__AnsiColorSet['AUDIT_STATUS'][background],
				self.__AnsiColorSet['AUDIT_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_AUDIT'][background],
				self.__AnsiColorSet['AUDIT_MESSAGE'][background],
				self.__AnsiColorSet['AUDIT_BACKGROUND'][background],
			], status_message_text, "~AUDIT", message_text, bold, italic, invert, background
		)

	def METRICS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Metrics information logging:
		Can be used to log metrics to track application performance and identify issues.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['METRICS_TIME'][background],
				self.__AnsiColorSet['METRICS_STATUS'][background],
				self.__AnsiColorSet['METRICS_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_METRICS'][background],
				self.__AnsiColorSet['METRICS_MESSAGE'][background],
				self.__AnsiColorSet['METRICS_BACKGROUND'][background],
			], status_message_text, "~METRICS", message_text, bold, italic, invert, background
		)

	def USER(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		User information logging:
		Can be used to add custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['USER_TIME'][background],
				self.__AnsiColorSet['USER_STATUS'][background],
				self.__AnsiColorSet['USER_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_USER'][background],
				self.__AnsiColorSet['USER_MESSAGE'][background],
				self.__AnsiColorSet['USER_BACKGROUND'][background],
			], status_message_text, "~USER", message_text, bold, italic, invert, background
		)

	def MESSAGE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['MESSAGE_TIME'][background],
				self.__AnsiColorSet['MESSAGE_STATUS'][background],
				self.__AnsiColorSet['MESSAGE_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_MESSAGE'][background],
				self.__AnsiColorSet['MESSAGE_MESSAGE'][background],
				self.__AnsiColorSet['MESSAGE_BACKGROUND'][background],
			], status_message_text, "@MESSAGE", message_text, bold, italic, invert, background
		)

	def INFO(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Default information logging:
		Can be used to display messages with specific content about the operation of the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['INFO_TIME'][background],
				self.__AnsiColorSet['INFO_STATUS'][background],
				self.__AnsiColorSet['INFO_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_INFO'][background],
				self.__AnsiColorSet['INFO_MESSAGE'][background],
				self.__AnsiColorSet['INFO_BACKGROUND'][background],
			], status_message_text, "@INFO", message_text, bold, italic, invert, background
		)

	def NOTICE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None) -> str:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_entry(
			[
				self.__AnsiColorSet['NOTICE_TIME'][background],
				self.__AnsiColorSet['NOTICE_STATUS'][background],
				self.__AnsiColorSet['NOTICE_STATUS_MESSAGE'][background],
				self.__AnsiColorSet['TYPE_NOTICE'][background],
				self.__AnsiColorSet['NOTICE_MESSAGE'][background],
				self.__AnsiColorSet['NOTICE_BACKGROUND'][background],
			], status_message_text, "@NOTICE", message_text, bold, italic, invert, background
		)

	def WARNING(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True) -> str:
		"""
		Warning information logging:
		Can be used to display warnings that the program may work with unpredictable results.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				self.__AnsiColorSet['WARNING_TIME'][1 if local_background else 0],
				self.__AnsiColorSet['WARNING_STATUS'][1 if local_background else 0],
				self.__AnsiColorSet['WARNING_STATUS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['TYPE_WARNING'][1 if local_background else 0],
				self.__AnsiColorSet['WARNING_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['WARNING_BACKGROUND'][1 if local_background else 0],
			], status_message_text, "!WARNING", message_text, bold, italic, invert, local_background
		)

	def ERROR(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True) -> str:
		"""
		Error information logging:
		Used to display errors and crashes in the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				self.__AnsiColorSet['ERROR_TIME'][1 if local_background else 0],
				self.__AnsiColorSet['ERROR_STATUS'][1 if local_background else 0],
				self.__AnsiColorSet['ERROR_STATUS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['TYPE_ERROR'][1 if local_background else 0],
				self.__AnsiColorSet['ERROR_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['ERROR_BACKGROUND'][1 if local_background else 0],
			], status_message_text, "!!ERROR", message_text, bold, italic, invert, local_background
		)

	def CRITICAL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = True, italic: bool = False, invert: bool = False, local_background: bool = True) -> str:
		"""
		Critical error information logging:
		Used to display critical and unpredictable program failures.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				self.__AnsiColorSet['CRITICAL_TIME'][1 if local_background else 0],
				self.__AnsiColorSet['CRITICAL_STATUS'][1 if local_background else 0],
				self.__AnsiColorSet['CRITICAL_STATUS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['TYPE_CRITICAL'][1 if local_background else 0],
				self.__AnsiColorSet['CRITICAL_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['CRITICAL_BACKGROUND'][1 if local_background else 0],
			], status_message_text, "!!!@CRITICAL", message_text, bold, italic, invert, local_background
		)

	def START_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				self.__AnsiColorSet['PROGRESS_TIME'][1 if local_background else 0],
				self.__AnsiColorSet['PROGRESS_STATUS'][1 if local_background else 0],
				self.__AnsiColorSet['PROGRESS_STATUS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['TYPE_PROGRESS'][1 if local_background else 0],
				self.__AnsiColorSet['PROGRESS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['PROGRESS_BACKGROUND'][1 if local_background else 0],
			], status_message_text, "&PROGRESS [*******.............] - 37%", message_text, bold, italic, invert, local_background
		)
		pass
		# Must run on a thread

	def STOP_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		pass
		# Make transition to SUCCESS or FAIL

	def SUCCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, local_background: bool = True) -> str:
		"""
		Success information logging:
		Used to display a message about the success of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				self.__AnsiColorSet['SUCCESS_TIME'][1 if local_background else 0],
				self.__AnsiColorSet['SUCCESS_STATUS'][1 if local_background else 0],
				self.__AnsiColorSet['SUCCESS_STATUS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['TYPE_SUCCESS'][1 if local_background else 0],
				self.__AnsiColorSet['SUCCESS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['SUCCESS_BACKGROUND'][1 if local_background else 0],
			], status_message_text, "&SUCCESS", message_text, bold, italic, invert, local_background
		)

	def FAIL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, local_background: bool = True) -> str:
		"""
		Fail information logging:
		Used to display a message about the failed execution of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param invert: Display log in invert font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_entry(
			[
				self.__AnsiColorSet['FAIL_TIME'][1 if local_background else 0],
				self.__AnsiColorSet['FAIL_STATUS'][1 if local_background else 0],
				self.__AnsiColorSet['FAIL_STATUS_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['TYPE_FAIL'][1 if local_background else 0],
				self.__AnsiColorSet['FAIL_MESSAGE'][1 if local_background else 0],
				self.__AnsiColorSet['FAIL_BACKGROUND'][1 if local_background else 0],
			], status_message_text, "&FAIL", message_text, bold, italic, invert, local_background
		)


# Test
if __name__ == "__main__":
	logger = Logger(program_name="WiretappingScaner", global_background=False)
	print(logger.DEBUG(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message", local_background=False))
	print(logger.DEBUG_PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.EVENT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.AUDIT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.METRICS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.USER(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.MESSAGE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.INFO(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.NOTICE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.WARNING(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.ERROR(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.CRITICAL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.START_PROCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.SUCCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.FAIL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	# print(logger.FAIL(status_message_text="33", message_text="34", invert=True))

	# logger.timeEnabled(False)
	# print(logger.DEBUG(status_message_text="1", message_text="2"))
