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

## v0.0.1 (13.03.2023)

#### Release
The library implements the formation of a beautifully formatted colored text, similar to a log, which has all the necessary information:
- Logging time;
- Name of device and profile that logged;
- Log status;
- Description of the log status;
- Log type;
- Log message.

Any information to the output can be turned off (according to the standard, everything is included). It is also possible to change the output settings during the logging process. It is possible to change colors (class PickerModifierQ).

*!!!ATTEMPTION!!! At the moment, logging is implemented only in the form of HTML code for QTextBrowser for PyQt, since quite often I need to output the log not to the console, but to the program and save it to a file, including saving colors. Therefore, in this version, output to the console is not implemented, but only in QTextBrowser, however, in the next versions, a lot of functionality will be implemented for easy and convenient logging!*

---

## <span style='color: #ff3333;'>v0.0.2 (14.03.2023)</span>

#### Enhancements:
- Added new colors:
    - OCEANBLUE;
    - DARKOCEANBLUE.
- Changed color names:
    - CYAN -> BLUE;
    - DARKCYAN -> DARKBLUE.
- Added an ID to each logger class; 
- Added new methods to the Logger class:
	- SUCCESS();
	- FAIL();
	- START_PROCESS(); *stub - not implemented*
	- STOP_PROCESS(). *stub - not implemented*

---

## <span style='color: #ff3333;'>v0.0.3 (14.03.2023)</span>

#### Bug Fixes:
- Fixed some typos.

#### Enhancements:
- Added some links to PyPi.

---

## v0.0.4 (16.03.2023)

#### Bug Fixes:
- An error in the LoggerQ.INFO() method that accessed an unregistered color (a typo in the name of the color: instead of OCEANBLUE and DARKOCEANBLUE - OKEANBLUE and DARKOKEANBLUE, respectively). Do not use v0.0.2 and v0.0.3!

---

## <span style='color: #ff3333;'>v0.0.5 (17.03.2023)</span>

#### Documenting:
- The LoggerQ class is fully documented.

#### Enhancements:
- Added new types of log output:
    1. DEBUG_PERFORMANCE;
    2. PERFORMANCE;
    3. EVENT;
    4. AUDIT;
    5. METRICS;
    6. USER;
    7. MESSAGE;
    8. NOTICE.
- Added new colors:
    1.  FIREBRICK *replaced RED*
    2.  MEDIUMSPRINGGREEN
    3.  SPRINGGREEN
    4.  MEDIUMSEAGREEN
    5.  SEAGREEN
    6.  FORESTGREEN *not used yet*
    7.  YELLOWGREEN
    8.  OLIVEDRAB
    9.  OLIVE
    10. DARKOLIVEGREEN
    11. AQUAMARINE *replaced BLUE*
    12. TURQUOISE *replaced DARKBLUE*
    13. SKYBLUE *replaced OCEANBLUE*
    14. LIGHTSKYBLUE *replaced DARKOCEANBLUE*
    15. BLUE *Adopted its color according to the X11 standards table*
    16. MEDIUMBLUE
    17. DARKBLUE *Adopted its color according to the X11 standards table*
    18. NAVY
    19. BLUEVIOLET *replaced VIOLET*
    20. DARKVIOLET *Adopted its color according to the X11 standards table*
    21. GAINSBORO
    22. LIGHTGREY
    23. SILVER
    24. DIMGREY

---

## <span style='color: #ff3333;'>v0.0.6 (17.03.2023)</span>

#### Bug Fixes:
- I renamed the color VIOLET to BLUEVIOLET, and in the code I still refer to VIOLET. Fixed this bug.

---

## v0.0.7 (17.03.2023)

#### Bug Fixes:
- I renamed the color RED to FIREBRICK, and in the code I still refer to RED. Fixed this bug.

---

## <span style='color: #ff3333;'>v0.0.8 (25.03.2023)</span>

#### Bug Fixes:
- Found and fixed several minor bugs.

#### Documenting:
- The HtmlColorSetInitQ class is fully documented;
- Slightly fixed CHANGELOG.

#### Enhancements:
- The color system has been completely redesigned (i.e. the system for working with colors);
- Added ALL X11 table colors [from this page](https://en.wikipedia.org/wiki/Web_colors);
- Added functions for getting color values in different formats by their names;
- Added ColorException;
- Started work with console logger (*not yet available*);
- PickerModifierQ class renamed to HtmlColorSetInitQ;
- Now only one object of the HtmlColorSetInitQ class can be created;
- Now only one object of the LoggerQ class can be created;
- The color table of the LoggerQ logger has been changed - now the table does not store color names, but abstract names:
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
- Now, initially this table is not initialized and the logger will not be able to work. First you need to initialize the table by creating an object of the HtmlColorSetInitQ class, which also provides methods for changing this very logger color table;
- Implemented library functionality tests for early detection of minor bugs.

---

## v0.1.0 (26.03.2023)

#### Bug Fixes:
- Fixed a bug that occurs when passing arguments to the LoggerQ constructor;
- Fixed a bug due to which the color value was not correctly saved in the logger's color table when changing the color manually.

#### Documenting:
- Completed documentation of the library;
- Wrote the actual README.md (which corresponds to the current version).

#### Enhancements:
- Slightly redefined colors in the logger;
- Changed the order of colors in the color table.

---

## v0.2.0 (29.03.2023)

#### Documentation:
- Documented all new functionality;
- Fixed typos and outdated information in old documentation.

#### Enhancements:
- Added a large dictionary of all ANSI escape codes and the GetAnsi() function to get it;
- CodColor() function renamed to AnsiForegroundColor();
- Fully implemented AnsiColorSetInit and Logger classes based on HtmlColorSetInitQ and LoggerQ;
- Singleton pattern used by HtmlColorSetInitQ, LoggerQ, AnsiColorSetInit and Logger moved to a separate class;
- A base class has been created for LoggerQ and Logger, which includes initialization, setting up loggers and generating record strings (*at the moment, inherited classes are used to simplify interaction with the base class and use ready-made functionality, but in the future their own functionality will be expanded*);
- Optimized HexColor() and AnsiForegroundColor() functions;
- **The project structure has been completely changed** (*however, this only affects the development of the library and support for programs written with the version of the library v0.1.0 will remain, since the external attributes of communication with the library have not changed*);
- Added the DefaultColorScheme list, which stores a list of all colors that are used in the color schemes of the loggers and the GetDefaultColorScheme() function to get this list;
- Now the ColorPicker dictionary stores only color values in RGB, and other formats are obtained by converting RGB;
- Added functions Dec2Hex(), Dec2Ansi(), Hex2Dec(), Hex2Ansi(), Ansi2Dec(), Ansi2Hex(), which are used to convert one color value format to another;
- *The logic of assembling strings logging entry's has been completely changed*;
- The work of the HtmlColorSetInitQ and LoggerQ classes is adjusted to the new best functionality that is used in the new classes AnsiColorSetInit and Logger.

---

## v0.2.1 (31.03.2023)

#### Bug Fixes:
- Fixed old calls to Singleton and BasicLogger to new _Singleton and _BasicLogger in HtmlColorSetInitQ, LoggerQ, AnsiColorSetInit and Logger classes;
- Fixed a bug in the setColor() method of the AnsiColorSetInit class, where the value of the new argument was not passed to the Dec2Ansi() function after changing the GetAnsiFormat() function.

#### Documenting:
- Wrote the actual README.md (which takes into account changes in versions v0.2.0 and v0.2.1);
- Fixed a bug in the annotation of the setColor() method of the HtmlColorSetInitQ class;
- Changed the order of the changelog - now it goes in direct order from top to bottom (easy to read and understand), and not from bottom to top.

#### Enhancements:
- Renamed the GetAnsi() function to GetAnsiFormat(), implemented the _RecursiveGetAnsiFormat() helper function for it - now GetAnsiFormat() takes the path to the ANSI escape code value, recursively traverses the tree and returns the ANSI escape code value, which helps to make the code easier to understand and speed up development programs when using the library; here are some examples:
```python
# Before
print(f"{AnsiFormat['color']['set']['background'].replace('$', '255;165;0')}Test string")
print(f"{AnsiFormat['reset']['on']}Test string")

# After
print(f"{GetAnsiFormat('color/set/background/255;255;255')}Test string")
print(f"{GetAnsiFormat('reset/on')}Test string")
```
- Renamed the AnsiForegroundColor() function to AnsiColor() - if earlier the function returned only the color of the text (the usual foreground), now you can specify any of the five plans (this is necessary for the next update, where I will add a change not only to the color, but also to the background of the logs):
    1. foreground
    2. background
    3. bright foreground
    4. bright background
    5. underline
- Adapted the Dec2Ansi() and Hex2Ansi() functions to the modified AnsiColor();
- Protected the qt_colored_logger/basic directory - now it is called qt_colored_logger/_basic: you can still use its functionality, but now, according to the agreement, the IDE will issue a warning; *remember - protected modules are designed only for use inside the library*;
- The structure of the qt_colored_logger/_basic protected directory has been slightly changed;
- Changed names of keys in "AnsiFormat/font" dictionary from "1th alternative", "2th alternative" and "3th alternative" to "1st alternative", "2nd alternative" and "3rd alternative" respectively.

---

## v0.3.0 (05.04.2023)

#### Documenting:
- Updated documentation;
- Wrote the actual README.md (which corresponds to the current version).

#### Enhancements:
- Added support for inverting colors in posts (console);
- Added support for backgrounds in posts (console, HTML);
- Completely redesigned and written from scratch logger color table;
- Logger included AnsiColorSetInit;
- LoggerQ included HtmlColorSetInitQ;
- Removed list of default colors;
- Post types categorized:
    - Debugging (%);
    - Event (~);
    - Message (@);
    - Error (!);
    - Process (&).
- Argument names are now required;
- Added an introductory line with system initialized information;
- Added a global enable background setting;
- Started work on the text buffer;
- Added new CombinationException.

---

## v0.4.0 (09.04.2023)

#### Documenting:
- Split README.md, cutting DATA.md and APPLYING.md out of it;
- Published a plan for the next updates in README.md;
- Updated documentation;
- Wrote the actual README.md, DATA.md and APPLYING.md (which corresponds to the current version).

#### Enhancements:
- Added a package qt_colored_logger.text;
- Added TextBuffer (used for console) to qt_colored_logger.text package;
- Added BasicTextBuffer (used with HTML) to qt_colored_logger.text package;
- Loggers moved from qt_colored_logger root package to nested qt_colored_logger.logger;
- Entry methods rewritten - now they do not return strings of entries, but add them to the text buffer;
- Returned protected modules, making them fully available;
- Added blanks for the next updates;
- Reworked the principle of forming strings of records in the BasicLogger, getting rid of the string variable;
- Added get_buffer() method in loggers.

---
