"""
A module with implementation of ANSI escape codes.
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

AnsiFormat = {
	# Source: https://en.wikipedia.org/wiki/ANSI_escape_code
	'reset': {
		'on': '\033[0m',
	},

	'bold': {
		'on': '\033[1m',
		'off (doubly underlined)': '\033[21m',
	},

	'faint': {
		'on': '\033[2m',
		'off': '\033[22m',
	},

	'italic': {
		'on': '\033[3m',
		'fraktur': '\033[20m',
		'off': '\033[23m',
	},

	'underline': {
		'on': '\033[4m',
		'off': '\033[24m',
	},

	'blink': {  # not work
		'slow': '\033[5m',
		'rapid': '\033[6m',
		'off': '\033[25m',
	},

	'proportional spacing': {  # not work
		'on': '\033[26m',
		'off': '\033[50m',
	},

	'invert': {
		'on': '\033[7m',
		'off': '\033[27m',
	},

	'hide': {
		'on': '\033[8m',
		'off': '\033[28m',
	},

	'strike': {
		'on': '\033[9m',
		'off': '\033[29m',
	},

	'over line': {
		'on': '\033[53m',
		'off': '\033[55m',
	},

	'framed': {
		'on': '\033[51m',
		'encircled': '\033[52m',
		'off': '\033[54m',
	},

	'font': {
		'primary': '\033[10m',
		'1st alternative': '\033[11m',
		'2nd alternative': '\033[12m',
		'3rd alternative': '\033[13m',
		'4th alternative': '\033[14m',
		'5th alternative': '\033[15m',
		'6th alternative': '\033[16m',
		'7th alternative': '\033[17m',
		'8th alternative': '\033[18m',
		'9th alternative': '\033[19m',
	},

	'color': {
		'foreground': {
			'black': '\033[30m',
			'red': '\033[31m',
			'green': '\033[32m',
			'yellow': '\033[33m',
			'blue': '\033[34m',
			'magenta': '\033[35m',
			'cyan': '\033[36m',
			'white': '\033[37m',
		},
		'background': {
			'black': '\033[40m',
			'red': '\033[41m',
			'green': '\033[42m',
			'yellow': '\033[43m',
			'blue': '\033[44m',
			'magenta': '\033[45m',
			'cyan': '\033[46m',
			'white': '\033[47m',
		},
		'bright foreground': {
			'black': '\033[90m',
			'red': '\033[91m',
			'green': '\033[92m',
			'yellow': '\033[93m',
			'blue': '\033[94m',
			'magenta': '\033[95m',
			'cyan': '\033[96m',
			'white': '\033[97m',
		},
		'bright background': {
			'black': '\033[100m',
			'red': '\033[101m',
			'green': '\033[102m',
			'yellow': '\033[103m',
			'blue': '\033[104m',
			'magenta': '\033[105m',
			'cyan': '\033[106m',
			'white': '\033[107m',
		},
		'set': {
			'foreground': '\033[38;2;$m',
			'background': '\033[48;2;$m',
			'bright foreground': '\033[98;2;$m',
			'bright background': '\033[108;2;$m',
			'underline': '\033[58;2;$m',
		},
		'default': {
			'foreground': '\033[39m',
			'background': '\033[49m',
			'bright foreground': '\033[99m',
			'bright background': '\033[109m',
			'underline': '\033[59m',
		},
	},
}

def _RecursiveGetAnsiFormat(ansi_address: str, ansi: dict) -> str:
	"""
	Recursively extracts a string with an ANSI escape code from a heavily nested dictionary.

	:param ansi_address: Path to ANSI escape code value
	:param ansi: External/nested dictionary
	:return: value - ANSI escape code
	"""
	split_address = ansi_address.split("/")
	# print(split_address)
	if type(ansi[split_address[0]]) == dict:
		return _RecursiveGetAnsiFormat("/".join(split_address[1:]), ansi[split_address[0]])
	else:
		if len(split_address) == 2:
			return ansi[split_address[0]].replace('$', split_address[1])
		else:
			return ansi[split_address[0]]

def GetAnsiFormat(ansi_address: str) -> str:
	"""
	Returns the ANSI escape code value.\n
	The following values are possible: see the list inREADME.md/Data/"Tree of ANSI escape code"\n
	An example of getting an ANSI escape code:\n
	print(f"{GetAnsiFormat('italic/fraktur')}Test string")\n
	print(f"{GetAnsiFormat('blink/slow')}Test string")\n
	print(f"{GetAnsiFormat('invert/off')}Test string")\n
	print(f"{GetAnsiFormat('font/3th alternative')}Test string")\n
	print(f"{GetAnsiFormat('color/foreground/green')}Test string")\n
	print(f"{GetAnsiFormat('color/set/background/255;255;255')}Test string")\n
	print(f"{GetAnsiFormat('reset/on')}Test string")\n

	:param ansi_address: Path to ANSI escape code value
	:return: ANSI escape code
	"""
	return _RecursiveGetAnsiFormat(ansi_address, AnsiFormat)
