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

from re import sub

from mighty_logger.basic.lib_types.environment_type import EnvironmentType
from mighty_logger.src.environments import LogEnvironments

class Exporter:
	def __init__(
			self,
			entries: list[str],
			environment: EnvironmentType
	) -> None:
		self.__entries: list[str] = entries
		self.__env: EnvironmentType = environment
		self.__csv: list[dict] = []

	@property
	def entries(self) -> list[str]:
		return self.__entries

	def export_to_csv(self) -> None:
		cleared_entry = ""
		csv_entry = {}

		for entry in self.__entries[1:]:
			match self.__env.environment_name:
				case LogEnvironments.CONSOLE.environment_name:
					cleared_entry = sub(r"\033\[.*?m", "", entry)
				case LogEnvironments.PLAIN_CONSOLE.environment_name:
					cleared_entry = entry
				case LogEnvironments.HTML.environment_name:
					cleared_entry = sub(r"<.*?>", "", entry)
				case LogEnvironments.MARKDOWN.environment_name:
					cleared_entry = sub(r"<.*?>", "", entry)
				case LogEnvironments.PLAIN.environment_name:
					cleared_entry = entry
			if cleared_entry.startswith("-?"):
				parts = cleared_entry.split("*")
				entry_data = parts[1].split()

				csv_entry["Icon"] = entry_data[2]
				try:
					csv_entry["Duration"] = parts[0].split()[1]
				except IndexError:
					csv_entry["Duration"] = " "
				csv_entry["Time"] = " ".join(entry_data[0:2])
				csv_entry["Category"] = entry_data[4][0]
				csv_entry["Type"] = entry_data[4][1:]
				csv_entry["Message"] = " ".join(entry_data[6:])

				self.__csv.append(csv_entry.copy())
				csv_entry.clear()
				continue

	def save_to_csv(self, file_name: str) -> None:
		with open(f"{file_name}.csv", "w", encoding="utf-8") as csv:
			# Write headers (first line) to file
			headers = self.__csv[0].keys()
			csv.write(",".join(headers) + "\n")

			# Write data to file
			for row in self.__csv:
				values = [str(row[key]) for key in headers]
				csv.write(",".join(values) + "\n")
