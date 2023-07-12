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
from mighty_logger.src.animations import IndefiniteAnimations, DefiniteAnimations
from mighty_logger.src.entry_types import ServiceLogger,\
	LoggerEntryTypes,\
	ServiceProcessEntryTypes,\
	ServiceTimerEntryTypes
from mighty_logger.src.environments import LogEnvironments
from mighty_logger.src.sorting_keys import SortingKeys

class MightyLogger(BasicLogger):
	def __init__(
		self,
		*,
		program_name: str,
		log_environment: EnvironmentType,
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

	# ######################################################################################## #
	#                                                                                          #
	#                                         Property                                         #
	#                                                                                          #
	# ######################################################################################## #

	@property
	def settings(self) -> dict:
		return self._settings

	@property
	def buffer(self) -> list:
		return self._buffer.text_buffer

	# ######################################################################################## #
	#                                                                                          #
	#                                         Settings                                         #
	#                                                                                          #
	# ######################################################################################## #

	def _init_buffer(self, console_width: int) -> None:
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
		if self._environment.weak_environment:
			self.empty("<body style='background-color: #000000; color: #ffffff;'>")
		self.empty(self._initialized_data([
			ServiceLogger.initial[0][self._environment.environment_code][self._settings["global_background"]],
			ServiceLogger.initial[1][self._environment.environment_code][self._settings["global_background"]]
		]))
		if self._environment.updatable:
			self._buffer.update_console()

	def set_icons(self, icon_set: int) -> None:
		self._icon_set = icon_set if 0 < icon_set < 5 else 1

	def set_settings(
		self,
		*,
		global_bold_font: bool = None,
		global_italic_font: bool = None,
		global_invert_font: bool = None,
		global_background: bool = None
	) -> None:
		if global_bold_font is not None:
			self._settings['global_bold_font'] = global_bold_font
		if global_italic_font is not None:
			self._settings['global_italic_font'] = global_italic_font
		if global_invert_font is not None:
			self._settings['global_invert_font'] = global_invert_font
		if global_background is not None:
			self._settings['global_background'] = global_background

	# ######################################################################################## #
	#                                                                                          #
	#                                    Inputter of Logger                                    #
	#                                                                                          #
	# ######################################################################################## #

	def empty(self, entry: str) -> None:
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
		self.empty(".")
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
		sorter = Modifier(self._buffer.text_buffer.copy(), self._environment)
		sorter.sort(key)
		sorted_buffer = sorter.entries
		self.clearly()
		for entry in sorted_buffer:
			self.empty(entry)

	def sort_with_save(self, key: SortingKeyType, sort_file_name: str) -> None:
		original = self._buffer.text_buffer.copy()
		sorter = Modifier(self._buffer.get_data(), self._environment)
		sorter.sort(key)
		self._buffer.save(sort_file_name, False)
		self._buffer.get_data().clear()
		self._buffer.get_data().extend(original)

	def search(self, keyword: str, empty: bool) -> None:
		searcher = Modifier(self._buffer.text_buffer.copy(), self._environment)
		searcher.search(keyword, empty)
		searched_buffer = searcher.entries
		self.clearly()
		for entry in searched_buffer:
			self.empty(entry)

	def search_with_save(self, keyword: str, empty: bool, search_file_name: str) -> None:
		original = self._buffer.text_buffer.copy()
		searcher = Modifier(self._buffer.get_data(), self._environment)
		searcher.search(keyword, empty)
		self._buffer.save(search_file_name, False)
		self._buffer.get_data().clear()
		self._buffer.get_data().extend(original)

	def select(self, entry_type: EntryType) -> None:
		selector = Modifier(self._buffer.text_buffer.copy(), self._environment)
		selector.select(entry_type)
		selected_buffer = selector.entries
		self.clearly()
		for entry in selected_buffer:
			self.empty(entry)

	def select_with_save(self, entry_type: EntryType, select_file_name: str) -> None:
		original = self._buffer.text_buffer.copy()
		selector = Modifier(self._buffer.get_data(), self._environment)
		selector.select(entry_type)
		self._buffer.save(select_file_name, False)
		self._buffer.get_data().clear()
		self._buffer.get_data().extend(original)

	def export_to_csv(self, export_file_name: str) -> None:
		exporter = Exporter(self._buffer.text_buffer, self._environment)
		exporter.export_to_csv()
		exporter.save_to_csv(export_file_name)

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
		self.empty(f"    Background is set to {str(self._settings['global_background'])};")

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
	#                                    Entering to Logger                                    #
	#                                                                                          #
	# ######################################################################################## #

	def entry(
		self,
		entry_type: EntryType,
		message_text: str,
		local_settings: dict = None
	) -> None:
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
		if local_settings is None:
			local_settings = {}
		animation_index = 0
		self.empty(".")
		if self._environment.updatable:
			self._buffer.update_console()
		while not self._progress_interrupt:
			animation_item = self._animation.animation[animation_index]
			self._buffer.text_buffer[-1] = self._assemble_entry(
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
		if local_settings is None:
			local_settings = {}
		old_progress_rise = 0
		self.empty(".")
		if self._environment.updatable:
			self._buffer.update_console()
		while not self._progress_interrupt:
			if old_progress_rise == self._progress_rise:
				continue
			else:
				old_progress_rise = self._progress_rise
				animation_item = f"{self._animation.animation[(self._progress_rise // 15) + (2 if self._progress_rise == 100 else 1)]} - {self._progress_rise} %"
				self._buffer.text_buffer[-1] = self._assemble_entry(
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
		self._progress_rise = percent

	def note_process(
		self,
		entry_type: EntryType,
		message_text: str,
		local_settings: dict = None
	) -> None:
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
		stop_timer_value = datetime.now()
		self._progress_time = "^" + str(stop_timer_value - self._start_timer_value).split(".")[0]

		args = {'message_text': message_text}
		if local_settings is not None:
			args['local_settings'] = local_settings
		self.entry(ServiceTimerEntryTypes.stop_timer, **args)

		self._start_timer_value = None
		self._progress_time = "        "
