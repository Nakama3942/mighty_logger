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
        - [Default Color Scheme](#default-color-scheme-)
        - [Logger Color Chart](#logger-color-chart-)
        - [Tree of ANSI escape code](#tree-of-ansi-escape-code-)
    - [Troubleshooting](#troubleshooting)
    - [Authors](#authors)

## Preamble
I often came across the opinion that it is better to use not standard output to the console, but full-fledged logging... However, the standard libraries do not provide exactly what I need... Therefore, I decided to make my own library! Which will implement the functionality I need.

- [Content](#content)

## Overview
The library implements the formation of a beautifully formatted colored text, similar to a log, which has all the necessary information:
- Logging time
- Name of device and profile that logged
- Log status
- Description of the log status
- Log type
- Log message

Any information to the output can be turned off (according to the standard, everything is included). It is also possible to change the output settings during the logging process. It is possible to change colors (class AnsiColorSetInit and HtmlColorSetInitQ).

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
The library has a complete [X11 color table](#x11-color-table-). However, logger use their [own color tables](#logger-color-chart-) for themselves, where the names of colors are determined not by its real physical name, but by a virtual one formed from the place where this color is used. These tables are initially empty. To initialize them, you need to create an object of the AnsiColorSetInit class, which, in addition to filling the table, provides methods for changing colors in the table. After that, you can already use the color table, and therefore you can start the logging process.

*Since the library is under active development, not the best solutions have been applied at this stage, which will be corrected in the future. But at the moment it is NOT RECOMMENDED to name an object of class Logger by the name log!*

Logging is done by the LoggerQ class. To write to the log, you need to call a method with the desired entry type. There are 16 in total: [see section Data/"Entry types"](#entry-types-).

Not only the log itself has settings, but also each type of record. However, the log settings apply to all entries. Therefore, if you need to disable the output of a specific part of the record for a specific type of record, this must be done before each output of this record to the log (i.e., disable the output before writing and turn it back on after the output, so that this part of the information would be displayed for other types). This approach is used only if the part is disabled only for one or more data types.

There are few settings for each entry type. There you can turn on/off only the text format bold/italic/standard. Also, do not forget to pass the status text (if enabled) and the message text (if enabled) to the record, since the developer himself determines the data to be recorded.

Here is an example using the library:
```python
from qt_colored_logger import AnsiColorSetInit, Logger

if __name__ == '__main__':
    color = AnsiColorSetInit()
    logger = Logger(status_message=False)
    print(logger.DEBUG(message_text="Debug data"))
    print(logger.DEBUG(message_text="Debug data", bold=True))
    print(logger.DEBUG(message_text="Debug data", italic=True))
    print(logger.DEBUG(message_text="Debug data", bold=True, italic=True))
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='color: #da70d6;'>*2023-03-26 13:25:58.091911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span><br>
> <b><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></b><br>
> <i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i><br>
> <b><i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i></b><br>

If you want to change the color of a part of a post, you need to refer to the [logger's color chart](#logger-color-chart-). The class Logger has read access, and AnsiColorSetInit has write access. As already mentioned, AnsiColorSetInit not only forms a table, but also provides methods for changing colors. The Logger Color Chart has the following color names: [see section Data/"Logger Color Chart"](#logger-color-chart-).

Here is an example of a color change:
```python
from qt_colored_logger import AnsiColorSetInit, Logger

if __name__ == '__main__':
    color = AnsiColorSetInit()
    logger = Logger(status_message=False)
    print(logger.NOTICE(message_text="Notice data"))
    color.setColor("NOTICE_MESSAGE", [127, 255, 0])
    print(logger.NOTICE(message_text="Notice data"))
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='color: #da70d6;'>*2023-03-26 13:52:29.519001</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #00bfff;'>@NOTICE -</span> <span style='color: #1e90ff;'>Notice data</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:52:29.519001</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #00bfff;'>@NOTICE -</span> <span style='color: #7fff00;'>Notice data</span><br>

This is the simplest example of using the library:
```python
from qt_colored_logger import AnsiColorSetInit, Logger

if __name__ == "__main__":
	mod = AnsiColorSetInit()
	logger = Logger()
	print(logger.DEBUG("1", "2"))
	print(logger.DEBUG_PERFORMANCE("3", "4"))
	print(logger.PERFORMANCE("5", "6"))
	print(logger.EVENT("7", "8"))
	print(logger.AUDIT("9", "10"))
	print(logger.METRICS("11", "12"))
	print(logger.USER("13", "14"))
	print(logger.MESSAGE("15", "16"))
	print(logger.INFO("17", "18"))
	print(logger.NOTICE("19", "20"))
	print(logger.WARNING("21", "22"))
	print(logger.ERROR("23", "24"))
	print(logger.CRITICAL("25", "26"))
	# print(logger.START_PROCESS("27", "28"))
	print(logger.SUCCESS("29", "30"))
	print(logger.FAIL("31", "32"))
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.837031</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>1</span>	<span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>2</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>3</span>	<span style='color: #ffdead;'>@DEBUG PERFORMANCE -</span> <span style='color: #f5deb3;'>4</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>5</span>	<span style='color: #ffebcd;'>@PERFORMANCE -</span> <span style='color: #ffe4c4;'>6</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>7</span>	<span style='color: #3cb371;'>@EVENT -</span> <span style='color: #2e8b57;'>8</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>9</span>	<span style='color: #9acd32;'>@AUDIT -</span> <span style='color: #6b8e23;'>10</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>11</span>	<span style='color: #808000;'>@METRICS -</span> <span style='color: #556b2f;'>12</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>13</span>	<span style='color: #98fb98;'>@USER -</span> <span style='color: #90ee90;'>14</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>15</span>	<span style='color: #b0c4de;'>@MESSAGE -</span> <span style='color: #b0e0e6;'>16</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>17</span>	<span style='color: #afeeee;'>@INFO -</span> <span style='color: #add8e6;'>18</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>19</span>	<span style='color: #00bfff;'>@NOTICE -</span> <span style='color: #1e90ff;'>20</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>21</span>	<span style='color: #ffff00;'>@WARNING -</span> <span style='color: #ffcc00;'>22</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>23</span>	<span style='color: #b22222;'>!ERROR -</span> <span style='color: #8b0000;'>24</span><br>
> <b><span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>25</span>	<span style='color: #8b0000;'>!!!@CRITICAL -</span> <span style='color: #800000;'>26</span></b><br>
> <i><span style='color: #da70d6;'>*2023-03-26 13:54:25.869034</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>29</span>	<span style='color: #008000;'>@SUCCESS -</span> <span style='color: #006400;'>30</span></i><br>
> <i><span style='color: #da70d6;'>*2023-03-26 13:54:25.871033</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #ff8c00;'>31</span>	<span style='color: #b22222;'>@FAIL -</span> <span style='color: #8b0000;'>32</span></i><br>

## Usage in Qt
Разница между консолью и Qt в том, что Qt использует HTML для отображения форматированого текста, а консоль - ANSI escape code. Однако к базовой логике доступ не планируется, а внешний интерфейс между классами AnsiColorSetInit/HtmlColorSetInitQ и Logger/LoggerQ не отличается (кроме самих названий классов). Поэтому все преддыдущие примеры можно переписать так:
```python
from qt_colored_logger import HtmlColorSetInitQ, LoggerQ

...

self.color = HtmlColorSetInitQ()
self.logger = LoggerQ(status_message=False)
self.someTextBrowserObject.append(logger.DEBUG(message_text="Debug data"))
self.someTextBrowserObject.append(logger.DEBUG(message_text="Debug data", bold=True))
self.someTextBrowserObject.append(logger.DEBUG(message_text="Debug data", italic=True))
self.someTextBrowserObject.append(logger.DEBUG(message_text="Debug data", bold=True, italic=True))

...
```

```python
from qt_colored_logger import HtmlColorSetInitQ, LoggerQ

...

color = HtmlColorSetInitQ()
logger = LoggerQ(status_message=False)
self.someTextBrowserObject.append(logger.NOTICE(message_text="Notice data"))
color.setColor("NOTICE_MESSAGE", [127, 255, 0])
self.someTextBrowserObject.append(logger.NOTICE(message_text="Notice data"))

...
```


```python
from qt_colored_logger import HtmlColorSetInitQ, LoggerQ

...

mod = HtmlColorSetInitQ()
logger = LoggerQ()
self.someTextBrowserObject.append(logger.DEBUG("1", "2"))
self.someTextBrowserObject.append(logger.DEBUG_PERFORMANCE("3", "4"))
self.someTextBrowserObject.append(logger.PERFORMANCE("5", "6"))
self.someTextBrowserObject.append(logger.EVENT("7", "8"))
self.someTextBrowserObject.append(logger.AUDIT("9", "10"))
self.someTextBrowserObject.append(logger.METRICS("11", "12"))
self.someTextBrowserObject.append(logger.USER("13", "14"))
self.someTextBrowserObject.append(logger.MESSAGE("15", "16"))
self.someTextBrowserObject.append(logger.INFO("17", "18"))
self.someTextBrowserObject.append(logger.NOTICE("19", "20"))
self.someTextBrowserObject.append(logger.WARNING("21", "22"))
self.someTextBrowserObject.append(logger.ERROR("23", "24"))
self.someTextBrowserObject.append(logger.CRITICAL("25", "26"))
# self.someTextBrowserObject.append(logger.START_PROCESS("27", "28"))
self.someTextBrowserObject.append(logger.SUCCESS("29", "30"))
self.someTextBrowserObject.append(logger.FAIL("31", "32"))

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

###### Default Color Scheme:
- ORCHID
- MEDIUMORCHID
- ORANGE
- DARKORANGE
- BURLYWOOD
- TAN
- NAVAJOWHITE
- WHEAT
- BLANCHEDALMOND
- BISQUE
- MEDIUMSEAGREEN
- SEAGREEN
- YELLOWGREEN
- OLIVEDRAB
- OLIVE
- DARKOLIVEGREEN
- PALEGREEN
- LIGHTGREEN
- LIGHTSTEELBLUE
- POWDERBLUE
- PALETURQUOISE
- LIGHTBLUE
- DEEPSKYBLUE
- DODGERBLUE
- YELLOW
- DARKYELLOW
- FIREBRICK
- DARKRED
- MAROON
- SKYBLUE
- LIGHTSKYBLUE
- GREEN
- DARKGREEN

###### Logger Color Chart:
- TIME
- USER
- STATUS
- STATUS_MESSAGE
- TYPE_DEBUG
- DEBUG_MESSAGE
- TYPE_DEBUG_PERFORMANCE
- DEBUG_PERFORMANCE_MESSAGE
- TYPE_PERFORMANCE
- PERFORMANCE_MESSAGE
- TYPE_EVENT
- EVENT_MESSAGE
- TYPE_AUDIT
- AUDIT_MESSAGE
- TYPE_METRICS
- METRICS_MESSAGE
- TYPE_USER
- USER_MESSAGE
- TYPE_MESSAGE
- MESSAGE_MESSAGE
- TYPE_INFO
- INFO_MESSAGE
- TYPE_NOTICE
- NOTICE_MESSAGE
- TYPE_WARNING
- WARNING_MESSAGE
- TYPE_ERROR
- ERROR_MESSAGE
- TYPE_CRITICAL
- CRITICAL_MESSAGE
- TYPE_PROGRESS
- PROGRESS_MESSAGE
- TYPE_SUCCESS
- SUCCESS_MESSAGE
- TYPE_FAIL
- FAIL_MESSAGE

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
