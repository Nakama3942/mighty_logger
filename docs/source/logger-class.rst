Logger class
============

.. toctree::
	:maxdepth: 2
	:caption: Contents:
	:hidden:

	mighty_logger-class

Logger
------

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger import Logger

.. currentmodule:: mighty_logger.simple_logger

.. py:class:: Logger(*[, program_name: str = "Unknown", log_environment: EnvironmentType = LogEnvironments.PLAIN, console_width: int = 60, icon_set: int = 1, global_bold_font: bool = False, global_italic_font: bool = False, global_invert_font: bool = False, global_background: bool = False])

	Lightweight Logger automates work with entry types. We can say, figuratively, this class restores the Logger from v0.1.0.

	.. versionadded:: 0.7.0

	:param program_name: The name of the program being logged
	:type program_name: str
	:param log_environment: Mighty Logger environment
	:type log_environment: EnvironmentType
	:param console_width: Console width
	:type console_width: int
	:param icon_set: Icon set number
	:type icon_set: int
	:param global_bold_font: Sets the global setting "bold font"
	:type global_bold_font: bool
	:param global_italic_font: Sets the global setting "italic font"
	:type global_italic_font: bool
	:param global_invert_font: Sets the global setting "invert font"
	:type global_invert_font: bool
	:param global_background: Sets the global setting "background"
	:type global_background: bool

	.. property:: might

		Mighty Logger.

		.. versionadded:: v0.9.3

		:rtype: MightyLogger

	.. py:method:: debug(message_text: str) -> None

		Debugging information logging: Can be used to log entry any information while debugging an application.

		.. versionadded:: 0.0.1

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: debug_performance(message_text: str) -> None

		Performance debugging information logging: Can be used to log entry the execution time of operations or other performance information while the application is being debugged.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: performance(message_text: str) -> None

		Performance information logging: Can be used to log entry the execution time of operations or other application performance information.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: event(message_text: str) -> None

		Event information logging: Can be used to log entry specific events in the application, such as button presses or mouse cursor movements.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: audit(message_text: str) -> None

		Audit information logging: Can be used to log entry changes in the system, such as creating or deleting users, as well as changes in security settings.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: metrics(message_text: str) -> None

		Metrics information logging: Can be used to log entry metrics to track application performance and identify issues.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: user(message_text: str) -> None

		User information logging: Can be used to log entry custom logs to store additional information that may be useful for diagnosing problems.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: message(message_text: str) -> None

		Message information logging: Can be used for the usual output of ordinary messages about the program's operation.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: info(message_text: str) -> None

		Default information logging: Can be used to log entry messages with specific content about the operation of the program.

		.. versionadded:: 0.0.1

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: notice(message_text: str) -> None

		Notice information logging: Can be used to flag important events that might be missed with a normal logging level.

		.. versionadded:: 0.0.3

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: warning(message_text: str) -> None

		Warning information logging: Can be used to log entry warnings that the program may work with unpredictable results.

		.. versionadded:: 0.0.1

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: error(message_text: str) -> None

		Error information logging: Used to log entry errors and crashes in the program.

		.. versionadded:: 0.0.1

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: critical(message_text: str) -> None

		Critical error information logging: Used to log entry for critical and unpredictable program failures.

		.. versionadded:: 0.0.1

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: success(message_text: str) -> None

		Success information logging: Used to log entry a message about the success of the process.

		.. versionadded:: 0.0.2

		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: fail(message_text: str) -> None

		Fail information logging: Used to log entry a message about the failed execution of the process.

		.. versionadded:: 0.0.2

		:param message_text: Log entry message
		:type message_text: str
