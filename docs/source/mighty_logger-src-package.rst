"src" package
=============

A package with the implementation of various data (ANSI, colors, etc.).

.. versionadded:: v0.2.0

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.src import ...

Animations lists
----------------

.. currentmodule:: mighty_logger.src.animations

.. _list_of_animations:

List of animations
__________________

.. seealso::
	- `The source of Animations <https://github.com/kopensource/colored_logs/blob/develop/colored_logs/models/animation_type.py>`_

.. py:class:: IndefiniteAnimations

	The class with sets indefinite animations.

	.. versionadded:: v0.6.0

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`IndefiniteAnimationType <indefinite_animation_type>`.

	.. py:attribute:: Dots

		"Dots" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Wave

		"Wave" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: WaveAutoReverse

		"WaveAutoReverse" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Star

		"Star" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: StarAutoReverse

		"StarAutoReverse" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: StarHorizontalFill

		"StarHorizontalFill" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: StarHorizontalFillAutoReverse

		"StarHorizontalFillAutoReverse" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: Arrow

		"Arrow" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: ArrowAutoReverse

		"ArrowAutoReverse" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: Sunrise

		"Sunrise" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: Sunset

		"Sunset" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: SunriseSunset

		"SunriseSunset" animation.

		.. versionadded:: v0.6.1

	.. py:attribute:: Clock1

		"Clock1" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Clock2

		"Clock2" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Clock3

		"Clock3" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Circle

		"Circle" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: KnightRider

		"KnightRider" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: KnightRiderAutoReverse

		"KnightRiderAutoReverse" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Blocks1

		"Blocks1" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Blocks2

		"Blocks2" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Blocks3

		"Blocks3" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Blocks4

		"Blocks4" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: BlocksAutoReverse

		"BlocksAutoReverse" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: Line

		"Line" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: LineAutoReverse

		"LineAutoReverse" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: BlockVerticalFill

		"BlockVerticalFill" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: BlockVerticalFillAutoReverse

		"BlockVerticalFillAutoReverse" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: BlockHorizontalFillAutoReverse

		"BlockHorizontalFillAutoReverse" animation.

		.. versionadded:: v0.6.0

	.. py:attribute:: SuperSpace

		"SuperSpace" animation.

		.. versionadded:: v0.6.1

.. _list_of_progress_bars:

List of progress bars
_____________________

.. py:class:: DefiniteAnimations

	The class with sets definite animations.

	.. versionadded:: v0.6.0

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`DefiniteAnimationType <definite_animation_type>`.

	.. py:attribute:: Dots

		"Dots" progress bar.

		.. versionadded:: v0.6.0

	.. py:attribute:: Star

		"Star" progress bar.

		.. versionadded:: v0.6.1

	.. py:attribute:: Arrow

		"Arrow" progress bar.

		.. versionadded:: v0.6.1

	.. py:attribute:: KnightRider

		"KnightRider" progress bar.

		.. versionadded:: v0.6.0

	.. py:attribute:: Line

		"Line" progress bar.

		.. versionadded:: v0.6.0

	.. py:attribute:: BlockVerticalFill

		"BlockVerticalFill" progress bar.

		.. versionadded:: v0.6.0

ANSI Format
-----------

.. currentmodule:: mighty_logger.src.ansi_format

.. py:data:: AnsiFormat

	ANSI escape code dictionary.

	.. versionadded:: v0.2.0

	.. danger:: This is a hidden data that is inaccessible outside the library.

	.. seealso::
		Source of inspiration:

		- `ANSI escape code <https://en.wikipedia.org/wiki/ANSI_escape_code>`_
		- `ANSI Escape Sequences <https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797>`_

.. py:function:: _RecursiveGetAnsiFormat(ansi_address: str, ansi: dict) -> str

	Recursively extracts a string with an ANSI escape code from a heavily nested dictionary.

	.. versionadded:: v0.2.1

	:param ansi_address: Path to ANSI escape code value
	:type ansi_address: str
	:param ansi: External/nested dictionary
	:type ansi: dict
	:return: value - ANSI escape code
	:rtype: str

	.. danger:: This is a hidden function that is inaccessible outside the library.

.. py:function:: GetAnsiFormat(ansi_address: str) -> str

	Returns the ANSI escape code value.

	The following values are possible: see the list in :ref:`Tree of ANSI escape code <ansi>`.

	An example of getting an ANSI escape code:

	.. code-block:: python
		:linenos:

		from mighty_logger.src import GetAnsiFormat

		print(f"{GetAnsiFormat('italic/fraktur')}Test string")
		print(f"{GetAnsiFormat('blink/slow')}Test string")
		print(f"{GetAnsiFormat('invert/off')}Test string")
		print(f"{GetAnsiFormat('font/3th alternative')}Test string")
		print(f"{GetAnsiFormat('color/foreground/green')}Test string")
		print(f"{GetAnsiFormat('color/set/background/255;255;255')}Test string")
		print(f"{GetAnsiFormat('reset/on')}Test string")

	.. versionadded:: v0.2.1

	:param ansi_address: Path to ANSI escape code value
	:type ansi_address: str
	:return: ANSI escape code
	:rtype: str

Color picker
------------

.. currentmodule:: mighty_logger.src.color_picker

.. py:data:: ColorPicker

	Color table.

	.. versionadded:: v0.0.4

	.. danger:: This is a hidden data that is inaccessible outside the library.

	.. seealso::
		Source of inspiration:

		- `Web colors <https://en.wikipedia.org/wiki/Web_colors>`_

.. py:function:: DecColor(color_name: str) -> list[int, int, int]

	Returns a decimal color value.

	.. versionadded:: v0.0.4

	:param color_name: Color name
	:type color_name: str
	:return: Decimal color value
	:rtype: list[int, int, int]
	:raises ColorException: This color is not in the dictionary

.. py:function:: HexColor(color_name: str) -> str

	Returns a hexadecimal color value.

	.. versionadded:: v0.0.4

	:param color_name: Color name
	:type color_name: str
	:return: Hexadecimal color value
	:rtype: str
	:raises ColorException: This color is not in the dictionary

.. py:function:: AnsiColor(color_name: str, color_ground: str) -> str

	Returns an ANSI color value. In AnsiFormat, the following levels are available under the "color/set/..." path:

	- foreground
	- background
	- bright foreground
	- bright background
	- underline

	.. versionadded:: v0.0.4

	:param color_name: Color name
	:type color_name: str
	:param color_ground: Color level
	:type color_ground: str
	:return: ANSI color value
	:rtype: str
	:raises ColorException: This color is not in the dictionary

.. py:function:: Dec2Hex(dec_colors: list[int, int, int]) -> str

	Converts a decimal color value to a hexadecimal.

	.. versionadded:: v0.2.0

	:param dec_colors: Decimal color value
	:type dec_colors: list[int, int, int]
	:return: Hexadecimal color value
	:rtype: str

.. py:function:: Dec2Ansi(dec_colors: list[int, int, int], color_ground: str) -> str

	Converts a decimal color value to an ANSI escape code.

	.. versionadded:: v0.2.0

	:param dec_colors: Decimal color value
	:type dec_colors: list[int, int, int]
	:param color_ground: Color level (read AnsiColor() function documentation)
	:type color_ground: str
	:return: ANSI escape code color value
	:rtype: str

.. py:function:: Hex2Dec(hex_color: str) -> list[int, int, int]

	Converts a hexadecimal color value to a decimal.

	.. versionadded:: v0.2.0

	:param hex_color: Hexadecimal color value
	:type hex_color: str
	:return: Decimal color value
	:rtype: list[int, int, int]

.. py:function:: Hex2Ansi(hex_color: str, color_ground: str) -> str

	Converts a hexadecimal color value to an ANSI escape code.

	.. versionadded:: v0.2.0

	:param hex_color: Hexadecimal color value
	:type hex_color: str
	:param color_ground: Color level (read AnsiColor() function documentation)
	:type color_ground: str
	:return: ANSI escape code color value
	:rtype: str

.. py:function:: Ansi2Dec(ansi_color: str) -> list[int, int, int]

	Converts an ANSI escape code color value to a decimal. When converting to ANSI escape code, you need to know which level the color is applied to, and when from ANSI escape code, you don’t need to, because in other formats the levels are defined differently and are not included in the command along with the color.

	.. versionadded:: v0.2.0

	:param ansi_color: ANSI escape code color value
	:type ansi_color: str
	:return: Decimal color value
	:rtype: list[int, int, int]

.. py:function:: Ansi2Hex(ansi_color: str) -> str

	Converts an ANSI escape code color value to a hexadecimal. When converting to ANSI escape code, you need to know which level the color is applied to, and when from ANSI escape code, you don’t need to, because in other formats the levels are defined differently and are not included in the command along with the color.

	.. versionadded:: v0.2.0

	:param ansi_color: ANSI escape code color value
	:type ansi_color: str
	:return: Hexadecimal color value
	:rtype: str

.. _entry_types_collections:

Entry types collections
-----------------------

.. currentmodule:: mighty_logger.src.lib_types_collection.entry_types

.. py:class:: ServiceLogger

	.. danger:: This is a hidden class that is inaccessible outside the library.

	Class for Logger service strings.

	.. versionadded:: v0.7.0

	.. py:attribute:: initial

		Colors for the starting initialization string.

		.. versionadded:: v0.7.0

.. py:class:: LoggerEntryTypes

	.. tip:: Used in the ``entry()`` and ``note_process()`` methods.

	A class with standard entry types. Is available.

	.. versionadded:: v0.7.0

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`EntryType <entry_type>`.

	.. py:attribute:: debug

		Debugging information logging: Can be used to log entry any information while debugging an application.

		.. versionadded:: v0.6.0

	.. py:attribute:: debug_performance

		Performance debugging information logging: Can be used to log entry the execution time of operations or other performance information while the application is being debugged.

		.. versionadded:: v0.6.0

	.. py:attribute:: performance

		Performance information logging: Can be used to log entry the execution time of operations or other application performance information.

		.. versionadded:: v0.6.0

	.. py:attribute:: event

		Event information logging: Can be used to log entry specific events in the application, such as button presses or mouse cursor movements.

		.. versionadded:: v0.6.0

	.. py:attribute:: audit

		Audit information logging: Can be used to log entry changes in the system, such as creating or deleting users, as well as changes in security settings.

		.. versionadded:: v0.6.0

	.. py:attribute:: metrics

		Metrics information logging: Can be used to log entry metrics to track application performance and identify issues.

		.. versionadded:: v0.6.0

	.. py:attribute:: user

		User information logging: Can be used to log entry custom logs to store additional information that may be useful for diagnosing problems.

		.. versionadded:: v0.6.0

	.. py:attribute:: message

		Message information logging: Can be used for the usual output of ordinary messages about the program's operation.

		.. versionadded:: v0.6.0

	.. py:attribute:: info

		Default information logging: Can be used to log entry messages with specific content about the operation of the program.

		.. versionadded:: v0.6.0

	.. py:attribute:: notice

		Notice information logging: Can be used to flag important events that might be missed with a normal logging level.

		.. versionadded:: v0.6.0

	.. py:attribute:: warning

		Warning information logging: Can be used to log entry warnings that the program may work with unpredictable results.

		.. versionadded:: v0.6.0

	.. py:attribute:: error

		Error information logging: Used to log entry errors and crashes in the program.

		.. versionadded:: v0.6.0

	.. py:attribute:: critical

		Critical error information logging: Used to log entry for critical and unpredictable program failures.

		.. versionadded:: v0.6.0

	.. py:attribute:: resolved

		Resolved information logging: Used to log entry resolved solutions to problems and errors.

		.. versionadded:: v0.6.0

	.. py:attribute:: unresolved

		Unresolved information logging: Used to log entry unresolved solutions to problems and errors.

		.. versionadded:: v0.6.0

.. py:class:: ProcessEntryTypes

	.. tip:: Used in the ``note_process()`` methods.

	Class with additional entry types when logging Processes. Is available.

	.. versionadded:: v0.7.0

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`EntryType <entry_type>`.

	.. py:attribute:: achievement

		Achievement information logging: Used to log entry the achievements gained while executing a process.

		.. versionadded:: v0.6.0

	.. py:attribute:: milestone

		Milestone information logging: Used to log entry the milestones gained while executing a process.

		.. versionadded:: v0.6.0

.. py:class:: ServiceProcessEntryTypes

	.. danger:: This is a hidden class that is inaccessible outside the library.

	A class with utility types used for Process logging. Is not available.

	.. versionadded:: v0.7.0

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`EntryType <entry_type>`.

	.. py:attribute:: initiation

		Initiation information logging: Used to explain the running process.

		.. versionadded:: v0.7.0

	.. py:attribute:: process

		Process information logging: Used to refine the progress of a Process.

		.. versionadded:: v0.7.0

	.. py:attribute:: success

		Success information logging: Used to log entry a message about the success of the process.

		.. versionadded:: v0.7.0

	.. py:attribute:: fail

		Fail information logging: Used to log entry a message about the failed execution of the process.

		.. versionadded:: v0.7.0

.. py:class:: ServiceTimerEntryTypes

	.. danger:: This is a hidden class that is inaccessible outside the library.

	A class with utility types used for Timer logging. Is not available.

	.. versionadded:: v0.7.0

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`EntryType <entry_type>`.

	.. py:attribute:: start_timer

		Information logging of starting Timer: Used to notify the start of the Timer.

		.. versionadded:: v0.6.1

	.. py:attribute:: timer_mark

		Information logging of mark Timer: Used to notify the mark of the Timer.

		.. versionadded:: v0.6.1

	.. py:attribute:: stop_timer

		Information logging of stopping Timer: Used to notify the stop of the Timer.

		.. versionadded:: v0.6.1

.. py:class:: SelectionTypes

	.. tip:: Used in the ``select()`` and ``select_with_save()`` methods.

	A class with a list of all entry types. Needed only for the ``select()`` method of the Modifier class.

	.. versionadded:: v0.7.1

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`EntryType <entry_type>`.

	.. py:attribute:: debug

		Debugging information logging: Can be used to log entry any information while debugging an application.

		.. versionadded:: v0.7.1

	.. py:attribute:: debug_performance

		Performance debugging information logging: Can be used to log entry the execution time of operations or other performance information while the application is being debugged.

		.. versionadded:: v0.7.1

	.. py:attribute:: performance

		Performance information logging: Can be used to log entry the execution time of operations or other application performance information.

		.. versionadded:: v0.7.1

	.. py:attribute:: event

		Event information logging: Can be used to log entry specific events in the application, such as button presses or mouse cursor movements.

		.. versionadded:: v0.7.1

	.. py:attribute:: audit

		Audit information logging: Can be used to log entry changes in the system, such as creating or deleting users, as well as changes in security settings.

		.. versionadded:: v0.7.1

	.. py:attribute:: metrics

		Metrics information logging: Can be used to log entry metrics to track application performance and identify issues.

		.. versionadded:: v0.7.1

	.. py:attribute:: user

		User information logging: Can be used to log entry custom logs to store additional information that may be useful for diagnosing problems.

		.. versionadded:: v0.7.1

	.. py:attribute:: message

		Message information logging: Can be used for the usual output of ordinary messages about the program's operation.

		.. versionadded:: v0.7.1

	.. py:attribute:: info

		Default information logging: Can be used to log entry messages with specific content about the operation of the program.

		.. versionadded:: v0.7.1

	.. py:attribute:: notice

		Notice information logging: Can be used to flag important events that might be missed with a normal logging level.

		.. versionadded:: v0.7.1

	.. py:attribute:: warning

		Warning information logging: Can be used to log entry warnings that the program may work with unpredictable results.

		.. versionadded:: v0.7.1

	.. py:attribute:: error

		Error information logging: Used to log entry errors and crashes in the program.

		.. versionadded:: v0.7.1

	.. py:attribute:: critical

		Critical error information logging: Used to log entry for critical and unpredictable program failures.

		.. versionadded:: v0.7.1

	.. py:attribute:: resolved

		Resolved information logging: Used to log entry resolved solutions to problems and errors.

		.. versionadded:: v0.7.1

	.. py:attribute:: unresolved

		Unresolved information logging: Used to log entry unresolved solutions to problems and errors.

		.. versionadded:: v0.7.1

	.. py:attribute:: achievement

		Achievement information logging: Used to log entry the achievements gained while executing a process.

		.. versionadded:: v0.7.1

	.. py:attribute:: milestone

		Milestone information logging: Used to log entry the milestones gained while executing a process.

		.. versionadded:: v0.7.1

	.. py:attribute:: initiation

		Initiation information logging: Used to explain the running process.

		.. versionadded:: v0.7.1

	.. py:attribute:: process

		Process information logging: Used to refine the progress of a Process.

		.. versionadded:: v0.7.1

	.. py:attribute:: success

		Success information logging: Used to log entry a message about the success of the process.

		.. versionadded:: v0.7.1

	.. py:attribute:: fail

		Fail information logging: Used to log entry a message about the failed execution of the process.

		.. versionadded:: v0.7.1

	.. py:attribute:: start_timer

		Information logging of starting Timer: Used to notify the start of the Timer.

		.. versionadded:: v0.7.1

	.. py:attribute:: timer_mark

		Information logging of mark Timer: Used to notify the mark of the Timer.

		.. versionadded:: v0.7.1

	.. py:attribute:: stop_timer

		Information logging of stopping Timer: Used to notify the stop of the Timer.

		.. versionadded:: v0.7.1

.. py:class:: SelectionCategories

	.. tip:: Used in the ``select()`` and ``select_with_save()`` methods.

	A class with a list of all entry categories. Needed only for the ``select()`` method of the Modifier class.

	.. versionadded:: v0.7.2

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`EntryType <entry_type>`.

	.. py:attribute:: debug

		Category "debug", which combines

		- debug
		- debug_performance
		- performance

		.. versionadded:: v0.7.2

	.. py:attribute:: event

		Category "debug", which combines

		- event
		- audit
		- metrics
		- user

		.. versionadded:: v0.7.2

	.. py:attribute:: message

		Category "debug", which combines

		- message
		- info
		- notice

		.. versionadded:: v0.7.2

	.. py:attribute:: error

		Category "debug", which combines

		- warning
		- error
		- critical
		- resolved
		- unresolved

		.. versionadded:: v0.7.2

	.. py:attribute:: process

		Category "debug", which combines

		- achievement
		- milestone
		- initiation
		- process
		- success
		- fail

		.. versionadded:: v0.7.2

	.. py:attribute:: timer

		Category "debug", which combines

		- start_timer
		- timer_mark
		- stop_timer

		.. versionadded:: v0.7.2

.. _logger_environments_collections:

Logger environments collections
-------------------------------

.. currentmodule:: mighty_logger.src.lib_types_collection.environments

.. py:class:: LogEnvironments

	.. tip:: Use for those methods, one of whose parameters is of type EnvironmentType.

	Environments of Logger.

	.. versionadded:: v0.5.0-dev

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`EnvironmentType <environment_type>`.

	.. py:attribute:: CONSOLE

		A "CONSOLE" environment that supports displaying logs in the console, updating/changing them WITH support for ANSI escape code (hence - with support for formatting text and changing its color foreground and background).

		.. versionadded:: v0.5.0-dev

		.. note:: In fact, appeared as an environment type, but actually existed as a separate class of the whole Logger, adapted for this environment from v0.2.0 before merging Loggers into one class and creating an environment type.

	.. py:attribute:: PLAIN_CONSOLE

		A "PLAIN_CONSOLE" environment that supports displaying logs in the console, updating/changing them WITHOUT ANSI escape code support.

		.. versionadded:: v0.7.0

	.. py:attribute:: HTML

		An "HTML" environment that does NOT support displaying logs in the console, former text with HTML tags (with support for text formatting and changing colors) so that logs can be viewed in the Browser.

		.. versionadded:: v0.5.0-dev

		.. note:: In fact, appeared as an environment type, but actually existed as a separate class of the whole Logger, adapted for this environment from v0.0.1 before merging Loggers into one class and creating an environment type.

	.. py:attribute:: MARKDOWN

		A "MARKDOWN" environment that does NOT support displaying logs in the console, former text with HTML tags (with support for text formatting and changing colors) to allow viewing logs in note format.

		.. versionadded:: v0.7.0

	.. py:attribute:: PLAIN

		A "PLAIN" environment, which does NOT support the display of logs in the console and WITHOUT the use of HTML tags, is the most lightweight and simple to work with pure text without unnecessary load on the system.

		.. versionadded:: v0.7.0

.. _sorting_keys_collections:

Sorting keys collections
------------------------

.. currentmodule:: mighty_logger.src.lib_types_collection.sorting_keys

.. py:class:: SortingKeys

	.. tip:: Used in the ``sort()`` ``and sort_with_save()`` methods.

	Sort keys.

	.. versionadded:: v0.7.1

	.. hint:: Attributes are used to pass ready-made objects to fields of type :ref:`SortingKeyType <sorting_key_type>`.

	.. py:attribute:: SORT_ON_TIME

		Sort by entry *time*.

		.. versionadded:: v0.7.1

	.. py:attribute:: SORT_ON_TIME_WITH_REVERSE

		Sort by entry *time in reverse order*.

		.. versionadded:: v0.7.1

	.. py:attribute:: SORT_ON_CATEGORY

		Sort by entry *category*.

		.. versionadded:: v0.7.1

	.. py:attribute:: SORT_ON_TYPE

		Sort by entry *type*.

		.. versionadded:: v0.7.1
