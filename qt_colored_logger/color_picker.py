# ##########################   Qt_Сolored-logger   ########################### #
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

ColorPicker = {
	# https://en.wikipedia.org/wiki/Web_colors
	# Red
	'MAROON': ['800000', [128, 0, 0], '\033[38;2;128;0;0m'],
	'DARKRED': ['8b0000', [139, 0, 0], '\033[38;2;139;0;0m'],
	'RED': ['ff0000', [255, 0, 0], '\033[38;2;255;0;0m'],
	'LIGHTRED': ['ff3333', [255, 51, 51], '\033[38;2;255;51;51m'],
	'FIREBRICK': ['b22222', [178, 34, 34], '\033[38;2;178;34;34m'],
	'CRIMSON': ['Dc143c', [220, 20, 60], '\033[38;2;220;20;60m'],
	'INDIANRED': ['cd5c5c', [205, 92, 92], '\033[38;2;205;92;92m'],
	'LIGHTCORAL': ['f08080', [240, 158, 128], '\033[38;2;240;158;128m'],
	'SALMON': ['fa8072', [250, 128, 114], '\033[38;2;250;128;114m'],
	'DARKSALMON': ['e9967a', [133, 150, 122], '\033[38;2;133;150;122m'],
	'LIGHTSALMON': ['ffa07a', [255, 160, 122], '\033[38;2;255;160;122m'],
	# Pink
	'MEDIUMVIOLETRED': ['c71585', [199, 21, 133], '\033[38;2;199;21;133m'],
	'DEEPPINK': ['ff1493', [255, 20, 147], '\033[38;2;255;20;147m'],
	'PALEVIOLETRED': ['db7093', [219, 112, 147], '\033[38;2;219;112;147m'],
	'HOTPINK': ['ff69b4', [255, 105, 180], '\033[38;2;255;105;180m'],
	'LIGHTPINK': ['ffb6c1', [255, 182, 193], '\033[38;2;255;182;193m'],
	'PINK': ['ffc0cb', [255, 192, 203], '\033[38;2;255;192;203m'],
	# Orange
	'ORANGERED': ['ff4500', [255, 69, 0], '\033[38;2;255;69;0m'],
	'TOMATO': ['ff6347', [255, 99, 71], '\033[38;2;255;99;71m'],
	'DARKORANGE': ['ff8c00', [255, 140, 0], '\033[38;2;255;140;0m'],
	'CORAL': ['ff7f50', [255, 127, 80], '\033[38;2;255;127;80m'],
	'ORANGE': ['ffa500', [255, 165, 0], '\033[38;2;255;165;0m'],
	# Yellow
	'DARKKHAKI': ['bdb76b', [189, 183, 107], '\033[38;2;189;183;107m'],
	'GOLD': ['ffd700', [255, 215, 0], '\033[38;2;255;215;0m'],
	'KHAKI': ['f0e68c', [240, 230, 140], '\033[38;2;240;230;140m'],
	'PEACHPUFF': ['ffdab9', [255, 218, 185], '\033[38;2;255;218;185m'],
	'YELLOW': ['ffff00', [255, 255, 0], '\033[38;2;255;255;0m'],
	'DARKYELLOW': ['ffcc00', [255, 204, 0], '\033[38;2;255;204;0m'],
	'PALEGOLDENROD': ['eee8aa', [238, 232, 170], '\033[38;2;238;232;170m'],
	'MOCCASIN': ['ffe4b5', [255, 228, 181], '\033[38;2;255;228;181m'],
	# Purple
	'INDIGO': ['4b0082', [75, 0, 130], '\033[38;2;75;0;130m'],
	'PURPLE': ['800080', [128, 0, 128], '\033[38;2;128;0;128m'],
	'DARKMAGENTA': ['8b008b', [139, 0, 139], '\033[38;2;139;0;139m'],
	'DARKVIOLET': ['9400d3', [148, 0, 211], '\033[38;2;148;0;211m'],
	'DARKSLATEBLUE': ['483d8b', [82, 61, 139], '\033[38;2;82;61;139m'],
	'BLUEVIOLET': ['8a2be2', [138, 43, 226], '\033[38;2;138;43;226m'],
	'DARKORCHID': ['9932cc', [153, 50, 204], '\033[38;2;153;50;204m'],
	'FUCHSIA': ['ff00ff', [255, 0, 255], '\033[38;2;255;0;255m'],
	'SLATEBLUE': ['6a5acd', [106, 90, 205], '\033[38;2;106;90;205m'],
	'MEDIUMSLATEBLUE': ['7b68ee', [127, 104, 238], '\033[38;2;127;104;238m'],
	'MEDIUMORCHID': ['ba55d3', [186, 85, 211], '\033[38;2;186;85;211m'],
	'MEDIUMPURPLE': ['9370db', [147, 112, 219], '\033[38;2;147;112;219m'],
	'ORCHID': ['da70d6', [218, 112, 214], '\033[38;2;218;112;214m'],
	'VIOLET': ['ee82ee', [238, 130, 238], '\033[38;2;238;130;238m'],
	'PLUM': ['dda0dd', [221, 160, 221], '\033[38;2;221;160;221m'],
	'THISTLE': ['d8bfd8', [216, 191, 216], '\033[38;2;216;191;216m'],
	'LAVENDER': ['e6e6fa', [230, 230, 250], '\033[38;2;230;230;250m'],
	# Green
	'DARKGREEN': ['006400', [0, 100, 0], '\033[38;2;0;100;0m'],
	'GREEN': ['008000', [0, 128, 0], '\033[38;2;0;128;0m'],
	'DARKOLIVEGREEN': ['556b2f', [85, 107, 47], '\033[38;2;85;107;47m'],
	'FORESTGREEN': ['228b22', [34, 139, 34], '\033[38;2;34;139;34m'],  # -
	'SEAGREEN': ['2e8b57', [46, 139, 87], '\033[38;2;46;139;87m'],
	'DARKSLATEGRAY': ['2f4f4f', [47, 79, 79], '\033[38;2;47;79;79m'],
	'OLIVE': ['808000', [128, 128, 0], '\033[38;2;128;128;0m'],
	'OLIVEDRAB': ['6b8e23', [107, 142, 35], '\033[38;2;107;142;35m'],
	'MEDIUMSEAGREEN': ['3cb371', [60, 179, 113], '\033[38;2;60;179;113m'],
	'LIMEGREEN': ['32cd32', [50, 205, 50], '\033[38;2;50;205;50m'],
	'LIME': ['00ff00', [0, 255, 0], '\033[38;2;0;255;0m'],
	'SPRINGGREEN': ['00ff7f', [0, 255, 127], '\033[38;2;0;255;127m'],
	'MEDIUMSPRINGGREEN': ['00fa9a', [0, 250, 154], '\033[38;2;0;250;154m'],
	'DARKSEAGREEN': ['8fbc8f', [143, 188, 143], '\033[38;2;143;188;143m'],
	'MEDIUMAQUAMARINE': ['66cdaa', [102, 205, 170], '\033[38;2;102;205;170m'],
	'YELLOWGREEN': ['9acd32', [154, 205, 50], '\033[38;2;154;205;50m'],
	'LAWNGREEN': ['7cfc00', [124, 252, 0], '\033[38;2;124;252;0m'],
	'CHARTREUSE': ['7fff00', [127, 255, 0], '\033[38;2;127;255;0m'],
	'LIGHTGREEN': ['90ee90', [144, 238, 144], '\033[38;2;144;238;144m'],
	'GREENYELLOW': ['adff2f', [173, 255, 47], '\033[38;2;173;255;47m'],
	'PALEGREEN': ['98fb98', [152, 251, 152], '\033[38;2;152;251;152m'],
	# Aqua
	'TEAL': ['008080', [0, 128, 128], '\033[38;2;0;128;128m'],
	'DARKCYAN': ['008b8b', [0, 139, 139], '\033[38;2;0;139;139m'],
	'LIGHTSEAGREEN': ['20b2aa', [32, 178, 170], '\033[38;2;32;178;170m'],
	'CADETBLUE': ['5f9ea0', [95, 158, 160], '\033[38;2;95;158;160m'],
	'DARKTURQUOISE': ['00ced1', [0, 206, 209], '\033[38;2;0;206;209m'],
	'MEDIUMTURQUOISE': ['48d1cc', [72, 209, 204], '\033[38;2;72;209;204m'],
	'TURQUOISE': ['40e0d0', [64, 224, 208], '\033[38;2;64;224;208m'],
	'AQUA': ['00ffff', [0, 255, 255], '\033[38;2;0;255;255m'],
	'AQUAMARINE': ['7fffd4', [127, 255, 212], '\033[38;2;127;255;212m'],
	'SKYBLUE': ['87ceeb', [135, 206, 235], '\033[38;2;135;206;235m'],
	'LIGHTSKYBLUE': ['87cefa', [135, 206, 250], '\033[38;2;135;206;250m'],
	'LIGHTSTEELBLUE': ['b0c4de', [176, 196, 222], '\033[38;2;176;196;222m'],
	'LIGHTBLUE': ['add8e6', [173, 216, 230], '\033[38;2;173;216;230m'],
	'POWDERBLUE': ['b0e0e6', [176, 224, 230], '\033[38;2;176;224;230m'],
	'PALETURQUOISE': ['afeeee', [175, 238, 238], '\033[38;2;175;238;238m'],
	# Blue
	'MIDNIGHTBLUE': ['191970', [25, 25, 112], '\033[38;2;25;25;112m'],
	'NAVY': ['000080', [0, 0, 128], '\033[38;2;0;0;128m'],
	'DARKBLUE': ['00008b', [0, 0, 139], '\033[38;2;0;0;139m'],
	'MEDIUMBLUE': ['0000cd', [0, 0, 205], '\033[38;2;0;0;205m'],
	'BLUE': ['0000ff', [0, 0, 255], '\033[38;2;0;0;255m'],
	'ROYALBLUE': ['4169e1', [65, 105, 225], '\033[38;2;65;105;225m'],
	'STEELBLUE': ['4682b4', [90, 130, 180], '\033[38;2;90;130;180m'],
	'DODGERBLUE': ['1e90ff', [30, 144, 255], '\033[38;2;30;144;255m'],
	'DEEPSKYBLUE': ['00bfff', [0, 191, 255], '\033[38;2;0;191;255m'],
	'CORNFLOWERBLUE': ['6495ed', [100, 149, 237], '\033[38;2;100;149;237m'],
	# Brown
	'BROWN': ['a52a2a', [165, 42, 42], '\033[38;2;165;42;42m'],
	'SADDLEBROWN': ['8b4513', [139, 69, 19], '\033[38;2;139;69;19m'],
	'SIENNA': ['a0522d', [160, 82, 45], '\033[38;2;160;82;45m'],
	'CHOCOLATE': ['d2691e', [210, 105, 30], '\033[38;2;210;105;30m'],
	'DARKGOLDENROD': ['b8860b', [184, 134, 11], '\033[38;2;184;134;11m'],
	'PERU': ['cd853f', [205, 133, 63], '\033[38;2;205;133;63m'],
	'ROSYBROWN': ['bc8f8f', [188, 143, 143], '\033[38;2;188;143;143m'],
	'GOLDENROD': ['daa520', [218, 165, 32], '\033[38;2;218;165;32m'],
	'SANDYBROWN': ['f4a460', [244, 164, 96], '\033[38;2;244;164;96m'],
	'TAN': ['d2b48c', [210, 180, 140], '\033[38;2;210;180;140m'],
	'BURLYWOOD': ['deb887', [222, 184, 135], '\033[38;2;222;184;135m'],
	'WHEAT': ['f5deb3', [245, 222, 179], '\033[38;2;245;222;179m'],
	'NAVAJOWHITE': ['ffdead', [255, 222, 173], '\033[38;2;255;222;173m'],
	'BISQUE': ['ffe4c4', [255, 228, 196], '\033[38;2;255;228;196m'],
	'BLANCHEDALMOND': ['ffebcd', [255, 235, 205], '\033[38;2;255;235;205m'],
	# White
	'WHITE': ['ffffff', [255, 255, 255], '\033[38;2;255;255;255m'],
	'SNOW': ['fffafa', [255, 250, 250], '\033[38;2;255;250;250m'],
	'HONEYDEW': ['f0fff0', [240, 255, 240], '\033[38;2;240;255;240m'],
	'MINTCREAM': ['f5fffa', [245, 255, 250], '\033[38;2;245;255;250m'],
	'AZURE': ['f0ffff', [240, 255, 255], '\033[38;2;240;255;255m'],
	'LIGHTCYAN': ['e0ffff', [224, 255, 255], '\033[38;2;224;255;255m'],
	'ALICEBLUE': ['f0f8ff', [240, 248, 255], '\033[38;2;240;248;255m'],
	'GHOSTWHITE': ['f8f8ff', [248, 248, 255], '\033[38;2;248;248;255m'],
	'WHITESMOKE': ['f5f5f5', [245, 245, 245], '\033[38;2;245;245;245m'],
	'SEASHELL': ['fff5ee', [255, 245, 238], '\033[38;2;255;245;238m'],
	'BEIGE': ['f5f5dc', [245, 245, 220], '\033[38;2;245;245;220m'],
	'OLDLACE': ['fdf5e6', [253, 245, 230], '\033[38;2;253;245;230m'],
	'FLORALWHITE': ['fffaf0', [255, 250, 240], '\033[38;2;255;250;240m'],
	'IVORY': ['fffff0', [255, 255, 240], '\033[38;2;255;255;240m'],
	'ANTIQUEWHITE': ['faebd7', [250, 235, 215], '\033[38;2;250;235;215m'],
	'LINEN': ['faf0e6', [250, 240, 230], '\033[38;2;250;240;230m'],
	'LAVENDERBLUSH': ['fff0f5', [255, 240, 245], '\033[38;2;255;240;245m'],
	'MISTYROSE': ['ffe4e1', [255, 228, 225], '\033[38;2;255;228;225m'],
	'PAPAYAWHIP': ['ffefd5', [255, 239, 213], '\033[38;2;255;239;213m'],
	'LIGHTGOLDENRODYELLOW': ['fafad2', [250, 250, 210], '\033[38;2;255;255;210m'],
	'CORNSILK': ['fff8dc', [255, 248, 220], '\033[38;2;255;248;220m'],
	'LEMONCHIFFON': ['fffacd', [255, 250, 205], '\033[38;2;255;250;205m'],
	'LIGHTYELLOW': ['ffffe0', [255, 255, 224], '\033[38;2;255;255;224m'],
	# Gray and black
	'BLACK': ['000000', [0, 0, 0], '\033[38;2;0;0;0m'],
	'DARKGRAY': ['404040', [64, 64, 64], '\033[38;2;64;64;64m'],
	'DIMGRAY': ['696969', [105, 105, 105], '\033[38;2;105;105;105m'],
	'SLATEGRAY': ['708090', [112, 128, 144], '\033[38;2;112;128;144m'],
	'GRAY': ['808080', [128, 128, 128], '\033[38;2;128;128;128m'],
	'LIGHTSLATEGRAY': ['778899', [119, 136, 153], '\033[38;2;119;136;153m'],
	'SILVER': ['c0c0c0', [192, 192, 192], '\033[38;2;192;192;192m'],
	'LIGHTGRAY': ['d3d3d3', [211, 211, 211], '\033[38;2;211;211;211m'],
	'GAINSBORO': ['dcdcdc', [220, 220, 220], '\033[38;2;220;220;220m'],
}

def HexColor(color_name: str) -> str:
	from qt_colored_logger import ColorException
	if color_name in ColorPicker:
		return ColorPicker[color_name][0]
	else:
		raise ColorException("This color is not in the dictionary")

def DecColor(color_name: str) -> [int, int, int]:
	from qt_colored_logger import ColorException
	if color_name in ColorPicker:
		return ColorPicker[color_name][1]
	else:
		raise ColorException("This color is not in the dictionary")

def CodColor(color_name: str) -> str:
	from qt_colored_logger import ColorException
	if color_name in ColorPicker:
		return ColorPicker[color_name][2]
	else:
		raise ColorException("This color is not in the dictionary")

# Test
if __name__ == "__main__":
	print(HexColor('DIMGRAY'))
	print(DecColor('DIMGRAY'))
	print(f"{CodColor('AQUAMARINE')}Test string")
