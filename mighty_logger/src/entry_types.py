"""
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

from mighty_logger.basic.lib_types.entry_type import EntryType
from mighty_logger.src.color_picker import AnsiColor, HexColor

class ServiceLogger:
	initial = (
		(
			(AnsiColor('GOLD', "foreground"), AnsiColor('INDIGO', "foreground")),
			("", ""),
			(HexColor('GOLD'), HexColor('INDIGO')),
			(HexColor('GOLD'), HexColor('INDIGO')),
			("", "")
		), (
			("", AnsiColor('GOLD', "background")),
			("", ""),
			("", HexColor('GOLD')),
			("", HexColor('GOLD')),
			("", "")
		)
	)

class LoggerEntryTypes:
	debug = EntryType(
		type_category="%",
		type_name="DEBUG",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('BURLYWOOD'), HexColor('NAVY')),
			(HexColor('BURLYWOOD'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('TAN'), HexColor('MIDNIGHTBLUE')),
			(HexColor('TAN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('TAN', "background")),
			("", ""),
			("", HexColor('TAN')),
			("", HexColor('TAN')),
			("", "")
		),
		icon=('🐛', '🐞', '🚧', '🔬')
	)
	debug_performance = EntryType(
		type_category="%",
		type_name="DEBUG-PERFORMANCE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('NAVAJOWHITE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('NAVAJOWHITE'), HexColor('NAVY')),
			(HexColor('NAVAJOWHITE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('WHEAT', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('WHEAT'), HexColor('MIDNIGHTBLUE')),
			(HexColor('WHEAT'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('WHEAT', "background")),
			("", ""),
			("", HexColor('WHEAT')),
			("", HexColor('WHEAT')),
			("", "")
		),
		icon=('⏱️', '⌛️', '🔍', '📈')
	)
	performance = EntryType(
		type_category="%",
		type_name="PERFORMANCE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('BLANCHEDALMOND', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('BLANCHEDALMOND'), HexColor('NAVY')),
			(HexColor('BLANCHEDALMOND'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('BISQUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('BISQUE'), HexColor('MIDNIGHTBLUE')),
			(HexColor('BISQUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('BISQUE', "background")),
			("", ""),
			("", HexColor('BISQUE')),
			("", HexColor('BISQUE')),
			("", "")
		),
		icon=('⏱️', '🚀', '📊', '⚡️')
	)
	event = EntryType(
		type_category="~",
		type_name="EVENT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREENYELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('GREENYELLOW'), HexColor('NAVY')),
			(HexColor('GREENYELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('YELLOWGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('YELLOWGREEN'), HexColor('MIDNIGHTBLUE')),
			(HexColor('YELLOWGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('YELLOWGREEN', "background")),
			("", ""),
			("", HexColor('YELLOWGREEN')),
			("", HexColor('YELLOWGREEN')),
			("", "")
		),
		icon=('🔔', '🎉', '📣', '🚨')
	)
	audit = EntryType(
		type_category="~",
		type_name="AUDIT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('MEDIUMSPRINGGREEN', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('MEDIUMSPRINGGREEN'), HexColor('NAVY')),
			(HexColor('MEDIUMSPRINGGREEN'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SPRINGGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('SPRINGGREEN'), HexColor('MIDNIGHTBLUE')),
			(HexColor('SPRINGGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SPRINGGREEN', "background")),
			("", ""),
			("", HexColor('SPRINGGREEN')),
			("", HexColor('SPRINGGREEN')),
			("", "")
		),
		icon=('🔍', '🔒', '📋', '🔐')
	)
	metrics = EntryType(
		type_category="~",
		type_name="METRICS",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('PALEGREEN', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('PALEGREEN'), HexColor('NAVY')),
			(HexColor('PALEGREEN'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('LIGHTGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('LIGHTGREEN'), HexColor('MIDNIGHTBLUE')),
			(HexColor('LIGHTGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('LIGHTGREEN', "background")),
			("", ""),
			("", HexColor('LIGHTGREEN')),
			("", HexColor('LIGHTGREEN')),
			("", "")
		),
		icon=('📊', '📈', '📉', '📄')
	)
	user = EntryType(
		type_category="~",
		type_name="USER",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('CHARTREUSE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('CHARTREUSE'), HexColor('NAVY')),
			(HexColor('CHARTREUSE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('LAWNGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('LAWNGREEN'), HexColor('MIDNIGHTBLUE')),
			(HexColor('LAWNGREEN'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('LAWNGREEN', "background")),
			("", ""),
			("", HexColor('LAWNGREEN')),
			("", HexColor('LAWNGREEN')),
			("", "")
		),
		icon=('👤', '👥', '🙋‍♂️', '🙋‍♀️')
	)
	message = EntryType(
		type_category="@",
		type_name="MESSAGE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('PALETURQUOISE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('PALETURQUOISE'), HexColor('NAVY')),
			(HexColor('PALETURQUOISE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('POWDERBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('POWDERBLUE'), HexColor('MIDNIGHTBLUE')),
			(HexColor('POWDERBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('POWDERBLUE', "background")),
			("", ""),
			("", HexColor('POWDERBLUE')),
			("", HexColor('POWDERBLUE')),
			("", "")
		),
		icon=('💬', '📝', '🗒️', '📨')
	)
	info = EntryType(
		type_category="@",
		type_name="INFO",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SKYBLUE', "background")),
			("", ""),
			("", HexColor('SKYBLUE')),
			("", HexColor('SKYBLUE')),
			("", "")
		),
		icon=('ℹ️', '🔍', '📌', '🔔')
	)
	notice = EntryType(
		type_category="@",
		type_name="NOTICE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('LIGHTBLUE'), HexColor('NAVY')),
			(HexColor('LIGHTBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('LIGHTSTEELBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('LIGHTSTEELBLUE'), HexColor('MIDNIGHTBLUE')),
			(HexColor('LIGHTSTEELBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('LIGHTSTEELBLUE', "background")),
			("", ""),
			("", HexColor('LIGHTSTEELBLUE')),
			("", HexColor('LIGHTSTEELBLUE')),
			("", "")
		),
		icon=('📌', '📎', '🔖', '🚩')
	)
	warning = EntryType(
		type_category="!",
		type_name="WARNING",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('YELLOW'), HexColor('NAVY')),
			(HexColor('YELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKYELLOW', "background")),
			("", ""),
			("", HexColor('DARKYELLOW')),
			("", HexColor('DARKYELLOW')),
			("", "")
		),
		icon=('⚠️', '⚡️', '⛔️', '⚠️')
	)
	error = EntryType(
		type_category="!",
		type_name="!ERROR",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('PLUM')),
			(HexColor('ORCHID'), HexColor('PLUM')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('GAINSBORO', "foreground")),
			("", ""),
			(HexColor('FIREBRICK'), HexColor('GAINSBORO')),
			(HexColor('FIREBRICK'), HexColor('GAINSBORO')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTGRAY', "foreground")),
			("", ""),
			(HexColor('DARKRED'), HexColor('LIGHTGRAY')),
			(HexColor('DARKRED'), HexColor('LIGHTGRAY')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKRED', "background")),
			("", ""),
			("", HexColor('DARKRED')),
			("", HexColor('DARKRED')),
			("", "")
		),
		icon=('❌', '🚫', '💔', '🔺')
	)
	critical = EntryType(
		type_category="!",
		type_name="!!@CRITICAL",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('PLUM')),
			(HexColor('ORCHID'), HexColor('PLUM')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('DARKSALMON', "foreground")),
			("", ""),
			(HexColor('FIREBRICK'), HexColor('DARKSALMON')),
			(HexColor('FIREBRICK'), HexColor('DARKSALMON')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTSALMON', "foreground")),
			("", ""),
			(HexColor('DARKRED'), HexColor('LIGHTSALMON')),
			(HexColor('DARKRED'), HexColor('LIGHTSALMON')),
			("", "")
		),
		background_color=(
			("", AnsiColor('MAROON', "background")),
			("", ""),
			("", HexColor('MAROON')),
			("", HexColor('MAROON')),
			("", "")
		),
		icon=('🔥', '🚨', '⛔️', '🚒')
	)
	resolved = EntryType(
		type_category="!",
		type_name="RESOLVED",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			("", ""),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			("", ""),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", ""),
			("", HexColor('DARKGREEN')),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('✅', '❗', '🟦', '🟢')
	)
	unresolved = EntryType(
		type_category="!",
		type_name="UNRESOLVED",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")),
			("", ""),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")),
			("", ""),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKRED', "background")),
			("", ""),
			("", HexColor('DARKRED')),
			("", HexColor('DARKRED')),
			("", "")
		),
		icon=('❎', '❓', '🟥', '🔴')
	)

class ProcessEntryTypes:
	achievement = EntryType(
		type_category="&",
		type_name="ACHIEVEMENT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('YELLOW'), HexColor('NAVY')),
			(HexColor('YELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKYELLOW', "background")),
			("", ""),
			("", HexColor('DARKYELLOW')),
			("", HexColor('DARKYELLOW')),
			("", "")
		),
		icon=('🏆', '🏆', '🌟', '🎖️')
	)
	milestone = EntryType(
		type_category="&",
		type_name="MILESTONE",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			("", ""),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			("", ""),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", ""),
			("", HexColor('DARKGREEN')),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('🔖', '🔖', '🎯', '🗺️')
	)

class ServiceProcessEntryTypes:
	initiation = EntryType(
		type_category="&",
		type_name="INITIATION",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			("", ""),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			("", ""),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", ""),
			("", HexColor('DARKGREEN')),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('🚀', '🚀', '🔥', '🔧')
	)
	process = EntryType(
		type_category="&",
		type_name="PROGRESS",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SKYBLUE', "background")),
			("", ""),
			("", HexColor('SKYBLUE')),
			("", HexColor('SKYBLUE')),
			("", "")
		),
		icon=('⏳', '🔄', '⚙️', '🕰️')
	)
	success = EntryType(
		type_category="&",
		type_name="SUCCESS",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			("", ""),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			("", ""),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", ""),
			("", HexColor('DARKGREEN')),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('✔️', '🎉', '👍', '✅')
	)
	fail = EntryType(
		type_category="&",
		type_name="FAIL",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")),
			("", ""),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")),
			("", ""),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKRED', "background")),
			("", ""),
			("", HexColor('DARKRED')),
			("", HexColor('DARKRED')),
			("", "")
		),
		icon=('❌', '🚫', '👎', '❎')
	)

class ServiceTimerEntryTypes:
	start_timer = EntryType(
		type_category="^",
		type_name="START-TIMER",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		type_color=(
			(AnsiColor('SEAGREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			("", ""),
			(HexColor('SEAGREEN'), HexColor('PALEGREEN')),
			(HexColor('SEAGREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('FORESTGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			("", ""),
			(HexColor('FORESTGREEN'), HexColor('LIGHTGREEN')),
			(HexColor('FORESTGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('FORESTGREEN', "background")),
			("", ""),
			("", HexColor('FORESTGREEN')),
			("", HexColor('FORESTGREEN')),
			("", "")
		),
		icon=('⏰', '🕑', '🟩', '⏳')
	)
	timer_mark = EntryType(
		type_category="^",
		type_name="TIMER-MARK",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('KHAKI', "foreground"), AnsiColor('SIENNA', "foreground")),
			("", ""),
			(HexColor('KHAKI'), HexColor('SIENNA')),
			(HexColor('KHAKI'), HexColor('SIENNA')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKKHAKI', "foreground"), AnsiColor('SADDLEBROWN', "foreground")),
			("", ""),
			(HexColor('DARKKHAKI'), HexColor('SADDLEBROWN')),
			(HexColor('DARKKHAKI'), HexColor('SADDLEBROWN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKKHAKI', "background")),
			("", ""),
			("", HexColor('DARKKHAKI')),
			("", HexColor('DARKKHAKI')),
			("", "")
		),
		icon=('⌚', '🕕', '🟨', '⏱️')
	)
	stop_timer = EntryType(
		type_category="^",
		type_name="STOP-TIMER",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SKYBLUE', "background")),
			("", ""),
			("", HexColor('SKYBLUE')),
			("", HexColor('SKYBLUE')),
			("", "")
		),
		icon=('⏲️', '🕙', '🟪', '⌛')
	)

class AdditionalEntryTypes:
	hint = EntryType(
		type_category="/",
		type_name="HINT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			("", ""),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			("", ""),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", ""),
			("", HexColor('DARKGREEN')),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('🔍', '🔎', '🕵️', '🔬')
	)
	tip = EntryType(
		type_category="/",
		type_name="TIP",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			(HexColor('ORANGE'), HexColor('CHARTREUSE')),
			("", "")
		),
		type_color=(
			(AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")),
			("", ""),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			(HexColor('GREEN'), HexColor('PALEGREEN')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")),
			("", ""),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			(HexColor('DARKGREEN'), HexColor('LIGHTGREEN')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKGREEN', "background")),
			("", ""),
			("", HexColor('DARKGREEN')),
			("", HexColor('DARKGREEN')),
			("", "")
		),
		icon=('💡', '🌟', '🎯', '🔔')
	)
	important = EntryType(
		type_category="/",
		type_name="IMPORTANT",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			(HexColor('ORCHID'), HexColor('PURPLE')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			(HexColor('LIGHTSKYBLUE'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			(HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('SKYBLUE', "background")),
			("", ""),
			("", HexColor('SKYBLUE')),
			("", HexColor('SKYBLUE')),
			("", "")
		),
		icon=('❗️', '‼️', '⚠️', '🚨')
	)
	attention = EntryType(
		type_category="/",
		type_name="ATTENTION",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('YELLOW'), HexColor('NAVY')),
			(HexColor('YELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKYELLOW', "background")),
			("", ""),
			("", HexColor('DARKYELLOW')),
			("", HexColor('DARKYELLOW')),
			("", "")
		),
		icon=('⚡️', '⛔️', '⏰', '🛑')
	)
	caution = EntryType(
		type_category="/",
		type_name="CAUTION",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			(HexColor('ORCHID'), HexColor('DARKMAGENTA')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			(HexColor('ORANGE'), HexColor('DARKRED')),
			("", "")
		),
		type_color=(
			(AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")),
			("", ""),
			(HexColor('YELLOW'), HexColor('NAVY')),
			(HexColor('YELLOW'), HexColor('NAVY')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")),
			("", ""),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			(HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKYELLOW', "background")),
			("", ""),
			("", HexColor('DARKYELLOW')),
			("", HexColor('DARKYELLOW')),
			("", "")
		),
		icon=('⚠️', '⚡️', '⚙️', '🚧')
	)
	danger = EntryType(
		type_category="/",
		type_name="DANGER",
		time_color=(
			(AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")),
			("", ""),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			(HexColor('ORCHID'), HexColor('LAVENDERBLUSH')),
			("", "")
		),
		status_color=(
			(AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")),
			("", ""),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			(HexColor('ORANGE'), HexColor('ORANGE')),
			("", "")
		),
		type_color=(
			(AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")),
			("", ""),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			(HexColor('FIREBRICK'), HexColor('YELLOW')),
			("", "")
		),
		message_color=(
			(AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")),
			("", ""),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			(HexColor('DARKRED'), HexColor('DARKYELLOW')),
			("", "")
		),
		background_color=(
			("", AnsiColor('DARKRED', "background")),
			("", ""),
			("", HexColor('DARKRED')),
			("", HexColor('DARKRED')),
			("", "")
		),
		icon=('🔥', '💣', '☠️', '⚡️')
	)

class SelectionTypes:
	debug = EntryType(
		type_category="",
		type_name="DEBUG",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	debug_performance = EntryType(
		type_category="",
		type_name="DEBUG-PERFORMANCE",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	performance = EntryType(
		type_category="",
		type_name="PERFORMANCE",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	event = EntryType(
		type_category="",
		type_name="EVENT",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	audit = EntryType(
		type_category="",
		type_name="AUDIT",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	metrics = EntryType(
		type_category="",
		type_name="METRICS",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	user = EntryType(
		type_category="",
		type_name="USER",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	message = EntryType(
		type_category="",
		type_name="MESSAGE",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	info = EntryType(
		type_category="",
		type_name="INFO",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	notice = EntryType(
		type_category="",
		type_name="NOTICE",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	warning = EntryType(
		type_category="",
		type_name="WARNING",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	error = EntryType(
		type_category="",
		type_name="!ERROR",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	critical = EntryType(
		type_category="",
		type_name="!!@CRITICAL",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	resolved = EntryType(
		type_category="",
		type_name="RESOLVED",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	unresolved = EntryType(
		type_category="",
		type_name="UNRESOLVED",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	achievement = EntryType(
		type_category="",
		type_name="ACHIEVEMENT",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	milestone = EntryType(
		type_category="",
		type_name="MILESTONE",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	initiation = EntryType(
		type_category="",
		type_name="INITIATION",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	process = EntryType(
		type_category="",
		type_name="PROGRESS",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	success = EntryType(
		type_category="",
		type_name="SUCCESS",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	fail = EntryType(
		type_category="",
		type_name="FAIL",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	start_timer = EntryType(
		type_category="",
		type_name="START-TIMER",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	timer_mark = EntryType(
		type_category="",
		type_name="TIMER-MARK",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	stop_timer = EntryType(
		type_category="",
		type_name="STOP-TIMER",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	hint = EntryType(
		type_category="",
		type_name="HINT",
		time_color=(),
		status_color=(),
		type_color=(),
		message_color=(),
		background_color=(),
		icon=()
	)
	tip = EntryType(
		type_category="",
		type_name="TIP",
		time_color=(),
		status_color=(),
		type_color=(),
		message_color=(),
		background_color=(),
		icon=()
	)
	important = EntryType(
		type_category="",
		type_name="IMPORTANT",
		time_color=(),
		status_color=(),
		type_color=(),
		message_color=(),
		background_color=(),
		icon=()
	)
	attention = EntryType(
		type_category="",
		type_name="ATTENTION",
		time_color=(),
		status_color=(),
		type_color=(),
		message_color=(),
		background_color=(),
		icon=()
	)
	caution = EntryType(
		type_category="",
		type_name="CAUTION",
		time_color=(),
		status_color=(),
		type_color=(),
		message_color=(),
		background_color=(),
		icon=()
	)
	danger = EntryType(
		type_category="",
		type_name="DANGER",
		time_color=(),
		status_color=(),
		type_color=(),
		message_color=(),
		background_color=(),
		icon=()
	)

class SelectionCategories:
	debug = EntryType(
		type_category="%",
		type_name="",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	event = EntryType(
		type_category="~",
		type_name="",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	message = EntryType(
		type_category="@",
		type_name="",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	error = EntryType(
		type_category="!",
		type_name="",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	process = EntryType(
		type_category="&",
		type_name="",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	timer = EntryType(
		type_category="^",
		type_name="",
		time_color = (),
		status_color = (),
		type_color = (),
		message_color = (),
		background_color = (),
		icon = ()
	)
	additional = EntryType(
		type_category="/",
		type_name="",
		time_color=(),
		status_color=(),
		type_color=(),
		message_color=(),
		background_color=(),
		icon=()
	)
