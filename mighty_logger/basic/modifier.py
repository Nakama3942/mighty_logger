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

from mighty_logger.basic.lib_types.entry_type import EntryType
from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.basic.lib_types.sorting_key_type import SortingKeyType
from mighty_logger.src.environments import LogEnvironments
from mighty_logger.src.sorting_keys import SortingKeys

class Modifier:
	def __init__(
		self,
		entries: list[str],
		environment: EnvironmentType
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

	def sort(self, key: SortingKeyType) -> None:
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
				parts = cleared_entry.split("*")[1].split()
				sorting_entries.append([
					self.__entries.pop(index + 1 - len(sorting_entries) - count_separators),
					" ".join(parts[0:2]),
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

	def search(self, keyword: str, empty: bool = False) -> None:
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
				continue
			if cleared_entry.startswith("-?"):
				parts = cleared_entry.split(" - ")
				searching_entries.append([
					self.__entries.pop(index + 1 - len(searching_entries) - count_separators),
					" ".join(parts[1:])
				])
				continue
			if empty:
				empty = self.__entries.pop(index + 1 - len(searching_entries) - count_separators)
				searching_entries.append([empty, empty])
				continue

		searched_entries = []
		for searching_entry in searching_entries:
			if keyword in searching_entry[1]:
				searched_entries.append(searching_entry[0])

		self.__entries.append("------------------------------Systematized entries------------------------------")
		self.__entries.extend(searched_entries)
		self.__entries.append("--------------------------------------------------------------------------------")

	def select(self, entry_type: EntryType) -> None:
		cleared_entry = ""
		selected_entries = []
		count_excess = 0

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
				parts = cleared_entry.split("*")[1].split()
				if parts[4] == entry_type.type_name:
					selected_entries.append(self.__entries.pop(index + 1 - len(selected_entries) - count_excess))
					continue
			self.__entries.pop(index + 1 - len(selected_entries) - count_excess)
			count_excess += 1

		self.__entries.append("--------------------------------Selected entries--------------------------------")
		self.__entries.extend(selected_entries)
		self.__entries.append("--------------------------------------------------------------------------------")
