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
from mighty_logger.src.lib_types_collection.environments import LogEnvironments

class Exporter:
	"""
	A class that implements the functionality of exporting a string
	in the format of Logger entries to other formats.

	.. versionadded:: 0.0.0
	"""

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
		"""
		The method that implements the export of Logger entries rows to the csv table format.
		The strings are converted into dictionaries, from which it will then be possible
		to assemble a csv table at the time the file is saved in the new format.
		This method does not implement saving the exported data.

		.. versionadded:: 0.0.0
		"""
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
		"""
		Implements the saving of the generated dictionary strings to the csv file of the table.

		.. versionadded:: 0.0.0

		:param file_name: The name of the file where you want to save the csv table
		:type file_name: str
		"""
		with open(f"{file_name}.csv", "w", encoding="utf-8") as csv:
			# Write headers (first line) to file
			headers = self.__csv[0].keys()
			csv.write(",".join(headers) + "\n")

			# Write data to file
			for row in self.__csv:
				values = [str(row[key]) for key in headers]
				csv.write(",".join(values) + "\n")
