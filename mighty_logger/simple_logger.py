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

from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.basic.singleton import Singleton
from mighty_logger.src.entry_types import LoggerEntryTypes, ServiceProcessEntryTypes
from mighty_logger.src.environments import LogEnvironments
from mighty_logger.mighty_logger import MightyLogger

class Logger(Singleton):
	"""
	Lightweight Logger automates work with entry types.
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
		if MightyLogger._instance is not None:
			self.__logger = MightyLogger._instance
			self.notice("An existing logger was taken into use")
		else:
			self.__logger = MightyLogger(
				program_name=program_name,
				log_environment=log_environment,
				console_width=console_width,
				icon_set=icon_set,
				global_bold_font=global_bold_font,
				global_italic_font=global_italic_font,
				global_invert_font=global_invert_font,
				global_background=global_background
			)

	@property
	def might(self) -> MightyLogger:
		return self.__logger

	def debug(self, message_text: str) -> None:
		"""
		Debugging information logging:
		Can be used to log entry any information while debugging an application.

		:param message_text: Log entry message
		"""
		self.__logger.entry(LoggerEntryTypes.debug, message_text)

	def debug_performance(self, message_text: str) -> None:
		"""
		Performance debugging information logging:
		Can be used to log entry the execution time of operations or other
		performance information while the application is being debugged.
		"""
		self.__logger.entry(LoggerEntryTypes.debug_performance, message_text)

	def performance(self, message_text: str) -> None:
		"""
		Performance information logging:
		Can be used to log entry the execution time of operations or
		other application performance information.
		"""
		self.__logger.entry(LoggerEntryTypes.performance, message_text)

	def event(self, message_text: str) -> None:
		"""
		Event information logging:
		Can be used to log entry specific events in the application,
		such as button presses or mouse cursor movements.
		"""
		self.__logger.entry(LoggerEntryTypes.event, message_text)

	def audit(self, message_text: str) -> None:
		"""
		Audit information logging:
		Can be used to log entry changes in the system, such as creating or
		deleting users, as well as changes in security settings.
		"""
		self.__logger.entry(LoggerEntryTypes.audit, message_text)

	def metrics(self, message_text: str) -> None:
		"""
		Metrics information logging:
		Can be used to log entry metrics to track application performance and identify issues.
		"""
		self.__logger.entry(LoggerEntryTypes.metrics, message_text)

	def user(self, message_text: str) -> None:
		"""
		User information logging:
		Can be used to log entry custom logs to store additional information
		that may be useful for diagnosing problems.
		"""
		self.__logger.entry(LoggerEntryTypes.user, message_text)

	def message(self, message_text: str) -> None:
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.
		"""
		self.__logger.entry(LoggerEntryTypes.message, message_text)

	def info(self, message_text: str) -> None:
		"""
		Default information logging:
		Can be used to log entry messages with specific content about the operation of the program.
		"""
		self.__logger.entry(LoggerEntryTypes.info, message_text)

	def notice(self, message_text: str) -> None:
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.
		"""
		self.__logger.entry(LoggerEntryTypes.notice, message_text)

	def warning(self, message_text: str) -> None:
		"""
		Warning information logging:
		Can be used to log entry warnings that the program may work with unpredictable results.
		"""
		self.__logger.entry(LoggerEntryTypes.warning, message_text)

	def error(self, message_text: str) -> None:
		"""
		Error information logging:
		Used to log entry errors and crashes in the program.
		"""
		self.__logger.entry(LoggerEntryTypes.error, message_text)

	def critical(self, message_text: str) -> None:
		"""
		Critical error information logging:
		Used to log entry for critical and unpredictable program failures.
		"""
		self.__logger.entry(LoggerEntryTypes.critical, message_text)

	def success(self, message_text: str) -> None:
		"""
		Success information logging:
		Used to log entry a message about the success of the process.
		"""
		self.__logger.entry(ServiceProcessEntryTypes.success, message_text)

	def fail(self, message_text: str) -> None:
		"""
		Fail information logging:
		Used to log entry a message about the failed execution of the process.
		"""
		self.__logger.entry(ServiceProcessEntryTypes.fail, message_text)
