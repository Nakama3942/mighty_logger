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
    - [Usage](#usage)
        - [Usage notice](#usage-notice)
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

Any information to the output can be turned off (according to the standard, everything is included). It is also possible to change the output settings during the logging process. It is possible to change colors (class ~~HtmlColorSetInit and~~ HtmlColorSetInitQ).

*!!!ATTEMPTION!!! At the moment, logging is implemented only in the form of HTML code for QTextBrowser for PyQt, since quite often I need to output the log not to the console, but to the program and save it to a file, including saving colors. Therefore, in this version, output to the console is not implemented, but only in QTextBrowser, however, in the next versions, a lot of functionality will be implemented for easy and convenient logging!*

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

## Usage
The library has a complete X11 color table. However, logger use their own color tables for themselves, where the names of colors are determined not by its real physical name, but by a virtual one formed from the place where this color is used. These tables are initially empty. To initialize them, you need to create an object of the HtmlColorSetInitQ class, which, in addition to filling the table, provides methods for changing colors in the table. After that, you can already use the color table, and therefore you can start the logging process.

*Since the library is under active development, not the best solutions have been applied at this stage, which will be corrected in the future. But at the moment it is NOT RECOMMENDED to name an object of class LoggerQ by the name log!*

Logging is done by the LoggerQ class. To write to the log, you need to call a method with the desired record type. There are 16 in total:
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

Not only the log itself has settings, but also each type of record. However, the log settings apply to all entries. Therefore, if you need to disable the output of a specific part of the record for a specific type of record, this must be done before each output of this record to the log (i.e., disable the output before writing and turn it back on after the output, so that this part of the information would be displayed for other types). This approach is used only if the part is disabled only for one or more data types.

There are few settings for each type. There you can turn on/off only the text format bold/italic/standard. Also, do not forget to pass the status text (if enabled) and the message text (if enabled) to the record, since the developer himself determines the data to be recorded.

Here is an example using the library:
```python
from qt_colored_logger import HtmlColorSetInitQ, LoggerQ

if __name__ == '__main__':
    color = HtmlColorSetInitQ()
    logger = LoggerQ(status_message=False)
    print(logger.DEBUG(message_text="Debug data"))
    print(logger.DEBUG(message_text="Debug data", bold=True))
    print(logger.DEBUG(message_text="Debug data", italic=True))
    print(logger.DEBUG(message_text="Debug data", bold=True, italic=True))
```

The output in QTextBrowser will contain the following text:
> <span style='color: #da70d6;'>*2023-03-26 13:25:58.091911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span><br>
> <b><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></b><br>
> <i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i><br>
> <b><i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i></b><br>

If you want to change the color of a part of a post, you need to refer to the logger's color chart. The class LoggerQ has read access, and HtmlColorSetInitQ has write access. As already mentioned, HtmlColorSetInitQ not only forms a table, but also provides methods for changing colors. The logger Color Chart has the following color names:
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

Here is an example of a color change:
```python
from qt_colored_logger import HtmlColorSetInitQ, LoggerQ

if __name__ == '__main__':
    color = HtmlColorSetInitQ()
    logger = LoggerQ(status_message=False)
    print(logger.NOTICE(message_text="Notice data"))
    color.setColor("NOTICE_MESSAGE", 127, 255, 0)
    print(logger.NOTICE(message_text="Notice data"))
```

The output in QTextBrowser will contain the following text:
> <span style='color: #da70d6;'>*2023-03-26 13:52:29.519001</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #00bfff;'>@NOTICE -</span> <span style='color: #1e90ff;'>Notice data</span><br>
> <span style='color: #da70d6;'>*2023-03-26 13:52:29.519001</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #00bfff;'>@NOTICE -</span> <span style='color: #7fff00;'>Notice data</span><br>

This is the simplest example of using the library:
```python
from qt_colored_logger import HtmlColorSetInitQ, LoggerQ

if __name__ == "__main__":
	mod = HtmlColorSetInitQ()
	logger = LoggerQ()
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

The output in QTextBrowser will contain the following text:
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

#### Usage notice
In fact, these examples, at this stage of the development of the library, will not work that way. *The examples are simply tailored to fit the results and show a simplified usage that differs from actual usage in Qt.* However, when the console logger is implemented, it will be based on these rules. But in the future, with development, everything can change (most likely, **for sure** it will change). Don't forget that the logger generates an HTML string, and the print() method prints the text to the console. The results of the work only simulate how the text will look in the application program, and not in the console. So to get this result:
> <span style='color: #da70d6;'>*2023-03-26 13:25:58.091911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span><br>
> <b><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></b><br>
> <i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i><br>
> <b><i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i></b><br>

Need to write the following:
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

And the code from example:
```python
from qt_colored_logger import HtmlColorSetInitQ, LoggerQ

if __name__ == '__main__':
    color = HtmlColorSetInitQ()
    logger = LoggerQ(status_message=False)
    print(logger.DEBUG(message_text="Debug data"))
    print(logger.DEBUG(message_text="Debug data", bold=True))
    print(logger.DEBUG(message_text="Debug data", italic=True))
    print(logger.DEBUG(message_text="Debug data", bold=True, italic=True))
```

It just prints the following text to the console:
```html
<span style='color: #da70d6;'>*2023-03-26 13:25:58.091911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span>
<b><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></b>
<i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i>
<b><i><span style='color: #da70d6;'>*2023-03-26 13:25:58.093911</span>	<span style='color: #ba55d3;'>$DESKTOP-NUMBER^User</span>	<span style='color: #ffa500;'>#STATUS:</span> <span style='color: #deb887;'>@DEBUG -</span> <span style='color: #d2b48c;'>Debug data</span></i></b>
```

Work on the console logger has just begun. Wait for the completion of its development. The work is being actively carried out.

*Additional functionality is also planned. Let's keep it a secret for now. Let it be a surprise.*

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
