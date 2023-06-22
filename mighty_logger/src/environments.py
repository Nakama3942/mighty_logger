"""
A module with a list of environment options in which the modules work
and entry types that can be passed to an entry in Progress bar.
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

class EnvironmentType:
	def __init__(self, environment_name: str) -> None:
		self.__environment_name: str = environment_name

	@property
	def environment_name(self) -> str:
		return self.__environment_name

class LogEnvironments:
	"""
	Environments of Logger.
	"""
	CONSOLE = EnvironmentType("0")
	HTML = EnvironmentType("1")
	PLAIN = EnvironmentType("2")
	# PLAIN_CONSOLE = EnvironmentType("3")
	# MARKDOWN = EnvironmentType("4")
