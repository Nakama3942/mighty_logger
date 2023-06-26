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

import re, os

template = [
	"--------------------------------------------------------------------------------",
	"Sorted logs",
	"--------------------------------------------------------------------------------",
	"Unsorted empty entries"
]

category_order = {
	"%": 0,
	"~": 1,
	"@": 2,
	"!": 3,
	"&": 4,
	"^": 5
}

type_order = {
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

class SortingKeyType:
	def __init__(self, sorting_key: int):
		self.__sorting_key: int = sorting_key

	@property
	def sorting_key(self) -> int:
		return self.__sorting_key

class SortingKeys:
	SORT_ON_TIME = SortingKeyType(0)
	SORT_ON_TIME_WITH_REVERSE = SortingKeyType(1)
	SORT_ON_CATEGORY = SortingKeyType(2)
	SORT_ON_TYPE = SortingKeyType(3)

def sort(entries: list[str], key: SortingKeyType = SortingKeys.SORT_ON_TYPE) -> list:
	sorting_entries = []
	count_separators = 0

	for index, entry in enumerate(entries[1:]):
		cleared_entry = re.sub(r"\033\[.*?m", "", entry)
		if cleared_entry.startswith("-?"):
			parts = cleared_entry.split()
			sorting_entries.append([entries.pop(index + 1 - len(sorting_entries) - count_separators), " ".join(parts[1:3]), parts[4][0], parts[4][1:]])
			continue
		if cleared_entry.startswith("--"):
			entries.pop(index + 1 - len(sorting_entries) - count_separators)
			count_separators += 1
			continue

	match key:
		case SortingKeys.SORT_ON_TIME:
			sorting_entries.sort(key=lambda x: x[1])
		case SortingKeys.SORT_ON_TIME_WITH_REVERSE:
			sorting_entries.sort(key=lambda x: x[1], reverse=True)
		case SortingKeys.SORT_ON_CATEGORY:
			sorting_entries.sort(key=lambda x: category_order.get(x[2], float("inf")))
		case SortingKeys.SORT_ON_TYPE:
			sorting_entries.sort(key=lambda x: type_order.get(x[3], float("inf")))

	sorted_entries = [item[0] for item in sorting_entries]

	entries[1:1] = template
	entries[3:3] = sorted_entries

	return entries

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
	print("\n".join(old_logs))
	new_logs = sort(old_logs, SortingKeys.SORT_ON_TIME)
	print("\n".join(new_logs))
