#  Copyright © 2023 Kalynovsky Valentin. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import datetime, platform, os

ColorPickerQ = {
	'RED': '#dc0000',
	'DARKRED': '#8b0000',
	'ORANGE': '#ffa500',
	'DARKORANGE': '#ff8c00',
	'YELLOW': '#ffff00',
	'DARKYELLOW': '#ffcc00',
	'GREEN': '#008000',
	'DARKGREEN': '#006400',
	'CYAN': '#00ffff',
	'DARKCYAN': '#008b8b',
	'VIOLET': '#9400d3',
	'DARKVIOLET': '#800080',
	'GREY': '#a9a9a9',
	'DARKGREY': '#808080',
}

class PickerModifierQ:
	def __init__(self):
		pass

	def setHexColor(self, colorName: str, hexColorValue: str):
		ColorPickerQ[colorName] = hexColorValue

	def setColor(self, colorName: str, red: int, green: int, blue: int):
		ColorPickerQ[colorName] = f'#{hex(red)}{hex(green)}{hex(blue)}'

class LoggerQ:
	def __init__(self, time=True, name=True, status=True, status_message=True, status_type=True, message=True):
		self.time = time
		self.name = name
		self.status = status
		self.status_message = status_message
		self.status_type = status_type
		self.message = message

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

	def DEBUG(self, status_message_text: str = "", message_text: str = "") -> str:
		log = ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['GREY']};'>@DEBUG -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKGREY']};'>{message_text}</span>" if self.message else ""
		return log

	def INFO(self, status_message_text: str = "", message_text: str = "") -> str:
		log = ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['CYAN']};'>@INFO -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKCYAN']};'>{message_text}</span>" if self.message else ""
		return log

	def WARNING(self, status_message_text: str = "", message_text: str = "") -> str:
		log = ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['YELLOW']};'>@WARNING -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKYELLOW']};'>{message_text}</span>" if self.message else ""
		return log

	def ERROR(self, status_message_text: str = "", message_text: str = "") -> str:
		log = ""
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>!ERROR -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		return log

	def CRITICAL(self, status_message_text: str = "", message_text: str = "") -> str:
		log = f"<b>"
		log += f"<span style='color: {ColorPickerQ['VIOLET']};'>*{datetime.datetime.now()}</span>\t" if self.time else ""
		log += f"<span style='color: {ColorPickerQ['DARKVIOLET']};'>${platform.node()}^{os.getlogin()}</span>\t" if self.name else ""
		log += f"<span style='color: {ColorPickerQ['ORANGE']};'>#STATUS:</span>\t" if self.status else ""
		log += f"<span style='color: {ColorPickerQ['DARKORANGE']};'>{status_message_text}</span>\t" if self.status_message else ""
		log += f"<span style='color: {ColorPickerQ['RED']};'>!!!@CRITICAL -</span>\t" if self.status_type else ""
		log += f"<span style='color: {ColorPickerQ['DARKRED']};'>{message_text}</span>" if self.message else ""
		log += f"</b>"
		return log


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
