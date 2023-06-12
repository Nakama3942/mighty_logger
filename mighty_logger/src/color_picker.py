"""
A module with implementation of colors and their formatter functions.
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

from mighty_logger.basic.exceptions import ColorException
from mighty_logger.src.ansi_format import GetAnsiFormat

ColorPicker = {
	# Color table
	# Original: https://en.wikipedia.org/wiki/Web_colors
	# Red
	'MAROON': [128, 0, 0],
	'DARKRED': [139, 0, 0],
	'RED': [255, 0, 0],
	'LIGHTRED': [255, 51, 51],
	'FIREBRICK': [178, 34, 34],
	'CRIMSON': [220, 20, 60],
	'INDIANRED': [205, 92, 92],
	'LIGHTCORAL': [240, 158, 128],
	'SALMON': [250, 128, 114],
	'DARKSALMON': [233, 150, 122],
	'LIGHTSALMON': [255, 160, 122],
	# Pink
	'MEDIUMVIOLETRED': [199, 21, 133],
	'DEEPPINK': [255, 20, 147],
	'PALEVIOLETRED': [219, 112, 147],
	'HOTPINK': [255, 105, 180],
	'LIGHTPINK': [255, 182, 193],
	'PINK': [255, 192, 203],
	# Orange
	'ORANGERED': [255, 69, 0],
	'TOMATO': [255, 99, 71],
	'DARKORANGE': [255, 140, 0],
	'CORAL': [255, 127, 80],
	'ORANGE': [255, 165, 0],
	# Yellow
	'DARKKHAKI': [189, 183, 107],
	'GOLD': [255, 215, 0],
	'KHAKI': [240, 230, 140],
	'PEACHPUFF': [255, 218, 185],
	'YELLOW': [255, 255, 0],
	'DARKYELLOW': [255, 204, 0],
	'PALEGOLDENROD': [238, 232, 170],
	'MOCCASIN': [255, 228, 181],
	# Purple
	'INDIGO': [75, 0, 130],
	'PURPLE': [128, 0, 128],
	'DARKMAGENTA': [139, 0, 139],
	'DARKVIOLET': [148, 0, 211],
	'DARKSLATEBLUE': [82, 61, 139],
	'BLUEVIOLET': [138, 43, 226],
	'DARKORCHID': [153, 50, 204],
	'FUCHSIA': [255, 0, 255],
	'SLATEBLUE': [106, 90, 205],
	'MEDIUMSLATEBLUE': [127, 104, 238],
	'MEDIUMORCHID': [186, 85, 211],
	'MEDIUMPURPLE': [147, 112, 219],
	'ORCHID': [218, 112, 214],
	'VIOLET': [238, 130, 238],
	'PLUM': [221, 160, 221],
	'THISTLE': [216, 191, 216],
	'LAVENDER': [230, 230, 250],
	# Green
	'DARKGREEN': [0, 100, 0],
	'GREEN': [0, 128, 0],
	'DARKOLIVEGREEN': [85, 107, 47],
	'FORESTGREEN': [34, 139, 34],
	'SEAGREEN': [46, 139, 87],
	'DARKSLATEGRAY': [47, 79, 79],
	'OLIVE': [128, 128, 0],
	'OLIVEDRAB': [107, 142, 35],
	'MEDIUMSEAGREEN': [60, 179, 113],
	'LIMEGREEN': [50, 205, 50],
	'LIME': [0, 255, 0],
	'SPRINGGREEN': [0, 255, 127],
	'MEDIUMSPRINGGREEN': [0, 250, 154],
	'DARKSEAGREEN': [143, 188, 143],
	'MEDIUMAQUAMARINE': [102, 205, 170],
	'YELLOWGREEN': [154, 205, 50],
	'LAWNGREEN': [124, 252, 0],
	'CHARTREUSE': [127, 255, 0],
	'LIGHTGREEN': [144, 238, 144],
	'GREENYELLOW': [173, 255, 47],
	'PALEGREEN': [152, 251, 152],
	# Aqua
	'TEAL': [0, 128, 128],
	'DARKCYAN': [0, 139, 139],
	'LIGHTSEAGREEN': [32, 178, 170],
	'CADETBLUE': [95, 158, 160],
	'DARKTURQUOISE': [0, 206, 209],
	'MEDIUMTURQUOISE': [72, 209, 204],
	'TURQUOISE': [64, 224, 208],
	'AQUA': [0, 255, 255],
	'AQUAMARINE': [127, 255, 212],
	'SKYBLUE': [135, 206, 235],
	'LIGHTSKYBLUE': [135, 206, 250],
	'LIGHTSTEELBLUE': [176, 196, 222],
	'LIGHTBLUE': [173, 216, 230],
	'POWDERBLUE': [176, 224, 230],
	'PALETURQUOISE': [175, 238, 238],
	# Blue
	'MIDNIGHTBLUE': [25, 25, 112],
	'NAVY': [0, 0, 128],
	'DARKBLUE': [0, 0, 139],
	'MEDIUMBLUE': [0, 0, 205],
	'BLUE': [0, 0, 255],
	'ROYALBLUE': [65, 105, 225],
	'STEELBLUE': [90, 130, 180],
	'DODGERBLUE': [30, 144, 255],
	'DEEPSKYBLUE': [0, 191, 255],
	'CORNFLOWERBLUE': [100, 149, 237],
	# Brown
	'BROWN': [165, 42, 42],
	'SADDLEBROWN': [139, 69, 19],
	'SIENNA': [160, 82, 45],
	'CHOCOLATE': [210, 105, 30],
	'DARKGOLDENROD': [184, 134, 11],
	'PERU': [205, 133, 63],
	'ROSYBROWN': [188, 143, 143],
	'GOLDENROD': [218, 165, 32],
	'SANDYBROWN': [244, 164, 96],
	'TAN': [210, 180, 140],
	'BURLYWOOD': [222, 184, 135],
	'WHEAT': [245, 222, 179],
	'NAVAJOWHITE': [255, 222, 173],
	'BISQUE': [255, 228, 196],
	'BLANCHEDALMOND': [255, 235, 205],
	# White
	'WHITE': [255, 255, 255],
	'SNOW': [255, 250, 250],
	'HONEYDEW': [240, 255, 240],
	'MINTCREAM': [245, 255, 250],
	'AZURE': [240, 255, 255],
	'LIGHTCYAN': [224, 255, 255],
	'ALICEBLUE': [240, 248, 255],
	'GHOSTWHITE': [248, 248, 255],
	'WHITESMOKE': [245, 245, 245],
	'SEASHELL': [255, 245, 238],
	'BEIGE': [245, 245, 220],
	'OLDLACE': [253, 245, 230],
	'FLORALWHITE': [255, 250, 240],
	'IVORY': [255, 255, 240],
	'ANTIQUEWHITE': [250, 235, 215],
	'LINEN': [250, 240, 230],
	'LAVENDERBLUSH': [255, 240, 245],
	'MISTYROSE': [255, 228, 225],
	'PAPAYAWHIP': [255, 239, 213],
	'LIGHTGOLDENRODYELLOW': [250, 250, 210],
	'CORNSILK': [255, 248, 220],
	'LEMONCHIFFON': [255, 250, 205],
	'LIGHTYELLOW': [255, 255, 224],
	# Gray and black
	'BLACK': [0, 0, 0],
	'DARKGRAY': [64, 64, 64],
	'DIMGRAY': [105, 105, 105],
	'SLATEGRAY': [112, 128, 144],
	'GRAY': [128, 128, 128],
	'LIGHTSLATEGRAY': [119, 136, 153],
	'SILVER': [192, 192, 192],
	'LIGHTGRAY': [211, 211, 211],
	'GAINSBORO': [220, 220, 220],
}

def DecColor(color_name: str) -> list[int, int, int]:
	"""
	Returns a decimal color value.

	:param color_name: Color name
	:return: Decimal color value
	"""
	if color_name in ColorPicker:
		return ColorPicker[color_name]
	else:
		raise ColorException("This color is not in the dictionary")

def HexColor(color_name: str) -> str:
	"""
	Returns a hexadecimal color value.

	:param color_name: Color name
	:return: Hexadecimal color value
	"""
	return '{:02x}{:02x}{:02x}'.format(*DecColor(color_name))

def AnsiColor(color_name: str, color_ground: str) -> str:
	"""
	Returns an ANSI color value.\n
	In AnsiFormat, the following levels are available under the "color/set/..." path:\n
	- foreground
	- background
	- bright foreground
	- bright background
	- underline

	:param color_name: Color name
	:param color_ground: Color level
	:return: ANSI color value
	"""
	return GetAnsiFormat("color/set/{}/{};{};{}".format(color_ground, *DecColor(color_name)))

def Dec2Hex(dec_colors: list[int, int, int]) -> str:
	"""
	Converts a decimal color value to a hexadecimal.

	:param dec_colors: Decimal color value
	:return: Hexadecimal color value
	"""
	return '{:02x}{:02x}{:02x}'.format(*dec_colors)

def Dec2Ansi(dec_colors: list[int, int, int], color_ground: str) -> str:
	"""
	Converts a decimal color value to an ANSI escape code.

	:param dec_colors: Decimal color value
	:param color_ground: Color level (read AnsiColor() function documentation)
	:return: ANSI escape code color value
	"""
	return GetAnsiFormat("color/set/{}/{};{};{}".format(color_ground, *dec_colors))

def Hex2Dec(hex_color: str) -> list[int, int, int]:
	"""
	Converts a hexadecimal color value to a decimal.

	:param hex_color: Hexadecimal color value
	:return: Decimal color value
	"""
	return [
		int(hex_color[:2], base=16),
		int(hex_color[2:4], base=16),
		int(hex_color[4:], base=16)
	]

def Hex2Ansi(hex_color: str, color_ground: str) -> str:
	"""
	Converts a hexadecimal color value to an ANSI escape code.

	:param hex_color: Hexadecimal color value
	:param color_ground: Color level (read AnsiColor() function documentation)
	:return: ANSI escape code color value
	"""
	return GetAnsiFormat("color/set/{}/{};{};{}".format(
		color_ground,
		int(hex_color[:2], base=16),
		int(hex_color[2:4], base=16),
		int(hex_color[4:], base=16)
	))

def Ansi2Dec(ansi_color: str) -> list[int, int, int]:
	"""
	Converts an ANSI escape code color value to a decimal.
	When converting to ANSI escape code, you need to know which level the color is applied
	to, and when from ANSI escape code, you don’t need to, because in other formats the levels
	are defined differently and are not included in the command along with the color.

	:param ansi_color: ANSI escape code color value
	:return: Decimal color value
	"""
	return [
		int(ansi_color.split(';')[2]),
		int(ansi_color.split(';')[3]),
		int(ansi_color.split(';')[4][:-1])
	]

def Ansi2Hex(ansi_color: str) -> str:
	"""
	Converts an ANSI escape code color value to a hexadecimal.
	When converting to ANSI escape code, you need to know which level the color is applied
	to, and when from ANSI escape code, you don’t need to, because in other formats the levels
	are defined differently and are not included in the command along with the color.

	:param ansi_color: ANSI escape code color value
	:return: Hexadecimal color value
	"""
	return '{:02x}{:02x}{:02x}'.format(
		int(ansi_color.split(';')[2]),
		int(ansi_color.split(';')[3]),
		int(ansi_color.split(';')[4][:-1])
	)
