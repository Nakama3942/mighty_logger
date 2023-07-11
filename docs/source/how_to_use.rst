How to use
==========

Instructions for using the library for practical purposes.

.. attention:: The Logger library implements a lot of additional hidden functionality that has no value outside the library. All available functionality is provided by the library packages. It is HIGHLY RECOMMENDED not to use modules for import!

.. contents::
	:class: this-will-duplicate-information-and-it-is-still-useful-here

Nuts and bolts
--------------

.. note:: Completely redesigned in v0.5.0 and extended in v0.7.0.

There are 5 environments for which logging can be implemented:

1. CONSOLE *(available since v0.2.0; reimagined in v0.5.0)*
2. PLAIN_CONSOLE *(available since v0.7.0)*
3. HTML *(available since v0.0.1; reimagined in v0.5.0)*
4. MARKDOWN *(available since v0.7.0)*
5. PLAIN *(available since v0.7.0)*

Log entries are stored in a text buffer. If the logging environment is CONSOLE or PLAIN_CONSOLE, then when the update_console() method is called, the program output to the console is completely updated (the main thing is to specify the correct screen width). However, when logging HTML, MARKDOWN or PLAIN, it is not known where and how to output the text (despite the fact that the library was originally created for logging in Qt - the library does not use this framework at all), so you need to get the text from the buffer and use it manually. To get the contents of the buffer, it is sufficient to use the ``buffer`` property.

.. danger:: Better not to use the buffer directly at all. The work of the Logger is debugged to work with the buffer, and any interference with it can completely break the work of the Logger. Do not change the contents of the Buffer! Use it only when outputting to a GUI window.

.. tip:: Better use saving Logger entries to a file when using a non-console environment.

Logging is done by the Logger class. To write to the log, you need to call a method with the desired entry type. There are 15 in total:

- debug
- debug_performance
- performance
- event
- audit
- metrics
- user
- message
- info
- notice
- warning
- error
- critical
- success
- fail

Basic example:

.. code-block:: python
	:linenos:

	# Let's entry the message "Hello world!" to log in console
	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments

	if __name__ == "__main__":
		# You can customize the buffer - specify the name of the program, the environment
		# and the width (for CONSOLE), which will be 1 more than the number of characters
		# that fit on the screen.
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		logger.message("Hello world!")

Types of library
----------------

.. note:: Available since v0.7.0.

The ``basic.lib_types`` package contains modules that implement their own types, which can act as a data store (for example, ``EntryType``) or just a wrapper over a string or other data type (for example, ``SortingKeyType``).

In the first case, it's just convenient to store different data together. This is what ``EntryType`` and ``EnvironmentType`` do. Thanks to this approach, it was possible to combine a bunch of Logger methods, the task of which was simply to form a certain type of entries into one method. However, I had to add an additional argument to specify the entry type, and despite this, this greatly reduced the amount of code. In addition, it has become much easier to add new environments.

In the second case, it simply helps to better control and understand the code. This approach is used by ``BasicAnimationType`` (and inherited ones) and ``SortingKeyType``. Now one programmer does not need to know which string to transfer, and it will be easier for another to understand the code. After all, it is much easier and clearer when ready-made code is used.

A unique case is the Text Buffer. It is not enough for him to organize a data store and provide properties. It must also provide methods for working with these same data. This is a fully functional working class. And since the library has implemented many working environments that can be divided into 2 principles of work, therefore, you need to implement 2 different Text Buffers for each principle. But how can one Logger work with two different Buffers? To solve this issue, the Text Buffer Type was implemented, which is, for the most part, an ordinary abstract class for both principles, so that their uses could be combined.

For a practical understanding, look at the :ref:`Table of correspondence between collections and types <correspondence_table>`:

.. _correspondence_table:

.. list-table:: Table of correspondence between collections and types:

	* - Type
	  - Example
	* - IndefiniteAnimationType
	  -
		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import IndefiniteAnimationType
			from mighty_logger.src import IndefiniteAnimations

			animation: IndefiniteAnimationType = IndefiniteAnimations.Line

	* - DefiniteAnimationType
	  -
		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import DefiniteAnimationType
			from mighty_logger.src import DefiniteAnimations

			animation: DefiniteAnimationType = DefiniteAnimations.Line

	* - EntryType
	  -
		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import EntryType
			from mighty_logger.src import LoggerEntryTypes

			entry: EntryType = LoggerEntryTypes.message

		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import EntryType
			from mighty_logger.src import ProcessEntryTypes

			entry: EntryType = ProcessEntryTypes.achievement

	* - EnvironmentType
	  -
		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import EnvironmentType
			from mighty_logger.src import LogEnvironments

			env: EnvironmentType = LogEnvironments.CONSOLE

	* - SortingKeyType
	  -
		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import SortingKeyType
			from mighty_logger.src import SortingKeys

			key: SortingKeyType = SortingKeys.SORT_ON_TIME

	* - TextBufferType
	  -
		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import TextBufferType
			from mighty_logger.basic import BasicTextBuffer

			buffer: TextBufferType = BasicTextBuffer(...)

		.. code-block:: python
			:linenos:

			from mighty_logger.basic.lib_types import TextBufferType
			from mighty_logger.basic import TextBuffer

			buffer: TextBufferType = TextBuffer(...)

Base of library
---------------

.. note:: Available since v0.2.0.

The ``basic`` package implements the "*basic*" functionality that implements the algorithms used by the Logger, but it is possible (with reservations) to be used separately from the Logger.

The "*Basic Logger*" just implements the storage of the main fields of the Logger and provides methods-formers of strings ("introductory" and "entry").

The "*Exporter*" implements the functionality of exporting to other file formats. At the moment, each environment is saved to its :ref:`own file <environment_format_table>` type, and the Exporter allows you to export logs to csv.

.. note:: At the moment, only export to csv format is supported, and support for other formats is not planned in the near future.

.. _environment_format_table:

.. table:: Environment-Format Relationship Table
	:widths: 20, 20

	============= ===========
	Environment   Format
	============= ===========
	CONSOLE       ``.contxt``
	PLAIN_CONSOLE ``.txt``
	HTML          ``.html``
	MARKDOWN      ``.md``
	PLAIN         ``.txt``
	============= ===========

The "*Modifier*" already directly affects the Logger's Buffer. It allows you to sort logs, search for words/letters/phrases in log messages, and also select the necessary logs.

"*Singleton*" implements a pattern to prevent multiple Buffers or Loggers from being created.

.. hint:: It is possible to create Logger objects of different classes because "Simple" Logger uses "Mighty", but you cannot create multiple "Simple" or "Mighty" Loggers.

"*Text Buffers*" implement more complex functionality over a regular list.

The package also stores exceptions that Logger or any other module of the library can use.

All this functionality is actively used by the Logger, but outside the library it is almost of no value, and therefore it is hidden from the external user. The package provides nothing but exceptions and Text Buffers.

.. note:: Although this library can serve well as a source of algorithms. You can take any module and rewrite it to fit your needs.

.. code-block:: python
	:linenos:

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments
	from mighty_logger.basic import ReCreationException

	if __name__ == "__main__":
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		logger.message("Hello world!")
		try:
			logger_two = Logger(
				program_name="Test",
				log_environment=LogEnvironments.CONSOLE,
				console_width=115
			)
		except ReCreationException as error:
			logger.message(str(error))

Resources of library
--------------------

.. note:: Available since v0.2.0.

About the resources of the library, for the most part, it was described in `Types of library`_. To reiterate, resources are collections of ready-made data objects for their respective types.

But not all resources are such, despite the fact that they are collections. There are two modules that store data not in the library type, but in the standard type.

The ``ansi_format`` module stores the ``AnsiFormat`` dictionary, but it is not accessible from the package. The module implements a function that finds the required key in the dictionary and returns the value. And ``color_picker`` generally implements a whole bunch of functions that either look up a color in a dictionary, or convert a color from one format to another. The main thing is the essence. These are all the same data collections, but only of a standard type, and the package provides access only to the necessary functions.

.. important:: The ``entry_types`` module implements many collections of different entry types, but many are for internal use by the Logger and are not provided by the package. It is STRONGLY RECOMMENDED that you only use the collections provided by the package!

.. code-block:: python
	:linenos:

	from mighty_logger.src import GetAnsiFormat

	if __name__ == "__main__":
		print(f"{GetAnsiFormat('underline/on')}Hello, {GetAnsiFormat('bold/on')}World{GetAnsiFormat('reset/on')}!")

Complexity
----------

.. note:: Here is the history of Logger development from v0.1.0 to v0.7.0.

In order to understand the essence of the emergence of various difficulties of Loggers, you need to study history.

The library was originally created as a Logger for the Qt framework, however Qt uses HTML to display text in a text field, so any library that supports HTML can be adapted to Qt. For this reason, it was HTML that was implemented by the very first Logger environment.

Back then, "separated" methods were used to form different types of entries, since no mechanism was invented for how they could be combined into one method. The bottom line is that each method first formed itself, then passed different colors, types as a string, etc to the shaper. So these methods will be separated for a very long time.

In *v0.2.0* a new Logger environment will be added - console. In fact, it will be the same environment, with the only difference that HTML tags have been replaced with ANSI codes and additional improvements and changes have been made. From that moment on, the console environment became the main environment, and all new innovations were first tested in the console environment and then transferred to HTML.

Since all improvements were carried out in one environment and copied to another, it was possible to combine different environments. Let me clarify that different environments were just different classes of Loggers. In *v0.5.0*, an attempt was made to merge the classes into one. And this attempt was successful. Then the first library type was added in its understanding (not taking into account the unique one). And the biggest change happened to the entry builder itself.

Now it was quite easy to specify the desired environment in the class constructor, and not create one of the different classes representing the environment. In *v0.6.0*, new entry types were added, but mostly they were just copied, changing some details.

And in *v0.7.0* insight came! I finally figured out how to separate these details from all these methods while working on library types. If not for this experience, I would not have done it. It was then that all type methods were replaced by one single method, which also required specifying the entry type, i.e. if earlier it was enough to call the desired type method and pass the message, now you need to call the writer method, to which you need to pass the type and message. It began to take more code.

It was this complication that caused the addition of a simplified class, which type returned the old Logger from the first versions, which has only type methods that accept only messages.

It's actually just a wrapper that uses the same "Mighty" Logger, but makes it easier to work with. Therefore, if you need a simple Logger from v0.1.0, you should use the "Simple" Logger. However, if you need all the functionality of updates, then you should immediately use the "Mighty" Logger. It is possible to use a "Mighty" Logger from a "Simple" one through the ``might`` property (read the `Loggers Properties`_ section).

Settings system
---------------

.. note:: Available since v0.5.0 and updated in v0.8.0, v0.9.2.

With the merging of classes, the system for setting up the logger has been completely changed. It is now possible to configure each entry locally instead of changing the logger settings.

And local settings got their globality. Now you do not need to specify, for example, italic font in each entry.

Global settings are passed to the constructor separately for each argument. Local settings are formatted as a dictionary, which is passed to the ``local_settings`` argument. All global settings arguments and local settings dictionary keys can be found :ref:`here <settings>`.

Here is an example of setting up a logger and entering:

.. code-block:: python
	:linenos:

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments, LoggerEntryTypes

	if __name__ == "__main__":
		logger = Logger(
			log_environment=LogEnvironments.HTML,
			global_italic_font=True
		)
		logger.might.entry(LoggerEntryTypes.debug, "logger debugging")
		logger.might.entry(LoggerEntryTypes.debug, "logger debugging", {"bold": True})
		logger.might.set_settings(global_italic_font=False)
		logger.might.entry(LoggerEntryTypes.debug, "logger debugging")
		logger.might.savy("log", False)

.. note:: The settings do not affect the opening string.

.. hint:: Simplified Logger provides the ability to quickly add entries of certain types, and configuring them slows down the logging process, and therefore you cannot locally configure entries in the simplified Logger. To set up an entry locally, you need to use the ``entry()`` method, remembering to specify what type of entry you want to make.

Loggers Properties
------------------

.. note:: Available since v0.9.3.

.. table:: Properties Table

	========================== =======================
	Class                      Properties
	========================== =======================
	BasicTextBuffer/TextBuffer ``text_buffer``
	MightyLogger               ``settings``/``buffer``
	Logger                     ``might``
	========================== =======================

``text_buffer`` - returns a list of Buffer strings; if it is a Logger Buffer, returns a list of Logger entry strings.

``settings`` - returns a dictionary of Logger settings.

``buffer`` - returns a list of Logger entry strings.

``might`` - returns a pointer to the "Mighty" Logger.

.. hint:: Properties can be nested.

.. code-block:: python
	:linenos:

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments, LoggerEntryTypes

	if __name__ == "__main__":
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		logger.debug("Logger.....")

		mlogger = logger.might
		mlogger.entry(LoggerEntryTypes.debug, "MightyLogger")

		settings = mlogger.settings
		settings['global_italic_font'] = True
		mlogger.entry(LoggerEntryTypes.debug, "italic.....")

		buf = mlogger.buffer
		mlogger.empty(str(buf))

Initial opening entry
---------------------

.. note:: Available since v0.3.0.

Just like color detection, logging starts with an introductory entry that collects system data:

- Computer name
- Username
- System name
- System version
- Computer architecture

However, the ``_initialized_data()`` method of the parent class, which is only called from the protected ``_initial_log()`` method of the logger, does all this. If you override this method by removing the ``_initialized_data()`` call from ``_initial_log()``, then the data will not be collected and the string will not be displayed:

.. code-block:: python
	:linenos:

	from mighty_logger import MightyLogger
	from mighty_logger.src import LogEnvironments, LoggerEntryTypes

	# I remove the initialization string

	class MyLogger(MightyLogger):
		def _initial_log(self):
			pass

	if __name__ == "__main__":
		logger = MyLogger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		logger.entry(LoggerEntryTypes.message, "Message data")  # Now there is no initialization string before this entry

.. danger:: Please note that ``Logger`` is just a wrapper around the real Logger. And this class will not be inherited, but simply creates an object of the ``MightyLogger`` class, and therefore it will not be possible to use your own class and a simplified Logger. If you plan to use a simplified Logger, there is no way to remove the initialization line...

Text Buffer
-----------

.. note:: Available since v0.4.0.

Text Buffer Definition:
	A Text Buffer is an area of RAM used to temporarily store text. A buffer can store text as a sequence of characters or bytes. It is typically used to temporarily store text that the user types or copies into an application before it is saved or processed. A buffer can also be used to exchange data between different program components.

In our case, the Text Buffer is a memory area used for temporary storage of text. Used to store text that represents, mainly in our library, log entries as a list of strings.

A basic Text Buffer has been implemented, which is slightly more functional than the standard list and a standard Text Buffer designed for use in the console, as it uses complex logic for calculating the movement of the cursor in console.

By standard, the logger itself creates a Buffer, but it can be created earlier. In this case, the logger will simply take a link to an already existing logger.

.. caution:: The Text Buffer has been completely designed to be used by the Logger. However, its use is not prohibited. Try to avoid modifying the Buffer while the Logger is running.

.. important:: If you are creating a console logger or a standard Text Buffer, you need to specify the width of the console (i.e. the number of characters that fit in one line), increased by one.

The standard Text Buffer manually changes the console output, but the basic one does not. But also the base one does not have any buffer display functionality at all. The programmer must manually retrieve the content and form the display.

There are two options for the development of events:

1. First, a buffer is created:
	- Create a buffer (and configure if it's a console one)
	- Create a logger (it will pull up the buffer itself)
2. First, a logger is created:
	- Create a logger (and configure if it is a console one)
	- To get a buffer, use the (3)contents of the (1)logger (2)buffer

.. code-block:: python
	:linenos:

	# option №1

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments
	from mighty_logger.basic import TextBuffer

	if __name__ == "__main__":
		buf = TextBuffer(LogEnvironments.CONSOLE, 115)
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE
		)
		logger.message("Message data")  # Text output is automatic

.. code-block:: python
	:linenos:

	# option №2

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments
	from mighty_logger.basic import TextBuffer

	if __name__ == "__main__":
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.HTML
		)
		logger.message("Message data")
		print(logger.might.buffer[-1])  # Text output is manually
		#       1      2      3

Can also save the contents of the buffer by calling the save() method and passing it the name of the file.

The buffer supports:

- Adding a string
- Inserting a string
- Replacing a string
- Extracting a string
- Removing a string
- Buffer cleaning
- Reading buffer strings from files

Also buffer overrides methods:

- << (load Buffer from file)
- >> (save Buffer to file)
- < (adding string to Buffer)
- > (extract string from Buffer)

An example of using one buffer:

.. code-block:: python
	:linenos:

	from mighty_logger.basic import BasicTextBuffer
	from mighty_logger.src import LogEnvironments

	if __name__ == "__main__":
		buffer = BasicTextBuffer(LogEnvironments.PLAIN)
		for i in range(0, 10):
			buffer.append(str(i))
		buffer.insert(0, "2")
		buffer.replace(1, "3")
		buffer < "50"
		buffer > 4
		print(buffer.pop(3))
		buffer.remove(6)
		data = buffer.input("Enter: ")
		print(data)
		buffer >> "output"
		buffer << "output"
		print(buffer.text_buffer)

Contents of the output.txt file:

.. code-block:: text

	2
	3
	1
	4
	5
	6
	8
	9
	50

.. code-block:: console

	2
	Enter: 50
	50
	['2', '3', '1', '4', '5', '6', '8', '9', '50']

Empty entry (or "a story about Buffer wrappers")
------------------------------------------------

.. note:: Available since v0.6.0 and expanded in v0.7.0.

Some of the new functionality added in the *v0.6.0* update required changing some entries in places. But the available methods at that time were not enough. To do this, the functionality of extracting entries from the Logger was added, but how to return them? Right! We need to use the same writing method, but which will bypass the formation of strings, since we already have a formed string!

.. note:: Subsequently, the merged "enterer" itself will switch to using this new method.

In addition, adding a new method will allow you to add custom entries. Since they would not be formed, they were nicknamed "empty" (hence the name).

In addition, the naming of different types of Logger entries contributed to the choice of this name. All of them were called the word "entry" and not "record" or "post" (the native language of the author is not English, but Ukrainian). So it was accepted even in the documentation of the very first versions. And in *v0.7.0*, all types were combined with one method, which, according to the established tradition, was called "entry".

The *v0.7.0* update itself was supposed to add a lot of functionality to the Text Buffer. Some old methods have been rewritten and new ones added. At that point in the tests, it was found that using one method was not enough. We need to write whole algorithms. And so every time, otherwise Logger's subsequent behavior will be unpredictable. It was decided to prohibit the use of the Buffer outside the library and think over the algorithms for using all the buffer methods in the Logger itself as wrapper methods. Later, the Buffer will be available again, since it can also be used separately from the Logger, but in the case of using the Logger, it was decided to leave the methods in order not to write entire algorithms each time.

------

All this was a preface, without which it was very strange to present the names of Logger wrapper methods. As already mentioned, by tradition, it was customary to call an entry of a formed string "entry", and not a formed one - "empty". This is what motivated us to put forward the following requirements for all names of wrapper methods: "all names must end with the letter Y! Well, it is desirable that the name fits the meaning, but it can also be funny...". See the following table for the names of the :ref:`wrapper methods <wrapper_methods>`.

.. _wrapper_methods:

.. table:: Wrapper methods

	========================== =======================
	BasicTextBuffer/TextBuffer MightyLogger
	========================== =======================
	``append``                 ``empty``
	``insert``                 ``addy``
	``replace``                ``modify``
	``pop``                    ``catchy``
	``remove``                 ``extractly``
	``clear``                  ``clearly``
	``save``                   ``savy``
	``load``                   ``loady``
	``input``                  ``getty``
	========================== =======================

.. note:: Previously, the ``catchy`` wrapper method was supposed to be called ``poppy``, but when the author learned about all the possible meanings of the word, in order to avoid confusion, he decided to change the name of this wrapper method.

For an introduction to these methods, please read `Text Buffer`_.

.. code-block:: python
	:linenos:

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments

	if __name__ == "__main__":
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		for i in range(1, 10):
			logger.debug(str(i) * 10)

		logger.might.addy(5, logger.might.catchy(8))

Modifiers and Exporters
-----------------------

.. note:: Modifiers is available since v0.7.1; Exporters - since v0.8.0.

Logs can be modified and exported.

Modification of a Logger means any change to its Buffer. And sorting, and search, and selection correspond to the concept of modification, since they change the order of the Buffer entries, some entries are removed, some are added (separators).

Sorting can be done by four keys:

1. Sort by entry *time*
2. Sort by entry *time in reverse order*
3. Sort by entry *category*
4. Sort by entry *type*

After the introductory string, a separator is added indicating that the sorted logs follow. Next come the sorted logs themselves. Then a separator follows, indicating that "empty" entries follow, which do not take part in sorting (otherwise how to divide the string?) and finally the last simple separator is added.

.. hint:: Log - Logger entry, formed string.

The search is performed on all messages of entries. You can also enable the search in "empty" entries. You can search for a letter, word, or phrase. Let's call it the search key. All strings in which the key is not found will be deleted. From the beginning and from the end, the found entries are framed by simple separators.

The selection is carried out by the key, which is a specially prepared ``EntryType``. These are the ``SelectionTypes`` and ``SelectionCategories`` classes. In the first one, the attributes store the types that need to be selected in the logs, and the second - the categories. The method will leave in the logs only those entries that match the type/category. The result will also be framed with simple separators from the beginning and from the end.

The Modifier takes a list of the Buffer and all its changes are immediately reflected in the original Buffer (if you do not pass a copy of the list). Therefore, this is a dangerous class, because if you do not provide for the changes that the class makes, you can completely break the Buffer. In addition, the algorithms themselves are written in such a way that they will work only with Logger entries, and therefore it makes no sense to give access to this class.

The logger implements wrapper methods that implement ready-made algorithms for working with this class. You can make a modification directly to the Logger, or you can leave the Logger with the original Buffer, saving all modifications to a file.

------

Like the Modifier, the Exporter also works directly with the Buffer list. However, he does not modify it. The Buffer based on the list creates a dictionary of csv entries, and writes this dictionary to the csv file in a separate method.

.. warning:: Currently the Exporter only supports exporting to csv format.

This class is already Buffer safe, but it still remains hidden, since you need to implement a whole algorithm to work with it, which was implemented in a wrapper method, which makes it pointless to keep it available.

------

.. code-block:: python
	:linenos:

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments

	if __name__ == "__main__":
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		for i in range(1, 10):
			logger.debug(str(i) * 10)

		logger.might.export_to_csv("ex")
		logger.might.search("5", False)

Publishers
----------

.. note:: Available since v0.7.0.

Everything is simple here. Publisher methods simply write certain information to the logs, such as Logger settings, library author, etc.

The following publishers are available:

- ``publish_id()``
- ``publish_program_name()``
- ``publish_environment()``
- ``publish_global_settings()``
- ``publish_author()``
- ``publish_license()``
- ``separator()``

.. code-block:: python
	:linenos:

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments

	if __name__ == "__main__":
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		logger.might.publish_author()

Logger entry
------------

.. note:: Available since v0.7.0.

The ``entry()`` method is the most basic and used method of the library. A detailed history of the development of Loggers can be found in the "`Complexity`_" chapter.

I will describe the current algorithm for "writing" to the Logger. The base Logger implements a method for generating a Logger entry - a string in a specific format. All Logger entries and empty entries are stored in the Logger Buffer - Text Buffer that stores the entries in the list. And the task of ``entry()`` is to collect all the necessary data (now this is the ``type``, ``message`` and ``settings`` of the entry), form the entry using the base method and save the generated string to the list of entries.

Now all these tasks are divided between simple methods, but earlier all this was implemented in this method, which was also divided into different type methods. Now the same type-methods are implemented in the "Simplified" Logger, whose task is to return type-methods with an additional simplification in the form of hiding the setting.

.. code-block:: python
	:linenos:

	from mighty_logger import MightyLogger
	from mighty_logger.src import LogEnvironments, LoggerEntryTypes

	if __name__ == "__main__":
		logger = MightyLogger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		logger.entry(LoggerEntryTypes.message, "Using entry()")

Processes
---------

.. note:: Available since v0.6.0 and updated in v0.8.0, v0.9.2.

In the Library, you can not only make entries in the Logger, but also launch full-fledged Logger Processes.

.. important:: If you start a Process, then only that Process can be controlled at that moment and no other entries can be added to the log. However, through the ``Logger.note_process()`` method, you can add an entry of any type, which will be considered a Process Entry. What's more, two additional entry types are available for this method: *achievement* and *milestone*.

.. warning:: DO NOT run multiple Processes!

It is important to know that there are two types of Processes:

1. `Indefinite Processes`_
2. `Definite Processes`_

Process logging has its own entry types:

- *initiation*, denoting the start of the Process
- *progress* specifying the current state of the Process:
	- *indefinite progress*, playing animation during the execution of the Process
	- *definite progress*, showing the Progress bar of the Process execution
- *success* indicating successful execution of the Process
- *fail*, indicating that the Process failed

Process logging entry types are protected and only the class itself and inherited ones can access them. Control methods are provided to work with them, the unique *achievement* and *milestone* types, and in general for *managing* the Process. How to manage Processes is described in the subchapter on `Indefinite Processes`_ and in `Definite Processes`_.

An example of usage will be given at the end of this section "`Example using of Processes`_".

Indefinite Processes
____________________

Indefinite Process is expressed by the fact that it is not known how to evaluate the completion of the Process. The completion of the Process is indicated only by the receipt of the result and the intermediate Milestones of the Process do not affect the Process itself, more precisely, it is impossible to calculate from them how much the Process has been completed; well, or it consists of only one Milestone.

	It is possible to find out whether the Process is completed only by the result obtained and the intermediate Milestones of the Process (if any) do not affect this (completion calculation).

------

To start an indefinite Process, you need to call the ``Logger.start_indefinite_process()`` method. It has all the same arguments as regular entry types, but Processes differ in the presence of animation, and therefore it is required to specify it when starting the Process, which is an additional argument. Fortunately, animation is specified by default, and it does not need to be set in this method. The subsequent information that is passed to the method is applied to two entries at once: *initiation* and *indefinite progress*.

.. caution:: Once a Process has started, only those methods that are responsible for managing the Process MAY be used.

.. warning:: Also, DO NOT create multiple Processes!

*These restrictions are not contrived and not taken from the ceiling! There are two circumstances that follow from the same cause. The thing is that Process logging uses animation, which for optimization does not use a complete rewriting of the entire output (it is necessary that the output does not blink), but simply rewrites the last string (without overwriting). There is another reason, but it does not affect the circumstances. The Library does not yet implement a wide buffer management functionality and there is no easy controlled access to the buffer, despite the fact that it is possible. It might just break down. And even if it were, it would complicate even more the logic of working with the buffer in the Logger, so the Logger would still work only with the last string. Therefore, if you use the standard method of adding an entry to the log, it will be added to the end of the buffer, after which the streaming animation will overwrite the last string, leaving one of its frames on the penultimate one. To avoid this, the ``Logger.note_process()`` method was written, which adds an entry using a more complex algorithm. After all, it will not be enough just to add a new entry to the penultimate place - the animation does not overwrite the entire output, but only the last string, therefore all entries will be displayed only after the animation is completed... The same reason, you cannot create several Processes, since they will overwrite each other , and the result may be unexpected. Tests were not carried out, the result is not known to the author.*

The ``Logger.note_process()`` method makes it possible to make any entry to a Process and adds two new entry types: *achievement* and *milestone*. Just like ``Logger.start_indefinite_process()``, it has all the standard entry method arguments with an additional method to specify what type of entry to make to the Process. In this case, the new argument is already required.

And finally, to terminate the Process, you need to call the ``Logger.stop_process()`` method. It no longer has additional methods and focuses on the completion of the Process. It is measured in percentage. In this Library, it is considered that if the Process is completed completely, i.e. 100% - it means that it was completed successfully, however, if the Process could not be completely completed, then the Process failed. This determines the completion of the Process. By default, the Process starts with zero termination. Therefore, if the Process ended unsuccessfully, it is enough to simply call the ``Logger.stop_process()`` method. If the Process is completed successfully, you need to call ``Logger.progress_rise(100)`` before this method. More details about this method will be written here: "`Definite Processes`_".

An example of usage will be given at the end of this section "`Example using of Processes`_".

Definite Processes
__________________

A definite Process differs from an indefinite one in that its completion can be determined not only by the presence/absence of a result, but it is also possible to determine the percentage impact on the execution of the Process by each of its Milestones.

	Knowing which Milestone and how it was completed, you can determine how close the Process has come to its completion.

------

To start an indefinite Process, you need to call the ``Logger.start_definite_process()`` method. It differs from ``Logger.start_indefinite_process()`` only in that it accepts a different type of animation - animations of a specific Process (i.e. Progress bars) and outputs *initiation* and *definite progress* entries.

.. caution:: Once a Process has started, only those methods that are responsible for managing the Process MAY be used.

.. warning:: Also, DO NOT create multiple Processes!

Further, the Progress entry will no longer display a smooth animation, but a Progress bar with the percentage of the Process completed. As the Process progresses, you need to indicate how complete it is. This is done using the ``Logger.progress_rise(int)`` method. It indicates how the process is done. The programmer himself must calculate this. For example, if the task is to download 100 files, then after downloading each file, you can add one percent.

.. important:: It is important to note that this method does not add the specified percentage to the previous value, but sets it.

.. hint:: Those if the Process was completed by 30% and Progress has advanced by another 2%, then you need to pass not 2, but 32 to the ``Logger.progress_rise(int)`` method, since after adding 2% to 30%, the current Progress will already be 32%, and when passing 2%, the method will reset the Progress from 30% to 2%!

Everything is the same as in an indefinite Process, in a definite one you can add any entry of the Process using the ``Logger.note_process()`` method and terminate it with the ``Logger.stop_process()`` method (read the previous section "`Indefinite Processes`_").

An example of usage will be given at the end of this section "`Example using of Processes`_".

Example using of Processes
__________________________

Here is written an installer simulator-program. Instead of sleep(), some action should be performed that should bring the Process to an end.

.. code-block:: python
	:linenos:

	from time import sleep

	from mighty_logger import Logger
	from mighty_logger.src import LoggerEntryTypes, ProcessEntryTypes, LogEnvironments

	if __name__ == "__main__":
		logger = Logger(
			program_name="Installer",
			log_environment=LogEnvironments.PLAIN_CONSOLE,
			console_width=115
		)

		logger.message(message_text="Program installation started")

		sleep(1)
		logger.might.start_indefinite_process("File upload")
		sleep(2)
		logger.might.note_process(ProcessEntryTypes.achievement, "Files downloaded")
		sleep(3)
		logger.might.progress_rise(100)
		logger.might.stop_process("Files unzipped")

		logger.warning("Newer version found")

		sleep(1)
		logger.might.start_definite_process("Installing files")
		sleep(0.6)
		logger.might.progress_rise(3)
		sleep(1.1)
		logger.might.progress_rise(47)
		logger.might.note_process(ProcessEntryTypes.milestone, "Files prepared")
		sleep(1.3)
		logger.might.progress_rise(85)
		sleep(0.8)
		logger.might.note_process(LoggerEntryTypes.error, "Incompatibility found")
		sleep(1.3)
		logger.might.note_process(LoggerEntryTypes.resolved, "Incompatibility eliminated")
		sleep(1.1)
		logger.might.progress_rise(86)
		sleep(1.5)
		logger.might.progress_rise(100)
		sleep(1.3)
		logger.might.stop_process("Program installed")

Log:

.. code-block:: console

	-Installer?entry> $DESKTOP-8KG0R64:User:Windows:10.0.19045:64bit:WindowsPE:AMD64
	-?entry>          *2023-07-06 13:00:58.385749 📝 #STATUS: @MESSAGE - Program installation started
	-?entry> &0:00:00 *2023-07-06 13:00:59.386826 🚀 #STATUS: &INITIATION - File upload
	-?entry> &0:00:02 *2023-07-06 13:01:01.391737 🏆 #STATUS: &ACHIEVEMENT - Files downloaded
	-?entry> &0:00:05 *2023-07-06 13:01:04.503493 🎉 #STATUS: &SUCCESS - Files unzipped
	-?entry>          *2023-07-06 13:01:04.504493 ⚡️ #STATUS: !WARNING - Newer version found
	-?entry> &0:00:00 *2023-07-06 13:01:05.506823 🚀 #STATUS: &INITIATION - Installing files
	-?entry> &0:00:01 *2023-07-06 13:01:07.247407 🔖 #STATUS: &MILESTONE - Files prepared
	-?entry> &0:00:03 *2023-07-06 13:01:09.395409 🚫 #STATUS: !!ERROR - Incompatibility found
	-?entry> &0:00:05 *2023-07-06 13:01:10.784921 ❗ #STATUS: !RESOLVED - Incompatibility eliminated
	-?entry> &0:00:09 *2023-07-06 13:01:14.913956 🎉 #STATUS: &SUCCESS - Program installed

Timers
------

.. note:: Available since v0.6.1.

The Timer is a simplified Process, but judging by the algorithm, it is an extended Logger. The only thing it does, unlike ``entry()``, is set the start time stamp with the ``start_timer()`` method; finds out the difference between the current and start time - ``timer_mark()`` and in addition to ``timer_mark()`` resets the start time stamp - ``stop_timer()``.

However, it is similar to a Process, as it also indicates the elapsed time since the Process was started. And they use the same algorithm. But apart from the algorithm, they no longer have similarities. Their working principle is completely different. The Timer is still the same Logger with an additional time calculation, and the Process is a completely different logic running in a thread to display the animation of the Process execution.

Simply put, it can be represented as follows. A Logger entry is a string describing a "single action". However, if this "single action" is time consuming or may require the completion of subtasks, which in themselves are not full-fledged "actions", this is called a Process.

Yes, the Process is much more complicated, but in rank it is lower than the Logger, since this is just its auxiliary functionality. You can completely do without Processes, but without the animation playing, it may seem that the program is frozen. To avoid such embarrassment, the Process was implemented. And the Timer is on par with the Logger, as it performs the same task as the Logger, with a few additions.

In addition, the Timer can calculate any time frame and any number of "actions". For example, the Timer can determine at least the entire time of the Logger from start to finish, taking into account all the "actions", and the Process will be one of its "actions", i.e. a Process can be part of a Timer (as it is part of a Logger), but a Timer cannot be part of a Process in the same way that a Logger can be.

.. code-block:: python
	:linenos:

	from time import sleep

	from mighty_logger import Logger
	from mighty_logger.src import LogEnvironments

	if __name__ == "__main__":
		logger = Logger(
			program_name="Test",
			log_environment=LogEnvironments.CONSOLE,
			console_width=115
		)
		logger.might.start_timer("Start timer")
		sleep(1)
		logger.debug("Debug entry")
		sleep(1)
		logger.might.timer_mark("Timer mark")
		sleep(1)
		logger.might.stop_timer("Stop timer")
