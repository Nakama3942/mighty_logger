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
## v0.0.3 (14.03.2023)

#### Bug Fixes:
- Fixed some typos

#### Enhancements:
- Added some links to PyPi

---

## v0.0.2 (14.03.2023)

#### Enhancements:
- Added new colors:
    - OCEANBLUE;
    - DARKOCEANBLUE;
- Changed color names:
    - CYAN -> BLUE;
    - DARKCYAN -> DARKBLUE;
- Added an ID to each logger class; 
- Added new methods to the Logger class:
	- SUCCESS();
	- FAIL();
	- START_PROCESS(); *stub - not implemented*
	- STOP_PROCESS(); *stub - not implemented*

---

## v0.0.1 (13.03.2023)

#### Release
The library implements the formation of a beautifully formatted colored text, similar to a log, which has all the necessary information:
- Logging time
- Name of device and profile that logged
- Log status
- Description of the log status
- Log type
- Log message

Any information to the output can be turned off (according to the standard, everything is included). It is also possible to change the output settings during the logging process. It is possible to change colors (class PickerModifierQ).

*!!!ATTEMPTION!!! At the moment, logging is implemented only in the form of HTML code for QTextBrowser for PyQt, since quite often I need to output the log not to the console, but to the program and save it to a file, including saving colors. Therefore, in this version, output to the console is not implemented, but only in QTextBrowser, however, in the next versions, a lot of functionality will be implemented for easy and convenient logging!*
