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
## v0.0.6 (17.03.2023)

#### Bug Fixes:
- I renamed the color VIOLET to BLUEVIOLET, and in the code I still refer to VIOLET. Fixed this bug

---

## v0.0.5 (17.03.2023)

#### Documenting:
- The LoggerQ class is fully documented

#### Enhancements:
- Added new types of log output:
    1. DEBUG_PERFORMANCE
    2. PERFORMANCE
    3. EVENT
    4. AUDIT
    5. METRICS
    6. USER
    7. MESSAGE
    8. NOTICE
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

## v0.0.4 (16.03.2023)

#### Bug Fixes:
- An error in the LoggerQ.INFO() method that accessed an unregistered color (a typo in the name of the color: instead of OCEANBLUE and DARKOCEANBLUE - OKEANBLUE and DARKOKEANBLUE, respectively). Do not use v0.0.2 and v0.0.3!

---

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
