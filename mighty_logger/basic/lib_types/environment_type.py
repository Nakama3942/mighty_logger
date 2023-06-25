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

class EnvironmentType:
	def __init__(
		self,
		environment_name: str,
		environment_code: int,
		updatable: bool,
		weak_environment: bool
	) -> None:
		self.__environment_name: str = environment_name
		self.__environment_code: int = environment_code
		self.__updatable: bool = updatable
		self.__weak_environment: bool = weak_environment

	@property
	def environment_name(self) -> str:
		return self.__environment_name

	@property
	def environment_code(self) -> int:
		return self.__environment_code

	@property
	def updatable(self) -> int:
		return self.__updatable

	@property
	def weak_environment(self) -> int:
		return self.__weak_environment
