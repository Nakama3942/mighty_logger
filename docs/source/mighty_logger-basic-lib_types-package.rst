"lib types" package
===================

A package that contains the data types that are used in the library.

.. versionadded:: v0.7.0

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.basic.lib_types import ...

Animation type
--------------

.. currentmodule:: mighty_logger.basic.lib_types.animation_type

Type BasicAnimationType
_______________________

.. py:class:: BasicAnimationType(animation: list)

	.. danger:: This is a hidden class that is inaccessible outside the library.

	Basic wrapper class for animations type.

	.. versionadded:: v0.6.0

	:param animation: List of animation strings
	:type animation: list

	.. property:: animation

		List of animation strings.

		.. versionadded:: v0.6.0

		:rtype: list

Type IndefiniteAnimationType
____________________________

.. _indefinite_animation_type:

.. py:class:: IndefiniteAnimationType(animation: list)

	Wrapper class for indefinite animations type.

	.. versionadded:: v0.6.0

	:param animation: List of animation strings
	:type animation: list

	.. hint:: If this class is used as an argument type - just pass the value of one of the available attributes of the :ref:`List of animations <list_of_animations>`.

	.. seealso::
		- `Type BasicAnimationType`_

Type DefiniteAnimationType
__________________________

.. _definite_animation_type:

.. py:class:: DefiniteAnimationType(animation: list)

	Wrapper class for definite animations type.

	.. versionadded:: v0.6.0

	:param animation: List of animation strings
	:type animation: list

	.. hint:: If this class is used as an argument type - just pass the value of one of the available attributes of the :ref:`List of progress bars <list_of_progress_bars>`.

	.. seealso::
		- `Type BasicAnimationType`_

Type EntryType
--------------

.. currentmodule:: mighty_logger.basic.lib_types.entry_type

.. _entry_type:

.. py:class:: EntryType(*, type_category: str, type_name: str, time_color: tuple, status_color: tuple, type_color: tuple, message_color: tuple, background_color: tuple, icon: tuple)

	The data type that characterizes the entry type.

	.. versionadded:: v0.7.0

	:param type_category: Entry type category
	:type type_category: str
	:param type_name: The name of the entry type
	:type type_name: str
	:param time_color: The color of the time in the entry type
	:type time_color: tuple
	:param status_color: The color of the status in the entry type
	:type status_color: tuple
	:param type_color: The color of the type in the entry type
	:type type_color: tuple
	:param message_color: The color of the message in the entry type
	:type message_color: tuple
	:param background_color: The background color in the entry type
	:type background_color: tuple
	:param icon: Entry type icon
	:type icon: tuple

	.. hint:: If this class is used as an argument type - just pass the value of one of the available attributes of the :ref:`Entry types collections <entry_types_collections>`.

	.. property:: type_category

		Entry type category.

		.. versionadded:: v0.7.2

		:rtype: str

	.. property:: type_name

		The name of the entry type.

		.. versionadded:: v0.7.0

		:rtype: str

	.. property:: time_color

		The color of the time in the entry type.

		.. versionadded:: v0.7.0

		:rtype: tuple

	.. property:: status_color

		The color of the status in the entry type.

		.. versionadded:: v0.7.0

		:rtype: tuple

	.. property:: type_color

		The color of the type in the entry type.

		.. versionadded:: v0.7.0

		:rtype: tuple

	.. property:: message_color

		The color of the message in the entry type.

		.. versionadded:: v0.7.0

		:rtype: tuple

	.. property:: background_color

		The background color in the entry type.

		.. versionadded:: v0.7.0

		:rtype: tuple

	.. property:: icon

		Entry type icon.

		.. versionadded:: v0.7.0

		:rtype: tuple

Type EnvironmentType
--------------------

.. currentmodule:: mighty_logger.basic.lib_types.environment_type

.. _environment_type:

.. py:class:: EnvironmentType(environment_name: str, environment_code: int, updatable: bool, weak_environment: bool)

	A data type that characterizes the environments in which the Logger can operate.

	.. versionadded:: v0.7.0

	:param environment_name: The name of the environment
	:type environment_name: str
	:param environment_code: The code of the environment
	:type environment_code: int
	:param updatable: Is the environment updatable (uses a complex (console) Buffer)?
	:type updatable: bool
	:param weak_environment: Is the environment weak (requires preconfiguration)?
	:type weak_environment: bool

	.. hint:: If this class is used as an argument type - just pass the value of one of the available attributes of the :ref:`Logger environments collections <logger_environments_collections>`.

	.. property:: environment_name

		The name of the environment.

		.. versionadded:: v0.7.0

		:rtype: str

	.. property:: environment_code

		The code of the environment.

		.. versionadded:: v0.7.0

		:rtype: int

	.. property:: updatable

		Is the environment updatable (uses a complex (console) Buffer)?

		.. versionadded:: v0.7.0

		:rtype: bool

	.. property:: weak_environment

		Is the environment weak (requires preconfiguration)?

		.. versionadded:: v0.7.0

		:rtype: bool

Type SortingKeyType
-------------------

.. currentmodule:: mighty_logger.basic.lib_types.sorting_key_type

.. _sorting_key_type:

.. py:class:: SortingKeyType(sorting_key: str)

	A data type that characterizes the sort keys for entries.

	.. versionadded:: v0.7.1

	:param sorting_key: A string describing the sort key
	:type sorting_key: str

	.. hint:: If this class is used as an argument type - just pass the value of one of the available attributes of the :ref:`Sorting keys collections <sorting_keys_collections>`.

	.. property:: sorting_key

		The sort key number.

		.. versionadded:: v0.7.1

		:rtype: str

.. _text_buffer_type:

Type TextBufferType
-------------------

.. currentmodule:: mighty_logger.basic.lib_types.text_buffer_type

.. py:class:: TextBufferType(env: EnvironmentType)

	The data type that characterizes the Text Buffer.

	.. versionadded:: v0.5.0-dev

	:param env: Text Buffer environment
	:type env: EnvironmentType

	.. seealso::
		- Read about inherited classes in the section :ref:`Text Buffers <text_buffers>`.

	.. property:: text_buffer

		List of strings of the Text Buffer.

		.. versionadded:: v0.9.3

		:rtype: list

	.. py:method:: __lt__(message: str) -> None:

		Used to add a string to the end of the Text Buffer.

		.. versionadded:: v0.9.3

		:param name_file: The message to be appended to the end of the Text Buffer
		:type name_file: str

	.. py:method:: __gt__(number_string: int) -> str:

		Used to pop a string from the end of the Text Buffer.

		.. versionadded:: v0.9.3

		:param name_file: Line number to pop
		:type name_file: int
		:return: a string at the given number
		:rtype: str

	.. py:method:: __lshift__(name_file: str) -> None:

		Used to load a Text Buffer from the file.

		.. versionadded:: v0.4.0

		:param name_file: The name of the file from which to load the Text Buffer
		:type name_file: str

	.. py:method:: __rshift__(name_file: str) -> None:

		Used to save a Text Buffer to the file.

		.. versionadded:: v0.4.0

		:param name_file: The name of the file where you want to save the Text Buffer
		:type name_file: str

	.. _text_buffer_type_append:

	.. py:method:: append(message: str) -> None

		Adds a string to the end of the Text Buffer.

		.. versionadded:: v0.5.0-dev

		:param message: The string to be added
		:type message: str
		:raises NotImplementedError: Method append() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_append>`;
			- :ref:`TextBuffer <text_buffer_append>`.

	.. _text_buffer_type_insert:

	.. py:method:: insert(number_string: int, message: str) -> None

		Adds a string to the middle of the Text Buffer at the specified position.

		.. versionadded:: v0.5.0-dev

		:param number_string: Position (number) of the line to which you need to add a string
		:type number_string: int
		:param message: The string to be placed on the position
		:type message: str
		:raises NotImplementedError: Method insert() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_insert>`;
			- :ref:`TextBuffer <text_buffer_insert>`.

	.. _text_buffer_type_replace:

	.. py:method:: replace(number_string: int, message: str) -> None

		Replaces a specific string in a Text Buffer. If there is no such string, the method fills the list with empty strings up to the required position and *adds* the string.

		.. versionadded:: v0.5.0-dev

		:param number_string: Position (number) of the string to be replaced (added)
		:type number_string: int
		:param message: A string that will replace the previous one by position
		:type message: str
		:raises NotImplementedError: Method replace() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_replace>`;
			- :ref:`TextBuffer <text_buffer_replace>`.

	.. _text_buffer_type_pop:

	.. py:method:: pop([number_string: int = -1]) -> str

		Removes and returns the specified string from the Text Buffer.

		.. versionadded:: v0.6.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:return: The specified string
		:rtype: str
		:raises NotImplementedError: Method pop() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_pop>`;
			- :ref:`TextBuffer <text_buffer_pop>`.

	.. _text_buffer_type_remove:

	.. py:method:: remove([number_string: int = -1]) -> None

		Deletes without returning the specified string from the Text Buffer.

		.. versionadded:: v0.6.0

		:param number_string: The string to be removed from the Text Buffer
		:type number_string: int
		:raises NotImplementedError: Method remove() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_remove>`;
			- :ref:`TextBuffer <text_buffer_remove>`.

	.. _text_buffer_type_clear:

	.. py:method:: clear() -> None

		Clears the entire Text Buffer, making it empty.

		.. versionadded:: v0.7.0

		:raises NotImplementedError: Method clear() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_clear>`;
			- :ref:`TextBuffer <text_buffer_clear>`.

	.. _text_buffer_type_save:

	.. py:method:: save(name_file: str, clean: bool) -> None

		Saves the text of the Text Buffer to a file.

		.. versionadded:: v0.5.0-dev

		:param name_file: The name of the file where the Text Buffer will be saved
		:type name_file: str
		:param clean: Saving should be done in Plain text (ignored with plain text environment)?
		:type clean: bool
		:raises NotImplementedError: Method save() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_save>`;
			- :ref:`TextBuffer <text_buffer_save>`.

	.. _text_buffer_type_load:

	.. py:method:: load(name_file: str) -> None

		Loads the text of the Text Buffer from a file.

		.. versionadded:: v0.7.0

		:param name_file: The name of the file from which to load the saved text of the Text Buffer
		:type name_file: str
		:raises NotImplementedError: Method load() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_load>`;
			- :ref:`TextBuffer <text_buffer_load>`.

	.. _text_buffer_type_input:

	.. py:method:: input(input_text: str) -> str

		A wrapper method for the standard Python input() that prepares the Text Buffer before using this function, and performs certain actions after, so that the Text Buffer can continue to function normally.

		.. versionadded:: v0.7.0

		:param input_text: Displayed text on the screen that tells the user what to enter
		:type input_text: str
		:return: The string entered by the user
		:rtype: str
		:raises NotImplementedError: Method input() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_input>`;
			- :ref:`TextBuffer <text_buffer_input>`.

	.. _text_buffer_type_update_console:

	.. py:method:: update_console() -> None

		Refreshes the console, erasing output text and outputting an updated buffer.

		.. versionadded:: v0.5.0-dev

		:raises NotImplementedError: Method update_console() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_update_console>`;
			- :ref:`TextBuffer <text_buffer_update_console>`.

	.. _text_buffer_type_update_entry:

	.. py:method:: update_entry() -> None

		Rewrites the last line of output after updating the last line of the buffer. Used (mostly) by the Progress bar (that is Progress string).

		.. versionadded:: v0.6.0

		:raises NotImplementedError: Method update_entry() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_update_entry>`;
			- :ref:`TextBuffer <text_buffer_update_entry>`.

	.. _text_buffer_type_output_entry:

	.. py:method:: output_entry() -> None

		Appends to the console the string added by the ``append()`` method.

		.. versionadded:: v1.0.0

		:raises NotImplementedError: Method output_entry() is not implemented in the base class

		.. seealso::
			Read the method definitions in

			- :ref:`BasicTextBuffer <basic_text_buffer_output_entry>`;
			- :ref:`TextBuffer <text_buffer_output_entry>`.
