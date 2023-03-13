[![template](https://img.shields.io/badge/Repository-template-darkred)](https://github.com/Nakama3942/template_rep)
[![GitHub license](https://img.shields.io/github/license/Nakama3942/qt_colored_logger?color=gold&style=flat-square)](https://github.com/Nakama3942/qt_colored_logger/blob/master/LICENSE)

[![CHANGELOG](https://img.shields.io/badge/here-CHANGELOG-yellow)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CHANGELOG.md)
[![CONTRIBUTING](https://img.shields.io/badge/here-CONTRIBUTING-indigo)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CONTRIBUTING.md)
[![CODE_OF_CONDUCT](https://img.shields.io/badge/here-CODE_OF_CONDUCT-darkgreen)](https://github.com/Nakama3942/qt_colored_logger/blob/master/CODE_OF_CONDUCT.md)
[![PULL_REQUEST_TEMPLATE](https://img.shields.io/badge/here-PULL_REQUEST_TEMPLATE-orange)](https://github.com/Nakama3942/qt_colored_logger/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

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

# Qt_Сolored-logger
## Content
- [Qt_Сolored-logger](#qt_colored-logger)
    - [Content](#content)
    - [Preamble](#preamble)
    - [Overview](#overview)
    - [LICENSE](#license)
    - [Usage](#usage)
    - [Troubleshooting](#troubleshooting)
    - [Authors](#authors)

## Preamble
I often came across the opinion that it is better to use not standard output to the console, but full-fledged logging... However, the standard libraries do not provide exactly what I need... Therefore, I decided to make my own library! Which will implement the functionality I need.

## Overview
The library implements the formation of a beautifully formatted colored text, similar to a log, which has all the necessary information:
- Logging time
- Name of device and profile that logged
- Log status
- Description of the log status
- Log type
- Log message

Any information to the output can be turned off (according to the standard, everything is included). It is also possible to change the output settings during the logging process. It is possible to change colors (class ~~PickerModifier and~~ PickerModifierQ).

*!!!ATTEMPTION!!! At the moment, logging is implemented only in the form of HTML code for QTextBrowser for PyQt, since quite often I need to output the log not to the console, but to the program and save it to a file, including saving colors. Therefore, in this version, output to the console is not implemented, but only in QTextBrowser, however, in the next versions, a lot of functionality will be implemented for easy and convenient logging!*

## LICENSE
The full text of the license can be found at the following [link](https://github.com/Nakama3942/qt_colored_logger/blob/master/LICENSE).

> Copyright © 2022 Kalynovsky Valentin. All rights reserved.
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

## Usage
- Empty
<!--To install the library, you need to execute the command:
```sh
pip install dox-docs-translator
```
Installing the <i>dox_docs_translator</i> library should also install <i>googletrans</i>, but if the <i>googletrans</i> library is not installed or this script doesn't work, you need to install/reinstall the <i>googletrans</i>:
```sh
pip uninstall googletrans
pip install googletrans==4.0.0-rc1
```
Here is an example of using the script from my own experience, as I used it to translate the documentation of my ALGOR project:
```python
from dox_docs_translator import *

if __name__ == '__main__':
    doc_translator = DoxDocsTranslator()
    doc_translator.start_global_translate()
```
In this case, the DOCUMENTATION.ua.dox file will be translated from Ukrainian to English into the DOCUMENTATION.en.dox file. If you need to change these values, you can specify them in the class constructor:
```python
from dox_docs_translator import *

if __name__ == '__main__':
    doc_translator = DoxDocsTranslator('docs_file.dox', 'translated_docs.dox', 'en', 'fr')
    doc_translator.start_global_translate()
```
or
```python
from dox_docs_translator import *

if __name__ == '__main__':
    doc_translator = DoxDocsTranslator(from_lang='en',
                                       origin_doc_file='docs_file.dox',
                                       to_lang='fr',
                                       translated_doc_file='translated_docs.dox')
    doc_translator.start_global_translate()
```
<i><b>Artifacts may appear after translation. This happens during translation, and therefore the errors are not related to this library. After the translation, you should view the received file and correct the artifacts yourself.</b></i>-->

## Troubleshooting
All functionality of the library has been tested by me, but if you have problems using it, the code does not work, have suggestions for optimization or advice for improving the style of the code and the name - I invite you [here](https://github.com/Nakama3942/qt_colored_logger/blob/master/CONTRIBUTING.md) and [here](https://github.com/Nakama3942/qt_colored_logger/blob/master/CODE_OF_CONDUCT.md).

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
