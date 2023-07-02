"lib types" package
===================

A package that contains the data types that are used in the library.

.. versionadded:: 0.7.0

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.basic.lib_types import ...

.. currentmodule:: mighty_logger.basic.lib_types.animation_type

.. rubric:: type BasicAnimationType
.. py:class:: BasicAnimationType(animation: list)

	.. danger:: This is a hidden class that is inaccessible outside the library.

	Basic wrapper class for animations type.

	:property: animation
	:since: v0.6.0

.. rubric:: IndefiniteAnimationType
.. py:class:: IndefiniteAnimationType(animation: list)

	Wrapper class for indefinite animations type.

	:property: animation
	:since: v0.6.0

.. rubric:: DefiniteAnimationType
.. py:class:: DefiniteAnimationType(animation: list)

	Wrapper class for definite animations type.

	:property: animation
	:since: v0.6.0

.. currentmodule:: mighty_logger.basic.lib_types.entry_type

.. rubric:: EntryType
.. py:class:: EntryType(*, type_category: str, type_name: str, time_color: tuple, status_color: tuple, status_message_color: tuple, type_color: tuple, message_color: tuple, background_color: tuple, icon: tuple)

	The data type that characterizes the entry type.

	:properties:
		- type_category
		- type_name
		- time_color
		- status_color
		- type_color
		- message_color
		- background_color
		- icon
	:since: v0.7.0

.. currentmodule:: mighty_logger.basic.lib_types.environment_type

.. rubric:: EnvironmentType
.. py:class:: EnvironmentType(environment_name: str, environment_code: int, updatable: bool, weak_environment: bool)

	A data type that characterizes the environments in which the Logger can operate.

	:properties:
		- environment_name
		- environment_code
		- updatable
		- weak_environment
	:since: v0.7.0

.. currentmodule:: mighty_logger.basic.lib_types.sorting_key_type

.. rubric:: SortingKeyType
.. py:class:: SortingKeyType(sorting_key: str)

	A data type that characterizes the sort keys for entries.

	:property: sorting_key
	:since: v0.7.1

.. currentmodule:: mighty_logger.basic.lib_types.text_buffer_type

.. rubric:: TextBufferType
.. py:class:: TextBufferType(env: EnvironmentType)

	The data type that characterizes the Text Buffer.

	:property: data
	:since: v0.5.0-dev

	.. py:method:: __lshift__(message: str) -> None

		Used to add a string to the end of the Text Buffer.

		:since: v0.4.0
		:param message: The string to be added
		:type message: str

	.. py:method:: __rshift__(name: str) -> None

		Used to save a Text Buffer to the file.

		:since: v0.4.0
		:param name: The name of the file where you want to save the Text Buffer
		:type name: str

	.. py:method:: append(message: str) -> None

		Adds a string to the end of the Text Buffer.

		:since: v0.5.0-dev
		:param message: The string to be added
		:type message: str

	.. py:method:: insert(number_string: int, message: str) -> None

		Adds a string to the middle of the Text Buffer at the specified position.

		:since: v0.5.0-dev
		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str
		:raises NotImplementedError: Method insert() is not implemented in the base class

	.. py:method:: replace(number_string: int, message: str) -> None

		Replaces a specific string in a Text Buffer. If there is no such string, the method fills the list with empty strings up to the required position and *adds* the string.

		:since: v0.5.0-dev
		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str
		:raises NotImplementedError: Method replace() is not implemented in the base class

	.. py:method:: pop([number_string: int = -1]) -> str

		Removes and returns the specified string from the Text Buffer.

		:since: v0.6.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str
		:raises NotImplementedError: Method pop() is not implemented in the base class

	.. py:method:: remove([number_string: int = -1]) -> None

		Deletes without returning the specified string from the Text Buffer.

		:since: v0.6.0
		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:raises NotImplementedError: Method remove() is not implemented in the base class

	.. py:method:: clear() -> None

		Clears the entire Text Buffer, making it empty.

		:since: v0.7.0
		:raises NotImplementedError: Method clear() is not implemented in the base class

	.. py:method:: save(name_file: str, clean: bool) -> None

		Saves the text of the Text Buffer to a file.

		:since: v0.5.0-dev
		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool
		:raises NotImplementedError: Method save() is not implemented in the base class

	.. py:method:: load(name_file: str) -> None

		Loads the text of the Text Buffer from a file.

		:since: v0.7.0
		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str
		:raises NotImplementedError: Method load() is not implemented in the base class

	.. py:method:: input(input_text: str) -> None

		A wrapper method for the standard Python input() that prepares the Text Buffer before using this function, and performs certain actions after, so that the Text Buffer can continue to function normally.

		:since: v0.7.0
		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str
		:raises NotImplementedError: Method input() is not implemented in the base class

	.. py:method:: update_console() -> None

		Refreshes the console, erasing output text and outputting an updated buffer.

		:since: v0.5.0-dev
		:raises NotImplementedError: Method append() is not implemented in the base class

	.. py:method:: update_entry() -> None

		Rewrites the last line of output after updating the last line of the buffer. Used (mostly) by the Progress bar (that is Progress string).

		:since: v0.6.0
		:raises NotImplementedError: Method append() is not implemented in the base class
