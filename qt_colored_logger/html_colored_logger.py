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
from qt_colored_logger.src import HexColor, Dec2Hex

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

	def __init__(
			self,
			*,
			program_name: str = "Unknown",
			global_background: bool = False,
			time: bool = True,
			status: bool = True,
			status_message: bool = True,
			status_type: bool = True,
			message: bool = True
	):
		super().__init__(program_name, time, status, status_message, status_type, message)
		self._HtmlColorSet: dict = {}
		self._html_color_set_init()
		self.global_background = global_background
		# print(self._initial_log())

	def _html_color_set_init(self):
		"""
		Sets the colors of the logger.
		"""
		self._HtmlColorSet['INITIAL_COLOR'] = [HexColor('GOLD'), HexColor('INDIGO')]
		self._HtmlColorSet['INITIAL_BACKGROUND'] = ["", HexColor('GOLD')]
		# DEBUG colors
		self._HtmlColorSet['DEBUG_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['DEBUG_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['DEBUG_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_DEBUG'] = [HexColor('BURLYWOOD'), HexColor('NAVY')]
		self._HtmlColorSet['DEBUG_MESSAGE'] = [HexColor('TAN'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['DEBUG_BACKGROUND'] = ["", HexColor('TAN')]
		# DEBUG_PERFORMANCE colors
		self._HtmlColorSet['DEBUG_PERFORMANCE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['DEBUG_PERFORMANCE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_DEBUG_PERFORMANCE'] = [HexColor('NAVAJOWHITE'), HexColor('NAVY')]
		self._HtmlColorSet['DEBUG_PERFORMANCE_MESSAGE'] = [HexColor('WHEAT'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['DEBUG_PERFORMANCE_BACKGROUND'] = ["", HexColor('WHEAT')]
		# PERFORMANCE colors
		self._HtmlColorSet['PERFORMANCE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['PERFORMANCE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['PERFORMANCE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_PERFORMANCE'] = [HexColor('BLANCHEDALMOND'), HexColor('NAVY')]
		self._HtmlColorSet['PERFORMANCE_MESSAGE'] = [HexColor('BISQUE'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['PERFORMANCE_BACKGROUND'] = ["", HexColor('BISQUE')]
		# EVENT colors
		self._HtmlColorSet['EVENT_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['EVENT_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['EVENT_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_EVENT'] = [HexColor('GREENYELLOW'), HexColor('NAVY')]
		self._HtmlColorSet['EVENT_MESSAGE'] = [HexColor('YELLOWGREEN'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['EVENT_BACKGROUND'] = ["", HexColor('YELLOWGREEN')]
		# AUDIT colors
		self._HtmlColorSet['AUDIT_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['AUDIT_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['AUDIT_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_AUDIT'] = [HexColor('MEDIUMSPRINGGREEN'), HexColor('NAVY')]
		self._HtmlColorSet['AUDIT_MESSAGE'] = [HexColor('SPRINGGREEN'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['AUDIT_BACKGROUND'] = ["", HexColor('SPRINGGREEN')]
		# METRICS colors
		self._HtmlColorSet['METRICS_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['METRICS_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['METRICS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_METRICS'] = [HexColor('PALEGREEN'), HexColor('NAVY')]
		self._HtmlColorSet['METRICS_MESSAGE'] = [HexColor('LIGHTGREEN'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['METRICS_BACKGROUND'] = ["", HexColor('LIGHTGREEN')]
		# USER colors
		self._HtmlColorSet['USER_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['USER_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['USER_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_USER'] = [HexColor('CHARTREUSE'), HexColor('NAVY')]
		self._HtmlColorSet['USER_MESSAGE'] = [HexColor('LAWNGREEN'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['USER_BACKGROUND'] = ["", HexColor('LAWNGREEN')]
		# MESSAGE colors
		self._HtmlColorSet['MESSAGE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['MESSAGE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['MESSAGE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_MESSAGE'] = [HexColor('PALETURQUOISE'), HexColor('NAVY')]
		self._HtmlColorSet['MESSAGE_MESSAGE'] = [HexColor('POWDERBLUE'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['MESSAGE_BACKGROUND'] = ["", HexColor('POWDERBLUE')]
		# INFO colors
		self._HtmlColorSet['INFO_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['INFO_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['INFO_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_INFO'] = [HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
		self._HtmlColorSet['INFO_MESSAGE'] = [HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['INFO_BACKGROUND'] = ["", HexColor('SKYBLUE')]
		# NOTICE colors
		self._HtmlColorSet['NOTICE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['NOTICE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['NOTICE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_NOTICE'] = [HexColor('LIGHTBLUE'), HexColor('NAVY')]
		self._HtmlColorSet['NOTICE_MESSAGE'] = [HexColor('LIGHTSTEELBLUE'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['NOTICE_BACKGROUND'] = ["", HexColor('LIGHTSTEELBLUE')]
		# WARNING colors
		self._HtmlColorSet['WARNING_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._HtmlColorSet['WARNING_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['WARNING_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_WARNING'] = [HexColor('YELLOW'), HexColor('NAVY')]
		self._HtmlColorSet['WARNING_MESSAGE'] = [HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['WARNING_BACKGROUND'] = ["", HexColor('DARKYELLOW')]
		# ERROR colors
		self._HtmlColorSet['ERROR_TIME'] = [HexColor('ORCHID'), HexColor('PLUM')]
		self._HtmlColorSet['ERROR_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
		self._HtmlColorSet['ERROR_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
		self._HtmlColorSet['TYPE_ERROR'] = [HexColor('FIREBRICK'), HexColor('GAINSBORO')]
		self._HtmlColorSet['ERROR_MESSAGE'] = [HexColor('DARKRED'), HexColor('LIGHTGRAY')]
		self._HtmlColorSet['ERROR_BACKGROUND'] = ["", HexColor('DARKRED')]
		# CRITICAL colors
		self._HtmlColorSet['CRITICAL_TIME'] = [HexColor('ORCHID'), HexColor('PLUM')]
		self._HtmlColorSet['CRITICAL_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
		self._HtmlColorSet['CRITICAL_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
		self._HtmlColorSet['TYPE_CRITICAL'] = [HexColor('FIREBRICK'), HexColor('DARKSALMON')]
		self._HtmlColorSet['CRITICAL_MESSAGE'] = [HexColor('DARKRED'), HexColor('LIGHTSALMON')]
		self._HtmlColorSet['CRITICAL_BACKGROUND'] = ["", HexColor('MAROON')]
		# PROGRESS colors
		self._HtmlColorSet['PROGRESS_TIME'] = [HexColor('ORCHID'), HexColor('PURPLE')]
		self._HtmlColorSet['PROGRESS_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._HtmlColorSet['PROGRESS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._HtmlColorSet['TYPE_PROGRESS'] = [HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
		self._HtmlColorSet['PROGRESS_MESSAGE'] = [HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
		self._HtmlColorSet['PROGRESS_BACKGROUND'] = ["", HexColor('SKYBLUE')]
		# SUCCESS colors
		self._HtmlColorSet['SUCCESS_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		self._HtmlColorSet['SUCCESS_STATUS'] = [HexColor('ORANGE'), HexColor('CHARTREUSE')]
		self._HtmlColorSet['SUCCESS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
		self._HtmlColorSet['TYPE_SUCCESS'] = [HexColor('GREEN'), HexColor('PALEGREEN')]
		self._HtmlColorSet['SUCCESS_MESSAGE'] = [HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
		self._HtmlColorSet['SUCCESS_BACKGROUND'] = ["", HexColor('DARKGREEN')]
		# FAIL colors
		self._HtmlColorSet['FAIL_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		self._HtmlColorSet['FAIL_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
		self._HtmlColorSet['FAIL_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
		self._HtmlColorSet['TYPE_FAIL'] = [HexColor('FIREBRICK'), HexColor('YELLOW')]
		self._HtmlColorSet['FAIL_MESSAGE'] = [HexColor('DARKRED'), HexColor('DARKYELLOW')]
		self._HtmlColorSet['FAIL_BACKGROUND'] = ["", HexColor('DARKRED')]

	def _initial_log(self):
		return self._html_initial(
			[
				self._HtmlColorSet['INITIAL_COLOR'][self.global_background],
				self._HtmlColorSet['INITIAL_BACKGROUND'][self.global_background]
			]
		)

	def setHexColor(self, *, logger_color_name: str, hex_color_value: str, foreground: bool = True, background: bool = False):
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

		A method that sets the ANSI escape code color code in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys: see README.md/Data/"Logger Color Chart".

		todo описать, как работают флаги foreground и background

		:param logger_color_name: Color name in logger color table
		:param hex_color_value: Hexadecimal color value in logger color table
		:param foreground: Change foreground text color with/without background?
		:param background: Change background color?
		"""
		if logger_color_name in _HtmlColorSet:
			if background and not foreground:
				self._HtmlColorSet[logger_color_name][1] = hex_color_value
			elif background and foreground:
				self._HtmlColorSet[logger_color_name][1] = hex_color_value
			else:
				self._HtmlColorSet[logger_color_name][0] = hex_color_value
		else:
			raise ColorException("This color is not in the dictionary")

	def set_color(self, *, logger_color_name: str, color_value: list[int, int, int], foreground: bool = True, background: bool = False):
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
		if logger_color_name in self._HtmlColorSet:
			if background and not foreground:
				self._HtmlColorSet[logger_color_name][1] = Dec2Hex(color_value)
			elif background and foreground:
				self._HtmlColorSet[logger_color_name][1] = Dec2Hex(color_value)
			else:
				self._HtmlColorSet[logger_color_name][0] = Dec2Hex(color_value)
		else:
			raise ColorException("This color is not in the dictionary")

	def DEBUG(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Debugging information logging:
		Can be used to record any information while debugging an application.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['DEBUG_TIME'][background],
				self._HtmlColorSet['DEBUG_STATUS'][background],
				self._HtmlColorSet['DEBUG_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_DEBUG'][background],
				self._HtmlColorSet['DEBUG_MESSAGE'][background],
				self._HtmlColorSet['DEBUG_BACKGROUND'][background],
			], status_message_text, "%DEBUG", message_text, bold, italic
		)

	def DEBUG_PERFORMANCE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Performance debugging information logging:
		Can be used to record the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['DEBUG_PERFORMANCE_TIME'][background],
				self._HtmlColorSet['DEBUG_PERFORMANCE_STATUS'][background],
				self._HtmlColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_DEBUG_PERFORMANCE'][background],
				self._HtmlColorSet['DEBUG_PERFORMANCE_MESSAGE'][background],
				self._HtmlColorSet['DEBUG_PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%DEBUG PERFORMANCE", message_text, bold, italic
		)

	def PERFORMANCE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Performance information logging:
		Can be used to record the execution time of operations or
		other application performance information.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['PERFORMANCE_TIME'][background],
				self._HtmlColorSet['PERFORMANCE_STATUS'][background],
				self._HtmlColorSet['PERFORMANCE_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_PERFORMANCE'][background],
				self._HtmlColorSet['PERFORMANCE_MESSAGE'][background],
				self._HtmlColorSet['PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%PERFORMANCE", message_text, bold, italic
		)

	def EVENT(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Event information logging:
		Can be used to track specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['EVENT_TIME'][background],
				self._HtmlColorSet['EVENT_STATUS'][background],
				self._HtmlColorSet['EVENT_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_EVENT'][background],
				self._HtmlColorSet['EVENT_MESSAGE'][background],
				self._HtmlColorSet['EVENT_BACKGROUND'][background],
			], status_message_text, "~EVENT", message_text, bold, italic
		)

	def AUDIT(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Audit information logging:
		Can be used to track changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['AUDIT_TIME'][background],
				self._HtmlColorSet['AUDIT_STATUS'][background],
				self._HtmlColorSet['AUDIT_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_AUDIT'][background],
				self._HtmlColorSet['AUDIT_MESSAGE'][background],
				self._HtmlColorSet['AUDIT_BACKGROUND'][background],
			], status_message_text, "~AUDIT", message_text, bold, italic
		)

	def METRICS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Metrics information logging:
		Can be used to log metrics to track application performance and identify issues.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['METRICS_TIME'][background],
				self._HtmlColorSet['METRICS_STATUS'][background],
				self._HtmlColorSet['METRICS_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_METRICS'][background],
				self._HtmlColorSet['METRICS_MESSAGE'][background],
				self._HtmlColorSet['METRICS_BACKGROUND'][background],
			], status_message_text, "~METRICS", message_text, bold, italic
		)

	def USER(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		User information logging:
		Can be used to add custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['USER_TIME'][background],
				self._HtmlColorSet['USER_STATUS'][background],
				self._HtmlColorSet['USER_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_USER'][background],
				self._HtmlColorSet['USER_MESSAGE'][background],
				self._HtmlColorSet['USER_BACKGROUND'][background],
			], status_message_text, "~USER", message_text, bold, italic
		)

	def MESSAGE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['MESSAGE_TIME'][background],
				self._HtmlColorSet['MESSAGE_STATUS'][background],
				self._HtmlColorSet['MESSAGE_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_MESSAGE'][background],
				self._HtmlColorSet['MESSAGE_MESSAGE'][background],
				self._HtmlColorSet['MESSAGE_BACKGROUND'][background],
			], status_message_text, "@MESSAGE", message_text, bold, italic
		)

	def INFO(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Default information logging:
		Can be used to display messages with specific content about the operation of the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['INFO_TIME'][background],
				self._HtmlColorSet['INFO_STATUS'][background],
				self._HtmlColorSet['INFO_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_INFO'][background],
				self._HtmlColorSet['INFO_MESSAGE'][background],
				self._HtmlColorSet['INFO_BACKGROUND'][background],
			], status_message_text, "@INFO", message_text, bold, italic
		)

	def NOTICE(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = None) -> str:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		background = local_background if local_background is not None else self.global_background
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['NOTICE_TIME'][background],
				self._HtmlColorSet['NOTICE_STATUS'][background],
				self._HtmlColorSet['NOTICE_STATUS_MESSAGE'][background],
				self._HtmlColorSet['TYPE_NOTICE'][background],
				self._HtmlColorSet['NOTICE_MESSAGE'][background],
				self._HtmlColorSet['NOTICE_BACKGROUND'][background],
			], status_message_text, "@NOTICE", message_text, bold, italic
		)

	def WARNING(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = True) -> str:
		"""
		Warning information logging:
		Can be used to display warnings that the program may work with unpredictable results.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['WARNING_TIME'][local_background],
				self._HtmlColorSet['WARNING_STATUS'][local_background],
				self._HtmlColorSet['WARNING_STATUS_MESSAGE'][local_background],
				self._HtmlColorSet['TYPE_WARNING'][local_background],
				self._HtmlColorSet['WARNING_MESSAGE'][local_background],
				self._HtmlColorSet['WARNING_BACKGROUND'][local_background],
			], status_message_text, "!WARNING", message_text, bold, italic
		)

	def ERROR(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = True) -> str:
		"""
		Error information logging:
		Used to display errors and crashes in the program.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['ERROR_TIME'][local_background],
				self._HtmlColorSet['ERROR_STATUS'][local_background],
				self._HtmlColorSet['ERROR_STATUS_MESSAGE'][local_background],
				self._HtmlColorSet['TYPE_ERROR'][local_background],
				self._HtmlColorSet['ERROR_MESSAGE'][local_background],
				self._HtmlColorSet['ERROR_BACKGROUND'][local_background],
			], status_message_text, "!!ERROR", message_text, bold, italic
		)

	def CRITICAL(self, status_message_text: str = "...", message_text: str = "...", bold: bool = True, italic: bool = False, local_background: bool = True) -> str:
		"""
		Critical error information logging:
		Used to display critical and unpredictable program failures.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['CRITICAL_TIME'][local_background],
				self._HtmlColorSet['CRITICAL_STATUS'][local_background],
				self._HtmlColorSet['CRITICAL_STATUS_MESSAGE'][local_background],
				self._HtmlColorSet['TYPE_CRITICAL'][local_background],
				self._HtmlColorSet['CRITICAL_MESSAGE'][local_background],
				self._HtmlColorSet['CRITICAL_BACKGROUND'][local_background],
			], status_message_text, "!!!@CRITICAL", message_text, bold, italic
		)

	def START_PROCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = True) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['PROGRESS_TIME'][local_background],
				self._HtmlColorSet['PROGRESS_STATUS'][local_background],
				self._HtmlColorSet['PROGRESS_STATUS_MESSAGE'][local_background],
				self._HtmlColorSet['TYPE_PROGRESS'][local_background],
				self._HtmlColorSet['PROGRESS_MESSAGE'][local_background],
				self._HtmlColorSet['PROGRESS_BACKGROUND'][local_background],
			], status_message_text, "&PROGRESS [*******.............] - 37%", message_text, bold, italic
		)
		pass
		# Must run on a thread

	def STOP_PROCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, local_background: bool = True) -> str:
		"""
		Stub.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		pass
		# Make transition to SUCCESS or FAIL

	def SUCCESS(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, local_background: bool = True) -> str:
		"""
		Success information logging:
		Used to display a message about the success of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['SUCCESS_TIME'][local_background],
				self._HtmlColorSet['SUCCESS_STATUS'][local_background],
				self._HtmlColorSet['SUCCESS_STATUS_MESSAGE'][local_background],
				self._HtmlColorSet['TYPE_SUCCESS'][local_background],
				self._HtmlColorSet['SUCCESS_MESSAGE'][local_background],
				self._HtmlColorSet['SUCCESS_BACKGROUND'][local_background],
			], status_message_text, "&SUCCESS", message_text, bold, italic
		)

	def FAIL(self, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, local_background: bool = True) -> str:
		"""
		Fail information logging:
		Used to display a message about the failed execution of the process.

		:param status_message_text: Log status message
		:param message_text: Log message
		:param bold: Display log in bold font?
		:param italic: Display log in italic font?
		:param local_background: Display log with background?
		:return: the generated log string
		"""
		return self._assemble_html_entry(
			[
				self._HtmlColorSet['FAIL_TIME'][local_background],
				self._HtmlColorSet['FAIL_STATUS'][local_background],
				self._HtmlColorSet['FAIL_STATUS_MESSAGE'][local_background],
				self._HtmlColorSet['TYPE_FAIL'][local_background],
				self._HtmlColorSet['FAIL_MESSAGE'][local_background],
				self._HtmlColorSet['FAIL_BACKGROUND'][local_background],
			], status_message_text, "&FAIL", message_text, bold, italic
		)


# Test
if __name__ == "__main__":
	logger = LoggerQ(program_name="WiretappingScaner")
	print(logger._initial_log())
	print(logger.DEBUG(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.DEBUG_PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.EVENT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	logger.global_background = True
	print(logger.AUDIT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.METRICS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	logger.time = False
	print(logger.USER(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.MESSAGE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	logger.status_type = False
	print(logger.INFO(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.NOTICE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.WARNING(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.ERROR(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.CRITICAL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.START_PROCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.SUCCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.FAIL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	# print(logger.FAIL(status_message_text="33", message_text="34", invert=True))

	# logger2 = LoggerQ()
	# print(logger.ID)
	# print(logger2.ID)
	# logger.ID = 10
	# print(logger.ID)
	# print(logger2.ID)

	# print(logger.DEBUG(message_text="Debug data"))
	# print(logger.DEBUG(message_text="Debug data", bold=True))
	# print(logger.DEBUG(message_text="Debug data", italic=True))
	# print(logger.DEBUG(message_text="Debug data", bold=True, italic=True))
	#
	# print(logger.NOTICE(message_text="Debug data"))
	# mod.setColor("NOTICE_MESSAGE", 127, 255, 0)
	# print(logger.NOTICE(message_text="Debug data"))
