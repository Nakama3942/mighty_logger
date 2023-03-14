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

# The idea is taken here:
# https://github.com/Nakama3942/WiretappingScanner/commit/da5e0e71681b9e1462d5bba5438fc8b1fde8142e

import datetime, platform, os, random

ColorPickerQ = {
	'RED': '#dc0000',
	'DARKRED': '#8b0000',
	'ORANGE': '#ffa500',
	'DARKORANGE': '#ff8c00',
	'YELLOW': '#ffff00',
	'DARKYELLOW': '#ffcc00',
	'GREEN': '#008000',
	'DARKGREEN': '#006400',
	'BLUE': '#00ffff',
	'DARKBLUE': '#008b8b',
	'OCEANBLUE': '#0000dd',
	'DARKOCEANBLUE': '#00009b',
	'VIOLET': '#9400d3',
	'DARKVIOLET': '#800080',
	'GREY': '#a9a9a9',
	'DARKGREY': '#808080',
}

class PickerModifierQ:
	def __init__(self):
		pass

	def setHexColor(self, color_name: str, hex_color_value: str):
		ColorPickerQ[color_name] = hex_color_value

	def setColor(self, color_name: str, red: int, green: int, blue: int):
		ColorPickerQ[color_name] = f'#{hex(red)}{hex(green)}{hex(blue)}'

class LoggerQ:
	def __init__(self, time=True, name=True, status=True, status_message=True, status_type=True, message=True):
		self.time = time
		self.name = name
		self.status = status
		self.status_message = status_message
		self.status_type = status_type
		self.message = message
		self.ID = random.randint(1000000, 9999999)

	def timeEnabled(self, enabled: bool):
		self.time = enabled

	def nameEnabled(self, enabled: bool):
		self.name = enabled

	def statusEnabled(self, enabled: bool):
		self.status = enabled

	def status_messageEnabled(self, enabled: bool):
		self.status_message = enabled

	def status_typeEnabled(self, enabled: bool):
		self.status_type = enabled

	def messageEnabled(self, enabled: bool):
		self.message = enabled

	def DEBUG(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['GREY']};'>@DEBUG -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKGREY']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def INFO(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['OKEANBLUE']};'>@INFO -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKOKEANBLUE']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def WARNING(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['YELLOW']};'>@WARNING -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKYELLOW']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def ERROR(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>!ERROR -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def CRITICAL(self, status_message_text: str = "", message_text: str = "", bold: bool = True, italic: bool = False) -> str:
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>!!!@CRITICAL -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def SUCCESS(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = True) -> str:
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['GREEN']};'>@SUCCESS -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKGREEN']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def FAIL(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = True) -> str:
		log = ""
		log += f"<b>" if bold else ""
		log += f"<i>" if italic else ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>@FAIL -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		log += f"</i>" if italic else ""
		log += f"</b>" if bold else ""
		return log

	def START_PROCESS(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		# log = ""
		# log += f"<b>" if bold else ""
		# log += f"<i>" if italic else ""
		# log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		# log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		# log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		# log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		# log += f"<span style='color: {ColorPickerQ['BLUE']};'>@PROGRESS -</span>\t" if self.status_type else ""
		# log += f"<span style='color: {ColorPickerQ['DARKBLUE']};'>{message_text}</span>" if self.message else ""
		# log += f"</i>" if italic else ""
		# log += f"</b>" if bold else ""
		# return log
		pass
		# Должен выполняться в потоке

	def STOP_PROCESS(self, status_message_text: str = "", message_text: str = "", bold: bool = False, italic: bool = False) -> str:
		pass
		# Сделать переход в SUCCESS


# if __name__ == '__main__':
# 	logger = Logger()
# 	print(logger.DEBUG("1"))
# 	print(logger.INFO("2"))
# 	print(logger.WARNING("3"))
# 	print(logger.ERROR("4"))
# 	print(logger.CRITICAL("5"))
#
# 	loggerMod = PickerModifier()
# 	loggerMod.setHexColor('RED', '#151719')
# 	loggerMod.setColor('DARKRED', 50, 80, 149)
#
# 	print(logger.CRITICAL("6"))
