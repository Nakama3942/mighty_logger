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
	- [Processes](#processes--available-since-v060-)
		- [Indefinite Processes](#indefinite-processes)
		- [Definite Processes](#definite-processes)
		- [Example using of Processes](#example-using-of-processes)

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
<pre>
<span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span>
<span style='background-color: #;'><span style='color: #b0c4de;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 15:45:03.186454 </span>📌 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #b0c4de;'>Notice data</span></span>
<span style='background-color: #;'><span style='color: #7fff00;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-09 15:45:03.186454 </span>📌 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #7fff00;'>Notice data</span></span>
</pre>

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
<pre>
<span style='background-color: #;'><span style='color: #ffd700;'>-Unknown?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span>
<b><span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span>🐛 <span style='color: #ff8c00;'>... </span><span style='color: #d2b48c;'>logger debugging</span></span></b>
</pre>

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
<pre>
<span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span>
<span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span>
<span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span>
<span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Activated </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span>
<span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:28:45.582804 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Hooray </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span>
</pre>

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
<pre>
<span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span>
<span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span>🐛 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span>
<span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span>🚧 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span>
<span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span>🐞 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Hello world!</span></span>
<span style='background-color: #;'><span style='color: #f5deb3;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span> <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #ffdead;'>%DEBUG PERFORMANCE - </span><span style='color: #f5deb3;'>Hello world!</span></span>
<span style='background-color: #;'><span style='color: #ffe4c4;'>-?entry> </span><span style='color: #da70d6;'>*2023-06-08 17:58:59.773554 </span> <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>... </span><span style='color: #ffebcd;'>%PERFORMANCE - </span><span style='color: #ffe4c4;'>Hello world!</span></span>
</pre>

As you can see, if you create an incomplete set, then entries whose icons are not defined will be displayed without icons. You need to define your own set of icons completely, or use ready-made sets. If the task is to remove the icons completely, you can import an empty set `EmptyIconSet` and use it. Then the icons will not be displayed.

### Processes (available since v0.6.0)
In the Library, you can not only make entries in the Logger, but also launch full-fledged Logger Processes. **If you start a Process, then only that Process can be controlled at that moment and no other entries can be added to the log. However, through the `Logger.note_process()` method, you can add an entry of any type, which will be considered a Process Entry. What's more, two additional entry types are available for this method: ***achievement*** and ***milestone***. DO NOT run multiple Processes!**

It is important to know that there are two types of Processes:
1. [Indefinite](#indefinite-processes)
2. [Definite](#definite-processes)

Process logging has its own entry types:
- *initiation*, denoting the start of the Process;
- *progress* specifying the current state of the Process:
	- *indefinite progress*, playing animation during the execution of the Process;
	- *definite progress*, showing the Progress bar of the Process execution;
- *success* indicating successful execution of the Process;
- *fail*, indicating that the Process failed.

Process logging entry types are protected and only the class itself and inherited ones can access them. Control methods are provided to work with them, the unique *achievement* and *milestone* types, and in general for *managing* the Process. How to manage Processes is described [here](#indefinite-processes) and [here](#definite-processes).

An example of usage will be given at [the end of this section](#example-using-of-processes).

##### Indefinite Processes
Indefinite Process is expressed by the fact that it is not known how to evaluate the completion of the Process. The completion of the Process is indicated only by the receipt of the result and the intermediate Milestones of the Process do not affect the Process itself, more precisely, it is impossible to calculate from them how much the Process has been completed; well, or it consists of only one Milestone.

> It is possible to find out whether the Process is completed only by the result obtained and the intermediate Milestones of the Process (if any) do not affect this (completion calculation).

---

To start an indefinite Process, you need to call the `Logger.start_indefinite_process()` method. It has all the same arguments as regular entry types, but Processes differ in the presence of animation, and therefore it is required to specify it when starting the Process, which is an additional argument. Fortunately, animation is specified by default, and it does not need to be set in this method. The subsequent information that is passed to the method is applied to two entries at once: *initiation* and *indefinite progress*.

**Once a Process has started, DO NOT use the default entry types. Only those methods that are responsible for managing the Process MAY be used. Also, DO NOT create multiple Processes!**

*These restrictions are not contrived and not taken from the ceiling! There are two circumstances that follow from the same cause. The thing is that Process logging uses animation, which for optimization does not use a complete rewriting of the entire output (it is necessary that the output does not blink), but simply rewrites the last string (without overwriting). There is another reason, but it does not affect the circumstances. The Library does not yet implement a wide buffer management functionality and there is no easy controlled access to the buffer, despite the fact that it is possible. It might just break down. And even if it were, it would complicate even more the logic of working with the buffer in the Logger, so the Logger would still work only with the last string. Therefore, if you use the standard method of adding an entry to the log, it will be added to the end of the buffer, after which the streaming animation will overwrite the last string, leaving one of its frames on the penultimate one. To avoid this, the `Logger.note_process()` method was written, which adds an entry using a more complex algorithm. After all, it will not be enough just to add a new entry to the penultimate place - the animation does not overwrite the entire output, but only the last string, therefore all entries will be displayed only after the animation is completed ... For the same reason, you cannot create several Processes, since they will overwrite each other , and the result may be unexpected. Tests were not carried out, the result is not known to the author.*

The `Logger.note_process()` method makes it possible to make any entry to a Process and adds two new entry types: *achievement* and *milestone*. Just like `Logger.start_indefinite_process()`, it has all the standard entry method arguments with an additional method to specify what type of entry to make to the Process. In this case, the new argument is already required.

And finally, to terminate the Process, you need to call the `Logger.stop_process()` method. It no longer has additional methods and focuses on the completion of the Process. It is measured in percentage. In this Library, it is considered that if the Process is completed completely, i.e. 100% - it means that it was completed successfully, however, if the Process could not be completely completed, then the Process failed. This determines the completion of the Process. By default, the Process starts with zero termination. Therefore, if the Process ended unsuccessfully, it is enough to simply call the `Logger.stop_process()` method. If the Process is completed successfully, you need to call `Logger.progress_rise(100)` before this method. More details about this method will be written [here](#definite-processes).

An example of usage will be given at [the end of this section](#example-using-of-processes).

##### Definite Processes
A definite Process differs from an indefinite one in that its completion can be determined not only by the presence/absence of a result, but it is also possible to determine the percentage impact on the execution of the Process by each of its Milestones.

> Knowing which Milestone and how it was completed, you can determine how close the Process has come to its completion.

---

To start an indefinite Process, you need to call the `Logger.start_definite_process()` method. It differs from `Logger.start_indefinite_process()` only in that it accepts a different type of animation - animations of a specific Process (i.e. Progress bars) and outputs *initiation* and *definite progress* entries.

**Once a Process has started, DO NOT use the default entry types. Only those methods that are responsible for managing the Process MAY be used. Also, DO NOT create multiple Processes!**

Further, the Progress entry will no longer display a smooth animation, but a Progress bar with the percentage of the Process completed. As the Process progresses, you need to indicate how complete it is. This is done using the `Logger.progress_rise(int)` method. It indicates how the process is done. The programmer himself must calculate this. For example, if the task is to download 100 files, then after downloading each file, you can add one percent. **It is important to note that this method does not add the specified percentage to the previous value, but sets it.** *Those if the Process was completed by 30% and Progress has advanced by another 2%, then you need to pass not 2, but 32 to the `Logger.progress_rise(int)` method, since after adding 2% to 30%, the current Progress will already be 32%, and when passing 2%, the method will reset the Progress from 30% to 2%!*

Everything is the same as in an indefinite Process, in a definite one you can add any entry of the Process using the `Logger.note_process()` method and terminate it with the `Logger.stop_process()` method (read [the previous section](#indefinite-processes)).

An example of usage will be given at [the end of this section](#example-using-of-processes).

##### Example using of Processes

Here is written an installer simulator-program. Instead of sleep(), some action should be performed that should bring the Process to an end.

```python
from time import sleep

from mighty_logger import Logger
from mighty_logger.src import TypesEntries

if __name__ == "__main__":
	logger = Logger(program_name="Installer", console_width=115, status_message_global_entry=False)

	logger.message(message_text="Program installation started")

	sleep(1)
	logger.start_indefinite_process(message_text="File upload")
	sleep(2)
	logger.note_process(entry_type=TypesEntries.ACHIEVEMENT, message_text="Files downloaded")
	sleep(3)
	logger.progress_rise(100)
	logger.stop_process(message_text="Files unzipped")

	logger.warning(message_text="Newer version found")

	sleep(1)
	logger.start_definite_process(message_text="Installing files")
	sleep(0.6)
	logger.progress_rise(3)
	sleep(0.4)
	logger.progress_rise(7)
	sleep(0.3)
	logger.progress_rise(14)
	sleep(0.5)
	logger.progress_rise(16)
	sleep(1.1)
	logger.progress_rise(19)
	sleep(1.5)
	logger.progress_rise(25)
	sleep(1.4)
	logger.progress_rise(35)
	sleep(1.4)
	logger.progress_rise(45)
	sleep(1.6)
	logger.progress_rise(46)
	sleep(1.1)
	logger.progress_rise(47)
	logger.note_process(entry_type=TypesEntries.MILESTONE, message_text="Files prepared")
	sleep(3.7)
	logger.progress_rise(76)
	sleep(1.5)
	logger.progress_rise(77)
	sleep(1.4)
	logger.progress_rise(79)
	sleep(1.1)
	logger.progress_rise(81)
	sleep(1.2)
	logger.progress_rise(82)
	sleep(1.3)
	logger.progress_rise(85)
	sleep(0.8)
	logger.note_process(entry_type=TypesEntries.ERROR, message_text="Incompatibility found")
	sleep(1.3)
	logger.note_process(entry_type=TypesEntries.RESOLVED, message_text="Incompatibility eliminated")
	sleep(1.1)
	logger.progress_rise(86)
	sleep(0.6)
	logger.progress_rise(87)
	sleep(0.9)
	logger.progress_rise(88)
	sleep(0.9)
	logger.progress_rise(89)
	sleep(0.9)
	logger.progress_rise(90)
	sleep(1.4)
	logger.progress_rise(91)
	sleep(1.8)
	logger.progress_rise(97)
	sleep(1.5)
	logger.progress_rise(100)
	sleep(1.3)
	logger.stop_process(message_text="Program installed")
```

Log:

<pre>
<span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $DESKTOP-8KG0R64^User@Windows:10.0.19045:64bit:WindowsPE:AMD64</span></span>
<span style='background-color: #;'><span style='color: #b0e0e6;'>-?entry>         </span><span style='color: #da70d6;'>*2023-06-14 15:02:43.110952 </span>💬 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #afeeee;'>@MESSAGE - </span><span style='color: #b0e0e6;'>Program installation started</span></span>
<i><span style='background-color: #006400;'><span style='color: #90ee90;'>-?entry> 0:00:00 </span><span style='color: #fff0f5;'>*2023-06-14 15:02:44.112382 </span>🚀 <span style='color: #7fff00;'>#STATUS: </span><span style='color: #98fb98;'>&INITIATION - </span><span style='color: #90ee90;'>File upload</span></span></i>
<span style='background-color: #ffcc00;'><span style='color: #191970;'>-?entry> 0:00:02 </span><span style='color: #8b008b;'>*2023-06-14 15:02:46.113338 </span>🏆 <span style='color: #8b0000;'>#STATUS: </span><span style='color: #000080;'>&ACHIEVEMENT - </span><span style='color: #191970;'>Files downloaded</span></span>
<i><span style='background-color: #006400;'><span style='color: #90ee90;'>-?entry> 0:00:05 </span><span style='color: #fff0f5;'>*2023-06-14 15:02:49.113468 </span>✔️ <span style='color: #7fff00;'>#STATUS: </span><span style='color: #98fb98;'>&SUCCESS - </span><span style='color: #90ee90;'>Files unzipped</span></span></i>
<span style='background-color: #ffcc00;'><span style='color: #191970;'>-?entry>         </span><span style='color: #8b008b;'>*2023-06-14 15:02:49.223684 </span>⚠️ <span style='color: #8b0000;'>#STATUS: </span><span style='color: #000080;'>!WARNING - </span><span style='color: #191970;'>Newer version found</span></span>
<i><span style='background-color: #006400;'><span style='color: #90ee90;'>-?entry> 0:00:00 </span><span style='color: #fff0f5;'>*2023-06-14 15:02:50.224124 </span>🚀 <span style='color: #7fff00;'>#STATUS: </span><span style='color: #98fb98;'>&INITIATION - </span><span style='color: #90ee90;'>Installing files</span></span></i>
<span style='background-color: #006400;'><span style='color: #90ee90;'>-?entry> 0:00:10 </span><span style='color: #fff0f5;'>*2023-06-14 15:03:00.267287 </span>🔖 <span style='color: #7fff00;'>#STATUS: </span><span style='color: #98fb98;'>&MILESTONE - </span><span style='color: #90ee90;'>Files prepared</span></span>
<span style='background-color: #8b0000;'><span style='color: #d3d3d3;'>-?entry> 0:00:21 </span><span style='color: #dda0dd;'>*2023-06-14 15:03:11.355738 </span>❌ <span style='color: #ffa500;'>#STATUS: </span><span style='color: #dcdcdc;'>!!ERROR - </span><span style='color: #d3d3d3;'>Incompatibility found</span></span>
<span style='background-color: #006400;'><span style='color: #90ee90;'>-?entry> 0:00:22 </span><span style='color: #fff0f5;'>*2023-06-14 15:03:12.666348 </span>✅ <span style='color: #7fff00;'>#STATUS: </span><span style='color: #98fb98;'>!RESOLVED - </span><span style='color: #90ee90;'>Incompatibility eliminated</span></span>
<i><span style='background-color: #006400;'><span style='color: #90ee90;'>-?entry> 0:00:32 </span><span style='color: #fff0f5;'>*2023-06-14 15:03:23.164055 </span>✔️ <span style='color: #7fff00;'>#STATUS: </span><span style='color: #98fb98;'>&SUCCESS - </span><span style='color: #90ee90;'>Program installed</span></span></i>
</pre>

*Attention! The program runs for about 40 seconds.*
