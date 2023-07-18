"basic" package
===============

.. toctree::
	:maxdepth: 2
	:caption: Contents:
	:hidden:

	mighty_logger-basic-lib_types-package

A package with base classes intended for use within a library.

.. versionadded:: v0.2.0

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.basic import ...

Class BasicLogger
-----------------

.. danger:: This is a hidden functionality that is inaccessible outside the library.

.. currentmodule:: mighty_logger.basic.basic_logger

.. py:class:: BasicLogger(program_name: str, env: EnvironmentType)

	The base class of the Logger, which stores the main attributes and implements the most important functionality - the formation of the Logger entry string.

	.. versionadded:: v0.2.0

	:param program_name: The name of the program whose is being logged
	:type program_name: str
	:param env: Logger environment
	:type env: EnvironmentType

	.. py:method:: _initialized_data(colors: list[str, str]) -> str

		A method that assemble an entry of system initialized data.

		.. versionadded:: v0.3.0

		:param colors: Color string list of initialized data
		:type colors: list[str, str]
		:return: A string with initialized data
		:rtype: str

	.. py:method:: _assemble_entry(entry_type: EntryType, icon_set: int, animation: str, message_text: str, local_settings: dict) -> str

		A method that assemble an entry into a string and returns it.

		.. versionadded:: v0.2.0

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

Library exceptions
------------------

.. currentmodule:: mighty_logger.basic.exceptions

Exception ColorException
________________________

.. py:exception:: ColorException(message: str)

	The exception that is thrown when there is no color in any palette.

	.. versionadded:: v0.0.4

	:param message: Exception message
	:type message: str

Exception ReCreationException
_____________________________

.. py:exception:: ReCreationException(message: str)

	The exception that is thrown when an object of the Singleton category is re-created.

	.. versionadded:: v0.5.0

	:param message: Exception message
	:type message: str

Exception EnvironmentException
______________________________

.. py:exception:: EnvironmentException(message: str)

	The exception that is thrown when on environmental errors.

	.. versionadded:: v0.7.0

	:param message: Exception message
	:type message: str

Exception InitException
_______________________

.. py:exception:: InitException(message: str)

	The exception thrown on errors during initialization.

	.. versionadded:: v0.7.0

	:param message: Exception message
	:type message: str

Exception MessageException
__________________________

.. py:exception:: MessageException(message: str)

	The exception that is thrown when a write message is too short.

	.. versionadded:: v0.8.0

	:param message: Exception message
	:type message: str

Class Exporter
--------------

.. danger:: This is a hidden functionality that is inaccessible outside the library.

.. currentmodule:: mighty_logger.basic.exporter

.. py:class:: Exporter(entries: list[str], environment: EnvironmentType)

	A class that implements the functionality of exporting a string in the format of Logger entries to other formats.

	.. versionadded:: v0.8.0

	:param entries: List of entries to be exported
	:type entries: list[str]
	:param environment: The environment in which the list of entries was formed
	:type environment: EnvironmentType

	.. property:: entries

		List of entries from which the csv table is formed.

		.. versionadded:: v0.8.0

		:rtype: list[str]

	.. py:method:: _clearing_entry(dirty_entry: str) -> str

		A method that clears a string of formatting, since it is easier to use strings with pure text without formatting to parse entries.

		.. versionadded:: v1.0.0

		:param dirty_entry: The string to be cleared
		:type dirty_entry: str
		:return: Cleaned string
		:rtype: str

	.. py:method:: export_to_csv() -> None

		The method that implements the export of Logger entries rows to the csv table format. The strings are converted into dictionaries, from which it will then be possible to assemble a csv table at the time the file is saved in the new format. This method does not implement saving the exported data.

		.. versionadded:: v0.8.0

	.. py:method:: save_to_csv(file_name: str) -> None

		Implements the saving of the generated dictionary strings to the csv file of the table.

		.. versionadded:: v0.8.0

		:param file_name: The name of the file where you want to save the csv table
		:type file_name: str

Class Modifier
--------------

.. danger:: This is a hidden functionality that is inaccessible outside the library.

.. currentmodule:: mighty_logger.basic.modifier

.. py:class:: Modifier(entries: list[str], environment: EnvironmentType)

	A class that implements Looger's modification. Modification means any change in the Logger Text Buffer, namely, changing entries, moving, deleting and adding. Sorting, searching, and selecting algorithms make just such an impact on the Logger's Text Buffer.

	.. versionadded:: v0.7.1

	:param entries: List of entries to be exported
	:type entries: list[str]
	:param environment: The environment in which the list of entries was formed
	:type environment: EnvironmentType

	.. property:: entries

		List of entries from which the csv table is formed.

		.. versionadded:: v0.7.1

		:rtype: list[str]

	.. py:method:: _clearing_entry(dirty_entry: str) -> str

		A method that clears a string of formatting, since it is easier to use strings with pure text without formatting to parse entries.

		.. versionadded:: v1.0.0

		:param dirty_entry: The string to be cleared
		:type dirty_entry: str
		:return: Cleaned string
		:rtype: str

	.. py:method:: sort(key: SortingKeyType) -> None

		Method for sorting entries by key. The sort key is "sort by time", "sort by time in reverse order", "sort by category" and "sort by type".

		.. versionadded:: v0.7.1

		:param key: The key to sort by
		:type key: SortingKeyType

	.. py:method:: search(keyword: str, empty: bool) -> None

		A method that implements the search for entries in messages by a words/letters/phrases. It is possible to enable search not only in entries, but also in empty (custom) entries.

		.. versionadded:: v0.7.1

		:param keyword: Words/letters/phrases
		:type keyword: str
		:param empty: Flag indicating whether to search in custom strings
		:type empty: bool

	.. py:method:: select(entry_type: EntryType) -> None

		A method that selects entries either by a specific type or by an entire category.

		.. versionadded:: v0.7.1

		:param entry_type: Entries type/category
		:type entry_type: EntryType

Pattern Singleton
-----------------

.. danger:: This is a hidden functionality that is inaccessible outside the library.

.. currentmodule:: mighty_logger.basic.singleton

.. py:class:: Singleton

	A class that implements the Singleton pattern.

	.. versionadded:: v0.2.0

.. _text_buffers:

Text Buffers
------------

.. currentmodule:: mighty_logger.basic.text_buffer

Basic Text Buffer
_________________

.. py:class:: BasicTextBuffer(env: EnvironmentType)

	A class with a basic implementation of a simple Text Buffer. It is intended to be used in conjunction with HTML, but this is optional.

	.. versionadded:: v0.4.0

	:param env: Text Buffer environment
	:type env: EnvironmentType

	.. seealso::
		- Read the definition of the base class in :ref:`Type TextBufferType <text_buffer_type>`.

	.. _basic_text_buffer_append:

	.. py:method:: append(message: str) -> None

		Adds a string to the end of the Text Buffer.

		.. versionadded:: v0.4.0

		:param message: The string to be added
		:type message: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.append() <text_buffer_type_append>`.

	.. _basic_text_buffer_insert:

	.. py:method:: insert(number_string: int, message: str) -> None

		Adds a string to the middle of the Text Buffer at the specified position.

		.. versionadded:: v0.4.0

		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.insert() <text_buffer_type_insert>`.

	.. _basic_text_buffer_replace:

	.. py:method:: replace(number_string: int, message: str) -> None

		Replaces a specific string in a Text Buffer. If there is no such string, the method fills the list with empty strings up to the required position and *adds* the string.

		.. versionadded:: v0.4.0

		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.replace() <text_buffer_type_replace>`.

	.. _basic_text_buffer_pop:

	.. py:method:: pop([number_string: int = -1]) -> str

		Implements the saving of the generated dictionary strings to the csv file of the table.

		.. versionadded:: v0.6.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.pop() <text_buffer_type_pop>`.

	.. _basic_text_buffer_remove:

	.. py:method:: remove([number_string: int = -1]) -> None

		Deletes without returning the specified string from the Text Buffer.

		.. versionadded:: v0.6.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.remove() <text_buffer_type_remove>`.

	.. _basic_text_buffer_clear:

	.. py:method:: clear() -> None

		Clears the entire Text Buffer, making it empty.

		.. versionadded:: v0.7.0

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.clear() <text_buffer_type_clear>`.

	.. _basic_text_buffer_save:

	.. py:method:: save(name_file: str, clean: bool) -> None

		Saves the text of the Text Buffer to a file.

		.. versionadded:: v0.4.0

		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.save() <text_buffer_type_save>`.

	.. _basic_text_buffer_load:

	.. py:method:: load(name_file: str) -> None

		Loads the text of the Text Buffer from a file.

		.. versionadded:: v0.7.0

		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.load() <text_buffer_type_load>`.

	.. _basic_text_buffer_input:

	.. py:method:: input(input_text: str) -> str

		A wrapper method for the standard Python ``input()`` that prepares the Text Buffer before using this function, and performs certain actions after, so that the Text Buffer can continue to function normally.

		.. versionadded:: v0.7.0

		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.input() <text_buffer_type_input>`.

	.. _basic_text_buffer_update_console:

	.. py:method:: update_console() -> None

		Refreshes the console, erasing output text and outputting an updated buffer.

		.. versionadded:: v0.5.0-dev

		:raises NotImplementedError: Method append() is not implemented in the base class

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.update_console() <text_buffer_type_update_console>`.

	.. _basic_text_buffer_update_entry:

	.. py:method:: update_entry() -> None

		Rewrites the last line of output after updating the last line of the buffer. Used (mostly) by the Progress bar (that is Progress string).

		.. versionadded:: v0.6.0

		:raises NotImplementedError: Method append() is not implemented in the base class

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.update_entry() <text_buffer_type_update_entry>`.

	.. _basic_text_buffer_output_entry:

	.. py:method:: output_entry() -> None

		Appends to the console the string added by the ``append()`` method.

		.. versionadded:: v1.0.0

		:raises NotImplementedError: Method output_entry() is not implemented in the base class

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.output_entry() <text_buffer_type_output_entry>`.

.. py:class:: TextBuffer(env: EnvironmentType[, console_width: int = 60])

	A class with an advanced implementation of the console Text Buffer. It is not necessary to use it only in the console, but almost all methods are reimplemented for more complex algorithms, taking into account the width of the console (number of characters per line) and use ANSI escape codes that are only found in the console.

	.. versionadded:: v0.3.0

	.. caution:: It was just a test feature that didn't work on the release yet and was completed by the next update v0.4.0.

	:param env: Text Buffer environment
	:type env: EnvironmentType
	:param console_width: Console width
	:type console_width: int

	.. seealso::
		- Read the definition of the base class in :ref:`Type TextBufferType <text_buffer_type>`.

	.. _text_buffer_append:

	.. py:method:: append(message: str) -> None

		Adds a string to the end of the Text Buffer.

		.. versionadded:: v0.3.0

		.. caution:: It was just a test feature that didn't work on the release yet and was completed by the next update  v0.4.0.

		:param message: The string to be added
		:type message: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.append() <text_buffer_type_append>`.

	.. _text_buffer_insert:

	.. py:method:: insert(number_string: int, message: str) -> None

		Adds a string to the middle of the Text Buffer at the specified position.

		.. versionadded:: v0.4.0

		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.insert() <text_buffer_type_insert>`.

	.. _text_buffer_replace:

	.. py:method:: replace(number_string: int, message: str) -> None

		Replaces a specific string in a Text Buffer. If there is no such string, the method fills the list with empty strings up to the required position and *adds* the string.

		.. versionadded:: v0.3.0

		.. caution:: It was just a test feature that didn't work on the release yet and was completed by the next update  v0.4.0.

		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.replace() <text_buffer_type_replace>`.

	.. _text_buffer_pop:

	.. py:method:: pop([number_string: int = -1]) -> str

		Implements the saving of the generated dictionary strings to the csv file of the table.

		.. versionadded:: v0.6.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.pop() <text_buffer_type_pop>`.

	.. _text_buffer_remove:

	.. py:method:: remove([number_string: int = -1]) -> None

		Deletes without returning the specified string from the Text Buffer.

		.. versionadded:: v0.6.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.remove() <text_buffer_type_remove>`.

	.. _text_buffer_clear:

	.. py:method:: clear() -> None

		Clears the entire Text Buffer, making it empty.

		.. versionadded:: v0.7.0

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.clear() <text_buffer_type_clear>`.

	.. _text_buffer_save:

	.. py:method:: save(name_file: str, clean: bool) -> None

		Saves the text of the Text Buffer to a file.

		.. versionadded:: v0.4.0

		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.save() <text_buffer_type_save>`.

	.. _text_buffer_load:

	.. py:method:: load(name_file: str) -> None

		Loads the text of the Text Buffer from a file.

		.. versionadded:: v0.7.0

		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.load() <text_buffer_type_load>`.

	.. _text_buffer_input:

	.. py:method:: input(input_text: str) -> str

		A wrapper method for the standard Python input() that prepares the Text Buffer before using this function, and performs certain actions after, so that the Text Buffer can continue to function normally.

		.. versionadded:: v0.7.0

		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.input() <text_buffer_type_input>`.

	.. _text_buffer_update_console:

	.. py:method:: update_console() -> None

		Refreshes the console, erasing output text and outputting an updated buffer.

		.. versionadded:: v0.3.0

		.. caution:: It was just a test feature that didn't work on the release yet and was completed by the next update  v0.4.0.

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.update_console() <text_buffer_type_update_console>`.

	.. _text_buffer_update_entry:

	.. py:method:: update_entry() -> None

		Rewrites the last line of output after updating the last line of the buffer. Used (mostly) by the Progress bar (that is Progress string).

		.. versionadded:: v0.6.0

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.update_entry() <text_buffer_type_update_entry>`.

	.. _text_buffer_output_entry:

	.. py:method:: output_entry() -> None

		Appends to the console the string added by the ``append()`` method.

		.. versionadded:: v1.0.0

		.. seealso::
			- Read the basic method definition :ref:`TextBufferType.output_entry() <text_buffer_type_output_entry>`.
