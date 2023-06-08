## Applying
Instructions for using the library for practical purposes.

#### Content
- [Applying](#applying)
	- [Content](#content)
	- [Nuts and bolts](#nuts-and-bolts--fully-altered-since-v050-)
	- [Changing colors](#changing-colors--available-since-v030-)
		- [Single change](#single-change)
		- [Base change](#base-change)
	- [Initial opening entry](#initial-opening-entry--available-since-v030-)
	- [Text buffer](#text-buffer--available-since-v040-)
	- [Settings system](#settings-system--available-since-v050-)
    - [Status messages](#status-messages--available-since-v051-)
    - [Icon sets](#icon-sets--available-since-v051-)

### Nuts and bolts (fully altered since v0.5.0)
There are two environments (for now) for which logging can be implemented:
1. Console *(available since v0.2.0)*
2. HTML *(available since v0.0.1)*

Log entries are kept in a text buffer. If the logging environment is Console, then when the update_console() method is called, the program output to the console is completely updated (the main thing is to specify the correct screen width). However, when HTML logging, it is not known where and how to display the text (despite the fact that the library was originally created for logging in Qt - the library does not use this framework at all), so you need to get the text from the buffer and use it manually.

Logging is done by the Logger class. To write to the log, you need to call a method with the desired entry type. There are 16 in total: [see section Data/"Entry types"](/docs/DATA.md#entry-types--and-icon-in-set--).

The fundamental difference between the two logging environments:
```python
# Let's entry the message "Hello world!" to log in console
from mighty_logger import Logger

if __name__ == "__main__":
	# Since the logging environment Console is set by default - you
	# do not need to specify the environment, but you need to configure
	# the buffer - you need to specify the line width - the
	# number of characters that fit in the line + 1.
	logger = Logger(program_name="Test", console_width=115)
	logger.message(message_text="Hello world!")
```

```python
# Let's entry the message "Hello world!" to log in HTML
from mighty_logger import Logger
from mighty_logger.src import LogEnvironments

if __name__ == "__main__":
	# Since the logging environment Console is set by default, the HTML environment
	# must be specified, but now the console width does not need to be specified.
	logger = Logger(program_name="Test", log_environment=LogEnvironments.HTML)
	logger.message(message_text="Hello world!")
	# The library does not provide HTML output to the screen, since
	# it is not known where and how to do this. Therefore, it is easier
	# to just immediately save the buffer to a file and view it in the browser.
	logger.buffer().save("log.html")
	# But, for example, in Qt you can add a widget that will display
	# a log. Let it be a TextBrowser widget. In that case, we can do this:
	# self.someTextBrowserObject.append(self.logger.buffer().get_data()[-1])
```

That's the whole fundamental difference. To summarize: to create a logger in the console, you need to specify the width of the console increased by one, and to create a logger with an HTML log, you need to change the logging environment to `LogEnvironments.HTML` and, apart entering, process the output manually.

### Changing colors (available since v0.3.0)
The library has a complete [X11 color table](/docs/DATA.md#x11-color-table-). However, logger use their [own color tables](/docs/DATA.md#logger-color-scheme-) for themselves, where the names of colors are determined not by its real physical name, but by a virtual one formed from the place where this color is used. These tables are initially empty and are initialized when the logger is created. Also, the logger provides the functionality of [changing colors](#changing-colors--available-since-v030-) in color tables.

##### Single change
If you want to change the color of a part of a post, you need to refer to the [logger's color chart](/docs/DATA.md#logger-color-scheme-). It contains a table of colors used by the logger. There are 6 colors for each type of record. Their values in the table can be changed by referring to a specific name. To do this, you need to pass the setColor() method the color name, the new color value, and the level flags. If you pass True to the foreground flag, the color of the foreground text with/without background will change, depending on the background flag. If background is set to False, the color of the front text will be changed without a background, and if True - with a background. If background is set to True and foreground is set to False - the background color will be set. *Be careful - follow the names! It is quite possible to save the background color to the text color and the display may be completely broken. A False-False combination is not possible.*

|                  | Foreground level        | Background level   |
|------------------|-------------------------|--------------------|
| Text color       | (..., True, False)      | (..., True, True)  |
| Background color | ~~(..., False, False)~~ | (..., False, True) |

Here is an example of a color change:
```python
from mighty_logger import Logger

if __name__ == "__main__":
	logger = Logger(program_name="Test", console_width=115)
	logger.notice(message_text="Notice data")
	logger.set_color(logger_color_name="NOTICE_MESSAGE", color_value=[127, 255, 0], foreground=True, background=False)
	logger.notice(message_text="Notice data")

```

As already mentioned, you need to follow the flags and names, but in practice, the tests did not show anything bad. The background of the line has changed as intended, but in this case the color of the text that was specified loses its color. Simply put - loses color formatting (becomes a standard color). But once again I repeat - it is possible that a situation may occur when the record becomes completely unreadable...

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span><br>
> <span style='background-color: #;'><span style='color: #b0c4de;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 15:45:03.186454 </span>📌 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #b0c4de;'>Notice data</span></span><br>
> <span style='background-color: #;'><span style='color: #7fff00;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 15:45:03.186454 </span>📌 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #7fff00;'>Notice data</span></span><br>

##### Base change
The logger constructor calls the protected _color_scheme_init() method, which is responsible for initializing the logger color table. By overriding the method, you can change the color table or even create it from scratch.

6 colors are assigned to each entry (the sixth one is reserved for the background). Since a color with a background maybe difficult to read, there are two definitions for text color - with a background and without a background. The whole color selection logic is based on this table:

| Parts of the string     |          Foreground           |         Background         |
|:------------------------|:-----------------------------:|:--------------------------:|
| First part of the text  | Text color without background | Text color with background |
| Second part of the text | Text color without background | Text color with background |
| Third part of the text  | Text color without background | Text color with background |
| Fourth part of the text | Text color without background | Text color with background |
| Fifth part of the text  | Text color without background | Text color with background |
| Background              |               -               |      Background color      |

Each entry has its own individual color of the entry message. And the background color is formed according to the color of the entry message.

The entry consists of [5 parts](/README.md#overview). Since each entry has its own individual color of the entry message, therefore each entry has an individual background. And each of the entries may have such a situation that the text of some parts is poorly readable against the background. To avoid this, all colors for each entry are saved separately. Also need to take into account that colors need to be initiated differently for different environments. Because of this, the [color table of the logger](/docs/DATA.md#logger-color-scheme-) is very ~~fat~~ large.

Part of the _color_scheme_init() method code:
```python
match self._environment:
	case LogEnvironments.CONSOLE:
		# DEBUG colors
		self._AnsiColorSet['DEBUG_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
		self._AnsiColorSet['DEBUG_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
		self._AnsiColorSet['DEBUG_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
		self._AnsiColorSet['TYPE_DEBUG'] = [AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")]
		self._AnsiColorSet['DEBUG_MESSAGE'] = [AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
		self._AnsiColorSet['DEBUG_BACKGROUND'] = ["", AnsiColor('TAN', "background")]
	case LogEnvironments.HTML:
		# DEBUG colors
		self._ColorScheme['DEBUG_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
		self._ColorScheme['DEBUG_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
		self._ColorScheme['DEBUG_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
		self._ColorScheme['TYPE_DEBUG'] = [HexColor('BURLYWOOD'), HexColor('NAVY')]
		self._ColorScheme['DEBUG_MESSAGE'] = [HexColor('TAN'), HexColor('MIDNIGHTBLUE')]
		self._ColorScheme['DEBUG_BACKGROUND'] = ["", HexColor('TAN')]
```

The entire code of the _color_scheme_init() method can be found in the sources at [this](https://github.com/Nakama3942/qt_colored_logger/blob/master/qt_colored_logger/logger/colored_logger.py) link.

***Let's move from theory to practice.*** If it is not enough for you to change one color in the color table, and you want to modify all table or completely rewrite it, then you can create your own logger inherited from the Logger class from the library and override the _color_scheme_init() method in it. In the [sources](https://github.com/Nakama3942/qt_colored_logger/blob/master/qt_colored_logger/logger/colored_logger.py) or in the [table](/docs/DATA.md#logger-color-scheme-), you can find the names of all the colors that the Logger class uses. And the above code can serve as an example of exactly how to override a method. It is worth noting that if you will be using only one or a few entry types, then it is enough to define all the colors that use these entry types. However, if you use all types of posts, and you only need to change the colors in some types, then you can call the parent class method that will determine all the colors and then just redefine the colors you need. In this case, all types of entries will be available to you. An example will be given for the second variant of events.

An example of redefining a color table:
```python
from mighty_logger import Logger
from mighty_logger.src import AnsiColor

# I know that I will definitely not use the background in the MESSAGE and INFO entry
# types,so I only override the text colors without the background. Will also be
# console logging, hence the use of the AnsiColor() function.

class MyLogger(Logger):
	def color_scheme_init(self):
		super().color_scheme_init()
		# MESSAGE colors
		self._AnsiColorSet['MESSAGE_TIME'] = [AnsiColor('WHITE', "foreground"), ""]
		self._AnsiColorSet['MESSAGE_STATUS'] = [AnsiColor('WHITE', "foreground"), ""]
		self._AnsiColorSet['MESSAGE_STATUS_MESSAGE'] = [AnsiColor('WHITE', "foreground"), ""]
		self._AnsiColorSet['TYPE_MESSAGE'] = [AnsiColor('WHITE', "foreground"), ""]
		self._AnsiColorSet['MESSAGE_MESSAGE'] = [AnsiColor('WHITE', "foreground"), ""]
		self._AnsiColorSet['MESSAGE_BACKGROUND'] = ["", ""]
		# INFO colors
		self._AnsiColorSet['INFO_TIME'] = [AnsiColor('NAVAJOWHITE', "foreground"), ""]
		self._AnsiColorSet['INFO_STATUS'] = [AnsiColor('NAVAJOWHITE', "foreground"), ""]
		self._AnsiColorSet['INFO_STATUS_MESSAGE'] = [AnsiColor('NAVAJOWHITE', "foreground"), ""]
		self._AnsiColorSet['TYPE_INFO'] = [AnsiColor('NAVAJOWHITE', "foreground"), ""]
		self._AnsiColorSet['INFO_MESSAGE'] = [AnsiColor('NAVAJOWHITE', "foreground"), ""]
		self._AnsiColorSet['INFO_BACKGROUND'] = ["", ""]

if __name__ == "__main__":
	logger = MyLogger(program_name="Test", console_width=115)
	logger.message(message_text="Message data")  # Entry with overridden color
	logger.info(message_text="Info data")  # Entry with overridden color
	logger.notice(message_text="Notice data")  # Entry with default color
```

### Initial opening entry (available since v0.3.0)
Just like color detection, logging starts with an introductory entry that collects system data:
- Computer name
- Username
- System name
- System version
- Computer architecture

However, the _initialized_data() method of the parent class, which is only called from the protected _initial_log() method of the logger, does all this. If you override this method by removing the _initialized_data() call from _initial_log(), then the data will not be collected and the string will not be displayed:
```python
from mighty_logger import Logger

# I remove the initialization string

class MyLogger(Logger):
	def _initial_log(self):
		pass

if __name__ == "__main__":
	logger = MyLogger(program_name="Test", console_width=115)
	logger.message(message_text="Message data")  # Now there is no initialization string before this entry
```

### Text buffer (available since v0.4.0)
A Text Buffer is an area of RAM used to temporarily store text. A buffer can store text as a sequence of characters or bytes. It is typically used to temporarily store text that the user types or copies into an application before it is saved or processed. A buffer can also be used to exchange data between different program components.

In our case, the Text Buffer is a memory area used for temporary storage of text. The buffer stores text as a sequence of characters. Used to store text that represents, mainly in our library, log entries as a list of strings.

A basic text buffer has been implemented, which is slightly more functional than the standard list and a standard text buffer designed for use in the console, as it uses complex logic for calculating the movement of the cursor in console.

By standard, the logger itself creates a buffer, but it can be created earlier. In this case, the logger will simply take a link to an already existing logger.

*If you are creating a console logger or a regular text buffer, you need to specify the width of the console (i.e. the number of characters that fit in one line), increased by one.*

The standard text buffer manually changes the console output, but the basic one does not. But also the base one does not have any buffer display functionality at all. The programmer must manually retrieve the content and form the display.

There are two options for the development of events:
1. First, a buffer is created:
	- Create a buffer (and configure if it's a console one)
    - Create a logger (it will pull up the buffer itself)
2. First, a logger is created:
	- Create a logger (and configure if it is a console one)
    - To get a buffer, use the (3)contents of the (1)logger (2)buffer

```python
# option №1

from mighty_logger.text import TextBuffer
from mighty_logger import Logger

if __name__ == "__main__":
	buf = TextBuffer(115)
	logger = Logger(program_name="Test")
	logger.message(message_text="Message data")  # Text output is automatic
```

```python
# option №2

from mighty_logger.text import BasicTextBuffer
from mighty_logger import Logger

if __name__ == "__main__":
	self.logger = Logger(program_name="Test", log_environment=LogEnvironments.HTML)
	self.logger.message(message_text="Message data")
	self.someTextBrowserObject.append(logger.get_buffer().get_data()[-1])  # Text output is manually
#                                        1        2           3
```

Can also save the contents of the buffer by calling the save() method and passing it the name of the file.

The buffer supports:
- Adding a string
- Inserting a string
- Replacing a string
- ~~Deleting a string~~
- ~~Buffer flush~~
- ~~Reading buffer entries from files~~

Also buffer overrides methods:
- << (used to add a string)
- \>\> (used to save buffer)

An example of using one buffer:
```python
from mighty_logger.text import BasicTextBuffer

if __name__ == "__main__":
	buffer = BasicTextBuffer()
	buffer.append("1")
	buffer.insert(0, "2")
	buffer.replace(1, "3")
	buffer << "4"
	buffer >> "output.txt"
```

Contents of the output.txt file:
```text
2
3
4
```

### Settings system (available since v0.5.0)
With the merging of classes, the system for setting up the logger has been completely changed. It is now possible to configure each entry locally instead of changing the logger settings.

And local settings got their globality. Now you do not need to specify, for example, italic font in each entry.

Global settings are passed to the constructor separately for each argument. Local settings are formatted as a dictionary, which is passed to the `local_settings` argument. All global settings arguments and local settings dictionary keys can be found [here](/docs/DATA.md#settings-).

Here is an example of setting up a logger and recording:
```python
from mighty_logger import Logger
from mighty_logger.src import LogEnvironments

if __name__ == "__main__":
	logger = Logger(log_environment=LogEnvironments.HTML, status_global_entry=False)
	logger.debug(message_text="logger debugging", local_settings={"status_type_local_entry": False, "time_local_entry": False, "bold": True})
	logger.buffer() >> "log.html"
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Unknown?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span><br>
> <b><span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span>🐛 <span style='color: #ff8c00;'>... </span><span style='color: #d2b48c;'>logger debugging</span></span></b><br>

### Status messages (available since v0.5.1)
In v0.5.1, the understanding of the "status message" has been changed. Now this is not an ordinary string, but a full-fledged data type. Status message output is enabled by default, but it's not covered how to use it due to a change in v0.5.1. If no status message is specified, an empty message (which contains an ellipsis) will be displayed. Whatever the ellipsis is not displayed - you need to turn off its output either in the global or in the local settings.

However, there may be a situation where you need to enter a status message. To do this, you need to use the Status Message Template. There are 46 templates in total (excluding empty and custom ones).

All possible options for working with status message templates (for comparison):
```python
from mighty_logger import Logger
from mighty_logger.src import LogEnvironments
from mighty_logger.src import StatusMessagePatterns

if __name__ == "__main__":
	logger = Logger(program_name="Test", log_environment=LogEnvironments.HTML)
	logger.debug(message_text="Hello world!")
	logger.debug(message_text="Hello world!", local_settings={"status_message_local_entry": False})
	logger.debug(status_message=StatusMessagePatterns.activated(), message_text="Hello world!")
	logger.debug(status_message=StatusMessagePatterns.custom("Hooray"), message_text="Hello world!")
	logger.buffer().save("log.html", False)
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Activated </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Hooray </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span><br>

### Icon sets (available since v0.5.1)
Also in v0.5.1, in addition to changing the status message, icons were added. In fact, these are ordinary UTF8 emoticons, but you can quickly understand the type of post from them without reading the type itself or determining the color of the entry message (that's why the icon).

The library provides as many as four icon sets, but you can make your own set by inheriting from the icon set type.

By default, the first set is used, but you can import and transfer to the Logger another set from the library.

```python
from mighty_logger import Logger
from mighty_logger.src import LogEnvironments
from mighty_logger.text import IconSetType, IconSet3

class MyIconSet(IconSetType):
	debug = '🐞'
	debug_performance = ''

if __name__ == "__main__":
	logger = Logger(program_name="Test", log_environment=LogEnvironments.HTML)
	logger.debug(message_text="Hello world!")
	logger.set_icons(IconSet3())
	logger.debug(message_text="Hello world!")
	logger.set_icons(MyIconSet())
	logger.debug(message_text="Hello world!")
	logger.debug_performance(message_text="Hello world!")
	logger.performance(message_text="Hello world!")
	logger.buffer().save("log.html")
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span>🚧 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span>🐞 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span><br>
> <span style='background-color: #;'><span style='color: #f5deb3;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span> <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #ffdead;'>%DEBUG PERFORMANCE - </span><span style='color: #f5deb3;'>Hello world!</span></span><br>
> <span style='background-color: #;'><span style='color: #ffe4c4;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span> <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #ffebcd;'>%PERFORMANCE - </span><span style='color: #ffe4c4;'>Hello world!</span></span><br>

As you can see, if you create an incomplete set, then entries whose icons are not defined will be displayed without icons. You need to define your own set of icons completely, or use ready-made sets. If the task is to remove the icons completely, you can import an empty set `EmptyIconSet` and use it. Then the icons will not be displayed.
