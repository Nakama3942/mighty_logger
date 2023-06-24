"""
A package with the implementation of various data (ANSI, colors, etc.).
\n
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
"""

from .animation import IndefiniteAnimations, DefiniteAnimations
from .ansi_format import GetAnsiFormat
from .color_picker import DecColor,\
	HexColor,\
	AnsiColor,\
	Dec2Hex,\
	Dec2Ansi,\
	Hex2Dec,\
	Hex2Ansi,\
	Ansi2Dec,\
	Ansi2Hex
from .entry_types import LoggerEntryTypes, ProcessEntryTypes
from .environments import LogEnvironments
from .status_variables import StatusMessagePatterns
from .text_buffer import BasicTextBuffer, TextBuffer
