# Changelog
<!--
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
-->
<!--
## vX.X.X (DATE)

#### Bug Fixes:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Invalid Fixed:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Documenting:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Duplicating:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Enhancements:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

---
-->

## Alpha-release v0.0.1 (13.03.2023)

#### Release
The library implements the formation of a beautifully formatted colored text, similar to a log, which has all the necessary information:
- Logging time;
- Name of device and profile that logged;
- Log status;
- Description of the log status;
- Log type;
- Log message.

Any information to the output can be turned off (according to the standard, everything is included). It is also possible to change the output settings during the logging process. It is possible to change colors (class PickerModifierQ).

*!!!ATTEMPTION!!! At the moment, logging is implemented only in the form of HTML code for QTextBrowser for PyQt, since quite often I need to output the log not to the console, but to the program and save it to a file, including saving colors. Therefore, in this version, output to the console is not implemented, but only in QTextBrowser, however, in the next versions, a lot of functionality will be implemented for easy and convenient logging!*

---

## Little update v0.0.2 (16.03.2023)

#### Bug Fixes:
- Fixed some typos.

#### Enhancements:
- Added new colors:
	- OCEANBLUE;
	- DARKOCEANBLUE.
- Changed color names:
	- CYAN -> BLUE;
	- DARKCYAN -> DARKBLUE.
- Added an ID to each logger class;
- Added new methods to the Logger class:
	- SUCCESS();
	- FAIL();
	- START_PROCESS(); *stub - not implemented*
	- STOP_PROCESS(). *stub - not implemented*
- Added some links to PyPi.

---

## Types update v0.0.3 (17.03.2023)

#### Documenting:
- The LoggerQ class is fully documented.

#### Enhancements:
- Added new types of log output:
	1. DEBUG_PERFORMANCE;
	2. PERFORMANCE;
	3. EVENT;
	4. AUDIT;
	5. METRICS;
	6. USER;
	7. MESSAGE;
	8. NOTICE.
- Added new colors:
	1.  FIREBRICK *replaced RED*
	2.  MEDIUMSPRINGGREEN
	3.  SPRINGGREEN
	4.  MEDIUMSEAGREEN
	5.  SEAGREEN
	6.  FORESTGREEN *not used yet*
	7.  YELLOWGREEN
	8.  OLIVEDRAB
	9.  OLIVE
	10. DARKOLIVEGREEN
	11. AQUAMARINE *replaced BLUE*
	12. TURQUOISE *replaced DARKBLUE*
	13. SKYBLUE *replaced OCEANBLUE*
	14. LIGHTSKYBLUE *replaced DARKOCEANBLUE*
	15. BLUE *Adopted its color according to the X11 standards table*
	16. MEDIUMBLUE
	17. DARKBLUE *Adopted its color according to the X11 standards table*
	18. NAVY
	19. BLUEVIOLET *replaced VIOLET*
	20. DARKVIOLET *Adopted its color according to the X11 standards table*
	21. GAINSBORO
	22. LIGHTGREY
	23. SILVER
	24. DIMGREY

---

## Color update v0.0.4 (25.03.2023)

#### Bug Fixes:
- Found and fixed several minor bugs.

#### Documenting:
- The HtmlColorSetInitQ class is fully documented;
- Slightly fixed CHANGELOG.

#### Enhancements:
- The color system has been completely redesigned (i.e. the system for working with colors);
- Added ALL X11 table colors [from this page](https://en.wikipedia.org/wiki/Web_colors);
- Added functions for getting color values in different formats by their names;
- Added ColorException;
- Started work with console logger (*not yet available*);
- PickerModifierQ class renamed to HtmlColorSetInitQ;
- Now only one object of the HtmlColorSetInitQ class can be created;
- Now only one object of the LoggerQ class can be created;
- The color table of the LoggerQ logger has been changed - now the table does not store color names, but abstract names:
	- TIME;
	- USER;
	- STATUS;
	- STATUS_MESSAGE;
	- TYPE_DEBUG;
	- DEBUG_MESSAGE;
	- TYPE_DEBUG_PERFORMANCE;
	- DEBUG_PERFORMANCE_MESSAGE;
	- TYPE_PERFORMANCE;
	- PERFORMANCE_MESSAGE;
	- TYPE_EVENT;
	- EVENT_MESSAGE;
	- TYPE_AUDIT;
	- AUDIT_MESSAGE;
	- TYPE_METRICS;
	- METRICS_MESSAGE;
	- TYPE_USER;
	- USER_MESSAGE;
	- TYPE_MESSAGE;
	- MESSAGE_MESSAGE;
	- TYPE_INFO;
	- INFO_MESSAGE;
	- TYPE_NOTICE;
	- NOTICE_MESSAGE;
	- TYPE_WARNING;
	- WARNING_MESSAGE;
	- TYPE_ERROR;
	- ERROR_MESSAGE;
	- TYPE_CRITICAL;
	- CRITICAL_MESSAGE;
	- TYPE_PROGRESS;
	- PROGRESS_MESSAGE;
	- TYPE_SUCCESS;
	- SUCCESS_MESSAGE;
	- TYPE_FAIL;
	- FAIL_MESSAGE.
- Now, initially this table is not initialized and the logger will not be able to work. First you need to initialize the table by creating an object of the HtmlColorSetInitQ class, which also provides methods for changing this very logger color table;
- Implemented library functionality tests for early detection of minor bugs.

---

## First official release v0.1.0 (26.03.2023)

#### Bug Fixes:
- Fixed a bug that occurs when passing arguments to the LoggerQ constructor;
- Fixed a bug due to which the color value was not correctly saved in the logger's color table when changing the color manually.

#### Documenting:
- Completed documentation of the library;
- Wrote the actual README.md (which corresponds to the current version).

#### Enhancements:
- Slightly redefined colors in the logger;
- Changed the order of colors in the color table.

---

## Structural update v0.2.0 (29.03.2023)

#### Documentation:
- Documented all new functionality;
- Fixed typos and outdated information in old documentation.

#### Enhancements:
- Added a large dictionary of all ANSI escape codes and the GetAnsi() function to get it;
- CodColor() function renamed to AnsiForegroundColor();
- Fully implemented AnsiColorSetInit and Logger classes based on HtmlColorSetInitQ and LoggerQ;
- Singleton pattern used by HtmlColorSetInitQ, LoggerQ, AnsiColorSetInit and Logger moved to a separate class;
- A base class has been created for LoggerQ and Logger, which includes initialization, setting up loggers and generating record strings (*at the moment, inherited classes are used to simplify interaction with the base class and use ready-made functionality, but in the future their own functionality will be expanded*);
- Optimized HexColor() and AnsiForegroundColor() functions;
- **The project structure has been completely changed** (*however, this only affects the development of the library and support for programs written with the version of the library v0.1.0 will remain, since the external attributes of communication with the library have not changed*);
- Added the DefaultColorScheme list, which stores a list of all colors that are used in the color schemes of the loggers and the GetDefaultColorScheme() function to get this list;
- Now the ColorPicker dictionary stores only color values in RGB, and other formats are obtained by converting RGB;
- Added functions Dec2Hex(), Dec2Ansi(), Hex2Dec(), Hex2Ansi(), Ansi2Dec(), Ansi2Hex(), which are used to convert one color value format to another;
- *The logic of assembling strings logging entry's has been completely changed*;
- The work of the HtmlColorSetInitQ and LoggerQ classes is adjusted to the new best functionality that is used in the new classes AnsiColorSetInit and Logger.

---

## Tests and protections v0.2.1 (31.03.2023)

#### Bug Fixes:
- Fixed old calls to Singleton and BasicLogger to new _Singleton and _BasicLogger in HtmlColorSetInitQ, LoggerQ, AnsiColorSetInit and Logger classes;
- Fixed a bug in the setColor() method of the AnsiColorSetInit class, where the value of the new argument was not passed to the Dec2Ansi() function after changing the GetAnsiFormat() function.

#### Documenting:
- Wrote the actual README.md (which takes into account changes in versions v0.2.0 and v0.2.1);
- Fixed a bug in the annotation of the setColor() method of the HtmlColorSetInitQ class;
- Changed the order of the changelog - now it goes in direct order from top to bottom (easy to read and understand), and not from bottom to top.

#### Enhancements:
- Renamed the GetAnsi() function to GetAnsiFormat(), implemented the _RecursiveGetAnsiFormat() helper function for it - now GetAnsiFormat() takes the path to the ANSI escape code value, recursively traverses the tree and returns the ANSI escape code value, which helps to make the code easier to understand and speed up development programs when using the library; here are some examples:
```python
# Before
print(f"{AnsiFormat['color']['set']['background'].replace('$', '255;165;0')}Test string")
print(f"{AnsiFormat['reset']['on']}Test string")

# After
print(f"{GetAnsiFormat('color/set/background/255;255;255')}Test string")
print(f"{GetAnsiFormat('reset/on')}Test string")
```
- Renamed the AnsiForegroundColor() function to AnsiColor() - if earlier the function returned only the color of the text (the usual foreground), now you can specify any of the five plans (this is necessary for the next update, where I will add a change not only to the color, but also to the background of the logs):
	1. foreground
	2. background
	3. bright foreground
	4. bright background
	5. underline
- Adapted the Dec2Ansi() and Hex2Ansi() functions to the modified AnsiColor();
- Protected the qt_colored_logger/basic directory - now it is called qt_colored_logger/_basic: you can still use its functionality, but now, according to the agreement, the IDE will issue a warning; *remember - protected modules are designed only for use inside the library*;
- The structure of the qt_colored_logger/_basic protected directory has been slightly changed;
- Changed names of keys in "AnsiFormat/font" dictionary from "1th alternative", "2th alternative" and "3th alternative" to "1st alternative", "2nd alternative" and "3rd alternative" respectively.

---

## Background update v0.3.0 (05.04.2023)

#### Documenting:
- Updated documentation;
- Wrote the actual README.md (which corresponds to the current version).

#### Enhancements:
- Added support for inverting colors in posts (console);
- Added support for backgrounds in posts (console, HTML);
- Completely redesigned and written from scratch logger color table;
- Logger included AnsiColorSetInit;
- LoggerQ included HtmlColorSetInitQ;
- Removed list of default colors;
- Post types categorized:
	- Debugging (%);
	- Event (~);
	- Message (@);
	- Error (!);
	- Process (&).
- Argument names are now required;
- Added an introductory line with system initialized information;
- Added a global enable background setting;
- Started work on the text buffer;
- Added new CombinationException.

---

## Buffer update v0.4.0 (09.04.2023)

#### Documenting:
- Split README.md, cutting DATA.md and APPLYING.md out of it;
- Published a plan for the next updates in README.md;
- Updated documentation;
- Wrote the actual README.md, DATA.md and APPLYING.md (which corresponds to the current version).

#### Enhancements:
- Added a package qt_colored_logger.text;
- Added TextBuffer (used for console) to qt_colored_logger.text package;
- Added BasicTextBuffer (used with HTML) to qt_colored_logger.text package;
- Loggers moved from qt_colored_logger root package to nested qt_colored_logger.logger;
- Entry methods rewritten - now they do not return strings of entries, but add them to the text buffer;
- Returned protected modules, making them fully available;
- Added blanks for the next updates;
- Reworked the principle of forming strings of records in the BasicLogger, getting rid of the string variable;
- Added get_buffer() method in loggers.

---

## Dev-Unifying update v0.5.0-dev (10.04.2023)

#### Enhancements:
- _html_initialized_data() attached to _initialized_data();
- _assemble_html_entry() attached to _assemble_entry();
- Implemented LogEnvironment enumeration with Console and HTML values;
- The abstract class TextBufferBase is implemented as a type for buffers (it was necessary to combine two buffers BasicTextBuffer and TextBuffer);
- The Logger class has been rewritten;
- The LoggerQ class is hidden;

---

## Pre-Unifying update v0.5.0-pre (10.04.2023)

#### Documenting:
- Updated annotation of modules and packages.

#### Enhancements:
- The TextBufferBase class has been moved to the qt_colored_logger.basic package in the new text_buffer_type.py module and renamed to TextBufferType;
- Optimized the Logger class;
- Completed the LogEnvironments format and usage;
- Removed LoggerQ class and html_colored_logger.py module;
- Accounted for environment in the set_color() function in the Logger class;
- The colored_logger.py module has been renamed to powerful_logger.py and moved to the library root;
- Removed the empty qt_colored_logger.logger package;
- Renamed the library to mighty_logger.

---

## Unifying update v0.5.0 (13.04.2023)

#### Bug Fixes:
- Fixed TypeError in the message() method (because its name began to intersect with the setting responsible for displaying the message entry);
- A bug of possible unpredictable behavior of the Logger has been fixed, since when creating the second object, a link to the existing one is returned, but \_\_init\_\_() is still called, and in case of switching to HTML format or changing other settings, unexpected behavior of the program could occur (just re-initialization of the class was excluded);
- Fixed a bug in the save() method of the TextBufferType class and inherited classes: the fact is that TextBuffer overrides the method with the addition of the `clean` argument, which is not in the parent abstract TextBufferType class - now it (the argument) is defined in all classes;
- Fixed a bug when the buffer is created in advance: now there is a check if the buffer object exists; if it exists, the link is saved to the logger and a log is written that the buffer is borrowed, otherwise a new buffer is created.

#### Documenting:
- Updated documentation;
- Wrote the actual README.md, DATA.md and APPLYING.md (which corresponds to the current version).

#### Enhancements:
- Renamed the repository to mighty_logger;
- Translated the names of the recording methods from the Upper case format to the Lower case format;
- Added a new ReCreationException that is thrown when an object of a class inherited from Singleton is re-created;
- The settings system has been completely changed.

---

## v0.4.0.1 (13.04.2023)

#### Documenting:
- Preparing a renamed. Minor changes have been made to README.md, adding links to a new repository with a new name.

---

## Hints update v0.5.1 (08.06.2023)

#### Bug Fixes:
- Removed line breaks in HTML, since Qt's append() method adds a line break on its own; this way lists of HTML records will be displayed correctly in Qt (no unnecessary breaks), but when saving the file, you can choose whether to add line breaks between entries or not.

#### Documenting:
- Updated documentation;
- Wrote the actual README.md, DATA.md and APPLYING.md (which corresponds to the current version).

#### Enhancements:
- Added 4 sets of icons for entries with the ability to create your own sets;
- Added template status messages with the ability to specify your own status message.

---

## Progress update v0.6.0 (14.06.2023)

#### Documenting:
- Updated documentation;
- Wrote the actual README.md, DATA.md and APPLYING.md (which corresponds to the current version).

#### Enhancements:
- Implemented Processes (an abstract concept that appears to be a new functionality):
	- Added new entry types:
		- empty (available[^available]);
		- resolved (available[^available]);
		- unresolved (available[^available]);
		- initiation (hidden[^hidden]; auto[^auto]);
		- achievement (hidden[^hidden]; manual[^manual]);
		- milestone (hidden[^hidden]; manual[^manual]);
		- ~~progress~~ ->
			- indefinite_progress (hidden[^hidden]; auto[^auto]);
			- definite_progress (hidden[^hidden]; auto[^auto]);
		- success (available[^available]) -> (hidden[^hidden]; auto[^auto]);
        - fail (available[^available]) -> (hidden[^hidden]; auto[^auto]);
	- Added new *control* methods:
		- `Logger.start_indefinite_process()` - starts an indefinite Process;
		- `Logger.start_definite_process()` - starts a definite Process;
		- `Logger.progress_rise()` - sets the percentage of completion of the Process;
		- `Logger.note_process()` - adds an entry to the Process;
		- `Logger.stop_process()` - terminates the Process;
	- Added animations for Processes;
	- Added enum `TypesEntries` for `Logger.note_process()`;
- Added extraction of strings from the buffer by the `pop()` method;
- Beautifully decorated the code in the Logger class;
- Expanded icon set (for new entries).

[^available]: Can be used not only in Processes, but also in a regular Logger

[^hidden]: Can only be used in Processes, cannot call an entry from the Logger

[^auto]: Available only to Logger

[^manual]: Available to the programmer

---

## Progress update v0.6.1 (18.06.2023)

#### Bug Fixes:
- Fixed a bug where the percentage was changing just before adding a Process entry, and it was completely breaking the output (and a 0.01 second delay was enough to fix it);
- Fixed a bug that occurs when the last string in the console is removed, which occupies more than 1 line.

#### Documenting:
- Updated versioning;
- Updated documentation.

#### Enhancements:
- Added new animations and worked out the old ones;
- Added a new category of types: Timer, and 3 entries for it.

---

## "Buffer improvement" update v0.7.0 (26.06.2023)

#### Enhancements:
- All entry types were merged into one `entry()` method, and all type differences were moved to the `LoggerEntryTypes` (available), `ProcessEntryTypes` (available), `ServiceProcessEntryTypes` (not available), `ServiceTimerEntryTypes` (not available) classes;
- Due to the acquired complexity, a simplified version of the Logger was written - SimpleLogger, where all the cut Logger methods, such as `debug`, `message`, etc., were transferred;
- Removed the ability to create custom icon sets (and removed the icon set module);
- The ability to change the color of entries has been removed (now it is impossible to change the color scheme at all due to the new improved data storage system for entry types);
- Added new type `EnvironmentType`;
- Added new Logger environments:
	- `PLAIN_CONSOLE`;
	- `MARKDOWN`;
	- `PLAIN`;
- All types (classes) created for use within the library have been redefined from their original modules into the new `basic.lib_types` package;
- Animations and Text buffers module moved to `src` package;
- Removed emptied package `text`;
- Removed `CombinationException`;
- Added `EnvironmentException` and `InitException`;
- Buffer updated:
	- Added Buffer input implementation (because after creating a Logger object, you can't use the standard Python `print()`, `input()` and other functions that can affect console output when using the `CONSOLE` environment and the new `PLAIN_CONSOLE`) - now there is not only output in console, but also input (`input()` method in Buffer);
	- Updated the `save()` method of the Text buffer (now the `clean` argument is important for any environment, since the Buffer of Logger can store not only log entries, which allows the `empty()` method, which is a standard `print()` in the library);
	- The implementation of the `remove()` method in the buffer is complete;
	- Added `clear()` and `load()` methods;
	- `TextBufferType` is no longer an abstract class like other types-class;
	- Buffer development completed;
- Added methods-publishers in the Logger, which display certain information about the Logger in the logs:
	- `publish_id()` publishes the generated Logger ID;
	- `publish_program_name()` publishes the name of the program whose work is being logged;
	- `publish_environment()` publishes the environment in which the Logger works;
	- `publish_global_settings()` publishes global Logger settings;
	- `publish_author()` publishes the author of the library;
	- `publish_license()` publishes a library license;
	- `separator()` adds a separator in the form of a line of eighty dashes;
- Added wrapper methods in Logger for Buffer methods:
	- `Logger.addy()`[^strange] - `TextBufferType.insert()`;
	- `Logger.modify()`[^strange] - `TextBufferType.replace()`;
	- `Logger.catchy()`[^strange] - `TextBufferType.pop()`;
	- `Logger.extractly()`[^strange] - `TextBufferType.remove()`;
	- `Logger.clearly()`[^strange] - `TextBufferType.clear()`;
	- `Logger.savy()`[^strange] - `TextBufferType.save()`;
	- `Logger.loady()`[^strange] - `TextBufferType.load()`;
	- `Logger.getty()`[^strange] - `TextBufferType.input()`;
- Of the new wrapper and publisher methods, SimpleLogger implements:
	- `SimpleLogger.print()` - `Logger.empty()`;
	- `SimpleLogger.input()` - `Logger.getty()`;
	- `SimpleLogger.save()` - `Logger.savy()`;
	- `SimpleLogger.load()` - `Logger.loady()`;
	- `SimpleLogger.separator()` - `Logger.separator()`;
- Optimized buffer initialization.

[^strange]: Why such strange names were chosen is a big story here ... Initially, each entry type represented a different method, but in the documentation, the entry was always represented by the word "entry". When the author had to add the `Logger.note_process()` method, there was a need to add lines without forming them (that is, to do a regular `print()` in the Logger, since there was already a functional in the buffer). Since it was thought that such strings would be called "empty", they began to be called "empty". Having already two methods ending in "y", other names were invented for all other Buffer wrapper methods with the main condition - the last letter "y". This was done just for fun. The native language of the author is Ukrainian.

---

## Modding update v0.7.1 (28.06.2023)

#### Enhancements:
- Renamed `Logger` to `MightyLogger`;
- Renamed `SimpleLogger` to `Logger`;
- Renamed `Logger.get_logger()` to `Logger.might()`;
- Removed methods:
	- `Logger.print()`;
	- `Logger.input()`;
	- `Logger.save()`;
	- `Logger.load()`;
	- `Logger.separator()`;
- Added a new `Modifier` class with:
	- the `sort()` method for sorting logs by key;
	- the `search()` method to search for logs that contain a given string in the message;
	- the `select()` method for selecting logs by type;
	- the `entries` property, which returns a list;
- Added a new type `SortingKeyType`;
- Added a new list of keys `SortingKeys` for the `Modifier.sort()` method;
- Added a new list of entry types `SelectionTypes` for the `Modifier.select()` method;
- Reworked the signature of the `BasicLogger._assemble_entry()` method;
- Added methods to `MightyLogger` that make it easier and more automated to work with the new `Modifier` class:
	- `sort()`;
	- `sort_with_save()`;
	- `search()`;
	- `search_with_save()`;
	- `select()`;
	- `select_with_save()`;
- Created a new package src.lib_types_collection and filled with modules entry_types, environments, sorting_keys, status_variables;
- Renamed `animation` module to `animations`.

---

## Categories update v0.7.2 (28.06.2023)

#### Enhancements:
- Added a new property to `EntryType` - `type_category`;
- Added a new list of entry categories `SelectionCategories` for the `Modifier.select()` method;
- Now, depending on which list element is passed to `Modifier.select()` (`SelectionTypes` or `SelectionCategories`), this method will select entries either by types or by categories;
- The `powerful_logger` module has been renamed to `mighty_logger`.

---

## Export update v0.8.0 (29.06.2023)

#### Enhancements:
- Any references and functionality about status messages are completely cut out from the entire library:
	- Removed module `status_message_type` with nested type (class) `StatusMessageType`;
	- Removed module `status_variables` with nested list of `StatusMessagePatterns`;
	- Arguments that accept a status message have been removed from all methods;
	- In the entry builder (`BasicLogger._assemble_entry()`), the addition of a status message to the entry has been removed;
- Added new `Exporter` class with two methods:
	- `export_to_csv()`, which creates a list of dictionaries from a list of strings;
	- `save()`, which saves the list of dictionaries as a csv table;
- Added `export_to_csv()` method to Logger, which automates work with Exporter;
- Since both Exporter and Modifier divide the string according to certain patterns, I had to prohibit disabling any parts of the entry, otherwise the functionality of these classes becomes inoperative - it was originally designed for the full string (except the status message, which the author never used and decided to delete, as a rudimentary organ, because on the very first prototype, when the Logger was part of another project, it was the entry type that acted for the status message and no one knows why a separate status message was added...);
- Added a new argument to `sort_with_save()`, `search_with_save()`, `select_with_save()` and `export_to_csv()`, through which you can set the name of the file where you want to save the modified/exported logs;
- Moved the `text_buffer` module from the src package to the basic package and hid it from `__init__`, since now there is no need to keep the Buffer object separately due to the presence of new methods in the Logger itself, which provide access to all Buffer methods and, partially, simplify and automate the work with the Buffer;
- Renamed the `patterns` module to `singleton` and hidden from `__init__`, since its use is supposed only inside the library by some classes;
- Added a new MessageException thrown by the entry builder (`BasicLogger._assemble_entry()`) if the message length is less than 10 characters;
- Now it is necessary to enter a message (longer than 10 characters), but it is not necessary to enter the name of the arguments;
- The system of importing standard library packages has been optimized, which will ease the load on RAM when the Logger is running.

---

## Extension update v0.9.0 (29.06.2023)

*On PyPi, it was tested and removed.*

#### Enhancements:
- Moved from `setup.py` to `pyproject.toml`;
- Began to collect `wheel`;

---

## Documenting update v0.9.1 (30.06.2023)

#### Documenting:
- Updated documentation;

---
