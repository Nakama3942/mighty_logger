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

from threading import Thread
from time import sleep
from datetime import datetime

from mighty_logger.basic.lib_types.animation_type import BasicAnimationType,\
	IndefiniteAnimationType,\
	DefiniteAnimationType
from mighty_logger.basic.lib_types.entry_type import EntryType
from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.basic.lib_types.sorting_key_type import SortingKeyType
from mighty_logger.basic.lib_types.text_buffer_type import TextBufferType
from mighty_logger.basic.basic_logger import BasicLogger
from mighty_logger.basic.exceptions import ReCreationException, InitException
from mighty_logger.basic.exporter import Exporter
from mighty_logger.basic.modifier import Modifier
from mighty_logger.basic.text_buffer import BasicTextBuffer, TextBuffer
from mighty_logger.src.lib_types_collection.entry_types import ServiceLogger,\
	LoggerEntryTypes,\
	ServiceProcessEntryTypes,\
	ServiceTimerEntryTypes
from mighty_logger.src.lib_types_collection.environments import LogEnvironments
from mighty_logger.src.lib_types_collection.sorting_keys import SortingKeys
from mighty_logger.src.animations import IndefiniteAnimations, DefiniteAnimations

class MightyLogger(BasicLogger):
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

	.. versionadded:: 0.0.0
	"""

	def __init__(
		self,
		*,
		program_name: str = "Unknown",
		log_environment: EnvironmentType = LogEnvironments.PLAIN,
		console_width: int = 60,
		icon_set: int = 1,
		global_bold_font: bool = False,
		global_italic_font: bool = False,
		global_invert_font: bool = False,
		global_background: bool = False
	) -> None:
		if not hasattr(self, "_environment"):
			super().__init__(program_name, log_environment)
			self._animation: BasicAnimationType = BasicAnimationType([])
			self._icon_set = icon_set if 0 < icon_set < 5 else 1
			self._settings["global_bold_font"] = global_bold_font
			self._settings["global_italic_font"] = global_italic_font
			self._settings["global_invert_font"] = global_invert_font
			self._settings["global_background"] = global_background
			self._progress_rise = 0
			self._progress_start: datetime | None = None
			self._progress_time: str = "        "
			self._progress_interrupt = False
			self._start_timer_value: datetime | None = None
			self._buffer: TextBufferType = TextBufferType(log_environment)
			self._init_buffer(console_width)
			self._initial_log()
		else:
			raise ReCreationException("Logger class object already created")

	def _init_buffer(self, console_width: int) -> None:
		"""
		Initializes a Text Buffer.

		.. versionadded:: 0.0.0

		:param console_width: Console width
		:type console_width: int
		"""
		buffer_classes = {
			LogEnvironments.CONSOLE.environment_name: (TextBuffer, (self._environment, console_width)),
			LogEnvironments.PLAIN_CONSOLE.environment_name: (TextBuffer, (self._environment, console_width)),
			LogEnvironments.HTML.environment_name: (BasicTextBuffer, (self._environment,)),
			LogEnvironments.MARKDOWN.environment_name: (BasicTextBuffer, (self._environment,)),
			LogEnvironments.PLAIN.environment_name: (BasicTextBuffer, (self._environment,))
		}

		buffer_class, buffer_args = buffer_classes.get(self._environment.environment_name, (None, None))
		if buffer_class:
			if buffer_class._instance is not None:
				self._buffer = buffer_class._instance
				self.entry(
					entry_type=LoggerEntryTypes.notice,
					message_text="An existing buffer was taken into use",
					local_settings={"italic": True} if buffer_class == TextBuffer else None
				)
			else:
				self._buffer = buffer_class(*buffer_args)
		else:
			raise InitException("Text buffer initialization error")

	def _initial_log(self) -> None:
		"""
		Displays initialized information.

		.. versionadded:: 0.0.0
		"""
		if self._environment.weak_environment:
			self._buffer << "<body style='background-color: #000000; color: #ffffff;'>"
		self._buffer << self._initialized_data(
			[
				ServiceLogger.initial[0][self._environment.environment_code][self._settings["global_background"]],
				ServiceLogger.initial[1][self._environment.environment_code][self._settings["global_background"]]
			]
		)
		if self._environment.updatable:
			self._buffer.update_console()

	def set_icons(self, icon_set: int) -> None:
		"""
		Changes the current icon set used by the Logger.

		.. versionadded:: 0.0.0

		:param icon_set: Icon set to use
		:type icon_set: int
		"""
		self._icon_set = icon_set if 0 < icon_set < 5 else 1

	def set_settings(
		self,
		*,
		global_bold_font: bool = None,
		global_italic_font: bool = None,
		global_invert_font: bool = None,
		global_background: bool = None
	) -> None:
		"""
		Method that sets new Logger settings.

		.. versionadded:: 0.9.2

		:param global_bold_font: Sets the global setting "bold font"
		:type global_bold_font: bool
		:param global_italic_font: Sets the global setting "italic font"
		:type global_italic_font: bool
		:param global_invert_font: Sets the global setting "invert font"
		:type global_invert_font: bool
		:param global_background: Sets the global setting "background"
		:type global_background: bool
		"""
		if global_bold_font is not None:
			self._settings['global_bold_font'] = global_bold_font
		if global_italic_font is not None:
			self._settings['global_italic_font'] = global_italic_font
		if global_invert_font is not None:
			self._settings['global_invert_font'] = global_invert_font
		if global_background is not None:
			self._settings['global_background'] = global_background

	def get_settings(self) -> dict:
		"""
		Returns a dictionary of settings.

		.. versionadded:: 0.9.2

		:return: A dictionary of settings
		:rtype: dict
		"""
		return self._settings

	# ######################################################################################## #
	#                                                                                          #
	#                                        Publishers                                        #
	#                                                                                          #
	# ######################################################################################## #

	def publish_id(self) -> None:
		"""
		A method that publishes information about the Logger ID in the Logger's Buffer.

		.. versionadded:: 0.0.0
		"""
		self.empty(f"Logger ID is {str(self._ID)}")

	def publish_program_name(self) -> None:
		"""
		A method that publishes information about the name of the logging program in the Logger Buffer.

		.. versionadded:: 0.0.0
		"""
		self.empty(f"Program name which logging is {self._program_name}")

	def publish_environment(self) -> None:
		"""
		A method that publishes information about the Logger's environment to the Logger Buffer.

		.. versionadded:: 0.0.0
		"""
		self.empty(f"Logger environment is {self._environment.environment_name}")

	def publish_global_settings(self) -> None:
		"""
		A method that publishes information about the Logger's global settings to the Logger Buffer.

		.. versionadded:: 0.0.0
		"""
		self.empty("Global settings:")
		self.empty(f"    Bold font is set to {str(self._settings['global_bold_font'])};")
		self.empty(f"    Italic font is set to {str(self._settings['global_italic_font'])};")
		self.empty(f"    Invert font is set to {str(self._settings['global_invert_font'])};")
		self.empty(f"    Background is set to {str(self._settings['global_background'])};")

	def publish_author(self) -> None:
		"""
		A method that publishes information about the Author of the library to the Logger Buffer.

		.. versionadded:: 0.0.0
		"""
		self.empty("Developed by Kalynovsky Valentin © 2023")

	def publish_license(self) -> None:
		"""
		A method that publishes information about the Library's License to the Logger Buffer.

		.. versionadded:: 0.0.0
		"""
		self.empty("LICENSE")
		self.empty("    Copyright © 2023 Kalynovsky Valentin. All rights reserved.")
		self.empty("    Licensed under the Apache License, Version 2.0 (the 'License');")
		self.empty("    you may not use this file except in compliance with the License.")
		self.empty("    You may obtain a copy of the License at")
		self.empty("        http://www.apache.org/licenses/LICENSE-2.0")
		self.empty("    Unless required by applicable law or agreed to in writing, software")
		self.empty("    distributed under the License is distributed on an 'AS IS' BASIS,")
		self.empty("    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.")
		self.empty("    See the License for the specific language governing permissions and")
		self.empty("    limitations under the License.")

	def separator(self) -> None:
		"""
		A method that adds a separator.

		.. versionadded:: 0.0.0
		"""
		self.empty(f"{'-' * 80}")

	# ######################################################################################## #
	#                                                                                          #
	#                                    Inputter of Logger                                    #
	#                                                                                          #
	# ######################################################################################## #

	def empty(self, entry: str) -> None:
		"""
		Empty logging:
		A type denoting an "empty" entry - an entry that carries nothing but the purest text.

		.. versionadded:: 0.6.0

		:param entry: "Empty" entry
		:type entry: str
		"""
		self._buffer.append(entry)
		if self._environment.updatable:
			self._buffer.update_console()

	def addy(self, number_string: int, message: str) -> None:
		"""
		A method that adds the given string to the Logger Buffer at the given position.
		It is an add-on for the Buffer insert() method.

		.. versionadded:: 0.0.0

		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str
		"""
		self._buffer.insert(number_string, message)
		if self._environment.updatable:
			self._buffer.update_console()

	def modify(self, number_string: int, message: str) -> None:
		"""
		A method that replaces the string at the given position
		in the Logger Buffer with the given string.
		It is an add-on for the Buffer replace() method.

		.. versionadded:: 0.0.0

		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str
		"""
		self._buffer.replace(number_string, message)
		if self._environment.updatable:
			self._buffer.update_console()

	def catchy(self, number_string: int) -> str:
		"""
		A method that extracts the given string from the Logger Buffer and returns.
		It is an add-on for the Buffer pop() method.

		.. versionadded:: 0.0.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str
		"""
		data = self._buffer.pop(number_string)
		if self._environment.updatable:
			self._buffer.update_console()
		return data

	def extractly(self, number_string: int) -> None:
		"""
		A method that extracts the given string from the Logger Buffer without returning.
		It is an add-on for the Buffer remove() method.

		.. versionadded:: 0.0.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		"""
		self._buffer.remove(number_string)
		if self._environment.updatable:
			self._buffer.update_console()

	def clearly(self) -> None:
		"""
		A method that clears the entire Logger Buffer.
		It is an add-on for the Buffer clear() method.

		.. versionadded:: 0.0.0
		"""
		self._buffer.clear()
		if self._environment.updatable:
			self._buffer.update_console()

	def savy(self, name_file: str, clean: bool) -> None:
		"""
		A method that saves the Logger Buffer to a file. You can turn on formatting cleanup.
		It is an add-on for the Buffer save() method.

		.. versionadded:: 0.0.0

		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool
		"""
		self._buffer.save(name_file, clean)
		if self._environment.updatable:
			self._buffer.update_console()

	def loady(self, name_file: str) -> None:
		"""
		A method that loads the Logger Buffer from a file.
		It is an add-on for the Buffer load() method.

		.. versionadded:: 0.0.0

		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str
		"""
		self._buffer.load(name_file)
		if self._environment.updatable:
			self._buffer.update_console()

	def getty(self, input_text: str) -> str:
		"""
		A method that allows you to use the standard Python input()
		during the operation of the Logger, acting as its wrapper.
		It is an add-on for the Buffer input() method.

		.. versionadded:: 0.0.0

		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str
		"""
		self._buffer << "."
		if self._environment.updatable:
			self._buffer.update_console()
		data = self._buffer.input(input_text)
		self._buffer.replace(-1, f"{input_text}{data}")
		return data

	# ######################################################################################## #
	#                                                                                          #
	#                                    Modifier of Logger                                    #
	#                                                                                          #
	# ######################################################################################## #

	def sort(self, key: SortingKeyType) -> None:
		"""
		A method that sorts the Logger Buffer following the specified sort key.

		.. versionadded:: 0.0.0

		:param key: The key to sort by
		:type key: SortingKeyType
		"""
		sorter = Modifier(self._buffer.get_data().copy(), self._environment)
		sorter.sort(key)
		sorted_buffer = sorter.entries
		self.clearly()
		for entry in sorted_buffer:
			self.empty(entry)

	def sort_with_save(self, key: SortingKeyType, sort_file_name: str) -> None:
		"""
		A method that sorts the Logger Buffer following the specified sort key
		and saves it to a file. After saving, the Buffer is restored.

		.. versionadded:: 0.0.0

		:param key: The key to sort by
		:type key: SortingKeyType
		:param sort_file_name: The name of the file where you want to save the sorted Logs
		:type sort_file_name: str
		"""
		original = self._buffer.get_data().copy()
		sorter = Modifier(self._buffer.get_data(), self._environment)
		sorter.sort(key)
		self._buffer.save(sort_file_name, False)
		self._buffer.get_data().clear()
		self._buffer.get_data().extend(original)

	def search(self, keyword: str, empty: bool) -> None:
		"""
		A method that searches the Logger Buffer for a given keyword/letter/phrase.
		You can also enable the search for "empty" strings.

		.. versionadded:: 0.0.0

		:param keyword: Keyword/letter/phrase
		:type keyword: str
		:param empty: Flag indicating whether to search in custom strings
		:type empty: bool
		"""
		searcher = Modifier(self._buffer.get_data().copy(), self._environment)
		searcher.search(keyword, empty)
		searched_buffer = searcher.entries
		self.clearly()
		for entry in searched_buffer:
			self.empty(entry)

	def search_with_save(self, keyword: str, empty: bool, search_file_name: str) -> None:
		"""
		A method that searches the Logger Buffer for a given keyword/letter/phrase.
		You can also enable the search for "empty" strings.
		The found strings are saved to a file. After saving, the Buffer is restored.

		.. versionadded:: 0.0.0

		:param keyword: Keyword/letter/phrase
		:type keyword: str
		:param empty: Flag indicating whether to search in custom strings
		:type empty: bool
		:param search_file_name: The name of the file where you want to save the searched Logs
		:type search_file_name: str
		"""
		original = self._buffer.get_data().copy()
		searcher = Modifier(self._buffer.get_data(), self._environment)
		searcher.search(keyword, empty)
		self._buffer.save(search_file_name, False)
		self._buffer.get_data().clear()
		self._buffer.get_data().extend(original)

	def select(self, entry_type: EntryType) -> None:
		"""
		A method that selects entries in the Logger Buffer with the specified category or type.

		.. versionadded:: 0.0.0

		:param entry_type: Entries Type/Category
		:type entry_type: EntryType
		"""
		selector = Modifier(self._buffer.get_data().copy(), self._environment)
		selector.select(entry_type)
		selected_buffer = selector.entries
		self.clearly()
		for entry in selected_buffer:
			self.empty(entry)

	def select_with_save(self, entry_type: EntryType, select_file_name: str) -> None:
		"""
		A method that selects entries in the Logger Buffer with the specified
		category or type and saves them to a file. After saving, the Buffer is restored.

		.. versionadded:: 0.0.0

		:param entry_type: Entries Type/Category
		:type entry_type: EntryType
		:param select_file_name: The name of the file where you want to save the selected Logs
		:type select_file_name: str
		"""
		original = self._buffer.get_data().copy()
		selector = Modifier(self._buffer.get_data(), self._environment)
		selector.select(entry_type)
		self._buffer.save(select_file_name, False)
		self._buffer.get_data().clear()
		self._buffer.get_data().extend(original)

	def export_to_csv(self, export_file_name: str) -> None:
		"""
		Method that exports the Logger Buffer to a csv table.

		.. versionadded:: 0.0.0

		:param export_file_name: The name of the file where you want to save the csv table
		:type export_file_name: str
		"""
		exporter = Exporter(self._buffer.get_data(), self._environment)
		exporter.export_to_csv()
		exporter.save_to_csv(export_file_name)

	# ######################################################################################## #
	#                                                                                          #
	#                                    Entering to Logger                                    #
	#                                                                                          #
	# ######################################################################################## #

	def entry(
		self,
		entry_type: EntryType,
		message_text: str,
		local_settings: dict = None
	) -> None:
		"""
		A method that generates and adds an entry to the Logger.

		.. versionadded:: 0.0.0

		:param entry_type: Entry type
		:type entry_type: EntryType
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		if local_settings is None:
			local_settings = {}
		self.empty(
			self._assemble_entry(
				entry_type,
				self._icon_set,
				self._progress_time,
				message_text,
				local_settings
			)
		)

	# ######################################################################################## #
	#                                                                                          #
	#                                  Entering to Processes                                   #
	#                                                                                          #
	# ######################################################################################## #

	def start_indefinite_process(
		self,
		message_text: str,
		animation: IndefiniteAnimationType = IndefiniteAnimations.Line,
		local_settings: dict = None
	) -> None:
		"""
		A method that starts the whole process of indefinite logging. While the process
		is running, you cannot start other processes in the Logger and call the entering
		methods directly. While the process is running - the last entry will play
		the animation of the process. Before starting a process, you can specify that
		the process Logs and configure Initiation and Progress entries.

		.. versionadded:: 0.6.0

		:param message_text: Log entry message
		:type message_text: str
		:param animation: The name of the animation that will play in the Progress entry
		:type animation: IndefiniteAnimationType
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		self._animation = animation

		self._progress_start = datetime.now()
		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(ServiceProcessEntryTypes.initiation, **args)

		thread = Thread(target=self._indefinite_progress, kwargs=args)
		thread.start()

	def _indefinite_progress(
		self,
		message_text: str,
		local_settings: dict = None
	) -> None:
		"""
		A method that creates an animation entry. Only works on the last string.
		You need to run in a thread. Terminates when the process stop flag
		is set by the Logger.stop_process() method.

		.. versionadded:: 0.6.0

		:param message_text: Log entry message
		:type message_text: str
		:param local_background: Display entry with background?
		:type local_background: bool
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		if local_settings is None:
			local_settings = {}
		animation_index = 0
		self._buffer << "."
		if self._environment.updatable:
			self._buffer.update_console()
		while not self._progress_interrupt:
			animation_item = self._animation.animation[animation_index]
			self._buffer.get_data()[-1] = self._assemble_entry(
				ServiceProcessEntryTypes.process,
				self._icon_set,
				animation_item,
				message_text,
				local_settings
			)
			animation_index = (animation_index + 1) % len(self._animation.animation)
			if self._environment.updatable:
				self._buffer.update_entry()
			sleep(0.1)
		if self._environment.updatable:
			self._buffer.update_console()

	def start_definite_process(
		self,
		message_text: str,
		progress_bar: DefiniteAnimationType = DefiniteAnimations.Line,
		local_settings: dict = None
	) -> None:
		"""
		A method that starts the whole process of a definite logging. While the process
		is running, you cannot start other processes in the Logger and call the entering
		methods directly. While the process is running - the last entry will display
		the progress of the process. Before starting a process, you can specify that
		the process Logs and configure Initiation and Progress entries.

		.. versionadded:: 0.6.0

		:param message_text: Log entry message
		:type message_text: str
		:param progress_bar: The name of the progress bar that will play in the Progress entry
		:type progress_bar: DefiniteAnimationType
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		self._animation = progress_bar

		self._progress_start = datetime.now()
		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(ServiceProcessEntryTypes.initiation, **args)

		thread = Thread(target=self._definite_progress, kwargs=args)
		thread.start()

	def _definite_progress(
		self,
		message_text: str,
		local_settings: dict = None
	) -> None:
		"""
		A method that creates a progress bar entry. Only works on the last string.
		You need to run in a thread. Terminates when the process stop flag
		is set by the Logger.stop_process() method.

		.. versionadded:: 0.6.0

		:param message_text: Log entry message
		:type message_text: str
		:param local_background: Display entry with background?
		:type local_background: bool
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		if local_settings is None:
			local_settings = {}
		old_progress_rise = 0
		self._buffer << "."
		if self._environment.updatable:
			self._buffer.update_console()
		while not self._progress_interrupt:
			if old_progress_rise == self._progress_rise:
				continue
			else:
				old_progress_rise = self._progress_rise
				animation_item = f"{self._animation.animation[(self._progress_rise // 15) + (2 if self._progress_rise == 100 else 1)]} - {self._progress_rise} %"
				self._buffer.get_data()[-1] = self._assemble_entry(
					ServiceProcessEntryTypes.process,
					self._icon_set,
					animation_item,
					message_text,
					local_settings
				)
				if self._environment.updatable:
					self._buffer.update_entry()
			sleep(0.1)
		if self._environment.updatable:
			self._buffer.update_console()

	def progress_rise(self, percent: int) -> None:
		"""
		Sets the process completion percentage. Usually used for a specific process.
		However, it is used for both types of processes as a flag for the success
		of the process. If you set the percentage of completion to 100% before terminating
		the process, the process will complete successfully, otherwise it will fail.

		.. versionadded:: 0.6.0

		:param percent: Process completion percentage
		:type percent: int
		"""
		self._progress_rise = percent

	def note_process(
		self,
		entry_type: EntryType,
		message_text: str,
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
		Use `from mighty_logger.src import LoggerEntryTypes`
		or `from mighty_logger.src import ProcessEntryTypes` for `entry_type`.

		.. versionadded:: 0.6.0

		:param entry_type: The type of entry to be entered in the progress history
		:type entry_type: EntryType
		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		sleep(0.001)
		last = self._buffer.pop()

		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(entry_type, **args)

		self.empty(last)

	def stop_process(
		self,
		message_text: str,
		local_settings: dict = None
	) -> None:
		"""
		The method that terminates the process. If before the end of the process
		its execution has reached 100% - the process was completed successfully,
		otherwise - failed. After calling this method, the Progress entry will be replaced
		by the entry with the result of the process execution.

		.. versionadded:: 0.6.0

		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		self._progress_interrupt = True
		sleep(0.11)
		self._buffer.remove()

		progress_stop = datetime.now()
		self._progress_time = "&" + str(progress_stop - self._progress_start).split(".")[0]
		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(
			ServiceProcessEntryTypes.success if self._progress_rise == 100 else ServiceProcessEntryTypes.fail,
			**args
		)

		self._progress_rise = 0
		self._progress_start = None
		self._progress_time = "        "
		self._progress_interrupt = False

	# ######################################################################################## #
	#                                                                                          #
	#                                     Entering to Timer                                    #
	#                                                                                          #
	# ######################################################################################## #

	def start_timer(
		self,
		message_text: str,
		local_settings: dict = None
	) -> None:
		"""
		Stores the current time as the start time and write entry about the current time.

		.. versionadded:: 0.6.1
		?

		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		self._start_timer_value = datetime.now()
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(ServiceTimerEntryTypes.start_timer, **args)

		self._progress_time = "        "

	def timer_mark(
		self,
		message_text: str,
		local_settings: dict = None
	) -> None:
		"""
		Calculates the difference between current and start time
		and write entry about the difference.

		.. versionadded:: 0.6.1
		?

		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		mark_timer_value = datetime.now()
		self._progress_time = "^" + str(mark_timer_value - self._start_timer_value).split(".")[0]

		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(ServiceTimerEntryTypes.timer_mark, **args)

		self._progress_time = "        "

	def stop_timer(
		self,
		message_text: str,
		local_settings: dict = None
	) -> None:
		"""
		Calculates the difference between the current and start time,
		write entry about the difference, and resets the start time.

		.. versionadded:: 0.6.1
		?

		:param message_text: Log entry message
		:type message_text: str
		:param local_settings: Dictionary of local entering settings
		:type local_settings: dict
		"""
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(ServiceTimerEntryTypes.stop_timer, **args)

		self._start_timer_value = None
		self._progress_time = "        "
