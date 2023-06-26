<div align="center">

[![template](https://img.shields.io/badge/Repository-template-darkred?style=for-the-badge)](https://github.com/Nakama3942/template_rep)
[![GitHub license](https://img.shields.io/github/license/Nakama3942/mighty_logger?color=gold&style=for-the-badge)](https://github.com/Nakama3942/mighty_logger/blob/master/LICENSE)
[![CHANGELOG](https://img.shields.io/badge/here-CHANGELOG-yellow?style=for-the-badge)](https://github.com/Nakama3942/mighty_logger/blob/master/CHANGELOG.md)
[![PULL_REQUEST_TEMPLATE](https://img.shields.io/badge/here-PULL_REQUEST_TEMPLATE-orange?style=for-the-badge)](https://github.com/Nakama3942/mighty_logger/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

![PyPI](https://img.shields.io/pypi/v/mighty-logger?color=yellow&logo=pypi&logoColor=white&style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Nakama3942/mighty_logger?label=latest%20release&logo=github&style=for-the-badge)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Nakama3942/mighty_logger?color=orange&include_prereleases&label=latest%20pre-release&logo=github&style=for-the-badge)
![GitHub commits since latest release (by date including pre-releases)](https://img.shields.io/github/commits-since/Nakama3942/mighty_logger/v0.5.0?include_prereleases&style=for-the-badge)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mighty-logger?style=for-the-badge)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/mighty-logger?style=for-the-badge)
![PyPI - Format](https://img.shields.io/pypi/format/mighty-logger?label=PyPI%20format&style=for-the-badge)
![PyPI - Status](https://img.shields.io/pypi/status/mighty-logger?label=PyPI%20status&style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/Nakama3942/mighty_logger?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/Nakama3942/mighty_logger?style=for-the-badge)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/Nakama3942/mighty_logger?label=%28pre-%29release%20date&style=for-the-badge)

![GitHub repo size](https://img.shields.io/github/repo-size/Nakama3942/mighty_logger?color=darkgreen&style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Nakama3942/mighty_logger?color=darkgreen&style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/Nakama3942/mighty_logger?style=for-the-badge)

</div>

# Mighty Logger

### Content

- [Qt_Сolored-logger](#mighty-logger)
  - [Content](#content)
  - [Preamble](#preamble)
  - [Overview](#overview)
  - [Important releases](#important-releases)
  - [LICENSE](#license)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Additional functionality](#additional-functionality)
  - [Data](#data)
  - [Troubleshooting](#troubleshooting)
  - [Authors](#authors)

## Preamble

<!--
This library it was renamed to "Mighty logger" but before this library named is "Qt Colored logger". Old commits may search in this repository, but download old build may on next link: https://pypi.org/project/qt-colored-logger/ .
-->

> I often came across the opinion that it is better to use not standard output to the console, but full-fledged logging... However, the standard libraries do not provide exactly what I need... Therefore, I decided to make my own library! Which will implement the functionality I need.

I was inspired by the [colored-logs](https://pypi.org/project/colored-logs/) library.

---

*This library has been renamed to "Mighty logger", but this library used to be called "Qt Colored logger". You can search for old commits in this repository, but you can download the old build from the [link](https://pypi.org/project/qt-colored-logger/).*

- [Content](#content)

## Overview

The library implements the formation of a beautifully formatted colored text, similar to a log, which has all the necessary information:

- Device name and registered profile, system name, etc. (this data is displayed only once at the beginning of the logging)
- Log entry time
- Log entry status
- Log entry type
- Entry message

Any information to the output can be turned off (according to the default, everything is included). It is also possible to change the output settings during the logging process. It is possible to change the colors of the foreground text and the background, icons ~~and animations~~.

- [Content](#content)

## Important releases

<details><summary>See the important releases (possible spoilers)</summary>

- [x] v0.0.1 - Alpha-release (the very first version of the simplest Logger has been published)
- [x] v0.0.2 - Little update (added multiple entry types and colors)
- [x] v0.0.3 - Types update (added even more multiple entry types and colors)
- [x] v0.0.4 - Color update (added the entire X11 color table and reworked the color system)
- [x] v0.1.0 - First official release (complete basic HTML logger)
- [x] v0.2.0 - Structural update (added basic console logger with HTML base)
- [x] v0.3.0 - Background update (added background for log entries)
- [x] v0.4.0 - Buffer update (added text buffer)
- [x] v0.5.0 - Unifying update (console and HTML are combined into one class)
- [x] v0.5.1 - Hints update (added status message templates and hint symbols (icons) near log entries status)
- [x] v0.6.0 - Progress update (added start of some log entries in threads (process))
- [x] v0.6.1 - Animation update (added animations in processes)
- [x] v0.7.0 - "Buffer improvement" update (buffer development completed and entry type system reworked)
- [ ] v0.7.1 - Search update (added search by log entry types)
- [ ] v0.8.0 - Export update (added conversion to different types, such as csv, pdf, etc.)
- [ ] v0.9.0 - Extension update (made wheel format and instruction of toml)
- [ ] v0.9.1 - Documenting update (all updates since v0.7.0 are documented; updated old documentation; documentation site generation added)
- [ ] v1.0.0 - Completion of logger development (logger development completed)
- [ ] v1.1.0 - Font update (added a class that formats text outside the logger)

</details>

- [Content](#content)

## LICENSE

The full text of the license can be found at the following [link](https://github.com/Nakama3942/mighty_logger/blob/master/LICENSE).

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

To install the library, enter the command:

```sh
pip install mighty_logger
```

## Usage

ATTENTION!!! OUTDATED MATERIAL! RELEVANCE - v0.6.1! WILL BE OVERWRITTEN IN v0.9.1!

This is the simplest example of using the library:

```python
from mighty_logger import Logger
from mighty_logger.src import StatusMessagePatterns

if __name__ == "__main__":
	logger = Logger(program_name="Test", console_width=115)
	logger.message(status_message=StatusMessagePatterns.custom("Hooray"), message_text="Hello world!")
```

The outputs in console will contain the following text (GitHub, PyPi and possibly some other sites do not support displaying colors in Markdown - use resources that support them, such as PyCharm):

<pre>
<span style='background-color: #;'><span style='color: #ffd700;'>-Test?entry> $███████████████^████@███████:██████████:█████:█████████:█████</span></span>
<span style='background-color: #;'><span style='color: #b0e0e6;'>-?entry>         </span><span style='color: #da70d6;'>*2023-06-08 14:01:39.423493 </span>💬 <span style='color: #ffa500;'>#STATUS: </span><span style='color: #ff8c00;'>Hooray </span><span style='color: #afeeee;'>@MESSAGE - </span><span style='color: #b0e0e6;'>Hello world!</span></span>
</pre>

See the APPLYING.md file for more details.

- [Content](#content)

## *Additional functionality*

*Additional functionality is also planned. Let's keep it a secret for now. Let it be a surprise.*

- [Content](#content)

## Data

See the DATA.md file.

- [Content](#content)

## Troubleshooting

All functionality of the library has been tested by me, but if you have problems using it, the code does not work, have suggestions for optimization or advice for improving the style of the code and the name - I invite you [here](https://github.com/Nakama3942/mighty_logger/blob/master/CONTRIBUTING.md) and [here](https://github.com/Nakama3942/mighty_logger/blob/master/CODE_OF_CONDUCT.md).

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
