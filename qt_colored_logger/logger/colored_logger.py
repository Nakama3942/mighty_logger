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

from qt_colored_logger._basic import _Singleton, _BasicLogger, ColorException, CombinationException
from qt_colored_logger.src import AnsiColor, Dec2Ansi
from qt_colored_logger.text import TextBuffer

class Logger(_Singleton, _BasicLogger):
	"""
	The Logger class is a class that implements the functionality
	of logging the work of software in different directions.\n
	It has a color output of information, settings for the operation of the log.
	Only one class object can be created!!!\n
	Implements the output of the following information:\n
	1) Record creation time;
	2) Record status;
	3) Recording status message;
	4) Record type;
	5) Write message.
	\nImplements the output of the following types of records:\n
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
			text_buffer: TextBuffer = TextBuffer(),
			global_background: bool = False,
			time: bool = True,
			status: bool = True,
			status_message: bool = True,
			status_type: bool = True,
			message: bool = True
	):
		super().__init__(program_name, time, status, status_message, status_type, message)
		self._buffer = text_buffer
		self._AnsiColorSet: dict = {}
		self._ansi_color_set_init()
		self.global_background = global_background
		self._initial_log()

	def _ansi_color_set_init(self):
		"""
		Sets the colors of the logger.
		"""
		self._AnsiColorSet['INITIAL_COLOR'] = [AnsiColor('GOLD', "foreground"), AnsiColor('INDIGO', "foreground")]
		self._AnsiColorSet['INITIAL_BACKGROUND'] = ["", AnsiColor('GOLD', "background")]
		# DEBUG colors
		self._AnsiColorSet['DEBUG_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['DEBUG_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['DEBUG_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_DEBUG'] = [AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['DEBUG_MESSAGE'] = [AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['DEBUG_BACKGROUND'] = ["", AnsiColor('TAN', "background")]
		# DEBUG_PERFORMANCE colors
		self._AnsiColorSet['DEBUG_PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['DEBUG_PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_DEBUG_PERFORMANCE'] = [AnsiColor('NAVAJOWHITE', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'] = [AnsiColor('WHEAT', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'] = ["", AnsiColor('WHEAT', "background")]
		# PERFORMANCE colors
		self._AnsiColorSet['PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_PERFORMANCE'] = [AnsiColor('BLANCHEDALMOND', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['PERFORMANCE_MESSAGE'] = [AnsiColor('BISQUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['PERFORMANCE_BACKGROUND'] = ["", AnsiColor('BISQUE', "background")]
		# EVENT colors
		self._AnsiColorSet['EVENT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['EVENT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['EVENT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_EVENT'] = [AnsiColor('GREENYELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['EVENT_MESSAGE'] = [AnsiColor('YELLOWGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['EVENT_BACKGROUND'] = ["", AnsiColor('YELLOWGREEN', "background")]
		# AUDIT colors
		self._AnsiColorSet['AUDIT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['AUDIT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['AUDIT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_AUDIT'] = [AnsiColor('MEDIUMSPRINGGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['AUDIT_MESSAGE'] = [AnsiColor('SPRINGGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['AUDIT_BACKGROUND'] = ["", AnsiColor('SPRINGGREEN', "background")]
		# METRICS colors
		self._AnsiColorSet['METRICS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['METRICS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['METRICS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_METRICS'] = [AnsiColor('PALEGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['METRICS_MESSAGE'] = [AnsiColor('LIGHTGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['METRICS_BACKGROUND'] = ["", AnsiColor('LIGHTGREEN', "background")]
		# USER colors
		self._AnsiColorSet['USER_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['USER_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['USER_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_USER'] = [AnsiColor('CHARTREUSE', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['USER_MESSAGE'] = [AnsiColor('LAWNGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['USER_BACKGROUND'] = ["", AnsiColor('LAWNGREEN', "background")]
		# MESSAGE colors
		self._AnsiColorSet['MESSAGE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['MESSAGE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['MESSAGE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_MESSAGE'] = [AnsiColor('PALETURQUOISE', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['MESSAGE_MESSAGE'] = [AnsiColor('POWDERBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['MESSAGE_BACKGROUND'] = ["", AnsiColor('POWDERBLUE', "background")]
		# INFO colors
		self._AnsiColorSet['INFO_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['INFO_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['INFO_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_INFO'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['INFO_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['INFO_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
		# NOTICE colors
		self._AnsiColorSet['NOTICE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['NOTICE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['NOTICE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_NOTICE'] = [AnsiColor('LIGHTBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['NOTICE_MESSAGE'] = [AnsiColor('LIGHTSTEELBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['NOTICE_BACKGROUND'] = ["", AnsiColor('LIGHTSTEELBLUE', "background")]
		# WARNING colors
		self._AnsiColorSet['WARNING_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['WARNING_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['WARNING_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_WARNING'] = [AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['WARNING_MESSAGE'] = [AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['WARNING_BACKGROUND'] = ["", AnsiColor('DARKYELLOW', "background")]
		# ERROR colors
		self._AnsiColorSet['ERROR_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
		self._AnsiColorSet['ERROR_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
		self._AnsiColorSet['ERROR_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
		self._AnsiColorSet['TYPE_ERROR'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('GAINSBORO', "foreground")]
		self._AnsiColorSet['ERROR_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTGRAY', "foreground")]
		self._AnsiColorSet['ERROR_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]
		# CRITICAL colors
		self._AnsiColorSet['CRITICAL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
		self._AnsiColorSet['CRITICAL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
		self._AnsiColorSet['CRITICAL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
		self._AnsiColorSet['TYPE_CRITICAL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('DARKSALMON', "foreground")]
		self._AnsiColorSet['CRITICAL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTSALMON', "foreground")]
		self._AnsiColorSet['CRITICAL_BACKGROUND'] = ["", AnsiColor('MAROON', "background")]
		# PROGRESS colors
		self._AnsiColorSet['PROGRESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")]
		self._AnsiColorSet['PROGRESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['PROGRESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_PROGRESS'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['PROGRESS_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['PROGRESS_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
		# SUCCESS colors
		self._AnsiColorSet['SUCCESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
		self._AnsiColorSet['SUCCESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
		self._AnsiColorSet['SUCCESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
		self._AnsiColorSet['TYPE_SUCCESS'] = [AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
		self._AnsiColorSet['SUCCESS_MESSAGE'] = [AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
		self._AnsiColorSet['SUCCESS_BACKGROUND'] = ["", AnsiColor('DARKGREEN', "background")]
		# FAIL colors
		self._AnsiColorSet['FAIL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
		self._AnsiColorSet['FAIL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
		self._AnsiColorSet['FAIL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
		self._AnsiColorSet['TYPE_FAIL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")]
		self._AnsiColorSet['FAIL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")]
		self._AnsiColorSet['FAIL_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]

	def _initial_log(self):
		"""
		Displays initialized information.
		"""
		self._buffer.append(self._initialized_data(
			[
				self._AnsiColorSet['INITIAL_COLOR'][self.global_background],
				self._AnsiColorSet['INITIAL_BACKGROUND'][self.global_background]
			]
		))
		self._buffer.update_console()

	def set_color(self, *, logger_color_name: str, color_value: list[int, int, int], foreground: bool = True, background: bool = False):
		"""
		A method that sets the ANSI escape code color code in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys: see README.md/Data/"Logger Color Chart".\n
		Boolean flags: If foreground is set to True, then the color of the foreground text will change
		with/without a background (it all depends on the background flag). If in this case background
		is set to False (the standard combination of arguments) - then the color of the specifically
		front text that is displayed without a background changes, otherwise it changes the color
		of the specifically front text that is displayed with a background. If the foreground is set
		to False with background set to True, the background itself will change. The last combination,
		when both arguments are False, is an impossible combination that throws a CombinationException.

		:param logger_color_name: Color name in logger color table
		:param color_value: Color value in RGB
		:param foreground: Change foreground text color with/without background?
		:param background: Change background color?
		"""
		if logger_color_name in self._AnsiColorSet:
			if background and not foreground:
				self._AnsiColorSet[logger_color_name][1] = Dec2Ansi(color_value, "background")
			elif background and foreground:
				self._AnsiColorSet[logger_color_name][1] = Dec2Ansi(color_value, "foreground")
			elif not background and foreground:
				self._AnsiColorSet[logger_color_name][0] = Dec2Ansi(color_value, "foreground")
			else:
				raise CombinationException("False-False combination of foreground-background flags not possible")
		else:
			raise ColorException("This color is not in the dictionary")

	def DEBUG(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Debugging information logging:
		Can be used to log entry any information while debugging an application.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['DEBUG_TIME'][background],
				self._AnsiColorSet['DEBUG_STATUS'][background],
				self._AnsiColorSet['DEBUG_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_DEBUG'][background],
				self._AnsiColorSet['DEBUG_MESSAGE'][background],
				self._AnsiColorSet['DEBUG_BACKGROUND'][background],
			], status_message_text, "%DEBUG", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def DEBUG_PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Performance debugging information logging:
		Can be used to log entry the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['DEBUG_PERFORMANCE_TIME'][background],
				self._AnsiColorSet['DEBUG_PERFORMANCE_STATUS'][background],
				self._AnsiColorSet['DEBUG_PERFORMANCE_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_DEBUG_PERFORMANCE'][background],
				self._AnsiColorSet['DEBUG_PERFORMANCE_MESSAGE'][background],
				self._AnsiColorSet['DEBUG_PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%DEBUG PERFORMANCE", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Performance information logging:
		Can be used to log entry the execution time of operations or
		other application performance information.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['PERFORMANCE_TIME'][background],
				self._AnsiColorSet['PERFORMANCE_STATUS'][background],
				self._AnsiColorSet['PERFORMANCE_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_PERFORMANCE'][background],
				self._AnsiColorSet['PERFORMANCE_MESSAGE'][background],
				self._AnsiColorSet['PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%PERFORMANCE", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def EVENT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Event information logging:
		Can be used to log entry specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['EVENT_TIME'][background],
				self._AnsiColorSet['EVENT_STATUS'][background],
				self._AnsiColorSet['EVENT_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_EVENT'][background],
				self._AnsiColorSet['EVENT_MESSAGE'][background],
				self._AnsiColorSet['EVENT_BACKGROUND'][background],
			], status_message_text, "~EVENT", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def AUDIT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Audit information logging:
		Can be used to log entry changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['AUDIT_TIME'][background],
				self._AnsiColorSet['AUDIT_STATUS'][background],
				self._AnsiColorSet['AUDIT_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_AUDIT'][background],
				self._AnsiColorSet['AUDIT_MESSAGE'][background],
				self._AnsiColorSet['AUDIT_BACKGROUND'][background],
			], status_message_text, "~AUDIT", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def METRICS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Metrics information logging:
		Can be used to log entry metrics to track application performance and identify issues.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['METRICS_TIME'][background],
				self._AnsiColorSet['METRICS_STATUS'][background],
				self._AnsiColorSet['METRICS_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_METRICS'][background],
				self._AnsiColorSet['METRICS_MESSAGE'][background],
				self._AnsiColorSet['METRICS_BACKGROUND'][background],
			], status_message_text, "~METRICS", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def USER(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		User information logging:
		Can be used to log entry custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['USER_TIME'][background],
				self._AnsiColorSet['USER_STATUS'][background],
				self._AnsiColorSet['USER_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_USER'][background],
				self._AnsiColorSet['USER_MESSAGE'][background],
				self._AnsiColorSet['USER_BACKGROUND'][background],
			], status_message_text, "~USER", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def MESSAGE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['MESSAGE_TIME'][background],
				self._AnsiColorSet['MESSAGE_STATUS'][background],
				self._AnsiColorSet['MESSAGE_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_MESSAGE'][background],
				self._AnsiColorSet['MESSAGE_MESSAGE'][background],
				self._AnsiColorSet['MESSAGE_BACKGROUND'][background],
			], status_message_text, "@MESSAGE", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def INFO(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Default information logging:
		Can be used to log entry messages with specific content about the operation of the program.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['INFO_TIME'][background],
				self._AnsiColorSet['INFO_STATUS'][background],
				self._AnsiColorSet['INFO_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_INFO'][background],
				self._AnsiColorSet['INFO_MESSAGE'][background],
				self._AnsiColorSet['INFO_BACKGROUND'][background],
			], status_message_text, "@INFO", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def NOTICE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['NOTICE_TIME'][background],
				self._AnsiColorSet['NOTICE_STATUS'][background],
				self._AnsiColorSet['NOTICE_STATUS_MESSAGE'][background],
				self._AnsiColorSet['TYPE_NOTICE'][background],
				self._AnsiColorSet['NOTICE_MESSAGE'][background],
				self._AnsiColorSet['NOTICE_BACKGROUND'][background],
			], status_message_text, "@NOTICE", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def WARNING(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Warning information logging:
		Can be used to log entry warnings that the program may work with unpredictable results.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['WARNING_TIME'][local_background],
				self._AnsiColorSet['WARNING_STATUS'][local_background],
				self._AnsiColorSet['WARNING_STATUS_MESSAGE'][local_background],
				self._AnsiColorSet['TYPE_WARNING'][local_background],
				self._AnsiColorSet['WARNING_MESSAGE'][local_background],
				self._AnsiColorSet['WARNING_BACKGROUND'][local_background],
			], status_message_text, "!WARNING", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def ERROR(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Error information logging:
		Used to log entry errors and crashes in the program.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['ERROR_TIME'][local_background],
				self._AnsiColorSet['ERROR_STATUS'][local_background],
				self._AnsiColorSet['ERROR_STATUS_MESSAGE'][local_background],
				self._AnsiColorSet['TYPE_ERROR'][local_background],
				self._AnsiColorSet['ERROR_MESSAGE'][local_background],
				self._AnsiColorSet['ERROR_BACKGROUND'][local_background],
			], status_message_text, "!!ERROR", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def CRITICAL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = True, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Critical error information logging:
		Used to log entry for critical and unpredictable program failures.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['CRITICAL_TIME'][local_background],
				self._AnsiColorSet['CRITICAL_STATUS'][local_background],
				self._AnsiColorSet['CRITICAL_STATUS_MESSAGE'][local_background],
				self._AnsiColorSet['TYPE_CRITICAL'][local_background],
				self._AnsiColorSet['CRITICAL_MESSAGE'][local_background],
				self._AnsiColorSet['CRITICAL_BACKGROUND'][local_background],
			], status_message_text, "!!!@CRITICAL", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def START_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Stub.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		# self._buffer << self._assemble_entry(
		# 	[
		# 		self._AnsiColorSet['PROGRESS_TIME'][local_background],
		# 		self._AnsiColorSet['PROGRESS_STATUS'][local_background],
		# 		self._AnsiColorSet['PROGRESS_STATUS_MESSAGE'][local_background],
		# 		self._AnsiColorSet['TYPE_PROGRESS'][local_background],
		# 		self._AnsiColorSet['PROGRESS_MESSAGE'][local_background],
		# 		self._AnsiColorSet['PROGRESS_BACKGROUND'][local_background],
		# 	], status_message_text, "&PROGRESS [*******.............] - 37%", message_text, bold, italic, invert
		# )
		# self._buffer.update_console()
		pass
		# Must run on a thread

	def STOP_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Stub.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		pass
		# Make transition to SUCCESS or FAIL

	def SUCCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, local_background: bool = True):
		"""
		Success information logging:
		Used to log entry a message about the success of the process.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['SUCCESS_TIME'][local_background],
				self._AnsiColorSet['SUCCESS_STATUS'][local_background],
				self._AnsiColorSet['SUCCESS_STATUS_MESSAGE'][local_background],
				self._AnsiColorSet['TYPE_SUCCESS'][local_background],
				self._AnsiColorSet['SUCCESS_MESSAGE'][local_background],
				self._AnsiColorSet['SUCCESS_BACKGROUND'][local_background],
			], status_message_text, "&SUCCESS", message_text, bold, italic, invert
		)
		self._buffer.update_console()

	def FAIL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, local_background: bool = True):
		"""
		Fail information logging:
		Used to log entry a message about the failed execution of the process.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._AnsiColorSet['FAIL_TIME'][local_background],
				self._AnsiColorSet['FAIL_STATUS'][local_background],
				self._AnsiColorSet['FAIL_STATUS_MESSAGE'][local_background],
				self._AnsiColorSet['TYPE_FAIL'][local_background],
				self._AnsiColorSet['FAIL_MESSAGE'][local_background],
				self._AnsiColorSet['FAIL_BACKGROUND'][local_background],
			], status_message_text, "&FAIL", message_text, bold, italic, invert
		)
		self._buffer.update_console()


# Test
if __name__ == "__main__":
	buf = TextBuffer(115)
	logger = Logger(program_name="WiretappingScaner", text_buffer=buf)
	logger.DEBUG(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.DEBUG_PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.EVENT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.global_background = True
	logger.AUDIT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.METRICS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.time = False
	logger.USER(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.MESSAGE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.status_type = False
	logger.INFO(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message")
	logger.NOTICE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	# buf.replace(7, "7")
	logger.WARNING(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.ERROR(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.CRITICAL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	# logger.START_PROCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.SUCCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.FAIL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	# print(logger.FAIL(status_message_text="33", message_text="34", invert=True))
	buf << "55"
	logger.INFO(status_message_text="Test text", message_text="Entrying was successful!", bold=True)
	buf >> "buf"

	# logger.timeEnabled(False)
	# print(logger.DEBUG(status_message_text="1", message_text="2"))
