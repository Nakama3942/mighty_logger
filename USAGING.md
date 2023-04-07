**USAGING.md is incomplete. The examples may not be valid. The file will be finalized before release.**

## Usage in console (available since v0.2.0)
The library has a complete [X11 color table](#x11-color-table-). However, logger use their [own color tables](#logger-color-chart-) for themselves, where the names of colors are determined not by its real physical name, but by a virtual one formed from the place where this color is used. These tables are initially empty and are initialized when the logger is created. Also, the logger provides the functionality of changing colors in color tables.

*Since the library is under active development, not the best solutions have been applied at this stage, which will be corrected in the future. But at the moment it is NOT RECOMMENDED to name an object of class Logger by the name log!*

Logging is done by the Logger class. To write to the log, you need to call a method with the desired entry type. There are 16 in total: [see section Data/"Entry types"](#entry-types-).

Not only the log itself has settings, but also each type of record. However, the log settings apply to all entries. Therefore, if you need to disable the output of a specific part of the record for a specific type of record, this must be done before each output of this record to the log (i.e., disable the output before writing and turn it back on after the output, so that this part of the information would be displayed for other types). This approach is used only if the part is disabled only for one or more data types.

There are few settings for each entry type. There you can turn on/off only the text format bold/italic/invert(does not support HTML)/background. Also, do not forget to pass the status text (if enabled) and the message text (if enabled) to the record, since the developer himself determines the data to be recorded.

Here is an example using the library:
```python
from qt_colored_logger import Logger

if __name__ == '__main__':
    logger = Logger(program_name="Test", status_message=False)
    print(logger.DEBUG(message_text="Debug data"))
    print(logger.DEBUG(message_text="Debug data", bold=True))
    print(logger.DEBUG(message_text="Debug data", italic=True))
    print(logger.DEBUG(message_text="Debug data", bold=True, italic=True))
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $***************^****@*******:**********:*****:*********:*****</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 15:41:18.616238 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Debug data</span></span><br>
> <b><span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 15:41:18.616238 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Debug data</span></span></b><br>
> <i><span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 15:41:18.616238 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Debug data</span></span></i><br>
> <b><i><span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 15:41:18.616238 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Debug data</span></span></i></b><br>

If you want to change the color of a part of a post, you need to refer to the [logger's color chart](#logger-color-chart-). It contains a table of colors used by the logger. There are 6 colors for each type of record. Their values in the table can be changed by referring to a specific name. To do this, you need to pass the setColor() method (there is an additional setHexColor() in LoggerQ) the color name, the new color value, and the level flags. If you pass True to the foreground flag, the color of the foreground text with/without background will change, depending on the background flag. If background is set to False, the color of the front text will be changed without a background, and if True - with a background. If background is set to True and foreground is set to False - the background color will be set. Be careful - follow the names! It is quite possible to save the background color to the text color and the display may be completely broken. A False-False combination is not possible.

|                  | Foreground level        | Background level   |
|------------------|-------------------------|--------------------|
| Text color       | (..., True, False)      | (..., True, True)  |
| Background color | ~~(..., False, False)~~ | (..., False, True) |

Here is an example of a color change:
```python
from qt_colored_logger import Logger

if __name__ == '__main__':
    logger = Logger(program_name="Test", status_message=False)
    print(logger.NOTICE(message_text="Notice data"))
    logger.set_color(logger_color_name="NOTICE_MESSAGE", color_value=[127, 255, 0], foreground=True, background=False)
    print(logger.NOTICE(message_text="Notice data"))
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $***************^****@*******:**********:*****:*********:*****</span></span><br>
> <span style='background-color: #;'><span style='color: #b0c4de;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:09:39.103436 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #b0c4de;'>Notice data</span></span><br>
> <span style='background-color: #;'><span style='color: #7fff00;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:09:39.103436 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #7fff00;'>Notice data</span></span><br>

This is the simplest example of using the library:
```python
from qt_colored_logger import Logger

if __name__ == "__main__":
	logger = Logger(program_name="Test")
	print(logger.DEBUG(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.DEBUG_PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.EVENT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.AUDIT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.METRICS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.USER(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.MESSAGE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.INFO(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.NOTICE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.WARNING(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.ERROR(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.CRITICAL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	# print(logger.START_PROCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.SUCCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
	print(logger.FAIL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $***************^****@*******:**********:*****:*********:*****</span></span><br>
> <span style='background-color: #;'><span style='color: #d2b48c;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #deb887;'>%DEBUG - </span><span style='color: #d2b48c;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #f5deb3;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #ffdead;'>%DEBUG PERFORMANCE - </span><span style='color: #f5deb3;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #ffe4c4;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #ffebcd;'>%PERFORMANCE - </span><span style='color: #ffe4c4;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #9acd32;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #adff2f;'>~EVENT - </span><span style='color: #9acd32;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #00ff7f;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #00fa9a;'>~AUDIT - </span><span style='color: #00ff7f;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #90ee90;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #98fb98;'>~METRICS - </span><span style='color: #90ee90;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #7cfc00;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #7fff00;'>~USER - </span><span style='color: #7cfc00;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #b0e0e6;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #afeeee;'>@MESSAGE - </span><span style='color: #b0e0e6;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #87ceeb;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #87cefa;'>@INFO - </span><span style='color: #87ceeb;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #;'><span style='color: #b0c4de;'>-?entry> </span><span style='color: #da70d6;'>*2023-04-05 17:17:48.365753 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #add8e6;'>@NOTICE - </span><span style='color: #b0c4de;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #ffcc00;'><span style='color: #191970;'>-?entry> </span><span style='color: #8b008b;'>*2023-04-05 17:17:48.367751 </span><span style='color: #8b0000;'>#STATUS: </span><span style='color: #800000;'>Test text </span><span style='color: #000080;'>!WARNING - </span><span style='color: #191970;'>Test message Test message Test message Test message Test message</span></span><br>
> <span style='background-color: #8b0000;'><span style='color: #d3d3d3;'>-?entry> </span><span style='color: #dda0dd;'>*2023-04-05 17:17:48.367751 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #dcdcdc;'>!!ERROR - </span><span style='color: #d3d3d3;'>Test message Test message Test message Test message Test message</span></span><br>
> <b><span style='background-color: #800000;'><span style='color: #ffa07a;'>-?entry> </span><span style='color: #dda0dd;'>*2023-04-05 17:17:48.367751 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #e9967a;'>!!!@CRITICAL - </span><span style='color: #ffa07a;'>Test message Test message Test message Test message Test message</span></span></b><br>
> <i><span style='background-color: #006400;'><span style='color: #90ee90;'>-?entry> </span><span style='color: #fff0f5;'>*2023-04-05 17:17:48.367751 </span><span style='color: #7fff00;'>#STATUS: </span><span style='color: #7cfc00;'>Test text </span><span style='color: #98fb98;'>&SUCCESS - </span><span style='color: #90ee90;'>Test message Test message Test message Test message Test message</span></span></i><br>
> <i><span style='background-color: #8b0000;'><span style='color: #ffcc00;'>-?entry> </span><span style='color: #fff0f5;'>*2023-04-05 17:17:48.367751 </span><span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Test text </span><span style='color: #ffff00;'>&FAIL - </span><span style='color: #ffcc00;'>Test message Test message Test message Test message Test message</span></span></i><br>

## Usage in Qt (available since v0.0.1)
The difference between the console and Qt is that Qt uses HTML to display formatted text, while the console uses ANSI escape code. However, access to the basic logic is not planned, and the external interface between the Logger/LoggerQ classes is the same (except for the class names themselves). Therefore, all previous examples can be rewritten like this:
```python
from qt_colored_logger import LoggerQ

...

self.logger = LoggerQ(program_name="Test", status_message=False)
self.someTextBrowserObject.append(self.logger.DEBUG(message_text="Debug data"))
self.someTextBrowserObject.append(self.logger.DEBUG(message_text="Debug data", bold=True))
self.someTextBrowserObject.append(self.logger.DEBUG(message_text="Debug data", italic=True))
self.someTextBrowserObject.append(self.logger.DEBUG(message_text="Debug data", bold=True, italic=True))

...
```

```python
from qt_colored_logger import LoggerQ

...

self.logger = LoggerQ(program_name="Test", status_message=False)
self.someTextBrowserObject.append(self.logger.NOTICE(message_text="Notice data"))
self.logger.set_color(logger_color_name="NOTICE_MESSAGE", color_value=[127, 255, 0], foreground=True, background=False)
self.someTextBrowserObject.append(self.logger.NOTICE(message_text="Notice data"))

...
```


```python
from qt_colored_logger import LoggerQ

...

self.logger = LoggerQ(program_name="Test")
self.someTextBrowserObject.append(self.logger.DEBUG(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.DEBUG_PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.EVENT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.AUDIT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.METRICS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.USER(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.MESSAGE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.INFO(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.NOTICE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.WARNING(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.ERROR(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.CRITICAL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
# self.someTextBrowserObject.append(logger.START_PROCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.SUCCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))
self.someTextBrowserObject.append(self.logger.FAIL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message"))

...
```

## Changing colors (available since v0.3.0)
todo Описать, как менять цветовую таблицу

## Text buffer (available since v0.4.0)
todo Описать, как пользоваться текстовым буфером
