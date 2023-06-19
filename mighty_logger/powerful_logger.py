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
from mighty_logger.src.entry_types import EntryType, ServiceLogger, ServiceProcessEntryTypes, ServiceTimerEntryTypes
from mighty_logger.src.log_enums import LogEnvironments
from mighty_logger.src.status_variables import StatusMessageType
from mighty_logger.text.animation import BasicAnimationType, IndefiniteAnimationType, DefiniteAnimationType, IndefiniteAnimations, DefiniteAnimations
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
		log_environment: bool = LogEnvironments.CONSOLE,
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
			super().__init__(program_name)
			self._animation: BasicAnimationType = BasicAnimationType([])
			self._icon_set = 1 if 4 < icon_set < 1 else icon_set
			self._settings["global_bold_font"] = global_bold_font
			self._settings["global_italic_font"] = global_italic_font
			self._settings["global_invert_font"] = global_invert_font
			self._settings["time_global_entry"] = time_global_entry
			self._settings["status_global_entry"] = status_global_entry
			self._settings["status_message_global_entry"] = status_message_global_entry
			self._settings["status_type_global_entry"] = status_type_global_entry
			self._settings["message_global_entry"] = message_global_entry
			self._environment = log_environment
			self._progress_rise = 0
			self._progress_start: datetime | None = None
			self._progress_time: str = "        "
			self._progress_interrupt = False
			self._start_timer_value: datetime | None = None
			self.global_background = global_background
			if self._environment:
				if BasicTextBuffer._instance is not None:
					self._buffer = BasicTextBuffer._instance
					self.notice(
						message_text="An existing logger was taken into use",
						status_message=StatusMessageType("Note"),
						local_settings={"italic": True}
					)
				else:
					self._buffer = BasicTextBuffer()
			else:
				if TextBuffer._instance is not None:
					self._buffer = TextBuffer._instance
					self.notice(
						message_text="An existing logger was taken into use",
						status_message=StatusMessageType("Note"),
						local_settings={"italic": True}
					)
				else:
					self._buffer = TextBuffer(console_width)
			self._initial_log()
		else:
			raise ReCreationException("Logger class object already created")

	def _initial_log(self) -> None:
		"""
		Displays initialized information.
		"""
		if self._environment:
			self._buffer << "<body style='background-color: #000000; color: #ffffff;'>"
		self._buffer << self._initialized_data(
			[
				ServiceLogger.initial[0][self._environment][self.global_background],
				ServiceLogger.initial[1][self._environment][self.global_background]
			], self._environment
		)
		if not self._environment:
			self._buffer.update_console()

	def set_icons(self, icon_set: int) -> None:
		"""
		Changes the current icon set used by the Logger.

		:param icon_set: Icon set to use
		"""
		if 4 < icon_set < 1:
			...
		else:
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
				self._ColorScheme[logger_color_name][1] = Dec2Ansi(color_value, "background") if not self._environment else Dec2Hex(color_value)
			elif background and foreground:
				self._ColorScheme[logger_color_name][1] = Dec2Ansi(color_value, "foreground") if not self._environment else Dec2Hex(color_value)
			elif not background and foreground:
				self._ColorScheme[logger_color_name][0] = Dec2Ansi(color_value, "foreground") if not self._environment else Dec2Hex(color_value)
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
		if not self._environment:
			self._buffer.update_console()

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
		self._buffer << self._assemble_entry(
			[
				entry_type.time_color[self._environment][background],
				entry_type.status_color[self._environment][background],
				entry_type.status_message_color[self._environment][background],
				entry_type.type_color[self._environment][background],
				entry_type.message_color[self._environment][background],
				entry_type.background_color[self._environment][background]
			],
			self._progress_time,
			entry_type.icon[self._icon_set],
			status_message.current_status_message,
			entry_type.type_name,
			message_text,
			self._environment,
			local_settings
		)
		if not self._environment:
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
		if not self._environment:
			self._buffer.update_console()
		while not self._progress_interrupt:
			animation_item = self._animation.animation[animation_index]
			background = local_background if local_background is not None else self.global_background
			self._buffer.get_data()[-1] = self._assemble_entry(
				[
					ServiceProcessEntryTypes.process.time_color[self._environment][background],
					ServiceProcessEntryTypes.process.status_color[self._environment][background],
					ServiceProcessEntryTypes.process.status_message_color[self._environment][background],
					ServiceProcessEntryTypes.process.type_color[self._environment][background],
					ServiceProcessEntryTypes.process.message_color[self._environment][background],
					ServiceProcessEntryTypes.process.background_color[self._environment][background]
				],
				animation_item,
				ServiceProcessEntryTypes.process.icon[self._icon_set],
				status_message.current_status_message,
				ServiceProcessEntryTypes.process.type_name,
				message_text,
				self._environment,
				local_settings
			)
			animation_index = (animation_index + 1) % len(self._animation.animation)
			if not self._environment:
				self._buffer.update_entry()
			sleep(0.1)
		if not self._environment:
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
		if not self._environment:
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
						ServiceProcessEntryTypes.process.time_color[self._environment][background],
						ServiceProcessEntryTypes.process.status_color[self._environment][background],
						ServiceProcessEntryTypes.process.status_message_color[self._environment][background],
						ServiceProcessEntryTypes.process.type_color[self._environment][background],
						ServiceProcessEntryTypes.process.message_color[self._environment][background],
						ServiceProcessEntryTypes.process.background_color[self._environment][background]
					],
					animation_item,
					ServiceProcessEntryTypes.process.icon[self._icon_set],
					status_message.current_status_message,
					ServiceProcessEntryTypes.process.type_name,
					message_text,
					self._environment,
					local_settings
				)
				if not self._environment:
					self._buffer.update_entry()
			sleep(0.1)
		if not self._environment:
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
