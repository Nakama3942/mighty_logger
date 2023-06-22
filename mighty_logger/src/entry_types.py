"""
...
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

from mighty_logger.src.color_picker import AnsiColor, HexColor

class EntryType:
	def __init__(
		self,
		*,
		type_name: str,
		time_color: tuple,
		status_color: tuple,
		status_message_color: tuple,
		type_color: tuple,
		message_color: tuple,
		background_color: tuple,
		icon: tuple
	) -> None:
		self.__type_name: str = type_name
		self.__time_color: tuple = time_color
		self.__status_color: tuple = status_color
		self.__status_message_color: tuple = status_message_color
		self.__type_color: tuple = type_color
		self.__message_color: tuple = message_color
		self.__background_color: tuple = background_color
		self.__icon: tuple = icon

	@property
	def type_name(self) -> str:
		return self.__type_name

	@property
	def time_color(self) -> tuple:
		return self.__time_color

	@property
	def status_color(self) -> tuple:
		return self.__status_color

	@property
	def status_message_color(self) -> tuple:
		return self.__status_message_color

	@property
	def type_color(self) -> tuple:
		return self.__type_color

	@property
	def message_color(self) -> tuple:
		return self.__message_color

	@property
	def background_color(self) -> tuple:
		return self.__background_color

	@property
	def icon(self) -> tuple:
		return self.__icon

class ServiceLogger:
	initial = (
		(
			(AnsiColor('GOLD', "foreground"), AnsiColor('INDIGO', "foreground")),
			(HexColor('GOLD'), HexColor('INDIGO')),
			("", "")
		), (
			("", AnsiColor('GOLD', "background")),
			("", HexColor('GOLD')),
			("", "")
		)
	)

class LoggerEntryTypes:
	debug = EntryType(
		type_name="%DEBUG",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('BURLYWOOD'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('TAN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('TAN', "background")),
			("", HexColor('TAN')),
			("", "")
		),
		icon=('🐛', '🐞', '🚧', '🔬')
	)
	"""
	Debugging information logging:
	Can be used to log entry any information while debugging an application.
	"""
	debug_performance = EntryType(
		type_name="%DEBUG PERFORMANCE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('NAVAJOWHITE', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('NAVAJOWHITE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('WHEAT', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('WHEAT'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('WHEAT', "background")),
			("", HexColor('WHEAT')),
			("", "")
		),
		icon=('⏱️', '⌛️', '🔍', '📈')
	)
	"""
	Performance debugging information logging:
	Can be used to log entry the execution time of operations or other
	performance information while the application is being debugged.
	"""
	performance = EntryType(
		type_name="%PERFORMANCE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('BLANCHEDALMOND', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('BLANCHEDALMOND'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('BISQUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('BISQUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('BISQUE', "background")),
			("", HexColor('BISQUE')),
			("", "")
		),
		icon=('⏱️', '🚀', '📊', '⚡️')
	)
	"""
	Performance information logging:
	Can be used to log entry the execution time of operations or
	other application performance information.
	"""
	event = EntryType(
		type_name="~EVENT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREENYELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('GREENYELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('YELLOWGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('YELLOWGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('YELLOWGREEN', "background")),
			("", HexColor('YELLOWGREEN')),
			("", "")
		),
		icon=('🔔', '🎉', '📣', '🚨')
	)
	"""
	Event information logging:
	Can be used to log entry specific events in the application,
	such as button presses or mouse cursor movements.
	"""
	audit = EntryType(
		type_name="~AUDIT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('MEDIUMSPRINGGREEN', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('MEDIUMSPRINGGREEN'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SPRINGGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('SPRINGGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SPRINGGREEN', "background")),
			("", HexColor('SPRINGGREEN')),
			("", "")
		),
		icon=('🔍', '🔒', '📋', '🔐')
	)
	"""
	Audit information logging:
	Can be used to log entry changes in the system, such as creating or
	deleting users, as well as changes in security settings.
	"""
	metrics = EntryType(
		type_name="~METRICS",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('PALEGREEN', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('PALEGREEN'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('LIGHTGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('LIGHTGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('LIGHTGREEN', "background")),
			("", HexColor('LIGHTGREEN')),
			("", "")
		),
		icon=('📊', '📈', '📉', '📄')
	)
	"""
	Metrics information logging:
	Can be used to log entry metrics to track application performance and identify issues.
	"""
	user = EntryType(
		type_name="~USER",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('CHARTREUSE', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('CHARTREUSE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('LAWNGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('LAWNGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('LAWNGREEN', "background")),
			("", HexColor('LAWNGREEN')),
			("", "")
		),
		icon=('👤', '👥', '🙋‍♂️', '🙋‍♀️')
	)
	"""
	User information logging:
	Can be used to log entry custom logs to store additional information
	that may be useful for diagnosing problems.
	"""
	message = EntryType(
		type_name="@MESSAGE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('PALETURQUOISE', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('PALETURQUOISE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('POWDERBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('POWDERBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('POWDERBLUE', "background")),
			("", HexColor('POWDERBLUE')),
			("", "")
		),
		icon=('💬', '📝', '🗒️', '📨')
	)
	"""
	Message information logging:
	Can be used for the usual output of ordinary messages about the program's operation.
	"""
	info = EntryType(
		type_name="@INFO",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SKYBLUE', "background")),
			("", HexColor('SKYBLUE')),
			("", "")
		),
		icon=('ℹ️', '🔍', '📌', '🔔')
	)
	"""
	Default information logging:
	Can be used to log entry messages with specific content about the operation of the program.
	"""
	notice = EntryType(
		type_name="@NOTICE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('LIGHTBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('LIGHTSTEELBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('LIGHTSTEELBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('LIGHTSTEELBLUE', "background")),
			("", HexColor('LIGHTSTEELBLUE')),
			("", "")
		),
		icon=('📌', '📎', '🔖', '🚩')
	)
	"""
	Notice information logging:
	Can be used to flag important events that might be missed with a normal logging level.
	"""
	warning = EntryType(
		type_name="!WARNING",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('YELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKYELLOW', "background")),
			("", HexColor('DARKYELLOW')),
			("", "")
		),
		icon=('⚠️', '⚡️', '⛔️', '⚠️')
	)
	"""
	Warning information logging:
	Can be used to log entry warnings that the program may work with unpredictable results.
	"""
	error = EntryType(
		type_name="!!ERROR",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")),
			(HexColor('ORCHID'), HexColor('PLUM')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")),
			(HexColor('DARKORANGE'), HexColor('DARKORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('GAINSBORO', "foreground")),
			(HexColor('FIREBRICK'), HexColor('GAINSBORO')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTGRAY', "foreground")),
			(HexColor('DARKRED'), HexColor('LIGHTGRAY')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKRED', "background")),
			("", HexColor('DARKRED')),
			("", "")
		),
		icon=('❌', '🚫', '💔', '🔺')
	)
	"""
	Error information logging:
	Used to log entry errors and crashes in the program.
	"""
	critical = EntryType(
		type_name="!!!@CRITICAL",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")),
			(HexColor('ORCHID'), HexColor('PLUM')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")),
			(HexColor('DARKORANGE'), HexColor('DARKORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('DARKSALMON', "foreground")),
			(HexColor('FIREBRICK'), HexColor('DARKSALMON')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTSALMON', "foreground")),
			(HexColor('DARKRED'), HexColor('LIGHTSALMON')),
			("", "")
		),
		background_color=(
			("", AnsiColor('MAROON', "background")),
			("", HexColor('MAROON')),
			("", "")
		),
		icon=('🔥', '🚨', '⛔️', '🚒')
	)
	"""
	Critical error information logging:
	Used to log entry for critical and unpredictable program failures.
	"""
	resolved = EntryType(
		type_name="!RESOLVED",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")),
			(HexColor('DARKORANGE'), HexColor('LAWNGREEN')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('✅', '❗', '🟦', '🟢')
	)
	"""
	Resolved information logging:
	Used to log entry resolved solutions to problems and errors.
	\n
	Since v0.6.0
	"""
	unresolved = EntryType(
		type_name="!UNRESOLVED",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")),
			(HexColor('DARKORANGE'), HexColor('DARKORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKRED', "background")),
			("", HexColor('DARKRED')),
			("", "")
		),
		icon=('❎', '❓', '🟥', '🔴')
	)
	"""
	Unresolved information logging:
	Used to log entry unresolved solutions to problems and errors.
	\n
	Since v0.6.0
	"""

class ProcessEntryTypes:
	achievement = EntryType(
		type_name="&ACHIEVEMENT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('YELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKYELLOW', "background")),
			("", HexColor('DARKYELLOW')),
			("", "")
		),
		icon=('🏆', '🏆', '🌟', '🎖️')
	)
	"""
	Achievement information logging:
	Used to log entry the achievements gained while executing a process.
	"""
	milestone = EntryType(
		type_name="&MILESTONE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")),
			(HexColor('DARKORANGE'), HexColor('LAWNGREEN')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('🔖', '🔖', '🎯', '🗺️')
	)
	"""
	Milestone information logging:
	Used to log entry the milestones gained while executing a process.
	"""

class ServiceProcessEntryTypes:
	initiation = EntryType(
		type_name="&INITIATION",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")),
			(HexColor('DARKORANGE'), HexColor('LAWNGREEN')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('🚀', '🚀', '🔥', '🔧')
	)
	"""
	Initiation information logging:
	Used to explain the running process.
	"""
	process = EntryType(
		type_name="&PROGRESS",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SKYBLUE', "background")),
			("", HexColor('SKYBLUE')),
			("", "")
		),
		icon=('⏳', '🔄', '⚙️', '🕰️')
	)
	"""
	...
	"""
	success = EntryType(
		type_name="&SUCCESS",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")),
			(HexColor('DARKORANGE'), HexColor('LAWNGREEN')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('✔️', '🎉', '👍', '✅')
	)
	"""
	Success information logging:
	Used to log entry a message about the success of the process.
	"""
	fail = EntryType(
		type_name="&FAIL",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")),
			(HexColor('DARKORANGE'), HexColor('DARKORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKRED', "background")),
			("", HexColor('DARKRED')),
			("", "")
		),
		icon=('❌', '🚫', '👎', '❎')
	)
	"""
	Fail information logging:
	Used to log entry a message about the failed execution of the process.
	"""

class ServiceTimerEntryTypes:
	start_timer = EntryType(
		type_name="^START TIMER",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")),
			(HexColor('DARKORANGE'), HexColor('LAWNGREEN')),
			("", "")
		),
		type_color=(
			(AnsiColor('SEAGREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			(HexColor('SEAGREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('FORESTGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			(HexColor('FORESTGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('FORESTGREEN', "background")),
			("", HexColor('FORESTGREEN')),
			("", "")
		),
		icon=('⏰', '🕑', '🟩', '⏳')
	)
	"""
	Information logging of starting Timer:
	Used to notify the start of the Timer.
	"""
	timer_mark = EntryType(
		type_name="^TIMER MARK",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('KHAKI', "foreground"), AnsiColor('SIENNA', "foreground")),
			(HexColor('KHAKI'), HexColor('SIENNA')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKKHAKI', "foreground"), AnsiColor('SADDLEBROWN', "foreground")),
			(HexColor('DARKKHAKI'), HexColor('SADDLEBROWN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKKHAKI', "background")),
			("", HexColor('DARKKHAKI')),
			("", "")
		),
		icon=('⌚', '🕕', '🟨', '⏱️')
	)
	"""
	Information logging of mark Timer:
	Used to notify the mark of the Timer.
	"""
	stop_timer = EntryType(
		type_name="^STOP TIMER",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		status_message_color=(
			(AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")),
			(HexColor('DARKORANGE'), HexColor('MAROON')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SKYBLUE', "background")),
			("", HexColor('SKYBLUE')),
			("", "")
		),
		icon=('⏲️', '🕙', '🟪', '⌛')
	)
	"""
	Information logging of stopping Timer:
	Used to notify the stop of the Timer.
	"""
