[![template](https://img.shields.io/badge/Repository-template-darkred)](https://github.com/Nakama3942/template_rep)
[![GitHub license](https://img.shields.io/github/license/Nakama3942/qt_colored_logger?color=gold&style=flat-square)](https://github.com/Nakama3942/qt_colored_logger/blob/master/LICENSE)

![PyPI](https://img.shields.io/pypi/v/qt-colored-logger?color=yellow&logo=pypi&logoColor=white&style=flat-square)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Nakama3942/qt_colored_logger?label=latest%20release&logo=github&style=flat-square)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Nakama3942/qt_colored_logger?color=orange&include_prereleases&label=latest%20pre-release&logo=github&style=flat-square)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qt_colored_logger?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/qt_colored_logger?style=flat-square)
![PyPI - Format](https://img.shields.io/pypi/format/qt_colored_logger?label=PyPI%20format&style=flat-square)
![PyPI - Status](https://img.shields.io/pypi/status/qt_colored_logger?label=PyPI%20status&style=flat-square)

![GitHub commits since latest release (by date including pre-releases)](https://img.shields.io/github/commits-since/Nakama3942/qt_colored_logger/v0.3.0?include_prereleases&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Nakama3942/qt_colored_logger?style=flat-square)
![GitHub Release Date](https://img.shields.io/github/release-date/Nakama3942/qt_colored_logger?style=flat-square)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/Nakama3942/qt_colored_logger?label=%28pre-%29release%20date&style=flat-square)

![GitHub repo size](https://img.shields.io/github/repo-size/Nakama3942/qt_colored_logger?color=darkgreen&style=flat-square)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Nakama3942/qt_colored_logger?color=darkgreen&style=flat-square)

[![CHANGELOG](https://img.shields.io/badge/here-CHANGELOG-yellow)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CHANGELOG.md)
[![CONTRIBUTING](https://img.shields.io/badge/here-CONTRIBUTING-indigo)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CONTRIBUTING.md)
[![CODE_OF_CONDUCT](https://img.shields.io/badge/here-CODE_OF_CONDUCT-darkgreen)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CODE_OF_CONDUCT.md)
[![PULL_REQUEST_TEMPLATE](https://img.shields.io/badge/here-PULL_REQUEST_TEMPLATE-orange)](https://github.com/Nakama3942/qt_colored_logger/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

**README.md is incomplete. The examples may not be valid. The file will be finalized before release.**

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

I was inspired by the [colored-logs](https://pypi.org/project/colored-logs/) library.

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

## Important releases
<details><summary>See the important releases (possible spoilers)</summary>

- [x] v0.1.0 - First official release
- [x] v0.2.0 - Structural update (the structure of the project has been changed)
- [x] v0.3.0 - Background update (added background for log entries)
- [ ] v0.4.0 - Buffer update (added text buffer)
- [ ] v0.5.0 - Unifying update (console and HTML are combined into one class)
- [ ] v0.6.0 - Progress update (added start of some log entries in threads (process))
- [ ] v0.7.0 - Symbols update (added hint symbols near log entries types)

</details>

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
This is the simplest example of using the library:
```python
from qt_colored_logger.text import TextBuffer
from qt_colored_logger.logger import Logger

if __name__ == "__main__":
	buf = TextBuffer(115)
	logger = Logger(program_name="Test", text_buffer=buf)
	logger.DEBUG(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.DEBUG_PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.EVENT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.AUDIT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.METRICS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.USER(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.MESSAGE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.INFO(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.NOTICE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.WARNING(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.ERROR(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.CRITICAL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.SUCCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.FAIL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
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

See the DATA.md file for more details.

- [Content](#content)

## *Additional functionality*
*Additional functionality is also planned. Let's keep it a secret for now. Let it be a surprise.*

- [Content](#content)

## Data
See the DATA.md file.

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
