# ##########################   Qt_Colored-logger   ########################### #
# ---------------------------------------------------------------------------- #
#                                                                              #
# Copyright © 2023 Kalynovsky Valentin. All rights reserved.                   #
#                                                                              #
# Licensed under the Apache License, Version 2.0 (the "License");              #
# you may not use this file except in compliance with the License.             #
# You may obtain a copy of the License at                                      #
#                                                                              #
#     http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS,            #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.     #
# See the License for the specific language governing permissions and          #
# limitations under the License.                                               #
#                                                                              #
# ---------------------------------------------------------------------------- #
# ############################################################################ #

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

	'proportional spacing ': {  # not work
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
		'1th alternative': '\033[11m',
		'2th alternative': '\033[12m',
		'3th alternative': '\033[13m',
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

def GetAnsi() -> dict:
	"""
	todo Expand the functionality of the function
	Returns a complete dictionary of all ANSI escape codes.\n
	An example of working with ANSI escape codes:\n
	print(f"{GetAnsi()['reset']['on']}Test string")\n
	print(f"{GetAnsi()['italic']['fraktur']}Test string")\n
	print(f"{GetAnsi()['blink']['slow']}Test string")\n
	print(f"{GetAnsi()['invert']['off']}Test string")\n
	print(f"{GetAnsi()['font']['3th alternative']}Test string")\n
	print(f"{GetAnsi()['color']['foreground']['green']}Test string")\n
	How to work with GetAnsi()['color']['set']:\n
	ANSI standard - command '38', '48', '58', '98', '108'; he argument - 'N;R;G;B';\n
	N - const - NUMBER = 2;\n
	R - red value, G - green value, B - blue value;\n
	syntax = '\033[38;N;R;G;Bm', for example, white = '\033[38;2;255;255;255m';\n
	therefore, '\033[38;2;-m' is ANSI format and '-255;255;255-' is color code.\n
	To save this command, the color in the dictionary has been encoded with the $ symbol and to
	use it you need to return the color instead of the $ symbol, which is why you need to use replace():\n
	print(f"{GetAnsi()['color']['set']['background'].replace('$', '255;255;255')}Test string")

	:return: ANSI escape codes
	"""
	return AnsiFormat

if __name__ == "__main__":
	print(f"{AnsiFormat['italic']['fraktur']}Test string")
	print(f"{AnsiFormat['blink']['slow']}Test string")
	print(f"{AnsiFormat['invert']['off']}Test string")
	print(f"{AnsiFormat['font']['3th alternative']}Test string")
	print(f"{AnsiFormat['color']['foreground']['green']}Test string")
	print(f"{AnsiFormat['color']['set']['background'].replace('$', '255;165;0')}Test string")
	print(f"{AnsiFormat['reset']['on']}Test string")
