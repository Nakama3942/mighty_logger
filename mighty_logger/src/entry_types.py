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
		type_name: str,
		time_color: list,
		status_color: list,
		status_message_color: list,
		type_color: list,
		message_color: list,
		background_color: list,
		icon: list
	) -> None:
		self.__type_name: str = type_name
		self.__time_color: list = time_color
		self.__status_color: list = status_color
		self.__status_message_color: list = status_message_color
		self.__type_color: list = type_color
		self.__message_color: list = message_color
		self.__background_color: list = background_color
		self.__icon: list = icon

	@property
	def type_name(self) -> str:
		return self.__type_name

	@property
	def time_color(self) -> list:
		return self.__time_color

	@property
	def status_color(self) -> list:
		return self.__status_color

	@property
	def status_message_color(self) -> list:
		return self.__status_message_color

	@property
	def type_color(self) -> list:
		return self.__type_color

	@property
	def message_color(self) -> list:
		return self.__message_color

	@property
	def background_color(self) -> list:
		return self.__background_color

	@property
	def icon(self) -> list:
		return self.__icon

class ServiceLogger:
	initial = [
		[
			[AnsiColor('GOLD', "foreground"), AnsiColor('INDIGO', "foreground")],
			[HexColor('GOLD'), HexColor('INDIGO')]
		], [
			["", AnsiColor('GOLD', "background")],
			["", HexColor('GOLD')]
		]
	]

class LoggerEntryTypes:
	debug = EntryType(
		"%DEBUG",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('BURLYWOOD'), HexColor('NAVY')]
		], [
			[AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('TAN'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('TAN', "background")],
			["", HexColor('TAN')]
		],
		['🐛', '🐞', '🚧', '🔬']
	)
	"""
	Debugging information logging:
	Can be used to log entry any information while debugging an application.
	"""
	debug_performance = EntryType(
		"%DEBUG PERFORMANCE",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('NAVAJOWHITE', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('NAVAJOWHITE'), HexColor('NAVY')]
		], [
			[AnsiColor('WHEAT', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('WHEAT'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('WHEAT', "background")],
			["", HexColor('WHEAT')]
		],
		['⏱️', '⌛️', '🔍', '📈']
	)
	"""
	Performance debugging information logging:
	Can be used to log entry the execution time of operations or other
	performance information while the application is being debugged.
	"""
	performance = EntryType(
		"%PERFORMANCE",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('BLANCHEDALMOND', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('BLANCHEDALMOND'), HexColor('NAVY')]
		], [
			[AnsiColor('BISQUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('BISQUE'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('BISQUE', "background")],
			["", HexColor('BISQUE')]
		],
		['⏱️', '🚀', '📊', '⚡️']
	)
	"""
	Performance information logging:
	Can be used to log entry the execution time of operations or
	other application performance information.
	"""
	event = EntryType(
		"~EVENT",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('GREENYELLOW', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('GREENYELLOW'), HexColor('NAVY')]
		], [
			[AnsiColor('YELLOWGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('YELLOWGREEN'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('YELLOWGREEN', "background")],
			["", HexColor('YELLOWGREEN')]
		],
		['🔔', '🎉', '📣', '🚨']
	)
	"""
	Event information logging:
	Can be used to log entry specific events in the application,
	such as button presses or mouse cursor movements.
	"""
	audit = EntryType(
		"~AUDIT",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('MEDIUMSPRINGGREEN', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('MEDIUMSPRINGGREEN'), HexColor('NAVY')]
		], [
			[AnsiColor('SPRINGGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('SPRINGGREEN'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('SPRINGGREEN', "background")],
			["", HexColor('SPRINGGREEN')]
		],
		['🔍', '🔒', '📋', '🔐']
	)
	"""
	Audit information logging:
	Can be used to log entry changes in the system, such as creating or
	deleting users, as well as changes in security settings.
	"""
	metrics = EntryType(
		"~METRICS",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('PALEGREEN', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('PALEGREEN'), HexColor('NAVY')]
		], [
			[AnsiColor('LIGHTGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('LIGHTGREEN'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('LIGHTGREEN', "background")],
			["", HexColor('LIGHTGREEN')]
		],
		['📊', '📈', '📉', '📄']
	)
	"""
	Metrics information logging:
	Can be used to log entry metrics to track application performance and identify issues.
	"""
	user = EntryType(
		"~USER",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('CHARTREUSE', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('CHARTREUSE'), HexColor('NAVY')]
		], [
			[AnsiColor('LAWNGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('LAWNGREEN'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('LAWNGREEN', "background")],
			["", HexColor('LAWNGREEN')]
		],
		['👤', '👥', '🙋‍♂️', '🙋‍♀️']
	)
	"""
	User information logging:
	Can be used to log entry custom logs to store additional information
	that may be useful for diagnosing problems.
	"""
	message = EntryType(
		"@MESSAGE",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('PALETURQUOISE', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('PALETURQUOISE'), HexColor('NAVY')]
		], [
			[AnsiColor('POWDERBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('POWDERBLUE'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('POWDERBLUE', "background")],
			["", HexColor('POWDERBLUE')]
		],
		['💬', '📝', '🗒️', '📨']
	)
	"""
	Message information logging:
	Can be used for the usual output of ordinary messages about the program's operation.
	"""
	info = EntryType(
		"@INFO",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
		], [
			[AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('SKYBLUE', "background")],
			["", HexColor('SKYBLUE')]
		],
		['ℹ️', '🔍', '📌', '🔔']
	)
	"""
	Default information logging:
	Can be used to log entry messages with specific content about the operation of the program.
	"""
	notice = EntryType(
		"@NOTICE",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('LIGHTBLUE', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('LIGHTBLUE'), HexColor('NAVY')]
		], [
			[AnsiColor('LIGHTSTEELBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('LIGHTSTEELBLUE'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('LIGHTSTEELBLUE', "background")],
			["", HexColor('LIGHTSTEELBLUE')]
		],
		['📌', '📎', '🔖', '🚩']
	)
	"""
	Notice information logging:
	Can be used to flag important events that might be missed with a normal logging level.
	"""
	warning = EntryType(
		"!WARNING",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('YELLOW'), HexColor('NAVY')]
		], [
			[AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('DARKYELLOW', "background")],
			["", HexColor('DARKYELLOW')]
		],
		['⚠️', '⚡️', '⛔️', '⚠️']
	)
	"""
	Warning information logging:
	Can be used to log entry warnings that the program may work with unpredictable results.
	"""
	error = EntryType(
		"!!ERROR",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")],
			[HexColor('ORCHID'), HexColor('PLUM')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")],
			[HexColor('ORANGE'), HexColor('ORANGE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")],
			[HexColor('DARKORANGE'), HexColor('DARKORANGE')]
		], [
			[AnsiColor('FIREBRICK', "foreground"), AnsiColor('GAINSBORO', "foreground")],
			[HexColor('FIREBRICK'), HexColor('GAINSBORO')]
		], [
			[AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTGRAY', "foreground")],
			[HexColor('DARKRED'), HexColor('LIGHTGRAY')]
		], [
			["", AnsiColor('DARKRED', "background")],
			["", HexColor('DARKRED')]
		],
		['❌', '🚫', '💔', '🔺']
	)
	"""
	Error information logging:
	Used to log entry errors and crashes in the program.
	"""
	critical = EntryType(
		"!!!@CRITICAL",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")],
			[HexColor('ORCHID'), HexColor('PLUM')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")],
			[HexColor('ORANGE'), HexColor('ORANGE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")],
			[HexColor('DARKORANGE'), HexColor('DARKORANGE')]
		], [
			[AnsiColor('FIREBRICK', "foreground"), AnsiColor('DARKSALMON', "foreground")],
			[HexColor('FIREBRICK'), HexColor('DARKSALMON')]
		], [
			[AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTSALMON', "foreground")],
			[HexColor('DARKRED'), HexColor('LIGHTSALMON')]
		], [
			["", AnsiColor('MAROON', "background")],
			["", HexColor('MAROON')]
		],
		['🔥', '🚨', '⛔️', '🚒']
	)
	"""
	Critical error information logging:
	Used to log entry for critical and unpredictable program failures.
	"""
	resolved = EntryType(
		"!RESOLVED",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")],
			[HexColor('ORANGE'), HexColor('CHARTREUSE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")],
			[HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
		], [
			[AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")],
			[HexColor('GREEN'), HexColor('PALEGREEN')]
		], [
			[AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")],
			[HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
		], [
			["", AnsiColor('DARKGREEN', "background")],
			["", HexColor('DARKGREEN')]
		],
		['✅', '❗', '🟦', '🟢']
	)
	"""
	Resolved information logging:
	Used to log entry resolved solutions to problems and errors.
	\n
	Since v0.6.0
	"""
	unresolved = EntryType(
		"!UNRESOLVED",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")],
			[HexColor('ORANGE'), HexColor('ORANGE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")],
			[HexColor('DARKORANGE'), HexColor('DARKORANGE')]
		], [
			[AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")],
			[HexColor('FIREBRICK'), HexColor('YELLOW')]
		], [
			[AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")],
			[HexColor('DARKRED'), HexColor('DARKYELLOW')]
		], [
			["", AnsiColor('DARKRED', "background")],
			["", HexColor('DARKRED')]
		],
		['❎', '❓', '🟥', '🔴']
	)
	"""
	Unresolved information logging:
	Used to log entry unresolved solutions to problems and errors.
	\n
	Since v0.6.0
	"""

class ProcessEntryTypes:
	achievement = EntryType(
		"&ACHIEVEMENT",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('YELLOW'), HexColor('NAVY')]
		], [
			[AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('DARKYELLOW', "background")],
			["", HexColor('DARKYELLOW')]
		],
		['🏆', '🏆', '🌟', '🎖️']
	)
	"""
	Achievement information logging:
	Used to log entry the achievements gained while executing a process.
	"""
	milestone = EntryType(
		"&MILESTONE",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")],
			[HexColor('ORANGE'), HexColor('CHARTREUSE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")],
			[HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
		], [
			[AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")],
			[HexColor('GREEN'), HexColor('PALEGREEN')]
		], [
			[AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")],
			[HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
		], [
			["", AnsiColor('DARKGREEN', "background")],
			["", HexColor('DARKGREEN')]
		],
		['🔖', '🔖', '🎯', '🗺️']
	)
	"""
	Milestone information logging:
	Used to log entry the milestones gained while executing a process.
	"""

class ServiceProcessEntryTypes:
	initiation = EntryType(
		"&INITIATION",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")],
			[HexColor('ORANGE'), HexColor('CHARTREUSE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")],
			[HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
		], [
			[AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")],
			[HexColor('GREEN'), HexColor('PALEGREEN')]
		], [
			[AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")],
			[HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
		], [
			["", AnsiColor('DARKGREEN', "background")],
			["", HexColor('DARKGREEN')]
		],
		['🚀', '🚀', '🔥', '🔧']
	)
	"""
	Initiation information logging:
	Used to explain the running process.
	"""
	process = EntryType(
		"&PROGRESS",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")],
			[HexColor('ORCHID'), HexColor('PURPLE')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
		], [
			[AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('SKYBLUE', "background")],
			["", HexColor('SKYBLUE')]
		],
		['⏳', '🔄', '⚙️', '🕰️']
	)
	"""
	...
	"""
	success = EntryType(
		"&SUCCESS",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")],
			[HexColor('ORANGE'), HexColor('CHARTREUSE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")],
			[HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
		], [
			[AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")],
			[HexColor('GREEN'), HexColor('PALEGREEN')]
		], [
			[AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")],
			[HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
		], [
			["", AnsiColor('DARKGREEN', "background")],
			["", HexColor('DARKGREEN')]
		],
		['✔️', '🎉', '👍', '✅']
	)
	"""
	Success information logging:
	Used to log entry a message about the success of the process.
	"""
	fail = EntryType(
		"&FAIL",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")],
			[HexColor('ORANGE'), HexColor('ORANGE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")],
			[HexColor('DARKORANGE'), HexColor('DARKORANGE')]
		], [
			[AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")],
			[HexColor('FIREBRICK'), HexColor('YELLOW')]
		], [
			[AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")],
			[HexColor('DARKRED'), HexColor('DARKYELLOW')]
		], [
			["", AnsiColor('DARKRED', "background")],
			["", HexColor('DARKRED')]
		],
		['❌', '🚫', '👎', '❎']
	)
	"""
	Fail information logging:
	Used to log entry a message about the failed execution of the process.
	"""

class ServiceTimerEntryTypes:
	start_timer = EntryType(
		"^START TIMER",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")],
			[HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")],
			[HexColor('ORANGE'), HexColor('CHARTREUSE')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")],
			[HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
		], [
			[AnsiColor('SEAGREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")],
			[HexColor('SEAGREEN'), HexColor('PALEGREEN')]
		], [
			[AnsiColor('FORESTGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")],
			[HexColor('FORESTGREEN'), HexColor('LIGHTGREEN')]
		], [
			["", AnsiColor('FORESTGREEN', "background")],
			["", HexColor('FORESTGREEN')]
		],
		['⏰', '🕑', '🟩', '⏳']
	)
	"""
	Information logging of starting Timer:
	Used to notify the start of the Timer.
	"""
	timer_mark = EntryType(
		"^TIMER MARK",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")],
			[HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('KHAKI', "foreground"), AnsiColor('SIENNA', "foreground")],
			[HexColor('KHAKI'), HexColor('SIENNA')]
		], [
			[AnsiColor('DARKKHAKI', "foreground"), AnsiColor('SADDLEBROWN', "foreground")],
			[HexColor('DARKKHAKI'), HexColor('SADDLEBROWN')]
		], [
			["", AnsiColor('DARKKHAKI', "background")],
			["", HexColor('DARKKHAKI')]
		],
		['⌚', '🕕', '🟨', '⏱️']
	)
	"""
	Information logging of mark Timer:
	Used to notify the mark of the Timer.
	"""
	stop_timer = EntryType(
		"^STOP TIMER",
		[
			[AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")],
			[HexColor('ORCHID'), HexColor('PURPLE')]
		], [
			[AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")],
			[HexColor('ORANGE'), HexColor('DARKRED')]
		], [
			[AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")],
			[HexColor('DARKORANGE'), HexColor('MAROON')]
		], [
			[AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")],
			[HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
		], [
			[AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")],
			[HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
		], [
			["", AnsiColor('SKYBLUE', "background")],
			["", HexColor('SKYBLUE')]
		],
		['⏲️', '🕙', '🟪', '⌛']
	)
	"""
	Information logging of stopping Timer:
	Used to notify the stop of the Timer.
	"""
