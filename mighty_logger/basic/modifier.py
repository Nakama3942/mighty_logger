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

import re

from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.basic.lib_types.sorting_key_type import SortingKeyType
from mighty_logger.src.environments import LogEnvironments
from mighty_logger.src.sorting_keys import SortingKeys

class Modifier:
	def __init__(
		self,
		entries: list[str],
		environment: EnvironmentType = LogEnvironments.CONSOLE
	):
		self.__category_order = {
			"%": 0,
			"~": 1,
			"@": 2,
			"!": 3,
			"&": 4,
			"^": 5
		}
		self.__type_order = {
			'DEBUG': 0,
			'DEBUG-PERFORMANCE': 1,
			'PERFORMANCE': 2,
			'EVENT': 3,
			'AUDIT': 4,
			'METRICS': 5,
			'USER': 6,
			'MESSAGE': 7,
			'INFO': 8,
			'NOTICE': 9,
			'WARNING': 10,
			'!ERROR': 11,
			'!!@CRITICAL': 12,
			'RESOLVED': 13,
			'UNRESOLVED': 14,
			'INITIATION': 15,
			'PROGRESS': 16,
			'ACHIEVEMENT': 17,
			'MILESTONE': 18,
			'SUCCESS': 19,
			'FAIL': 20,
			'START-TIMER': 21,
			'TIMER-MARK': 22,
			'STOP-TIMER': 23
		}
		self.__entries: list[str] = entries
		self.__env: EnvironmentType = environment

	@property
	def entries(self) -> list[str]:
		return self.__entries

	def sort(self, key: SortingKeyType = SortingKeys.SORT_ON_TYPE) -> None:
		cleared_entry = ""
		sorting_entries = []
		count_separators = 0

		for index, entry in enumerate(self.__entries[1:]):
			match self.__env.environment_name:
				case LogEnvironments.CONSOLE.environment_name:
					cleared_entry = re.sub(r"\033\[.*?m", "", entry)
				case LogEnvironments.PLAIN_CONSOLE.environment_name:
					cleared_entry = entry
				case LogEnvironments.HTML.environment_name:
					cleared_entry = re.sub(r"<.*?>", "", entry)
				case LogEnvironments.MARKDOWN.environment_name:
					cleared_entry = re.sub(r"<.*?>", "", entry)
				case LogEnvironments.PLAIN.environment_name:
					cleared_entry = entry
			if cleared_entry.startswith("-?"):
				parts = cleared_entry.split()
				sorting_entries.append([
					self.__entries.pop(index + 1 - len(sorting_entries) - count_separators),
					" ".join(parts[1:3]),
					parts[4][0],
					parts[4][1:]
				])
				continue
			if cleared_entry.startswith("--"):
				self.__entries.pop(index + 1 - len(sorting_entries) - count_separators)
				count_separators += 1
				continue

		match key:
			case SortingKeys.SORT_ON_TIME:
				sorting_entries.sort(key=lambda x: x[1])
			case SortingKeys.SORT_ON_TIME_WITH_REVERSE:
				sorting_entries.sort(key=lambda x: x[1], reverse=True)
			case SortingKeys.SORT_ON_CATEGORY:
				sorting_entries.sort(key=lambda x: self.__category_order.get(x[2], float("inf")))
			case SortingKeys.SORT_ON_TYPE:
				sorting_entries.sort(key=lambda x: self.__type_order.get(x[3], float("inf")))

		sorted_entries = [item[0] for item in sorting_entries]

		self.__entries.insert(1, "----------------------------------Ordered logs----------------------------------")
		self.__entries.insert(2, "-----------------------------Unsorted empty entries-----------------------------")
		self.__entries[2:2] = sorted_entries
		self.__entries.append("--------------------------------------------------------------------------------")

	def search(self, keyword: str):
		cleared_entry = ""
		searching_entries = []
		count_separators = 0

		for index, entry in enumerate(self.__entries[1:]):
			match self.__env.environment_name:
				case LogEnvironments.CONSOLE.environment_name:
					cleared_entry = re.sub(r"\033\[.*?m", "", entry)
				case LogEnvironments.PLAIN_CONSOLE.environment_name:
					cleared_entry = entry
				case LogEnvironments.HTML.environment_name:
					cleared_entry = re.sub(r"<.*?>", "", entry)
				case LogEnvironments.MARKDOWN.environment_name:
					cleared_entry = re.sub(r"<.*?>", "", entry)
				case LogEnvironments.PLAIN.environment_name:
					cleared_entry = entry
			if cleared_entry.startswith("--"):
				self.__entries.pop(index + 1 - len(searching_entries) - count_separators)
				count_separators += 1
			elif cleared_entry.startswith("-?"):
				parts = cleared_entry.split(" - ")
				searching_entries.append([
					self.__entries.pop(index + 1 - len(searching_entries) - count_separators),
					" ".join(parts[1:])
				])
			else:
				empty = self.__entries.pop(index + 1 - len(searching_entries) - count_separators)
				searching_entries.append([empty, empty])

		deleting_entries = 0
		for index, searching_entry in enumerate(searching_entries):
			if not keyword in searching_entry[1]:
				searching_entries.pop(index - deleting_entries)
				deleting_entries += 1

		searched_entries = [item[0] for item in searching_entries]

		self.__entries.append("------------------------------Systematized entries------------------------------")
		self.__entries.extend(searched_entries)
		self.__entries.append("--------------------------------------------------------------------------------")

if __name__ == "__main__":
	old_logs = [
		"\033[38;2;255;215;0m-Installer?entry> $DESKTOP-8KG0R64:User:Windows:10.0.19045:64bit:WindowsPE:AMD64\033[0m",
		"--------------------------------------------------------------------------------",
		"Enter password: 1234",
		"\033[38;2;139;0;0m-?entry>          \033[38;2;218;112;214m*2023-06-26 21:00:53.276473 🚫 \033[38;2;178;34;34m!!ERROR - \033[38;2;139;0;0mIncompatibility found\033[0m",
		"\033[38;2;139;0;0m-?entry>          \033[38;2;218;112;214m*2023-06-26 21:00:54.277457 🚫 \033[38;2;178;34;34m&FAIL - \033[38;2;139;0;0mProgram not installed\033[0m",
		"1234",
		"\033[38;2;210;180;140m-?entry>          \033[38;2;218;112;214m*2023-06-26 21:00:59.284448 🐞 \033[38;2;222;184;135m%DEBUG - \033[38;2;210;180;140mbla bla bla\033[0m",
		"\033[38;2;210;180;140m-?entry>          \033[38;2;218;112;214m*2023-06-26 21:01:01.287537 🐞 \033[38;2;222;184;135m%DEBUG - \033[38;2;210;180;140mString has deleted\033[0m",
		"\033[38;2;176;224;230m-?entry>          \033[38;2;218;112;214m*2023-06-26 21:00:46.818626 📝 \033[38;2;175;238;238m@MESSAGE - \033[38;2;176;224;230mProgram installation started\033[0m",
	]
	mod = Modifier(old_logs, LogEnvironments.CONSOLE)
	# mod.sort(SortingKeys.SORT_ON_TIME)
	mod.search("o")
	new_logs = mod.entries
	print("\n".join(new_logs))
