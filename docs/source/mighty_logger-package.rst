"Mighty logger" package
=======================

.. toctree::
	:maxdepth: 2
	:caption: Contents:
	:hidden:

	mighty_logger-basic-package
	mighty_logger-src-package

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.basic.lib_types import ...

.. currentmodule:: mighty_logger.mighty_logger

.. rubric:: class MightyLogger
.. py:class:: MightyLogger(*[, program_name: str = "Unknown", log_environment: EnvironmentType = LogEnvironments.PLAIN, console_width: int = 60, icon_set: int = 1, global_bold_font: bool = False, global_italic_font: bool = False, global_invert_font: bool = False, global_background: bool = False])

	The Logger class is a class that implements the functionality of logging the work of software in different directions.

	It has a color output of information, settings for the operation of the log. Only one class object can be created!!!

	Implements the output of the following information:

	1. Record creation time
	2. Record status
	3. Recording status message
	4. Record type
	5. Write message

	Implements the output of the following types of records:
	see the /docs/DATA.md/"Entry types"

	:since: v0.0.1

	.. rubric:: Logger settings

	.. py:method:: _init_buffer(console_width: int) -> None

		Initializes a Text Buffer.

		:since: v0.7.0
		:param console_width: Console width
		:type console_width: int

	.. py:method:: _initial_log() -> None

		Displays initialized information.

		:since: v0.3.0

	.. py:method:: set_icons(icon_set: int) -> None

		Changes the current icon set used by the Logger.

		:since: v0.6.0
		:param icon_set: Icon set to use
		:type icon_set: int

	.. py:method:: set_settings(*, global_bold_font: bool = None, global_italic_font: bool = None, global_invert_font: bool = None, global_background: bool = None) -> None

		Method that sets new Logger settings.

		:since: v0.9.2
		:param global_bold_font: Sets the global setting "bold font"
		:type global_bold_font: bool
		:param global_italic_font: Sets the global setting "italic font"
		:type global_italic_font: bool
		:param global_invert_font: Sets the global setting "invert font"
		:type global_invert_font: bool
		:param global_background: Sets the global setting "background"
		:type global_background: bool

	.. py:method:: get_settings() -> dict

		Returns a dictionary of settings.

		:since: v0.9.2
		:return: A dictionary of settings
		:rtype: dict

	.. rubric:: Inputter of Logger

	.. py:method:: empty(entry: str) -> None

		Empty logging: A type denoting an "empty" entry - an entry that carries nothing but the purest text.

		:since: v0.6.0
		:param entry: "Empty" entry
		:type entry: str

	.. py:method:: addy(number_string: int, message: str) -> None

		A method that adds the given string to the Logger Buffer at the given position.

		It is an add-on for the Buffer insert() method.

		:since: v0.7.0
		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str

	.. py:method:: modify(number_string: int, message: str)) -> None

		A method that replaces the string at the given position in the Logger Buffer with the given string.

		It is an add-on for the Buffer replace() method.

		:since: v0.7.0
		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str

	.. py:method:: catchy(number_string: int) -> str

		A method that extracts the given string from the Logger Buffer and returns.

		It is an add-on for the Buffer pop() method.

		:since: v0.7.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str

	.. py:method:: extractly(number_string: int) -> None

		A method that extracts the given string from the Logger Buffer without returning.

		It is an add-on for the Buffer remove() method.

		:since: v0.7.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int

	.. py:method:: clearly() -> None

		A method that clears the entire Logger Buffer.

		It is an add-on for the Buffer clear() method.

		:since: v0.7.0
		:param console_width: Console width
		:type console_width: int

	.. py:method:: savy(name_file: str, clean: bool) -> None

		A method that saves the Logger Buffer to a file. You can turn on formatting cleanup.

		It is an add-on for the Buffer save() method.

		:since: v0.7.0
		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool

	.. py:method:: loady(name_file: str) -> None

		A method that loads the Logger Buffer from a file.

		It is an add-on for the Buffer load() method.

		:since: v0.7.0
		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str

	.. py:method:: getty(input_text: str) -> str

		A method that allows you to use the standard Python input() during the operation of the Logger, acting as its wrapper.

		It is an add-on for the Buffer input() method.

		:since: v0.7.0
		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str

	.. rubric:: Modifier of Logger

	.. py:method:: sort(key: SortingKeyType) -> None

		A method that sorts the Logger Buffer following the specified sort key.

		:since: v0.7.1
		:param key: The key to sort by
		:type key: SortingKeyType

	.. py:method:: sort_with_save(key: SortingKeyType, sort_file_name: str) -> None

		A method that sorts the Logger Buffer following the specified sort key and saves it to a file. After saving, the Buffer is restored.

		:since: v0.7.1
		:param key: The key to sort by
		:type key: SortingKeyType
		:param sort_file_name: The name of the file where you want to save the sorted Logs
		:type sort_file_name: str

	.. py:method:: search(keyword: str, empty: bool) -> None

		A method that searches the Logger Buffer for a given keyword/letter/phrase. You can also enable the search for "empty" strings.

		:since: v0.7.1
		:param keyword: Keyword/letter/phrase
		:type keyword: str
		:param empty: Flag indicating whether to search in custom strings
		:type empty: bool

	.. py:method:: search_with_save(keyword: str, empty: bool, search_file_name: str) -> None

		A method that searches the Logger Buffer for a given keyword/letter/phrase. You can also enable the search for "empty" strings. The found strings are saved to a file. After saving, the Buffer is restored.

		:since: v0.7.1
		:param keyword: Keyword/letter/phrase
		:type keyword: str
		:param empty: Flag indicating whether to search in custom strings
		:type empty: bool
		:param search_file_name: The name of the file where you want to save the searched Logs
		:type search_file_name: str

	.. py:method:: select(entry_type: EntryType) -> None

		A method that selects entries in the Logger Buffer with the specified category or type.

		:since: v0.7.1
		:param entry_type: Entries Type/Category
		:type entry_type: EntryType

	.. py:method:: select_with_save(entry_type: EntryType, select_file_name: str) -> None

		A method that selects entries in the Logger Buffer with the specified category or type and saves them to a file. After saving, the Buffer is restored.

		:since: v0.7.1
		:param entry_type: Entries Type/Category
		:type entry_type: EntryType
		:param select_file_name: The name of the file where you want to save the selected Logs
		:type select_file_name: str

	.. py:method:: export_to_csv(export_file_name: str) -> None

		Method that exports the Logger Buffer to a csv table.

		:since: v0.8.0
		:param export_file_name: The name of the file where you want to save the csv table
		:type export_file_name: str

	.. rubric:: Publishers

	.. py:method:: publish_id() -> None

		A method that publishes information about the Logger ID in the Logger's Buffer.

		:since: v0.7.0

	.. py:method:: publish_program_name() -> None

		A method that publishes information about the name of the logging program in the Logger Buffer.

		:since: v0.7.0

	.. py:method:: publish_environment() -> None

		A method that publishes information about the Logger's environment to the Logger Buffer.

		:since: v0.7.0

	.. py:method:: publish_global_settings() -> None

		A method that publishes information about the Logger's global settings to the Logger Buffer.

		:since: v0.7.0

	.. py:method:: publish_author() -> None

		A method that publishes information about the Author of the library to the Logger Buffer.

		:since: v0.7.0

	.. py:method:: publish_license() -> None

		A method that publishes information about the Library's License to the Logger Buffer.

		:since: v0.7.0

	.. py:method:: separator() -> None

		A method that adds a separator.

		:since: v0.7.0

	.. rubric:: Entering to Logger

	.. py:method:: entry(entry_type: EntryType, message_text: str[, local_settings: dict = None]) -> None

		A method that generates and adds an entry to the Logger.

		:since: v0.7.0
		:param entry_type: Entry type
		:type entry_type: EntryType
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. rubric:: Entering to Processes

	.. py:method:: start_indefinite_process(message_text: str[, animation: IndefiniteAnimationType = IndefiniteAnimations.Line, local_settings: dict = None]) -> None

		A method that starts the whole process of indefinite logging. While the process is running, you cannot start other processes in the Logger and call the entering methods directly. While the process is running - the last entry will play the animation of the process. Before starting a process, you can specify that the process Logs and configure Initiation and Progress entries.

		:since: v0.6.0
		:param message_text: Log entry message
		:type message_text: str
		:param animation: The name of the animation that will play in the Progress entry
		:type animation: IndefiniteAnimationType
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. py:method:: _indefinite_progress(message_text: str[, local_settings: dict = None]) -> None

		A method that creates an animation entry. Only works on the last string. You need to run in a thread. Terminates when the process stop flag is set by the Logger.stop_process() method.

		:since: v0.6.0
		:param message_text: Log entry message
		:type message_text: str
		:param local_background: Display entry with background?
		:type local_background: bool
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. py:method:: start_definite_process(message_text: str[, progress_bar: DefiniteAnimationType = DefiniteAnimations.Line, local_settings: dict = None]) -> None

		A method that starts the whole process of a definite logging. While the process is running, you cannot start other processes in the Logger and call the entering methods directly. While the process is running - the last entry will display the progress of the process. Before starting a process, you can specify that the process Logs and configure Initiation and Progress entries.

		:since: v0.6.0
		:param message_text: Log entry message
		:type message_text: str
		:param progress_bar: The name of the progress bar that will play in the Progress entry
		:type progress_bar: DefiniteAnimationType
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. py:method:: _definite_progress(message_text: str[, local_settings: dict = None]) -> None

		A method that creates a progress bar entry. Only works on the last string. You need to run in a thread. Terminates when the process stop flag is set by the Logger.stop_process() method.

		:since: v0.6.0
		:param message_text: Log entry message
		:type message_text: str
		:param local_background: Display entry with background?
		:type local_background: bool
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. py:method:: progress_rise(percent: int) -> None

		Sets the process completion percentage. Usually used for a specific process. However, it is used for both types of processes as a flag for the success of the process. If you set the percentage of completion to 100% before terminating the process, the process will complete successfully, otherwise it will fail.

		:since: v0.6.0
		:param percent: Process completion percentage
		:type percent: int

	.. py:method:: note_process(entry_type: EntryType, message_text: str[, local_settings: dict = None]) -> None

		An important method that allows you to add standard non-process entry types while a process is running. It's important to note that this entry will still be associated with the process, so it's best to use this entry when you want to describe intermediate process execution entries beyond process initiation, progress, and success/failure entries. Adds the ability to use two additional entry types that cannot be used outside a process: achievement and milestone.

		Use `from mighty_logger.src import LoggerEntryTypes` or `from mighty_logger.src import ProcessEntryTypes` for `entry_type`.

		:since: v0.6.0
		:param entry_type: The type of entry to be entered in the progress history
		:type entry_type: EntryType
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. py:method:: stop_process(message_text: str[, local_settings: dict = None]) -> None

		The method that terminates the process. If before the end of the process its execution has reached 100% - the process was completed successfully, otherwise - failed. After calling this method, the Progress entry will be replaced by the entry with the result of the process execution.

		:since: v0.6.0
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. rubric:: Entering to Timer

	.. py:method:: start_timer(message_text: str[, local_settings: dict = None]) -> None

		Stores the current time as the start time and write entry about the current time.

		:since: v0.6.1
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. py:method:: timer_mark(message_text: str[, local_settings: dict = None]) -> None

		Calculates the difference between current and start time and write entry about the difference.

		:since: v0.6.1
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

	.. py:method:: stop_timer(message_text: str[, local_settings: dict = None]) -> None

		Calculates the difference between the current and start time, write entry about the difference, and resets the start time.

		:since: v0.6.1
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict

.. currentmodule:: mighty_logger.simple_logger

.. rubric:: class Logger
.. py:class:: Logger(*[, program_name: str = "Unknown", log_environment: EnvironmentType = LogEnvironments.PLAIN, console_width: int = 60, icon_set: int = 1, global_bold_font: bool = False, global_italic_font: bool = False, global_invert_font: bool = False, global_background: bool = False])

	Lightweight Logger automates work with entry types.

	:since: v0.7.0

	.. py:method:: might() -> MightyLogger

		Provides access to "mighty" Logger methods.

		:since: v0.7.0
		:return: A "mighty" Logger
		:rtype: MightyLogger

	.. py:method:: debug(message_text: str) -> None

		Debugging information logging: Can be used to log entry any information while debugging an application.

		:since: v0.0.1
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: debug_performance(message_text: str) -> None

		Performance debugging information logging: Can be used to log entry the execution time of operations or other performance information while the application is being debugged.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: performance(message_text: str) -> None

		Performance information logging: Can be used to log entry the execution time of operations or other application performance information.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: event(message_text: str) -> None

		Event information logging: Can be used to log entry specific events in the application, such as button presses or mouse cursor movements.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: audit(message_text: str) -> None

		Audit information logging: Can be used to log entry changes in the system, such as creating or deleting users, as well as changes in security settings.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: metrics(message_text: str) -> None

		Metrics information logging: Can be used to log entry metrics to track application performance and identify issues.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: user(message_text: str) -> None

		User information logging: Can be used to log entry custom logs to store additional information that may be useful for diagnosing problems.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: message(message_text: str) -> None

		Message information logging: Can be used for the usual output of ordinary messages about the program's operation.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: info(message_text: str) -> None

		Default information logging: Can be used to log entry messages with specific content about the operation of the program.

		:since: v0.0.1
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: notice(message_text: str) -> None

		Notice information logging: Can be used to flag important events that might be missed with a normal logging level.

		:since: v0.0.3
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: warning(message_text: str) -> None

		Warning information logging: Can be used to log entry warnings that the program may work with unpredictable results.

		:since: v0.0.1
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: error(message_text: str) -> None

		Error information logging: Used to log entry errors and crashes in the program.

		:since: v0.0.1
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: critical(message_text: str) -> None

		Critical error information logging: Used to log entry for critical and unpredictable program failures.

		:since: v0.0.1
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: success(message_text: str) -> None

		Success information logging: Used to log entry a message about the success of the process.

		:since: v0.0.2
		:param message_text: Log entry message
		:type message_text: str

	.. py:method:: fail(message_text: str) -> None

		Fail information logging: Used to log entry a message about the failed execution of the process.

		:since: v0.0.2
		:param message_text: Log entry message
		:type message_text: str
