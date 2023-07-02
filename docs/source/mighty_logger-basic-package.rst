"basic" package
===============

.. toctree::
	:maxdepth: 2
	:caption: Contents:
	:hidden:

	mighty_logger-basic-lib_types-package

A package with base classes intended for use within a library.

.. versionadded:: 0.2.0

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.basic import ...

.. currentmodule:: mighty_logger.basic.basic_logger

.. rubric:: class BasicLogger
.. py:class:: BasicLogger(program_name: str, env: EnvironmentType)

	The base class of the Logger, which stores the main attributes and implements the most important functionality - the formation of the Logger entry string.

	:since: v0.2.0

	.. py:method:: _initialized_data(colors: list[str, str]) -> str

		A method that assemble an entry of system initialized data.

		:since: v0.3.0
		:param colors: Color string list of initialized data
		:type colors: list[str, str]
		:return: A string with initialized data
		:rtype: str

	.. py:method:: _assemble_entry(entry_type: EntryType, icon_set: int, animation: str, message_text: str, local_settings: dict) -> str

		A method that assemble an entry into a string and returns it.

		:since: v0.2.0
		:param entry_type: Type of entry to be generated
		:type entry_type: EntryType
		:param icon_set: Icon set number
		:type icon_set: int
		:param animation: Animation frame of entry
		:type animation: str
		:param message_text: Message of entry
		:type message_text: str
		:param local_settings: Settings for the string of the current entry
		:type local_settings: dict
		:return: The formed entry string
		:rtype: str
		:raises MessageException: Message is too short (less than 10 characters)

.. currentmodule:: mighty_logger.basic.exceptions

.. rubric:: exception ColorException
.. py:exception:: ColorException(message: str)

	The exception that is thrown when there is no color in any palette.

	:since: v0.0.4

.. rubric:: exception ReCreationException
.. py:exception:: ReCreationException(message: str)

	The exception that is thrown when an object of the Singleton category is re-created.

	:since: v0.5.0

.. rubric:: exception EnvironmentException
.. py:exception:: EnvironmentException(message: str)

	The exception that is thrown when on environmental errors.

	:since: v0.7.0

.. rubric:: exception InitException
.. py:exception:: InitException(message: str)

	The exception thrown on errors during initialization.

	:since: v0.7.0

.. rubric:: exception MessageException
.. py:exception:: MessageException(message: str)

	The exception that is thrown when a write message is too short.

	:since: v0.8.0

.. currentmodule:: mighty_logger.basic.exporter

.. rubric:: class Exporter
.. py:class:: Exporter(entries: list[str], environment: EnvironmentType)

	A class that implements the functionality of exporting a string in the format of Logger entries to other formats.

	:property: entries
	:since: v0.8.0

	.. py:method:: export_to_csv()

		The method that implements the export of Logger entries rows to the csv table format. The strings are converted into dictionaries, from which it will then be possible to assemble a csv table at the time the file is saved in the new format. This method does not implement saving the exported data.

		:since: 0.8.0

	.. py:method:: save_to_csv(file_name: str)

		Implements the saving of the generated dictionary strings to the csv file of the table.

		:since: v0.8.0
		:param file_name: The name of the file where you want to save the csv table
		:type file_name: str

.. currentmodule:: mighty_logger.basic.modifier

.. rubric:: class Modifier
.. py:class:: Modifier(entries: list[str], environment: EnvironmentType)

	A class that implements Looger's modification. Modification means any change in the Logger Text Buffer, namely, changing entries, moving, deleting and adding. Sorting, searching, and selecting algorithms make just such an impact on the Logger's Text Buffer.

	:property: entries
	:since: 0.7.1

	.. py:method:: sort(key: SortingKeyType)

		Method for sorting entries by key. The sort key is "sort by time", "sort by time in reverse order", "sort by category" and "sort by type".

		:since: v0.7.1
		:param key: The key to sort by
		:type key: SortingKeyType

	.. py:method:: search(keyword: str, empty: bool)

		A method that implements the search for entries in messages by a keyword/letter/phrase. It is possible to enable search not only in entries, but also in empty (custom) entries.

		:since: v0.7.1
		:param keyword: Keyword/letter/phrase
		:type keyword: str
		:param empty: Flag indicating whether to search in custom strings
		:type empty: bool

	.. py:method:: select(entry_type: EntryType)

		A method that selects entries either by a specific type or by an entire category.

		:since: v0.7.1
		:param entry_type: Entries type/category
		:type entry_type: EntryType

.. currentmodule:: mighty_logger.basic.singleton

.. rubric:: class Singleton
.. py:class:: Singleton

	A class that implements the Singleton pattern.

	:since: v0.2.0

.. currentmodule:: mighty_logger.basic.text_buffer

.. rubric:: type BasicAnimationType
.. py:class:: BasicTextBuffer(env: EnvironmentType)

	A class with a basic implementation of a simple Text Buffer. It is intended to be used in conjunction with HTML, but this is optional.

	:since: v0.4.0

	.. py:method:: append(message: str)

		Adds a string to the end of the Text Buffer.

		:since: v0.4.0
		:param message: The string to be added
		:type message: str

	.. py:method:: insert(number_string: int, message: str)

		Adds a string to the middle of the Text Buffer at the specified position.

		:since: v0.4.0
		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str

	.. py:method:: replace(number_string: int, message: str)

		Replaces a specific string in a Text Buffer. If there is no such string, the method fills the list with empty strings up to the required position and *adds* the string.

		:since: v0.4.0
		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str

	.. py:method:: pop([number_string: int = -1]) -> str

		Implements the saving of the generated dictionary strings to the csv file of the table.

		:since: v0.6.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str

	.. py:method:: remove(file_name: str)

		Deletes without returning the specified string from the Text Buffer.

		:since: v0.6.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int

	.. py:method:: clear()

		Clears the entire Text Buffer, making it empty.

		:since: v0.7.0

	.. py:method:: save(name_file: str, clean: bool)

		Saves the text of the Text Buffer to a file.

		:since: v0.4.0
		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool

	.. py:method:: load(name_file: str)

		Loads the text of the Text Buffer from a file.

		:since: v0.7.0
		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str

	.. py:method:: input(input_text: str) -> str

		A wrapper method for the standard Python input() that prepares the Text Buffer before using this function, and performs certain actions after, so that the Text Buffer can continue to function normally.

		:since: v0.7.0
		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str

	.. py:method:: update_console(file_name: str)

		Refreshes the console, erasing output text and outputting an updated buffer.

		:since: v0.5.0-dev
		:raises NotImplementedError: Method append() is not implemented in the base class

	.. py:method:: update_entry(file_name: str)

		Rewrites the last line of output after updating the last line of the buffer. Used (mostly) by the Progress bar (that is Progress string).

		:since: v0.6.0
		:raises NotImplementedError: Method append() is not implemented in the base class

.. py:class:: TextBuffer(env: EnvironmentType[, console_width: int = 60])

	A class with an advanced implementation of the console Text Buffer. It is not necessary to use it only in the console, but almost all methods are reimplemented for more complex algorithms, taking into account the width of the console (number of characters per line) and use ANSI escape codes that are only found in the console.

	:since: v0.3.0

	.. py:method:: append(message: str)

		Adds a string to the end of the Text Buffer.

		:since: v0.3.0
		:param message: The string to be added
		:type message: str

	.. py:method:: insert(number_string: int, message: str)

		Adds a string to the middle of the Text Buffer at the specified position.

		:since: v0.4.0
		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str

	.. py:method:: replace(number_string: int, message: str)

		Replaces a specific string in a Text Buffer. If there is no such string, the method fills the list with empty strings up to the required position and *adds* the string.

		:since: v0.3.0
		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str

	.. py:method:: pop([number_string: int = -1]) -> str

		Implements the saving of the generated dictionary strings to the csv file of the table.

		:since: v0.6.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str

	.. py:method:: remove(file_name: str)

		Deletes without returning the specified string from the Text Buffer.

		:since: v0.6.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int

	.. py:method:: clear()

		Clears the entire Text Buffer, making it empty.

		:since: v0.7.0

	.. py:method:: save(name_file: str, clean: bool)

		Saves the text of the Text Buffer to a file.

		:since: v0.4.0
		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool

	.. py:method:: load(name_file: str)

		Loads the text of the Text Buffer from a file.

		:since: v0.7.0
		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str

	.. py:method:: input(input_text: str) -> str

		A wrapper method for the standard Python input() that prepares the Text Buffer before using this function, and performs certain actions after, so that the Text Buffer can continue to function normally.

		:since: v0.7.0
		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str

	.. py:method:: update_console(file_name: str)

		Refreshes the console, erasing output text and outputting an updated buffer.

		:since: v0.3.0

	.. py:method:: update_entry(file_name: str)

		Rewrites the last line of output after updating the last line of the buffer. Used (mostly) by the Progress bar (that is Progress string).

		:since: v0.6.0
