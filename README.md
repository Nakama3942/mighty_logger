[![template](https://img.shields.io/badge/Repository-template-darkred)](https://github.com/Nakama3942/template_rep)
[![GitHub license](https://img.shields.io/github/license/Nakama3942/qt_colored_logger?color=gold&style=flat-square)](https://github.com/Nakama3942/qt_colored_logger/blob/master/LICENSE)

[![CHANGELOG](https://img.shields.io/badge/here-CHANGELOG-yellow)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CHANGELOG.md)
[![CONTRIBUTING](https://img.shields.io/badge/here-CONTRIBUTING-indigo)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CONTRIBUTING.md)
[![CODE_OF_CONDUCT](https://img.shields.io/badge/here-CODE_OF_CONDUCT-darkgreen)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CODE_OF_CONDUCT.md)
[![PULL_REQUEST_TEMPLATE](https://img.shields.io/badge/here-PULL_REQUEST_TEMPLATE-orange)](https://github.com/Nakama3942/qt_colored_logger/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

# Qt_Сolored-logger
## Content
- [Qt_Сolored-logger](#qtсolored-logger)
    - [Content](#content)
    - [Preamble](#preamble)
    - [Overview](#overview)
    - [LICENSE](#license)
    - [Installation](#installation)
    - [Usage in console](#usage-in-console)
    - [Usage in Qt](#usage-in-qt)
    - [Additional functionality](#additional-functionality)
    - [Data](#data)
        - [Entry types](#entry-types-)
        - [X11 color table](#x11-color-table-)
        - [Logger Color Chart](#logger-color-chart-)
        - [Tree of ANSI escape code](#tree-of-ansi-escape-code-)
    - [Troubleshooting](#troubleshooting)
    - [Authors](#authors)

## Preamble
I often came across the opinion that it is better to use not standard output to the console, but full-fledged logging... However, the standard libraries do not provide exactly what I need... Therefore, I decided to make my own library! Which will implement the functionality I need.

- [Content](#content)

## Overview
The library implements the formation of a beautifully formatted colored text, similar to a log, which has all the necessary information:
- Device name and registered profile, system name, etc. (this data is displayed only once at the beginning of the logging)
- Log entry time
- Log entry status
- Description of the log entry status
- Log entry type
- Entry message

Any information to the output can be turned off (according to the standard, everything is included). It is also possible to change the output settings during the logging process. It is possible to change the colors of the foreground text and the background.

- [Content](#content)

## LICENSE
The full text of the license can be found at the following [link](https://github.com/Nakama3942/qt_colored_logger/blob/master/LICENSE).

> Copyright © 2023 Kalynovsky Valentin. All rights reserved.
> 
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
> 
>     http://www.apache.org/licenses/LICENSE-2.0
> 
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and

- [Content](#content)

## Installation
Despite the fact that the library was originally developed for use in PyQt, it does not require PyQt to be installed, since this framework for outputting to Text fields, which support not only Plain Text, uses HTML and this library simply simplifies the logging process, since the creation process already formatted strings is registered in this library.

*However, it is possible that this will be changed in the future, as the plans are to implement not just the formation of formatted strings, but to fully control the text flow in the console or text fields.*

To install the library, enter the command:
```sh
pip install qt-colored-logger
```

## Usage in console
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
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $DESKTOP-8KG0R64^User@Windows:10.0.19045:64bit:WindowsPE:AMD64</span></span><br>
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
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $DESKTOP-8KG0R64^User@Windows:10.0.19045:64bit:WindowsPE:AMD64</span></span><br>
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
> <span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $DESKTOP-8KG0R64^User@Windows:10.0.19045:64bit:WindowsPE:AMD64</span></span><br>
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

## Usage in Qt
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

## *Additional functionality*
*Additional functionality is also planned. Let's keep it a secret for now. Let it be a surprise.*

- [Content](#content)

## Data
The library stores various important data for use that you may need to know while using the library.

###### Entry types:
- DEBUG
- DEBUG_PERFORMANCE
- PERFORMANCE
- EVENT
- AUDIT
- METRICS
- USER
- MESSAGE
- INFO
- NOTICE
- WARNING
- ERROR
- CRITICAL
- ~~PROGRESS~~ (*not implemented because the non-implemented START_PROCESS and STOP_PROCESS methods control this type*)
- SUCCESS
- FAIL

###### X11 color table:
- Red category:
    - MAROON
    - DARKRED
    - RED
    - LIGHTRED
    - FIREBRICK
    - CRIMSON
    - INDIANRED
    - LIGHTCORAL
    - SALMON
    - DARKSALMON
    - LIGHTSALMON
- Pink category:
    - MEDIUMVIOLETRED
    - DEEPPINK
    - PALEVIOLETRED
    - HOTPINK
    - LIGHTPINK
    - PINK
- Orange category:
    - ORANGERED
    - TOMATO
    - DARKORANGE
    - CORAL
    - ORANGE
- Yellow category:
    - DARKKHAKI
    - GOLD
    - KHAKI
    - PEACHPUFF
    - YELLOW
    - DARKYELLOW
    - PALEGOLDENROD
    - MOCCASIN
- Purple category:
    - INDIGO
    - PURPLE
    - DARKMAGENTA
    - DARKVIOLET
    - DARKSLATEBLUE
    - BLUEVIOLET
    - DARKORCHID
    - FUCHSIA
    - SLATEBLUE
    - MEDIUMSLATEBLUE
    - MEDIUMORCHID
    - MEDIUMPURPLE
    - ORCHID
    - VIOLET
    - PLUM
    - THISTLE
    - LAVENDER
- Green category:
    - DARKGREEN
    - GREEN
    - DARKOLIVEGREEN
    - FORESTGREEN
    - SEAGREEN
    - DARKSLATEGRAY
    - OLIVE
    - OLIVEDRAB
    - MEDIUMSEAGREEN
    - LIMEGREEN
    - LIME
    - SPRINGGREEN
    - MEDIUMSPRINGGREEN
    - DARKSEAGREEN
    - MEDIUMAQUAMARINE
    - YELLOWGREEN
    - LAWNGREEN
    - CHARTREUSE
    - LIGHTGREEN
    - GREENYELLOW
    - PALEGREEN
- Aqua category:
    - TEAL
    - DARKCYAN
    - LIGHTSEAGREEN
    - CADETBLUE
    - DARKTURQUOISE
    - MEDIUMTURQUOISE
    - TURQUOISE
    - AQUA
    - AQUAMARINE
    - SKYBLUE
    - LIGHTSKYBLUE
    - LIGHTSTEELBLUE
    - LIGHTBLUE
    - POWDERBLUE
    - PALETURQUOISE
- Blue category:
    - MIDNIGHTBLUE
    - NAVY
    - DARKBLUE
    - MEDIUMBLUE
    - BLUE
    - ROYALBLUE
    - STEELBLUE
    - DODGERBLUE
    - DEEPSKYBLUE
    - CORNFLOWERBLUE
- Brown category:
    - BROWN
    - SADDLEBROWN
    - SIENNA
    - CHOCOLATE
    - DARKGOLDENROD
    - PERU
    - ROSYBROWN
    - GOLDENROD
    - SANDYBROWN
    - TAN
    - BURLYWOOD
    - WHEAT
    - NAVAJOWHITE
    - BISQUE
    - BLANCHEDALMOND
- White category:
    - WHITE
    - SNOW
    - HONEYDEW
    - MINTCREAM
    - AZURE
    - LIGHTCYAN
    - ALICEBLUE
    - GHOSTWHITE
    - WHITESMOKE
    - SEASHELL
    - BEIGE
    - OLDLACE
    - FLORALWHITE
    - IVORY
    - ANTIQUEWHITE
    - LINEN
    - LAVENDERBLUSH
    - MISTYROSE
    - PAPAYAWHIP
    - LIGHTGOLDENRODYELLOW
    - CORNSILK
    - LEMONCHIFFON
    - LIGHTYELLOW
- Gray and black category:
    - BLACK
    - DARKGRAY
    - DIMGRAY
    - SLATEGRAY
    - GRAY
    - LIGHTSLATEGRAY
    - SILVER
    - LIGHTGRAY
    - GAINSBORO

###### Logger Color Chart:
| Color name                        | Foreground color  | Background color |
|-----------------------------------|-------------------|------------------|
| INITIAL_COLOR                     | GOLD              | INDIGO           |
| INITIAL_BACKGROUND                | -                 | GOLD             |
| DEBUG_TIME                        | ORCHID            | DARKMAGENTA      |
| DEBUG_STATUS                      | ORANGE            | DARKRED          |
| DEBUG_STATUS_MESSAGE              | DARKORANGE        | MAROON           |
| TYPE_DEBUG                        | BURLYWOOD         | NAVY             |
| DEBUG_MESSAGE                     | TAN               | MIDNIGHTBLUE     |
| DEBUG_BACKGROUND                  | -                 | TAN              |
| DEBUG_PERFORMANCE_TIME            | ORCHID            | DARKMAGENTA      |
| DEBUG_PERFORMANCE_STATUS          | ORANGE            | DARKRED          |
| DEBUG_PERFORMANCE_STATUS_MESSAGE  | DARKORANGE        | MAROON           |
| TYPE_DEBUG_PERFORMANCE            | NAVAJOWHITE       | NAVY             |
| DEBUG_PERFORMANCE_MESSAGE         | WHEAT             | MIDNIGHTBLUE     |
| DEBUG_PERFORMANCE_BACKGROUND      | -                 | WHEAT            |
| PERFORMANCE_TIME                  | ORCHID            | DARKMAGENTA      |
| PERFORMANCE_STATUS                | ORANGE            | DARKRED          |
| PERFORMANCE_STATUS_MESSAGE        | DARKORANGE        | MAROON           |
| TYPE_PERFORMANCE                  | BLANCHEDALMOND    | NAVY             |
| PERFORMANCE_MESSAGE               | BISQUE            | MIDNIGHTBLUE     |
| PERFORMANCE_BACKGROUND            | -                 | BISQUE           |
| EVENT_TIME                        | ORCHID            | DARKMAGENTA      |
| EVENT_STATUS                      | ORANGE            | DARKRED          |
| EVENT_STATUS_MESSAGE              | DARKORANGE        | MAROON           |
| TYPE_EVENT                        | GREENYELLOW       | NAVY             |
| EVENT_MESSAGE                     | YELLOWGREEN       | MIDNIGHTBLUE     |
| EVENT_BACKGROUND                  | -                 | YELLOWGREEN      |
| AUDIT_TIME                        | ORCHID            | DARKMAGENTA      |
| AUDIT_STATUS                      | ORANGE            | DARKRED          |
| AUDIT_STATUS_MESSAGE              | DARKORANGE        | MAROON           |
| TYPE_AUDIT                        | MEDIUMSPRINGGREEN | NAVY             |
| AUDIT_MESSAGE                     | SPRINGGREEN       | MIDNIGHTBLUE     |
| AUDIT_BACKGROUND                  | -                 | SPRINGGREEN      |
| METRICS_TIME                      | ORCHID            | DARKMAGENTA      |
| METRICS_STATUS                    | ORANGE            | DARKRED          |
| METRICS_STATUS_MESSAGE            | DARKORANGE        | MAROON           |
| TYPE_METRICS                      | PALEGREEN         | NAVY             |
| METRICS_MESSAGE                   | LIGHTGREEN        | MIDNIGHTBLUE     |
| METRICS_BACKGROUND                | -                 | LIGHTGREEN       |
| USER_TIME                         | ORCHID            | DARKMAGENTA      |
| USER_STATUS                       | ORANGE            | DARKRED          |
| USER_STATUS_MESSAGE               | DARKORANGE        | MAROON           |
| TYPE_USER                         | CHARTREUSE        | NAVY             |
| USER_MESSAGE                      | LAWNGREEN         | MIDNIGHTBLUE     |
| USER_BACKGROUND                   | -                 | LAWNGREEN        |
| MESSAGE_TIME                      | ORCHID            | DARKMAGENTA      |
| MESSAGE_STATUS                    | ORANGE            | DARKRED          |
| MESSAGE_STATUS_MESSAGE            | DARKORANGE        | MAROON           |
| TYPE_MESSAGE                      | PALETURQUOISE     | NAVY             |
| MESSAGE_MESSAGE                   | POWDERBLUE        | MIDNIGHTBLUE     |
| MESSAGE_BACKGROUND                | -                 | POWDERBLUE       |
| INFO_TIME                         | ORCHID            | DARKMAGENTA      |
| INFO_STATUS                       | ORANGE            | DARKRED          |
| INFO_STATUS_MESSAGE               | DARKORANGE        | MAROON           |
| TYPE_INFO                         | LIGHTSKYBLUE      | NAVY             |
| INFO_MESSAGE                      | SKYBLUE           | MIDNIGHTBLUE     |
| INFO_BACKGROUND                   | -                 | SKYBLUE          |
| NOTICE_TIME                       | ORCHID            | DARKMAGENTA      |
| NOTICE_STATUS                     | ORANGE            | DARKRED          |
| NOTICE_STATUS_MESSAGE             | DARKORANGE        | MAROON           |
| TYPE_NOTICE                       | LIGHTBLUE         | NAVY             |
| NOTICE_MESSAGE                    | LIGHTSTEELBLUE    | MIDNIGHTBLUE     |
| NOTICE_BACKGROUND                 | -                 | LIGHTSTEELBLUE   |
| WARNING_TIME                      | ORCHID            | DARKMAGENTA      |
| WARNING_STATUS                    | ORANGE            | DARKRED          |
| WARNING_STATUS_MESSAGE            | DARKORANGE        | MAROON           |
| TYPE_WARNING                      | YELLOW            | NAVY             |
| WARNING_MESSAGE                   | DARKYELLOW        | MIDNIGHTBLUE     |
| WARNING_BACKGROUND                | -                 | DARKYELLOW       |
| ERROR_TIME                        | ORCHID            | PLUM             |
| ERROR_STATUS                      | ORANGE            | ORANGE           |
| ERROR_STATUS_MESSAGE              | DARKORANGE        | DARKORANGE       |
| TYPE_ERROR                        | FIREBRICK         | GAINSBORO        |
| ERROR_MESSAGE                     | DARKRED           | LIGHTGRAY        |
| ERROR_BACKGROUND                  | -                 | DARKRED          |
| CRITICAL_TIME                     | ORCHID            | PLUM             |
| CRITICAL_STATUS                   | ORANGE            | ORANGE           |
| CRITICAL_STATUS_MESSAGE           | DARKORANGE        | DARKORANGE       |
| TYPE_CRITICAL                     | FIREBRICK         | DARKSALMON       |
| CRITICAL_MESSAGE                  | DARKRED           | LIGHTSALMON      |
| CRITICAL_BACKGROUND               | -                 | MAROON           |
| PROGRESS_TIME                     | ORCHID            | PURPLE           |
| PROGRESS_STATUS                   | ORANGE            | DARKRED          |
| PROGRESS_STATUS_MESSAGE           | DARKORANGE        | MAROON           |
| TYPE_PROGRESS                     | LIGHTSKYBLUE      | NAVY             |
| PROGRESS_MESSAGE                  | SKYBLUE           | MIDNIGHTBLUE     |
| PROGRESS_BACKGROUND               | -                 | SKYBLUE          |
| SUCCESS_TIME                      | ORCHID            | LAVENDERBLUSH    |
| SUCCESS_STATUS                    | ORANGE            | CHARTREUSE       |
| SUCCESS_STATUS_MESSAGE            | DARKORANGE        | LAWNGREEN        |
| TYPE_SUCCESS                      | GREEN             | PALEGREEN        |
| SUCCESS_MESSAGE                   | DARKGREEN         | LIGHTGREEN       |
| SUCCESS_BACKGROUND                | -                 | DARKGREEN        |
| FAIL_TIME                         | ORCHID            | LAVENDERBLUSH    |
| FAIL_STATUS                       | ORANGE            | ORANGE           |
| FAIL_STATUS_MESSAGE               | DARKORANGE        | DARKORANGE       |
| TYPE_FAIL                         | FIREBRICK         | YELLOW           |
| FAIL_MESSAGE                      | DARKRED           | DARKYELLOW       |
| FAIL_BACKGROUND                   | -                 | DARKRED          |

###### Tree of ANSI escape code:
- reset
    - on
- bold
    - on
    - off (doubly underlined)
- faint
    - on
    - off
- italic
    - on
    - fraktur
    - off
- underline
    - on
    - off
- blink
    - slow
    - rapid
    - off
- proportional spacing
    - on
    - off
- invert
    - on
    - off
- hide
    - on
    - off
- strike
    - on
    - off
- over line
    - on
    - off
- framed
    - on
    - encircled
    - off
- font
    - primary
    - 1st alternative
    - 2nd alternative
    - 3rd alternative
    - 4th alternative
    - 5th alternative
    - 6th alternative
    - 7th alternative
    - 8th alternative
    - 9th alternative
- color
    - foreground
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - background
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - bright foreground
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - bright background
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - set
        - foreground
            - R;G;B
        - background
            - R;G;B
        - bright foreground
            - R;G;B
        - bright background
            - R;G;B
        - underline
            - R;G;B
    - default
        - foreground
        - background
        - bright foreground
        - bright background
        - underline

- [Content](#content)

## Troubleshooting
All functionality of the library has been tested by me, but if you have problems using it, the code does not work, have suggestions for optimization or advice for improving the style of the code and the name - I invite you [here](https://github.com/Nakama3942/qt_colored_logger/blob/master/CONTRIBUTING.md) and [here](https://github.com/Nakama3942/qt_colored_logger/blob/master/CODE_OF_CONDUCT.md).

- [Content](#content)

## Authors
<table align="center" style="border-width: 10; border-style: ridge">
	<tr>
		<td align="center"><a href="https://github.com/Nakama3942"><img src="https://avatars.githubusercontent.com/u/73797846?s=400&u=a9b7688ac521d739825d7003a5bd599aab74cb76&v=4" width="150px;" alt=""/><br /><sub><b>Kalynovsky Valentin</b></sub></a><sub><br />"Ideological inspirer and Author"</sub></td>
		<!--<td></td>-->
	</tr>
<!--
	<tr>
		<td></td>
		<td></td>
	</tr>
-->
</table>
