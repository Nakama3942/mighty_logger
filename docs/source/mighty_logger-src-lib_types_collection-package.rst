"lib types collection" package
==============================

A package containing lists of prebuilt objects of library types.

.. versionadded:: 0.7.1

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.src.lib_types_collection import ...

.. currentmodule:: mighty_logger.src.lib_types_collection.entry_types

.. rubric:: list ServiceLogger
.. py:class:: ServiceLogger

	.. danger:: This is a hidden class that is inaccessible outside the library.

	Class for Logger service strings.

	:since: v0.7.0

	.. py:attribute:: initial

		Colors for the starting initialization string.

		:since: v0.7.0

.. rubric:: list LoggerEntryTypes
.. py:class:: LoggerEntryTypes

	.. tip:: Used in the entry() and note_process() methods.

	A class with standard entry types. Is available.

	:since: v0.7.0

	.. py:attribute:: debug

		Debugging information logging: Can be used to log entry any information while debugging an application.

		:since: v0.6.0

	.. py:attribute:: debug_performance

		Performance debugging information logging: Can be used to log entry the execution time of operations or other performance information while the application is being debugged.

		:since: v0.6.0

	.. py:attribute:: performance

		Performance information logging: Can be used to log entry the execution time of operations or other application performance information.

		:since: v0.6.0

	.. py:attribute:: event

		Event information logging: Can be used to log entry specific events in the application, such as button presses or mouse cursor movements.

		:since: v0.6.0

	.. py:attribute:: audit

		Audit information logging: Can be used to log entry changes in the system, such as creating or deleting users, as well as changes in security settings.

		:since: v0.6.0

	.. py:attribute:: metrics

		Metrics information logging: Can be used to log entry metrics to track application performance and identify issues.

		:since: v0.6.0

	.. py:attribute:: user

		User information logging: Can be used to log entry custom logs to store additional information that may be useful for diagnosing problems.

		:since: v0.6.0

	.. py:attribute:: message

		Message information logging: Can be used for the usual output of ordinary messages about the program's operation.

		:since: v0.6.0

	.. py:attribute:: info

		Default information logging: Can be used to log entry messages with specific content about the operation of the program.

		:since: v0.6.0

	.. py:attribute:: notice

		Notice information logging: Can be used to flag important events that might be missed with a normal logging level.

		:since: v0.6.0

	.. py:attribute:: warning

		Warning information logging: Can be used to log entry warnings that the program may work with unpredictable results.

		:since: v0.6.0

	.. py:attribute:: error

		Error information logging: Used to log entry errors and crashes in the program.

		:since: v0.6.0

	.. py:attribute:: critical

		Critical error information logging: Used to log entry for critical and unpredictable program failures.

		:since: v0.6.0

	.. py:attribute:: resolved

		Resolved information logging: Used to log entry resolved solutions to problems and errors.

		:since: v0.6.0

	.. py:attribute:: unresolved

		Unresolved information logging: Used to log entry unresolved solutions to problems and errors.

		:since: v0.6.0

.. rubric:: list ProcessEntryTypes
.. py:class:: ProcessEntryTypes

	.. tip:: Used in the entry() and note_process() methods.

	Class with additional entry types when logging Processes. Is available.

	:since: v0.7.0

	.. py:attribute:: achievement

		Achievement information logging: Used to log entry the achievements gained while executing a process.

		:since: v0.6.0

	.. py:attribute:: milestone

		Milestone information logging: Used to log entry the milestones gained while executing a process.

		:since: v0.6.0

.. rubric:: list ServiceProcessEntryTypes
.. py:class:: ServiceProcessEntryTypes

	.. danger:: This is a hidden class that is inaccessible outside the library.

	A class with utility types used for Process logging. Is not available.

	:since: v0.7.0

	.. py:attribute:: initiation

		Initiation information logging: Used to explain the running process.

		:since: v0.7.0

	.. py:attribute:: process

		Process information logging: Used to refine the progress of a Process.

		:since: v0.7.0

	.. py:attribute:: success

		Success information logging: Used to log entry a message about the success of the process.

		:since: v0.7.0

	.. py:attribute:: fail

		Fail information logging: Used to log entry a message about the failed execution of the process.

		:since: v0.7.0

.. rubric:: list ServiceTimerEntryTypes
.. py:class:: ServiceTimerEntryTypes

	.. danger:: This is a hidden class that is inaccessible outside the library.

	A class with utility types used for Timer logging. Is not available.

	:since: v0.7.0

	.. py:attribute:: start_timer

		Information logging of starting Timer: Used to notify the start of the Timer.

		:since: v0.6.1

	.. py:attribute:: timer_mark

		Information logging of mark Timer: Used to notify the mark of the Timer.

		:since: v0.6.1

	.. py:attribute:: stop_timer

		Information logging of stopping Timer: Used to notify the stop of the Timer.

		:since: v0.6.1

.. rubric:: list SelectionTypes
.. py:class:: SelectionTypes

	.. tip:: Used in the select() and select_with_save() methods.

	A class with a list of all entry types.
	Needed only for the select() method of the Modifier class.

	:since: v0.7.1

	.. py:attribute:: debug

		Debugging information logging: Can be used to log entry any information while debugging an application.

		:since: v0.7.1

	.. py:attribute:: debug_performance

		Performance debugging information logging: Can be used to log entry the execution time of operations or other performance information while the application is being debugged.

		:since: v0.7.1

	.. py:attribute:: performance

		Performance information logging: Can be used to log entry the execution time of operations or other application performance information.

		:since: v0.7.1

	.. py:attribute:: event

		Event information logging: Can be used to log entry specific events in the application, such as button presses or mouse cursor movements.

		:since: v0.7.1

	.. py:attribute:: audit

		Audit information logging: Can be used to log entry changes in the system, such as creating or deleting users, as well as changes in security settings.

		:since: v0.7.1

	.. py:attribute:: metrics

		Metrics information logging: Can be used to log entry metrics to track application performance and identify issues.

		:since: v0.7.1

	.. py:attribute:: user

		User information logging: Can be used to log entry custom logs to store additional information that may be useful for diagnosing problems.

		:since: v0.7.1

	.. py:attribute:: message

		Message information logging: Can be used for the usual output of ordinary messages about the program's operation.

		:since: v0.7.1

	.. py:attribute:: info

		Default information logging: Can be used to log entry messages with specific content about the operation of the program.

		:since: v0.7.1

	.. py:attribute:: notice

		Notice information logging: Can be used to flag important events that might be missed with a normal logging level.

		:since: v0.7.1

	.. py:attribute:: warning

		Warning information logging: Can be used to log entry warnings that the program may work with unpredictable results.

		:since: v0.7.1

	.. py:attribute:: error

		Error information logging: Used to log entry errors and crashes in the program.

		:since: v0.7.1

	.. py:attribute:: critical

		Critical error information logging: Used to log entry for critical and unpredictable program failures.

		:since: v0.7.1

	.. py:attribute:: resolved

		Resolved information logging: Used to log entry resolved solutions to problems and errors.

		:since: v0.7.1

	.. py:attribute:: unresolved

		Unresolved information logging: Used to log entry unresolved solutions to problems and errors.

		:since: v0.7.1

	.. py:attribute:: achievement

		Achievement information logging: Used to log entry the achievements gained while executing a process.

		:since: v0.7.1

	.. py:attribute:: milestone

		Milestone information logging: Used to log entry the milestones gained while executing a process.

		:since: v0.7.1

	.. py:attribute:: initiation

		Initiation information logging: Used to explain the running process.

		:since: v0.7.1

	.. py:attribute:: process

		Process information logging: Used to refine the progress of a Process.

		:since: v0.7.1

	.. py:attribute:: success

		Success information logging: Used to log entry a message about the success of the process.

		:since: v0.7.1

	.. py:attribute:: fail

		Fail information logging: Used to log entry a message about the failed execution of the process.

		:since: v0.7.1

	.. py:attribute:: start_timer

		Information logging of starting Timer: Used to notify the start of the Timer.

		:since: v0.7.1

	.. py:attribute:: timer_mark

		Information logging of mark Timer: Used to notify the mark of the Timer.

		:since: v0.7.1

	.. py:attribute:: stop_timer

		Information logging of stopping Timer: Used to notify the stop of the Timer.

		:since: v0.7.1

.. rubric:: list SelectionCategories
.. py:class:: SelectionCategories

	.. tip:: Used in the select() and select_with_save() methods.

	A class with a list of all entry categories. Needed only for the select() method of the Modifier class.

	:since: v0.7.2

	.. py:attribute:: debug

		...

		:since: v0.7.2

	.. py:attribute:: event

		...

		:since: v0.7.2

	.. py:attribute:: message

		...

		:since: v0.7.2

	.. py:attribute:: error

		...

		:since: v0.7.2

	.. py:attribute:: process

		...

		:since: v0.7.2

	.. py:attribute:: timer

		...

		:since: v0.7.2

.. currentmodule:: mighty_logger.src.lib_types_collection.environments

.. rubric:: list LogEnvironments
.. py:class:: LogEnvironments

	.. tip:: Use for those methods, one of whose parameters is of type EnvironmentType.

	Environments of Logger.

	:since: v0.5.0-dev

	.. py:attribute:: CONSOLE

		...

		:since: v0.5.0-dev

	.. py:attribute:: PLAIN_CONSOLE

		...

		:since: v0.7.0

	.. py:attribute:: HTML

		...

		:since: v0.5.0-dev

	.. py:attribute:: MARKDOWN

		...

		:since: v0.7.0

	.. py:attribute:: PLAIN

		...

		:since: v0.7.0

.. currentmodule:: mighty_logger.src.lib_types_collection.sorting_keys

.. rubric:: list SortingKeys
.. py:class:: SortingKeys

	.. tip:: Used in the sort() and sort_with_save() methods.

	Sort keys.

	:since: v0.7.1

	.. py:attribute:: SORT_ON_TIME

		...

		:since: v0.7.1

	.. py:attribute:: SORT_ON_TIME_WITH_REVERSE

		...

		:since: v0.7.1

	.. py:attribute:: SORT_ON_CATEGORY

		...

		:since: v0.7.1

	.. py:attribute:: SORT_ON_TYPE

		...

		:since: v0.7.1

