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

from mighty_logger.basic.lib_types import EnvironmentType
from mighty_logger.src.entry_types import LoggerEntryTypes, ServiceProcessEntryTypes
from mighty_logger.src.environments import LogEnvironments
from mighty_logger import Logger

class SimpleLogger:
	"""
	...
	"""

	def __init__(
		self,
		program_name: str = "Unknown",
		environment: EnvironmentType = LogEnvironments.HTML,
		console_width: int = 60
	):
		self.__logger = Logger(
			program_name=program_name,
			log_environment=environment,
			console_width=console_width,
			status_global_entry=False,
			status_message_global_entry=False
		)

	def get_logger(self) -> Logger:
		return self.__logger

	def print(self, printing_text: str) -> None:
		self.__logger.empty(entry=printing_text)

	def input(self, printing_text: str) -> str:
		return self.__logger.getty(printing_text)

	def save(self, name_file: str, clean: bool = True) -> None:
		self.__logger.savy(name_file, clean)

	def load(self, name_file: str) -> None:
		self.__logger.loady(name_file)

	def separator(self) -> None:
		self.__logger.separator()

	def debug(self, message_text: str = "...") -> None:
		"""
		Debugging information logging:
		Can be used to log entry any information while debugging an application.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.debug,
			message_text=message_text
		)

	def debug_performance(self, message_text: str = "...") -> None:
		"""
		Performance debugging information logging:
		Can be used to log entry the execution time of operations or other
		performance information while the application is being debugged.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.debug_performance,
			message_text=message_text
		)

	def performance(self, message_text: str = "...") -> None:
		"""
		Performance information logging:
		Can be used to log entry the execution time of operations or
		other application performance information.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.performance,
			message_text=message_text
		)

	def event(self, message_text: str = "...") -> None:
		"""
		Event information logging:
		Can be used to log entry specific events in the application,
		such as button presses or mouse cursor movements.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.event,
			message_text=message_text
		)

	def audit(self, message_text: str = "...") -> None:
		"""
		Audit information logging:
		Can be used to log entry changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.audit,
			message_text=message_text
		)

	def metrics(self, message_text: str = "...") -> None:
		"""
		Metrics information logging:
		Can be used to log entry metrics to track application performance and identify issues.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.metrics,
			message_text=message_text
		)

	def user(self, message_text: str = "...") -> None:
		"""
		User information logging:
		Can be used to log entry custom logs to store additional information
		that may be useful for diagnosing problems.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.user,
			message_text=message_text
		)

	def message(self, message_text: str = "...") -> None:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.message,
			message_text=message_text
		)

	def info(self, message_text: str = "...") -> None:
		"""
		Default information logging:
		Can be used to log entry messages with specific content about the operation of the program.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.info,
			message_text=message_text
		)

	def notice(self, message_text: str = "...") -> None:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.notice,
			message_text=message_text
		)

	def warning(self, message_text: str = "...") -> None:
		"""
		Warning information logging:
		Can be used to log entry warnings that the program may work with unpredictable results.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.warning,
			message_text=message_text
		)

	def error(self, message_text: str = "...") -> None:
		"""
		Error information logging:
		Used to log entry errors and crashes in the program.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.error,
			message_text=message_text
		)

	def critical(self, message_text: str = "...") -> None:
		"""
		Critical error information logging:
		Used to log entry for critical and unpredictable program failures.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=LoggerEntryTypes.critical,
			message_text=message_text
		)

	def success(self, message_text: str = "...") -> None:
		"""
		Success information logging:
		Used to log entry a message about the success of the process.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=ServiceProcessEntryTypes.success,
			message_text=message_text
		)

	def fail(self, message_text: str = "...") -> None:
		"""
		Fail information logging:
		Used to log entry a message about the failed execution of the process.

		:param message_text: Log entry message
		"""
		self.__logger.entry(
			entry_type=ServiceProcessEntryTypes.fail,
			message_text=message_text
		)
