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

from mighty_logger.basic.lib_types.animation_type import BasicAnimationType,\
	IndefiniteAnimationType,\
	DefiniteAnimationType
from mighty_logger.basic.lib_types.entry_type import EntryType
from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.basic.lib_types.status_message_type import StatusMessageType
from mighty_logger.basic.lib_types.text_buffer_type import TextBufferType
from mighty_logger.basic.basic_logger import BasicLogger
from mighty_logger.basic.exceptions import ReCreationException, InitException
from mighty_logger.src.animation import IndefiniteAnimations, DefiniteAnimations
from mighty_logger.src.entry_types import ServiceLogger, LoggerEntryTypes, ServiceProcessEntryTypes, ServiceTimerEntryTypes
from mighty_logger.src.environments import LogEnvironments
from mighty_logger.src.text_buffer import BasicTextBuffer, TextBuffer

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
		log_environment: EnvironmentType = LogEnvironments.PLAIN,
		console_width: int = 60,
		icon_set: int = 1,
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
		if not hasattr(self, "_environment"):
			super().__init__(program_name, log_environment)
			self._animation: BasicAnimationType = BasicAnimationType([])
			self._icon_set = icon_set if 0 < icon_set < 5 else 1
			self._settings["global_bold_font"] = global_bold_font
			self._settings["global_italic_font"] = global_italic_font
			self._settings["global_invert_font"] = global_invert_font
			self._settings["time_global_entry"] = time_global_entry
			self._settings["status_global_entry"] = status_global_entry
			self._settings["status_message_global_entry"] = status_message_global_entry
			self._settings["status_type_global_entry"] = status_type_global_entry
			self._settings["message_global_entry"] = message_global_entry
			self._progress_rise = 0
			self._progress_start: datetime | None = None
			self._progress_time: str = "        "
			self._progress_interrupt = False
			self._start_timer_value: datetime | None = None
			self.global_background = global_background
			self._buffer: TextBufferType = TextBufferType(log_environment)
			self._init_buffer(console_width)
			self._initial_log()
		else:
			raise ReCreationException("Logger class object already created")

	def _init_buffer(self, console_width: int):
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
					status_message=StatusMessageType("Note"),
					local_settings={"italic": True} if buffer_class == TextBuffer else None
				)
			else:
				self._buffer = buffer_class(*buffer_args)
		else:
			raise InitException("Text buffer initialization error")

	def _initial_log(self) -> None:
		"""
		Displays initialized information.
		"""
		if self._environment.weak_environment:
			self._buffer << "<body style='background-color: #000000; color: #ffffff;'>"
		self._buffer << self._initialized_data(
			[
				ServiceLogger.initial[0][self._environment.environment_code][self.global_background],
				ServiceLogger.initial[1][self._environment.environment_code][self.global_background]
			]
		)
		if self._environment.updatable:
			self._buffer.update_console()

	def set_icons(self, icon_set: int) -> None:
		"""
		Changes the current icon set used by the Logger.

		:param icon_set: Icon set to use
		"""
		self._icon_set = icon_set if 0 < icon_set < 5 else 1

	def buffer(self) -> TextBufferType:
		"""
		The Text Buffer object is created in the class constructor and this
		method is used to access it. It returns a buffer.

		:return: a text buffer object
		"""
		return self._buffer

	# ######################################################################################## #
	#                                                                                          #
	#                                        Publishers                                        #
	#                                                                                          #
	# ######################################################################################## #

	def publish_id(self) -> None:
		self.empty(f"Logger ID is {str(self._ID)}")

	def publish_program_name(self) -> None:
		self.empty(f"Program name which logging is {self._program_name}")

	def publish_environment(self) -> None:
		self.empty(f"Logger environment is {self._environment.environment_name}")

	def publish_global_settings(self) -> None:
		self.empty("Global settings:")
		self.empty(f"    Bold font is set to {str(self._settings['global_bold_font'])};")
		self.empty(f"    Italic font is set to {str(self._settings['global_italic_font'])};")
		self.empty(f"    Invert font is set to {str(self._settings['global_invert_font'])};")
		self.empty(f"    Printing of the time in the entry is set to {str(self._settings['time_global_entry'])},")
		self.empty(f"    Printing of the status in the entry is set to {str(self._settings['status_global_entry'])},")
		self.empty(f"    Printing of the status message in the entry is set to {str(self._settings['status_message_global_entry'])},")
		self.empty(f"    Printing of the type of entry is set to {str(self._settings['status_type_global_entry'])},")
		self.empty(f"    Printing of the message of entry is set to {str(self._settings['message_global_entry'])};")

	def publish_author(self) -> None:
		self.empty("Developed by Kalynovsky Valentin © 2023")

	def publish_license(self) -> None:
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
		\n
		Since v0.6.0

		:param entry: "Empty" entry
		"""
		self._buffer.append(entry)
		if self._environment.updatable:
			self._buffer.update_console()

	def addy(self, number_string: int, message: str) -> None:
		self._buffer.insert(number_string, message)
		if self._environment.updatable:
			self._buffer.update_console()

	def modify(self, number_string: int, message: str) -> None:
		self._buffer.replace(number_string, message)
		if self._environment.updatable:
			self._buffer.update_console()

	def catchy(self, number_string: int) -> str:
		data = self._buffer.pop(number_string)
		if self._environment.updatable:
			self._buffer.update_console()
		return data

	def extractly(self, number_string: int) -> None:
		self._buffer.remove(number_string)
		if self._environment.updatable:
			self._buffer.update_console()

	def clearly(self) -> None:
		self._buffer.clear()
		if self._environment.updatable:
			self._buffer.update_console()

	def savy(self, name_file: str, clean: bool) -> None:
		self._buffer.save(name_file, clean)
		if self._environment.updatable:
			self._buffer.update_console()

	def loady(self, name_file: str) -> None:
		self._buffer.load(name_file)
		if self._environment.updatable:
			self._buffer.update_console()

	def getty(self, input_text: str) -> str:
		self._buffer << "."
		if self._environment.updatable:
			self._buffer.update_console()
		data = self._buffer.input(input_text)
		self._buffer.replace(-1, f"{input_text}{data}")
		return data

	# ######################################################################################## #
	#                                                                                          #
	#                                    Entering to Logger                                    #
	#                                                                                          #
	# ######################################################################################## #

	def entry(
		self,
		*,
		entry_type: EntryType,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		...

		:param entry_type:
		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		if local_settings is None:
			local_settings = {}
		background = local_background if local_background is not None else self.global_background
		self.empty(
			self._assemble_entry(
				[
					entry_type.time_color[self._environment.environment_code][background],
					entry_type.status_color[self._environment.environment_code][background],
					entry_type.status_message_color[self._environment.environment_code][background],
					entry_type.type_color[self._environment.environment_code][background],
					entry_type.message_color[self._environment.environment_code][background],
					entry_type.background_color[self._environment.environment_code][background]
				],
				self._progress_time,
				entry_type.icon[self._icon_set],
				status_message.current_status_message,
				entry_type.type_name,
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
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(entry_type=ServiceProcessEntryTypes.initiation, **args)

		thread = Thread(target=self._indefinite_progress, kwargs=args)
		thread.start()

	def _indefinite_progress(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
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
		if self._environment.updatable:
			self._buffer.update_console()
		while not self._progress_interrupt:
			animation_item = self._animation.animation[animation_index]
			background = local_background if local_background is not None else self.global_background
			self._buffer.get_data()[-1] = self._assemble_entry(
				[
					ServiceProcessEntryTypes.process.time_color[self._environment.environment_code][background],
					ServiceProcessEntryTypes.process.status_color[self._environment.environment_code][background],
					ServiceProcessEntryTypes.process.status_message_color[self._environment.environment_code][background],
					ServiceProcessEntryTypes.process.type_color[self._environment.environment_code][background],
					ServiceProcessEntryTypes.process.message_color[self._environment.environment_code][background],
					ServiceProcessEntryTypes.process.background_color[self._environment.environment_code][background]
				],
				animation_item,
				ServiceProcessEntryTypes.process.icon[self._icon_set],
				status_message.current_status_message,
				ServiceProcessEntryTypes.process.type_name,
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
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(entry_type=ServiceProcessEntryTypes.initiation, **args)

		thread = Thread(target=self._definite_progress, kwargs=args)
		thread.start()

	def _definite_progress(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
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
		if self._environment.updatable:
			self._buffer.update_console()
		while not self._progress_interrupt:
			if old_progress_rise == self._progress_rise:
				continue
			else:
				old_progress_rise = self._progress_rise
				animation_item = f"{self._animation.animation[(self._progress_rise // 15) + (2 if self._progress_rise == 100 else 1)]} - {self._progress_rise} %"
				background = local_background if local_background is not None else self.global_background
				self._buffer.get_data()[-1] = self._assemble_entry(
					[
						ServiceProcessEntryTypes.process.time_color[self._environment.environment_code][background],
						ServiceProcessEntryTypes.process.status_color[self._environment.environment_code][background],
						ServiceProcessEntryTypes.process.status_message_color[self._environment.environment_code][background],
						ServiceProcessEntryTypes.process.type_color[self._environment.environment_code][background],
						ServiceProcessEntryTypes.process.message_color[self._environment.environment_code][background],
						ServiceProcessEntryTypes.process.background_color[self._environment.environment_code][background]
					],
					animation_item,
					ServiceProcessEntryTypes.process.icon[self._icon_set],
					status_message.current_status_message,
					ServiceProcessEntryTypes.process.type_name,
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
		\n
		Since v0.6.0

		:param percent: Process completion percentage
		"""
		self._progress_rise = percent

	def note_process(
		self,
		*,
		entry_type: EntryType,
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
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(entry_type=entry_type, **args)

		self.empty(last)

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
		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(
			entry_type=ServiceProcessEntryTypes.success if self._progress_rise == 100 else ServiceProcessEntryTypes.fail,
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
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		...

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		self._start_timer_value = datetime.now()
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(entry_type=ServiceTimerEntryTypes.start_timer, **args)

		self._progress_time = "        "

	def timer_mark(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		...

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(entry_type=ServiceTimerEntryTypes.timer_mark, **args)

		self._progress_time = "        "

	def stop_timer(
		self,
		*,
		status_message: StatusMessageType = StatusMessageType("..."),
		message_text: str = "...",
		local_background: bool = None,
		local_settings: dict = None
	) -> None:
		"""
		...

		:param status_message: Log entry status message
		:param message_text: Log entry message
		:param local_background: Display entry with background?
		:param local_settings: Dictionary of local entering settings
		"""
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		args = {}
		if status_message != StatusMessageType("..."):
			args['status_message'] = status_message
		if message_text != "...":
			args['message_text'] = message_text
		if local_background is not None:
			args['local_background'] = local_background
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(entry_type=ServiceTimerEntryTypes.stop_timer, **args)

		self._start_timer_value = None
		self._progress_time = "        "
