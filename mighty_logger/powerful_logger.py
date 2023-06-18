"""
A module with the implementation of a powerful logger.
\n
Copyright © 2023 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from threading import Thread
from time import sleep
from datetime import datetime

from mighty_logger.basic.basic_logger import BasicLogger
from mighty_logger.basic.exceptions import ColorException, CombinationException, ReCreationException
from mighty_logger.basic.text_buffer_type import TextBufferType
from mighty_logger.src.color_picker import AnsiColor, HexColor, Dec2Ansi, Dec2Hex
from mighty_logger.src.log_enums import LogEnvironments
from mighty_logger.src.status_variables import StatusMessageType
from mighty_logger.text.animation import BasicAnimationType, IndefiniteAnimationType, DefiniteAnimationType, IndefiniteAnimations, DefiniteAnimations
from mighty_logger.text.icon_set import IconSetType, IconSet1
from mighty_logger.text.text_buffer import BasicTextBuffer, TextBuffer

class Logger(BasicLogger):
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
	\nImplements the output of the following types of records:
	see the /docs/DATA.md/"Entry types"
	"""

	def __init__(
		self,
		*,
		program_name: str = "Unknown",
		log_environment: str = LogEnvironments.CONSOLE,
		console_width: int = 60,
		icon_set: IconSetType = IconSet1(),
		time_global_entry: bool = True,
		status_global_entry: bool = True,
		status_message_global_entry: bool = True,
		status_type_global_entry: bool = True,
		message_global_entry: bool = True,
		global_bold_font: bool = False,
		global_italic_font: bool = False,
		global_invert_font: bool = False,
		global_background: bool = False,
	) -> None:
		if not hasattr(self, "_ColorScheme"):
			super().__init__(program_name)
			self._animation: BasicAnimationType = BasicAnimationType([])
			self._icon_set = icon_set
			self._settings["global_bold_font"] = global_bold_font
			self._settings["global_italic_font"] = global_italic_font
			self._settings["global_invert_font"] = global_invert_font
			self._settings["time_global_entry"] = time_global_entry
			self._settings["status_global_entry"] = status_global_entry
			self._settings["status_message_global_entry"] = status_message_global_entry
			self._settings["status_type_global_entry"] = status_type_global_entry
			self._settings["message_global_entry"] = message_global_entry
			self._ColorScheme: dict = {}
			self._environment = log_environment
			self._progress_rise = 0
			self._progress_start: datetime | None = None
			self._progress_time: str = "        "
			self._progress_interrupt = False
			self._start_timer_value: datetime | None = None
			self.global_background = global_background
			self._color_scheme_init()
			if self._environment == LogEnvironments.CONSOLE:
				if TextBuffer._instance is not None:
					self._buffer = TextBuffer._instance
					self.notice(
						message_text="An existing logger was taken into use",
						status_message=StatusMessageType("Note"),
						local_settings={"italic": True}
					)
				else:
					self._buffer = TextBuffer(console_width)
			else:
				if BasicTextBuffer._instance is not None:
					self._buffer = BasicTextBuffer._instance
					self.notice(
						message_text="An existing logger was taken into use",
						status_message=StatusMessageType("Note"),
						local_settings={"italic": True}
					)
				else:
					self._buffer = BasicTextBuffer()
			self._initial_log()
		else:
			raise ReCreationException("Logger class object already created")

	def _color_scheme_init(self) -> None:
		"""
		Sets the colors of the logger.
		"""
		match self._environment:
			case LogEnvironments.CONSOLE:
				self._ColorScheme['INITIAL_COLOR'] = [AnsiColor('GOLD', "foreground"), AnsiColor('INDIGO', "foreground")]
				self._ColorScheme['INITIAL_BACKGROUND'] = ["", AnsiColor('GOLD', "background")]
				# DEBUG colors
				self._ColorScheme['DEBUG_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['DEBUG_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['DEBUG_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_DEBUG'] = [AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['DEBUG_MESSAGE'] = [AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['DEBUG_BACKGROUND'] = ["", AnsiColor('TAN', "background")]
				# DEBUG_PERFORMANCE colors
				self._ColorScheme['DEBUG_PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_DEBUG_PERFORMANCE'] = [AnsiColor('NAVAJOWHITE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_MESSAGE'] = [AnsiColor('WHEAT', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_BACKGROUND'] = ["", AnsiColor('WHEAT', "background")]
				# PERFORMANCE colors
				self._ColorScheme['PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_PERFORMANCE'] = [AnsiColor('BLANCHEDALMOND', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['PERFORMANCE_MESSAGE'] = [AnsiColor('BISQUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['PERFORMANCE_BACKGROUND'] = ["", AnsiColor('BISQUE', "background")]
				# EVENT colors
				self._ColorScheme['EVENT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['EVENT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['EVENT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_EVENT'] = [AnsiColor('GREENYELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['EVENT_MESSAGE'] = [AnsiColor('YELLOWGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['EVENT_BACKGROUND'] = ["", AnsiColor('YELLOWGREEN', "background")]
				# AUDIT colors
				self._ColorScheme['AUDIT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['AUDIT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['AUDIT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_AUDIT'] = [AnsiColor('MEDIUMSPRINGGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['AUDIT_MESSAGE'] = [AnsiColor('SPRINGGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['AUDIT_BACKGROUND'] = ["", AnsiColor('SPRINGGREEN', "background")]
				# METRICS colors
				self._ColorScheme['METRICS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['METRICS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['METRICS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_METRICS'] = [AnsiColor('PALEGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['METRICS_MESSAGE'] = [AnsiColor('LIGHTGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['METRICS_BACKGROUND'] = ["", AnsiColor('LIGHTGREEN', "background")]
				# USER colors
				self._ColorScheme['USER_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['USER_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['USER_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_USER'] = [AnsiColor('CHARTREUSE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['USER_MESSAGE'] = [AnsiColor('LAWNGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['USER_BACKGROUND'] = ["", AnsiColor('LAWNGREEN', "background")]
				# MESSAGE colors
				self._ColorScheme['MESSAGE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['MESSAGE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['MESSAGE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_MESSAGE'] = [AnsiColor('PALETURQUOISE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['MESSAGE_MESSAGE'] = [AnsiColor('POWDERBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['MESSAGE_BACKGROUND'] = ["", AnsiColor('POWDERBLUE', "background")]
				# INFO colors
				self._ColorScheme['INFO_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['INFO_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['INFO_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_INFO'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['INFO_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['INFO_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
				# NOTICE colors
				self._ColorScheme['NOTICE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['NOTICE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['NOTICE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_NOTICE'] = [AnsiColor('LIGHTBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['NOTICE_MESSAGE'] = [AnsiColor('LIGHTSTEELBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['NOTICE_BACKGROUND'] = ["", AnsiColor('LIGHTSTEELBLUE', "background")]
				# WARNING colors
				self._ColorScheme['WARNING_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['WARNING_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['WARNING_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_WARNING'] = [AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['WARNING_MESSAGE'] = [AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['WARNING_BACKGROUND'] = ["", AnsiColor('DARKYELLOW', "background")]
				# ERROR colors
				self._ColorScheme['ERROR_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
				self._ColorScheme['ERROR_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
				self._ColorScheme['ERROR_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
				self._ColorScheme['TYPE_ERROR'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('GAINSBORO', "foreground")]
				self._ColorScheme['ERROR_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTGRAY', "foreground")]
				self._ColorScheme['ERROR_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]
				# CRITICAL colors
				self._ColorScheme['CRITICAL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
				self._ColorScheme['CRITICAL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
				self._ColorScheme['CRITICAL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
				self._ColorScheme['TYPE_CRITICAL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('DARKSALMON', "foreground")]
				self._ColorScheme['CRITICAL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTSALMON', "foreground")]
				self._ColorScheme['CRITICAL_BACKGROUND'] = ["", AnsiColor('MAROON', "background")]
				# RESOLVED colors
				self._ColorScheme['RESOLVED_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['RESOLVED_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
				self._ColorScheme['RESOLVED_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
				self._ColorScheme['TYPE_RESOLVED'] = [AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
				self._ColorScheme['RESOLVED_MESSAGE'] = [AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
				self._ColorScheme['RESOLVED_BACKGROUND'] = ["", AnsiColor('DARKGREEN', "background")]
				# UNRESOLVED colors
				self._ColorScheme['UNRESOLVED_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['UNRESOLVED_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
				self._ColorScheme['UNRESOLVED_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
				self._ColorScheme['TYPE_UNRESOLVED'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")]
				self._ColorScheme['UNRESOLVED_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")]
				self._ColorScheme['UNRESOLVED_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]
				# INITIATION colors
				self._ColorScheme['INITIATION_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['INITIATION_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
				self._ColorScheme['INITIATION_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
				self._ColorScheme['TYPE_INITIATION'] = [AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
				self._ColorScheme['INITIATION_MESSAGE'] = [AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
				self._ColorScheme['INITIATION_BACKGROUND'] = ["", AnsiColor('DARKGREEN', "background")]
				# PROGRESS colors
				self._ColorScheme['PROGRESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")]
				self._ColorScheme['PROGRESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['PROGRESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_PROGRESS'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['PROGRESS_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['PROGRESS_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
				# ACHIEVEMENT colors
				self._ColorScheme['ACHIEVEMENT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['ACHIEVEMENT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['ACHIEVEMENT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_ACHIEVEMENT'] = [AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['ACHIEVEMENT_MESSAGE'] = [AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['ACHIEVEMENT_BACKGROUND'] = ["", AnsiColor('DARKYELLOW', "background")]
				# MILESTONE colors
				self._ColorScheme['MILESTONE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['MILESTONE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
				self._ColorScheme['MILESTONE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
				self._ColorScheme['TYPE_MILESTONE'] = [AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
				self._ColorScheme['MILESTONE_MESSAGE'] = [AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
				self._ColorScheme['MILESTONE_BACKGROUND'] = ["", AnsiColor('DARKGREEN', "background")]
				# SUCCESS colors
				self._ColorScheme['SUCCESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['SUCCESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
				self._ColorScheme['SUCCESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
				self._ColorScheme['TYPE_SUCCESS'] = [AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
				self._ColorScheme['SUCCESS_MESSAGE'] = [AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
				self._ColorScheme['SUCCESS_BACKGROUND'] = ["", AnsiColor('DARKGREEN', "background")]
				# FAIL colors
				self._ColorScheme['FAIL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['FAIL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
				self._ColorScheme['FAIL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
				self._ColorScheme['TYPE_FAIL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")]
				self._ColorScheme['FAIL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")]
				self._ColorScheme['FAIL_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]
				# START_TIMER colors
				self._ColorScheme['START_TIMER_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['START_TIMER_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
				self._ColorScheme['START_TIMER_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
				self._ColorScheme['TYPE_START_TIMER'] = [AnsiColor('SEAGREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
				self._ColorScheme['START_TIMER_MESSAGE'] = [AnsiColor('FORESTGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
				self._ColorScheme['START_TIMER_BACKGROUND'] = ["", AnsiColor('FORESTGREEN', "background")]
				# TIMER_MARK colors
				self._ColorScheme['TIMER_MARK_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['TIMER_MARK_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['TIMER_MARK_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_TIMER_MARK'] = [AnsiColor('KHAKI', "foreground"), AnsiColor('SIENNA', "foreground")]
				self._ColorScheme['TIMER_MARK_MESSAGE'] = [AnsiColor('DARKKHAKI', "foreground"), AnsiColor('SADDLEBROWN', "foreground")]
				self._ColorScheme['TIMER_MARK_BACKGROUND'] = ["", AnsiColor('DARKKHAKI', "background")]
				# STOP_TIMER colors
				self._ColorScheme['STOP_TIMER_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")]
				self._ColorScheme['STOP_TIMER_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['STOP_TIMER_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_STOP_TIMER'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['STOP_TIMER_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['STOP_TIMER_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
			case LogEnvironments.HTML:
				self._ColorScheme['INITIAL_COLOR'] = [HexColor('GOLD'), HexColor('INDIGO')]
				self._ColorScheme['INITIAL_BACKGROUND'] = ["", HexColor('GOLD')]
				# DEBUG colors
				self._ColorScheme['DEBUG_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['DEBUG_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['DEBUG_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_DEBUG'] = [HexColor('BURLYWOOD'), HexColor('NAVY')]
				self._ColorScheme['DEBUG_MESSAGE'] = [HexColor('TAN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['DEBUG_BACKGROUND'] = ["", HexColor('TAN')]
				# DEBUG_PERFORMANCE colors
				self._ColorScheme['DEBUG_PERFORMANCE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_DEBUG_PERFORMANCE'] = [HexColor('NAVAJOWHITE'), HexColor('NAVY')]
				self._ColorScheme['DEBUG_PERFORMANCE_MESSAGE'] = [HexColor('WHEAT'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['DEBUG_PERFORMANCE_BACKGROUND'] = ["", HexColor('WHEAT')]
				# PERFORMANCE colors
				self._ColorScheme['PERFORMANCE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['PERFORMANCE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['PERFORMANCE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_PERFORMANCE'] = [HexColor('BLANCHEDALMOND'), HexColor('NAVY')]
				self._ColorScheme['PERFORMANCE_MESSAGE'] = [HexColor('BISQUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['PERFORMANCE_BACKGROUND'] = ["", HexColor('BISQUE')]
				# EVENT colors
				self._ColorScheme['EVENT_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['EVENT_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['EVENT_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_EVENT'] = [HexColor('GREENYELLOW'), HexColor('NAVY')]
				self._ColorScheme['EVENT_MESSAGE'] = [HexColor('YELLOWGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['EVENT_BACKGROUND'] = ["", HexColor('YELLOWGREEN')]
				# AUDIT colors
				self._ColorScheme['AUDIT_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['AUDIT_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['AUDIT_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_AUDIT'] = [HexColor('MEDIUMSPRINGGREEN'), HexColor('NAVY')]
				self._ColorScheme['AUDIT_MESSAGE'] = [HexColor('SPRINGGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['AUDIT_BACKGROUND'] = ["", HexColor('SPRINGGREEN')]
				# METRICS colors
				self._ColorScheme['METRICS_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['METRICS_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['METRICS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_METRICS'] = [HexColor('PALEGREEN'), HexColor('NAVY')]
				self._ColorScheme['METRICS_MESSAGE'] = [HexColor('LIGHTGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['METRICS_BACKGROUND'] = ["", HexColor('LIGHTGREEN')]
				# USER colors
				self._ColorScheme['USER_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['USER_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['USER_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_USER'] = [HexColor('CHARTREUSE'), HexColor('NAVY')]
				self._ColorScheme['USER_MESSAGE'] = [HexColor('LAWNGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['USER_BACKGROUND'] = ["", HexColor('LAWNGREEN')]
				# MESSAGE colors
				self._ColorScheme['MESSAGE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['MESSAGE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['MESSAGE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_MESSAGE'] = [HexColor('PALETURQUOISE'), HexColor('NAVY')]
				self._ColorScheme['MESSAGE_MESSAGE'] = [HexColor('POWDERBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['MESSAGE_BACKGROUND'] = ["", HexColor('POWDERBLUE')]
				# INFO colors
				self._ColorScheme['INFO_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['INFO_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['INFO_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_INFO'] = [HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
				self._ColorScheme['INFO_MESSAGE'] = [HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['INFO_BACKGROUND'] = ["", HexColor('SKYBLUE')]
				# NOTICE colors
				self._ColorScheme['NOTICE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['NOTICE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['NOTICE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_NOTICE'] = [HexColor('LIGHTBLUE'), HexColor('NAVY')]
				self._ColorScheme['NOTICE_MESSAGE'] = [HexColor('LIGHTSTEELBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['NOTICE_BACKGROUND'] = ["", HexColor('LIGHTSTEELBLUE')]
				# WARNING colors
				self._ColorScheme['WARNING_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['WARNING_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['WARNING_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_WARNING'] = [HexColor('YELLOW'), HexColor('NAVY')]
				self._ColorScheme['WARNING_MESSAGE'] = [HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['WARNING_BACKGROUND'] = ["", HexColor('DARKYELLOW')]
				# ERROR colors
				self._ColorScheme['ERROR_TIME'] = [HexColor('ORCHID'), HexColor('PLUM')]
				self._ColorScheme['ERROR_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
				self._ColorScheme['ERROR_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
				self._ColorScheme['TYPE_ERROR'] = [HexColor('FIREBRICK'), HexColor('GAINSBORO')]
				self._ColorScheme['ERROR_MESSAGE'] = [HexColor('DARKRED'), HexColor('LIGHTGRAY')]
				self._ColorScheme['ERROR_BACKGROUND'] = ["", HexColor('DARKRED')]
				# CRITICAL colors
				self._ColorScheme['CRITICAL_TIME'] = [HexColor('ORCHID'), HexColor('PLUM')]
				self._ColorScheme['CRITICAL_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
				self._ColorScheme['CRITICAL_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
				self._ColorScheme['TYPE_CRITICAL'] = [HexColor('FIREBRICK'), HexColor('DARKSALMON')]
				self._ColorScheme['CRITICAL_MESSAGE'] = [HexColor('DARKRED'), HexColor('LIGHTSALMON')]
				self._ColorScheme['CRITICAL_BACKGROUND'] = ["", HexColor('MAROON')]
				# RESOLVED colors
				self._ColorScheme['RESOLVED_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['RESOLVED_STATUS'] = [HexColor('ORANGE'), HexColor('CHARTREUSE')]
				self._ColorScheme['RESOLVED_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
				self._ColorScheme['TYPE_RESOLVED'] = [HexColor('GREEN'), HexColor('PALEGREEN')]
				self._ColorScheme['RESOLVED_MESSAGE'] = [HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
				self._ColorScheme['RESOLVED_BACKGROUND'] = ["", HexColor('DARKGREEN')]
				# UNRESOLVED colors
				self._ColorScheme['UNRESOLVED_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['UNRESOLVED_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
				self._ColorScheme['UNRESOLVED_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
				self._ColorScheme['TYPE_UNRESOLVED'] = [HexColor('FIREBRICK'), HexColor('YELLOW')]
				self._ColorScheme['UNRESOLVED_MESSAGE'] = [HexColor('DARKRED'), HexColor('DARKYELLOW')]
				self._ColorScheme['UNRESOLVED_BACKGROUND'] = ["", HexColor('DARKRED')]
				# INITIATION colors
				self._ColorScheme['INITIATION_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['INITIATION_STATUS'] = [HexColor('ORANGE'), HexColor('CHARTREUSE')]
				self._ColorScheme['INITIATION_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
				self._ColorScheme['TYPE_INITIATION'] = [HexColor('GREEN'), HexColor('PALEGREEN')]
				self._ColorScheme['INITIATION_MESSAGE'] = [HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
				self._ColorScheme['INITIATION_BACKGROUND'] = ["", HexColor('DARKGREEN')]
				# PROGRESS colors
				self._ColorScheme['PROGRESS_TIME'] = [HexColor('ORCHID'), HexColor('PURPLE')]
				self._ColorScheme['PROGRESS_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['PROGRESS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_PROGRESS'] = [HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
				self._ColorScheme['PROGRESS_MESSAGE'] = [HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['PROGRESS_BACKGROUND'] = ["", HexColor('SKYBLUE')]
				# ACHIEVEMENT colors
				self._ColorScheme['ACHIEVEMENT_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['ACHIEVEMENT_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['ACHIEVEMENT_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_ACHIEVEMENT'] = [HexColor('YELLOW'), HexColor('NAVY')]
				self._ColorScheme['ACHIEVEMENT_MESSAGE'] = [HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['ACHIEVEMENT_BACKGROUND'] = ["", HexColor('DARKYELLOW')]
				# MILESTONE colors
				self._ColorScheme['MILESTONE_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['MILESTONE_STATUS'] = [HexColor('ORANGE'), HexColor('CHARTREUSE')]
				self._ColorScheme['MILESTONE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
				self._ColorScheme['TYPE_MILESTONE'] = [HexColor('GREEN'), HexColor('PALEGREEN')]
				self._ColorScheme['MILESTONE_MESSAGE'] = [HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
				self._ColorScheme['MILESTONE_BACKGROUND'] = ["", HexColor('DARKGREEN')]
				# SUCCESS colors
				self._ColorScheme['SUCCESS_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['SUCCESS_STATUS'] = [HexColor('ORANGE'), HexColor('CHARTREUSE')]
				self._ColorScheme['SUCCESS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
				self._ColorScheme['TYPE_SUCCESS'] = [HexColor('GREEN'), HexColor('PALEGREEN')]
				self._ColorScheme['SUCCESS_MESSAGE'] = [HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
				self._ColorScheme['SUCCESS_BACKGROUND'] = ["", HexColor('DARKGREEN')]
				# FAIL colors
				self._ColorScheme['FAIL_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['FAIL_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
				self._ColorScheme['FAIL_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
				self._ColorScheme['TYPE_FAIL'] = [HexColor('FIREBRICK'), HexColor('YELLOW')]
				self._ColorScheme['FAIL_MESSAGE'] = [HexColor('DARKRED'), HexColor('DARKYELLOW')]
				self._ColorScheme['FAIL_BACKGROUND'] = ["", HexColor('DARKRED')]
				# START_TIMER colors
				self._ColorScheme['START_TIMER_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['START_TIMER_STATUS'] = [HexColor('ORANGE'), HexColor('CHARTREUSE')]
				self._ColorScheme['START_TIMER_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
				self._ColorScheme['TYPE_START_TIMER'] = [HexColor('SEAGREEN'), HexColor('PALEGREEN')]
				self._ColorScheme['START_TIMER_MESSAGE'] = [HexColor('FORESTGREEN'), HexColor('LIGHTGREEN')]
				self._ColorScheme['START_TIMER_BACKGROUND'] = ["", HexColor('FORESTGREEN')]
				# TIMER_MARK colors
				self._ColorScheme['TIMER_MARK_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['TIMER_MARK_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['TIMER_MARK_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_TIMER_MARK'] = [HexColor('KHAKI'), HexColor('SIENNA')]
				self._ColorScheme['TIMER_MARK_MESSAGE'] = [HexColor('DARKKHAKI'), HexColor('SADDLEBROWN')]
				self._ColorScheme['TIMER_MARK_BACKGROUND'] = ["", HexColor('DARKKHAKI')]
				# STOP_TIMER colors
				self._ColorScheme['STOP_TIMER_TIME'] = [HexColor('ORCHID'), HexColor('PURPLE')]
				self._ColorScheme['STOP_TIMER_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['STOP_TIMER_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_STOP_TIMER'] = [HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
				self._ColorScheme['STOP_TIMER_MESSAGE'] = [HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['STOP_TIMER_BACKGROUND'] = ["", HexColor('SKYBLUE')]

	def _initial_log(self) -> None:
		"""
		Displays initialized information.
		"""
		if self._environment == LogEnvironments.HTML:
			self._buffer << "<body style='background-color: #000000; color: #ffffff;'>"
		self._buffer << self._initialized_data(
			[
				self._ColorScheme['INITIAL_COLOR'][self.global_background],
				self._ColorScheme['INITIAL_BACKGROUND'][self.global_background]
			], self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def set_icons(self, icon_set: IconSetType) -> None:
		"""
		Changes the current icon set used by the Logger.

		:param icon_set: Icon set to use
		"""
		self._icon_set = icon_set

	def set_color(
		self,
		*,
		logger_color_name: str,
		color_value: list[int, int, int],
		foreground: bool = True,
		background: bool = False
	) -> None:
		"""
		A method that sets the ANSI escape code color in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys: see /docs/DATA.md/"Logger Color Scheme".\n
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
		if logger_color_name in self._ColorScheme:
			if background and not foreground:
				self._ColorScheme[logger_color_name][1] = Dec2Ansi(color_value, "background") if self._environment == LogEnvironments.CONSOLE else Dec2Hex(color_value)
			elif background and foreground:
				self._ColorScheme[logger_color_name][1] = Dec2Ansi(color_value, "foreground") if self._environment == LogEnvironments.CONSOLE else Dec2Hex(color_value)
			elif not background and foreground:
				self._ColorScheme[logger_color_name][0] = Dec2Ansi(color_value, "foreground") if self._environment == LogEnvironments.CONSOLE else Dec2Hex(color_value)
			else:
				raise CombinationException("False-False combination of foreground-background flags not possible")
		else:
			raise ColorException("This color is not in the dictionary")

	def buffer(self) -> TextBufferType:
		"""
		The Text Buffer object is created in the class constructor and this
		method is used to access it. It returns a buffer.

		:return: a text buffer object
		"""
		return self._buffer

	#todo v0.7.1 сделать конвертер из Console в HTML и наоборот

	# ######################################################################################## #
	#                                                                                          #
	#                                    Entering to Logger                                    #
	#                                                                                          #
	# ######################################################################################## #

	def empty(
		self,
		*,
		entry: str
	) -> None:
		"""
		Empty logging:
		A type denoting an "empty" entry - an entry that carries nothing but the purest text.
		\n
		Since v0.6.0

		:param entry: "Empty" entry
		"""
		self._buffer << entry
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def debug(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Debugging information logging:
		Can be used to log entry any information while debugging an application.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['DEBUG_TIME'][background],
				self._ColorScheme['DEBUG_STATUS'][background],
				self._ColorScheme['DEBUG_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_DEBUG'][background],
				self._ColorScheme['DEBUG_MESSAGE'][background],
				self._ColorScheme['DEBUG_BACKGROUND'][background],
			], self._progress_time, self._icon_set.debug, status_message.current_status_message, "%DEBUG", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def debug_performance(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Performance debugging information logging:
		Can be used to log entry the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['DEBUG_PERFORMANCE_TIME'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_DEBUG_PERFORMANCE'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_MESSAGE'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_BACKGROUND'][background],
			], self._progress_time, self._icon_set.debug_performance, status_message.current_status_message, "%DEBUG PERFORMANCE", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def performance(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Performance information logging:
		Can be used to log entry the execution time of operations or
		other application performance information.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['PERFORMANCE_TIME'][background],
				self._ColorScheme['PERFORMANCE_STATUS'][background],
				self._ColorScheme['PERFORMANCE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_PERFORMANCE'][background],
				self._ColorScheme['PERFORMANCE_MESSAGE'][background],
				self._ColorScheme['PERFORMANCE_BACKGROUND'][background],
			], self._progress_time, self._icon_set.performance, status_message.current_status_message, "%PERFORMANCE", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def event(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Event information logging:
		Can be used to log entry specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['EVENT_TIME'][background],
				self._ColorScheme['EVENT_STATUS'][background],
				self._ColorScheme['EVENT_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_EVENT'][background],
				self._ColorScheme['EVENT_MESSAGE'][background],
				self._ColorScheme['EVENT_BACKGROUND'][background],
			], self._progress_time, self._icon_set.event, status_message.current_status_message, "~EVENT", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def audit(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Audit information logging:
		Can be used to log entry changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['AUDIT_TIME'][background],
				self._ColorScheme['AUDIT_STATUS'][background],
				self._ColorScheme['AUDIT_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_AUDIT'][background],
				self._ColorScheme['AUDIT_MESSAGE'][background],
				self._ColorScheme['AUDIT_BACKGROUND'][background],
			], self._progress_time, self._icon_set.audit, status_message.current_status_message, "~AUDIT", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def metrics(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Metrics information logging:
		Can be used to log entry metrics to track application performance and identify issues.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['METRICS_TIME'][background],
				self._ColorScheme['METRICS_STATUS'][background],
				self._ColorScheme['METRICS_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_METRICS'][background],
				self._ColorScheme['METRICS_MESSAGE'][background],
				self._ColorScheme['METRICS_BACKGROUND'][background],
			], self._progress_time, self._icon_set.metrics, status_message.current_status_message, "~METRICS", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def user(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		User information logging:
		Can be used to log entry custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['USER_TIME'][background],
				self._ColorScheme['USER_STATUS'][background],
				self._ColorScheme['USER_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_USER'][background],
				self._ColorScheme['USER_MESSAGE'][background],
				self._ColorScheme['USER_BACKGROUND'][background],
			], self._progress_time, self._icon_set.user, status_message.current_status_message, "~USER", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def message(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['MESSAGE_TIME'][background],
				self._ColorScheme['MESSAGE_STATUS'][background],
				self._ColorScheme['MESSAGE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_MESSAGE'][background],
				self._ColorScheme['MESSAGE_MESSAGE'][background],
				self._ColorScheme['MESSAGE_BACKGROUND'][background],
			], self._progress_time, self._icon_set.message, status_message.current_status_message, "@MESSAGE", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def info(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Default information logging:
		Can be used to log entry messages with specific content about the operation of the program.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['INFO_TIME'][background],
				self._ColorScheme['INFO_STATUS'][background],
				self._ColorScheme['INFO_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_INFO'][background],
				self._ColorScheme['INFO_MESSAGE'][background],
				self._ColorScheme['INFO_BACKGROUND'][background],
			], self._progress_time, self._icon_set.info, status_message.current_status_message, "@INFO", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def notice(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['NOTICE_TIME'][background],
				self._ColorScheme['NOTICE_STATUS'][background],
				self._ColorScheme['NOTICE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_NOTICE'][background],
				self._ColorScheme['NOTICE_MESSAGE'][background],
				self._ColorScheme['NOTICE_BACKGROUND'][background],
			], self._progress_time, self._icon_set.notice, status_message.current_status_message, "@NOTICE", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def warning(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Warning information logging:
		Can be used to log entry warnings that the program may work with unpredictable results.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['WARNING_TIME'][local_background],
				self._ColorScheme['WARNING_STATUS'][local_background],
				self._ColorScheme['WARNING_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_WARNING'][local_background],
				self._ColorScheme['WARNING_MESSAGE'][local_background],
				self._ColorScheme['WARNING_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.warning, status_message.current_status_message, "!WARNING", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def error(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Error information logging:
		Used to log entry errors and crashes in the program.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['ERROR_TIME'][local_background],
				self._ColorScheme['ERROR_STATUS'][local_background],
				self._ColorScheme['ERROR_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_ERROR'][local_background],
				self._ColorScheme['ERROR_MESSAGE'][local_background],
				self._ColorScheme['ERROR_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.error, status_message.current_status_message, "!!ERROR", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def critical(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Critical error information logging:
		Used to log entry for critical and unpredictable program failures.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		if not 'bold' in local_settings:
			local_settings["bold"] = True
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['CRITICAL_TIME'][local_background],
				self._ColorScheme['CRITICAL_STATUS'][local_background],
				self._ColorScheme['CRITICAL_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_CRITICAL'][local_background],
				self._ColorScheme['CRITICAL_MESSAGE'][local_background],
				self._ColorScheme['CRITICAL_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.critical, status_message.current_status_message, "!!!@CRITICAL", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def resolved(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Resolved information logging:
		Used to log entry resolved solutions to problems and errors.
		\n
		Since v0.6.0

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['RESOLVED_TIME'][background],
				self._ColorScheme['RESOLVED_STATUS'][background],
				self._ColorScheme['RESOLVED_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_RESOLVED'][background],
				self._ColorScheme['RESOLVED_MESSAGE'][background],
				self._ColorScheme['RESOLVED_BACKGROUND'][background],
			], self._progress_time, self._icon_set.resolved, status_message.current_status_message, "!RESOLVED", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def unresolved(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Unresolved information logging:
		Used to log entry unresolved solutions to problems and errors.
		\n
		Since v0.6.0

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['UNRESOLVED_TIME'][background],
				self._ColorScheme['UNRESOLVED_STATUS'][background],
				self._ColorScheme['UNRESOLVED_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_UNRESOLVED'][background],
				self._ColorScheme['UNRESOLVED_MESSAGE'][background],
				self._ColorScheme['UNRESOLVED_BACKGROUND'][background],
			], self._progress_time, self._icon_set.unresolved, status_message.current_status_message, "!UNRESOLVED", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	# ######################################################################################## #
	#                                                                                          #
	#                                  Entering to Processes                                   #
	#                                                                                          #
	# ######################################################################################## #

	def start_indefinite_process(
		self,
		*,
		animation: IndefiniteAnimationType = IndefiniteAnimations.Line,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		A method that starts the whole process of indefinite logging. While the process
		is running, you cannot start other processes in the Logger and call the entering
		methods directly. While the process is running - the last entry will play
		the animation of the process. Before starting a process, you can specify that
		the process Logs and configure Initiation and Progress entries.
		\n
		Since v0.6.0

		:param animation: The name of the animation that will play in the Progress entry
		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		self._animation = animation

		self._progress_start = datetime.now()
		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		func = getattr(self, "_initiation", None)
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		func(**args)

		thread = Thread(target=self._indefinite_progress, kwargs=args)
		thread.start()

	def _indefinite_progress(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		A method that creates an animation entry. Only works on the last string.
		You need to run in a thread. Terminates when the process stop flag
		is set by the Logger.stop_process() method.
		\n
		Since v0.6.0

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		animation_index = 0
		self._buffer << "."
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()
		while not self._progress_interrupt:
			animation_item = self._animation.animation[animation_index]
			self._buffer.get_data()[-1] = self._assemble_entry(
				[
					self._ColorScheme['PROGRESS_TIME'][local_background],
					self._ColorScheme['PROGRESS_STATUS'][local_background],
					self._ColorScheme['PROGRESS_STATUS_MESSAGE'][local_background],
					self._ColorScheme['TYPE_PROGRESS'][local_background],
					self._ColorScheme['PROGRESS_MESSAGE'][local_background],
					self._ColorScheme['PROGRESS_BACKGROUND'][local_background],
				], animation_item, self._icon_set.process, status_message.current_status_message, "&PROGRESS", message_text, self._environment, local_settings
			)
			animation_index = (animation_index + 1) % len(self._animation.animation)
			if self._environment == LogEnvironments.CONSOLE:
				self._buffer.update_entry()
			sleep(0.1)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def start_definite_process(
		self,
		*,
		progress_bar: DefiniteAnimationType = DefiniteAnimations.Line,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		A method that starts the whole process of a definite logging. While the process
		is running, you cannot start other processes in the Logger and call the entering
		methods directly. While the process is running - the last entry will display
		the progress of the process. Before starting a process, you can specify that
		the process Logs and configure Initiation and Progress entries.
		\n
		Since v0.6.0

		:param progress_bar: The name of the progress bar that will play in the Progress entry
		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		self._animation = progress_bar

		self._progress_start = datetime.now()
		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		func = getattr(self, "_initiation", None)
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		func(**args)

		thread = Thread(target=self._definite_progress, kwargs=args)
		thread.start()

	def _definite_progress(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		A method that creates a progress bar entry. Only works on the last string.
		You need to run in a thread. Terminates when the process stop flag
		is set by the Logger.stop_process() method.
		\n
		Since v0.6.0

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		old_progress_rise = 0
		self._buffer << "."
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()
		while not self._progress_interrupt:
			if old_progress_rise == self._progress_rise:
				continue
			else:
				old_progress_rise = self._progress_rise
				animation_item = f"{self._animation.animation[(self._progress_rise // 15) + (2 if self._progress_rise == 100 else 1)]} - {self._progress_rise} %"
				self._buffer.get_data()[-1] = self._assemble_entry(
					[
						self._ColorScheme['PROGRESS_TIME'][local_background],
						self._ColorScheme['PROGRESS_STATUS'][local_background],
						self._ColorScheme['PROGRESS_STATUS_MESSAGE'][local_background],
						self._ColorScheme['TYPE_PROGRESS'][local_background],
						self._ColorScheme['PROGRESS_MESSAGE'][local_background],
						self._ColorScheme['PROGRESS_BACKGROUND'][local_background],
					], animation_item, self._icon_set.process, status_message.current_status_message, "&PROGRESS", message_text, self._environment, local_settings
				)
				if self._environment == LogEnvironments.CONSOLE:
					self._buffer.update_entry()
			sleep(0.1)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def progress_rise(self, percent: int) -> None:
		"""
		Sets the process completion percentage. Usually used for a specific process.
		However, it is used for both types of processes as a flag for the success
		of the process. If you set the percentage of completion to 100% before terminating
		the process, the process will complete successfully, otherwise it will fail.
		\n
		Since v0.6.0

		:param percent: Process completion percentage
		"""
		self._progress_rise = percent

	def note_process(
		self,
		*,
		entry_type: str,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		An important method that allows you to add standard non-process entry types
		while a process is running. It's important to note that this entry will still be
		associated with the process, so it's best to use this entry when you want to describe
		intermediate process execution entries beyond process initiation, progress, and
		success/failure entries. Adds the ability to use two additional entry types that
		cannot be used outside a process: achievement and milestone.
		\n
		Use `from mighty_logger.src import TypesEntries` for `entry_type`.
		\n
		Since v0.6.0

		:param entry_type: The type of entry to be entered in the progress history
		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		sleep(0.001)
		last = self._buffer.pop()

		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		func = getattr(self, entry_type, None)
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		func(**args)

		self.empty(entry=last)

	def stop_process(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		The method that terminates the process. If before the end of the process
		its execution has reached 100% - the process was completed successfully,
		otherwise - failed. After calling this method, the Progress entry will be replaced
		by the entry with the result of the process execution.
		\n
		Since v0.6.0

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		self._progress_interrupt = True
		sleep(0.11)
		self._buffer.remove()

		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		func = getattr(self, "_success", None) if self._progress_rise == 100 else getattr(self, "_fail", None)
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		func(**args)

		self._progress_rise = 0
		self._progress_start = None
		self._progress_time = "        "
		self._progress_interrupt = False

	def _initiation(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Initiation information logging:
		Used to explain the running process.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		if not 'italic' in local_settings:
			local_settings["italic"] = True
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['INITIATION_TIME'][local_background],
				self._ColorScheme['INITIATION_STATUS'][local_background],
				self._ColorScheme['INITIATION_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_INITIATION'][local_background],
				self._ColorScheme['INITIATION_MESSAGE'][local_background],
				self._ColorScheme['INITIATION_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.initiation, status_message.current_status_message, "&INITIATION", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def _achievement(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Achievement information logging:
		Used to log entry the achievements gained while executing a process.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['ACHIEVEMENT_TIME'][background],
				self._ColorScheme['ACHIEVEMENT_STATUS'][background],
				self._ColorScheme['ACHIEVEMENT_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_ACHIEVEMENT'][background],
				self._ColorScheme['ACHIEVEMENT_MESSAGE'][background],
				self._ColorScheme['ACHIEVEMENT_BACKGROUND'][background],
			], self._progress_time, self._icon_set.achievement, status_message.current_status_message, "&ACHIEVEMENT", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def _milestone(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Milestone information logging:
		Used to log entry the milestones gained while executing a process.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['MILESTONE_TIME'][background],
				self._ColorScheme['MILESTONE_STATUS'][background],
				self._ColorScheme['MILESTONE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_MILESTONE'][background],
				self._ColorScheme['MILESTONE_MESSAGE'][background],
				self._ColorScheme['MILESTONE_BACKGROUND'][background],
			], self._progress_time, self._icon_set.milestone, status_message.current_status_message, "&MILESTONE", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def _success(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Success information logging:
		Used to log entry a message about the success of the process.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		if not 'italic' in local_settings:
			local_settings["italic"] = True
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['SUCCESS_TIME'][local_background],
				self._ColorScheme['SUCCESS_STATUS'][local_background],
				self._ColorScheme['SUCCESS_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_SUCCESS'][local_background],
				self._ColorScheme['SUCCESS_MESSAGE'][local_background],
				self._ColorScheme['SUCCESS_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.success, status_message.current_status_message, "&SUCCESS", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def _fail(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Fail information logging:
		Used to log entry a message about the failed execution of the process.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		if not 'italic' in local_settings:
			local_settings["italic"] = True
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['FAIL_TIME'][local_background],
				self._ColorScheme['FAIL_STATUS'][local_background],
				self._ColorScheme['FAIL_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_FAIL'][local_background],
				self._ColorScheme['FAIL_MESSAGE'][local_background],
				self._ColorScheme['FAIL_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.fail, status_message.current_status_message, "&FAIL", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	# ######################################################################################## #
	#                                                                                          #
	#                                     Entering to Timer                                    #
	#                                                                                          #
	# ######################################################################################## #

	def start_timer(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Information logging of starting Timer:
		Used to notify the start of the Timer.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		self._start_timer_value = datetime.now()
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		if local_settings is None:
			local_settings = {}
		if not 'italic' in local_settings:
			local_settings["italic"] = True
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['START_TIMER_TIME'][local_background],
				self._ColorScheme['START_TIMER_STATUS'][local_background],
				self._ColorScheme['START_TIMER_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_START_TIMER'][local_background],
				self._ColorScheme['START_TIMER_MESSAGE'][local_background],
				self._ColorScheme['START_TIMER_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.start_timer, status_message.current_status_message, "^START TIMER", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

		self._progress_time = "        "

	def timer_mark(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Information logging of mark Timer:
		Used to notify the mark of the Timer.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		if local_settings is None:
			local_settings = {}
		if not 'italic' in local_settings:
			local_settings["italic"] = True
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['TIMER_MARK_TIME'][local_background],
				self._ColorScheme['TIMER_MARK_STATUS'][local_background],
				self._ColorScheme['TIMER_MARK_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_TIMER_MARK'][local_background],
				self._ColorScheme['TIMER_MARK_MESSAGE'][local_background],
				self._ColorScheme['TIMER_MARK_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.timer_mark, status_message.current_status_message, "^TIMER MARK", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

		self._progress_time = "        "

	def stop_timer(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = True,
		local_settings: dict = None
	) -> None:
		"""
		Information logging of stopping Timer:
		Used to notify the stop of the Timer.

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]


		if local_settings is None:
			local_settings = {}
		if not 'italic' in local_settings:
			local_settings["italic"] = True
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['STOP_TIMER_TIME'][local_background],
				self._ColorScheme['STOP_TIMER_STATUS'][local_background],
				self._ColorScheme['STOP_TIMER_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_STOP_TIMER'][local_background],
				self._ColorScheme['STOP_TIMER_MESSAGE'][local_background],
				self._ColorScheme['STOP_TIMER_BACKGROUND'][local_background],
			], self._progress_time, self._icon_set.stop_timer, status_message.current_status_message, "^STOP TIMER", message_text, self._environment, local_settings
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

		self._start_timer_value = None
		self._progress_time = "        "
