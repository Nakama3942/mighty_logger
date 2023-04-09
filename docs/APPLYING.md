## Applying
Instructions for using the library for practical purposes.

#### Content
- [Applying](#applying)
	- [Content](#content)
    - [Usage in console](#usage-in-console--available-since-v020-)
    - [Usage in Qt](#usage-in-qt--available-since-v001-)
    - [Changing colors](#changing-colors--available-since-v030-)
    - [Initial opening entry](#initial-opening-entry--available-since-v030-)
    - [Text buffer](#text-buffer--available-since-v040-)

### Usage in console (available since v0.2.0)
The library has a complete [X11 color table](/docs/DATA.md#x11-color-table-). However, logger use their [own color tables](/docs/DATA.md#logger-color-scheme-) for themselves, where the names of colors are determined not by its real physical name, but by a virtual one formed from the place where this color is used. These tables are initially empty and are initialized when the logger is created. Also, the logger provides the functionality of [changing colors](#changing-colors--available-since-v030-) in color tables.

Logging is done by the Logger class. To write to the log, you need to call a method with the desired entry type. There are 16 in total: [see section Data/"Entry types"](/docs/DATA.md#entry-types-).

Not only the log itself has settings, but also each type of record. However, the log settings apply to all entries. Therefore, if you need to disable the output of a specific part of the record for a specific type of record, this must be done before each output of this record to the log (i.e., disable the output before writing and turn it back on after the output, so that this part of the information would be displayed for other types). This approach is used only if the part is disabled only for one or more data types. If a part needs to be turned off on a permanent basis, then it is not necessary to turn it on. You can turn the output on and off during the logging process:
```python
from qt_colored_logger.text import TextBuffer
from qt_colored_logger.logger import Logger

if __name__ == '__main__':
	buf = TextBuffer(115)
	logger = Logger(text_buffer=buf)
	logger.time = False  # Just for example
```

There are few settings for each entry type. There you can turn on/off only the text format bold/italic/invert(does not support HTML)/background. Also, do not forget to pass the status text (if enabled) and the message text (if enabled) to the record, since the developer himself determines the data to be recorded.

Here is an example using the library:
```python
from qt_colored_logger.text import TextBuffer
from qt_colored_logger.logger import Logger

if __name__ == "__main__":
	buf = TextBuffer(115)
	logger = Logger(program_name="Test", text_buffer=buf, status_message=False)
	logger.MESSAGE(message_text="Message data")
	logger.MESSAGE(message_text="Message data", bold=True)
	logger.MESSAGE(message_text="Message data", italic=True)
	logger.MESSAGE(message_text="Message data", bold=True, italic=True)
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span><br>
> <span style='background-color: #;'><span style='color: #b0e0e6;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 14:47:00.330936 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #afeeee;'>@MESSAGE - </span><span style='color: #b0e0e6;'>Message data</span></span><br>
> <b><span style='background-color: #;'><span style='color: #b0e0e6;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 14:47:00.330936 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #afeeee;'>@MESSAGE - </span><span style='color: #b0e0e6;'>Message data</span></span></b><br>
> <i><span style='background-color: #;'><span style='color: #b0e0e6;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 14:47:00.330936 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #afeeee;'>@MESSAGE - </span><span style='color: #b0e0e6;'>Message data</span></span></i><br>
> <b><i><span style='background-color: #;'><span style='color: #b0e0e6;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 14:47:00.330936 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #afeeee;'>@MESSAGE - </span><span style='color: #b0e0e6;'>Message data</span></span></i></b><br>

If you want to change the color of a part of a post, you need to refer to the [logger's color chart](/docs/DATA.md#logger-color-scheme-). It contains a table of colors used by the logger. There are 6 colors for each type of record. Their values in the table can be changed by referring to a specific name. To do this, you need to pass the setColor() method (there is an additional setHexColor() in LoggerQ) the color name, the new color value, and the level flags. If you pass True to the foreground flag, the color of the foreground text with/without background will change, depending on the background flag. If background is set to False, the color of the front text will be changed without a background, and if True - with a background. If background is set to True and foreground is set to False - the background color will be set. Be careful - follow the names! It is quite possible to save the background color to the text color and the display may be completely broken. A False-False combination is not possible.

|                  | Foreground level        | Background level   |
|------------------|-------------------------|--------------------|
| Text color       | (..., True, False)      | (..., True, True)  |
| Background color | ~~(..., False, False)~~ | (..., False, True) |

Here is an example of a color change:
```python
from qt_colored_logger.text import TextBuffer
from qt_colored_logger.logger import Logger

if __name__ == "__main__":
	buf = TextBuffer(115)
	logger = Logger(program_name="Test", text_buffer=buf, status_message=False)
	logger.NOTICE(message_text="Notice data")
	logger.set_color(logger_color_name="NOTICE_MESSAGE", color_value=[127, 255, 0], foreground=True, background=False)
	logger.NOTICE(message_text="Notice data")

```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span><br>
> <span style='background-color: #;'><span style='color: #b0c4de;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 15:45:03.186454 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #b0c4de;'>Notice data</span></span><br>
> <span style='background-color: #;'><span style='color: #7fff00;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 15:45:03.186454 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #7fff00;'>Notice data</span></span><br>

### Usage in Qt (available since v0.0.1)
The difference between the console and Qt is that Qt uses HTML to display formatted text, while the console uses ANSI escape codes. However, access to the basic logic is not planned, and the external interface between the Logger/LoggerQ classes is the same (except for the class names themselves). Therefore, all previous examples can be rewritten like this:
```python
from qt_colored_logger.logger import LoggerQ

...

self.logger = Logger()
self.logger.time = False  # Just for example

...
```

```python
from qt_colored_logger.logger import LoggerQ

...

self.logger = LoggerQ(program_name="Test")
self.logger.MESSAGE(status_message_text="OK", message_text="Outputting the message")
self.someTextBrowserObject.setText('\n'.join(self.logger.get_buffer().get_data()))

...
```

```python
from qt_colored_logger.logger import LoggerQ

...

self.logger = LoggerQ(program_name="Test", status_message=False)
self.logger.MESSAGE(message_text="Message data")
self.logger.MESSAGE(message_text="Message data", bold=True)
self.logger.MESSAGE(message_text="Message data", italic=True)
self.logger.MESSAGE(message_text="Message data", bold=True, italic=True)
self.someTextBrowserObject.setText('\n'.join(self.logger.get_buffer().get_data()))

...
```

```python
from qt_colored_logger import LoggerQ

...

self.logger = LoggerQ(program_name="Test", status_message=False)
self.logger.NOTICE(message_text="Notice data")
self.logger.set_color(logger_color_name="NOTICE_MESSAGE", color_value=[127, 255, 0], foreground=True, background=False)
self.logger.NOTICE(message_text="Notice data")
self.someTextBrowserObject.append('\n'.join(self.logger.get_buffer().get_data()))

...
```

### Changing colors (available since v0.3.0)
The logger constructor calls the protected _ansi_color_set_init() method, which is responsible for initializing the logger color table. By overriding the method, you can change the color table or even create it from scratch.

6 colors are assigned to each entry (the sixth one is reserved for the background). Since a color with a background maybe difficult to read, there are two definitions for text color - with a background and without a background. The whole color selection logic is based on this table:

| Parts of the string     |          Foreground           |         Background         |
|:------------------------|:-----------------------------:|:--------------------------:|
| First part of the text  | Text color without background | Text color with background |
| Second part of the text | Text color without background | Text color with background |
| Third part of the text  | Text color without background | Text color with background |
| Fourth part of the text | Text color without background | Text color with background |
| fifth part of the text  | Text color without background | Text color with background |
| Background              |               -               |      Background color      |

Each entry has its own individual color of the entry message. And the background color is formed according to the color of the entry message.

The entry consists of [5 parts](/README.md#overview). Since each entry has its own individual color of the entry message, therefore each entry has an individual background. And each of the entries may have such a situation that the text of some parts is poorly readable against the background. To avoid this, all colors for each entry are saved separately. Because of this, the [color table of the logger](/docs/DATA.md#logger-color-scheme-) is very ~~fat~~ large.

Part of the _ansi_color_set_init() method code:
```python
# DEBUG colors
self._AnsiColorSet['DEBUG_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
self._AnsiColorSet['DEBUG_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
self._AnsiColorSet['DEBUG_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
self._AnsiColorSet['TYPE_DEBUG'] = [AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")]
self._AnsiColorSet['DEBUG_MESSAGE'] = [AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
self._AnsiColorSet['DEBUG_BACKGROUND'] = ["", AnsiColor('TAN', "background")]
```

The entire code of the _ansi_color_set_init() method can be found in the sources at [this](https://github.com/Nakama3942/qt_colored_logger/blob/master/qt_colored_logger/logger/colored_logger.py) link.

***Let's move from theory to practice.*** If it is not enough for you to change one color in the color table, and you want to modify all table or completely rewrite it, then you can create your own logger inherited from the Logger class from the library and override the _ansi_color_set_init() method in it. In the [sources](https://github.com/Nakama3942/qt_colored_logger/blob/master/qt_colored_logger/logger/colored_logger.py) or in the [table](/docs/DATA.md#logger-color-scheme-), you can find the names of all the colors that the Logger class uses. And the above code can serve as an example of exactly how to override a method. It is worth noting that if you will be using only one or a few entry types, then it is enough to define all the colors that use these entry types. However, if you use all types of posts, and you only need to change the colors in some types, then you can call the parent class method that will determine all the colors and then just redefine the colors you need. In this case, all types of entries will be available to you. An example will be given for the second variant of events.

An example of redefining a color table:
```python
from qt_colored_logger.text import TextBuffer
from qt_colored_logger.logger import Logger
from qt_colored_logger.src import AnsiColor

# I know that I will definitely not use the background in the MESSAGE and INFO entry
# types,so I only override the text colors without the background.

class MyLogger(Logger):
	def _ansi_color_set_init(self):
		super()._ansi_color_set_init()
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
	buf = TextBuffer(115)
	logger = MyLogger(program_name="Test", text_buffer=buf, status_message=False)
	logger.MESSAGE(message_text="Message data")  # Entry with overridden color
	logger.INFO(message_text="Info data")  # Entry with overridden color
	logger.NOTICE(message_text="Notice data")  # Entry with default color
```

All the same actions can be performed with the HTML logger. It is enough to replace:
- TextBuffer -> BasicTextBuffer
- Logger -> LoggerQ
- _AnsiColorSet -> _HtmlColorSet
- AnsiColor -> HexColor

### Initial opening entry (available since v0.3.0)
Just like color detection, logging starts with an introductory entry that collects system data:
- Computer name
- Username
- System name
- System version
- Computer architecture

However, the _initialized_data() method of the parent class, which is only called from the protected _initial_log() method of the logger, does all this. If you override this method by removing the _initialized_data() call, then the data will not be collected and the string will not be displayed:
```python
from qt_colored_logger.text import TextBuffer
from qt_colored_logger.logger import Logger

# I remove the initialization string

class MyLogger(Logger):
	def _initial_log(self):
		pass

if __name__ == "__main__":
	buf = TextBuffer(115)
	logger = MyLogger(program_name="Test", text_buffer=buf, status_message=False)
	logger.MESSAGE(message_text="Message data")  # Now there is no initialization string before this entry
```

All the same actions can be performed with the HTML logger. It is enough to replace:
- TextBuffer -> BasicTextBuffer
- Logger -> LoggerQ

### Text buffer (available since v0.4.0)
A Text Buffer is an area of RAM used to temporarily store text. A buffer can store text as a sequence of characters or bytes. It is typically used to temporarily store text that the user types or copies into an application before it is saved or processed. A buffer can also be used to exchange data between different program components.

In our case, the Text Buffer is a memory area used for temporary storage of text. The buffer stores text as a sequence of characters. Used to store text that represents, mainly in our library, log entries as a list of strings.

A basic text buffer has been implemented, which is slightly more functional than the standard list and a standard text buffer designed for use in the console, as it uses complex logic for calculating the movement of the console cursor.

The logger needs a buffer, otherwise where will it write to? If you do not pass a buffer to the logger, it will create it itself with standard settings, and the console width is included in the standard text buffer setting.

The standard text buffer manually changes the console output, but the basic one does not. But also the base one does not have any buffer display functionality at all. The programmer must manually retrieve the content and form the display.

There are two options for working with the buffer:
1. Working with standard text buffer (assuming console buffer is used):
	- Create a text buffer and customize it
    - Pass buffer to logger
2. Working with a basic text buffer (assuming an HTML buffer is used):
	- Create a logger (it will create a buffer itself)
    - When generating output, use the (3)contents of the (1)logger (2)buffer

```python
# option №1

from qt_colored_logger.text import TextBuffer
from qt_colored_logger.logger import Logger

if __name__ == "__main__":
	buf = TextBuffer(115)
	logger = Logger(program_name="Test", text_buffer=buf)
	logger.MESSAGE(message_text="Message data")  # Text output is automatic
```

```python
# option №2

from qt_colored_logger.text import BasicTextBuffer
from qt_colored_logger.logger import LoggerQ

...

self.logger = LoggerQ(program_name="Test")
self.logger.MESSAGE(message_text="Message data")
self.someTextBrowserObject.append('\n'.join(logger.get_buffer().get_data()))  # Text output is manually
#                                              1        2           3
...
```

You can also save the contents of the buffer by calling the save() method and passing it the name of the file.

The buffer supports:
- Adding a string
- Inserting a string
- Replacing a string

Also buffer overrides methods:
- << (used to add a string)
- \>\> (used to save buffer)

An example of using one buffer:
```python
from qt_colored_logger.text import BasicTextBuffer

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
