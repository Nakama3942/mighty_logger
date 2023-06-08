"""
A module with the icon sets.
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

class IconSetType:
	"""
	Template class for creating custom icon sets.
	"""
	debug = ''
	debug_performance = ''
	performance = ''
	event = ''
	audit = ''
	metrics = ''
	user = ''
	message = ''
	info = ''
	notice = ''
	warning = ''
	error = ''
	critical = ''
	process = ''
	success = ''
	fail = ''

class EmptyIconSet(IconSetType):
	...

class IconSet1(IconSetType):
	"""
	First icon set.
	"""
	debug = '🐛'
	debug_performance = '⏱️'
	performance = '⏱️'
	event = '🔔'
	audit = '🔍'
	metrics = '📊'
	user = '👤'
	message = '💬'
	info = 'ℹ️'
	notice = '📌'
	warning = '⚠️'
	error = '❌'
	critical = '🔥'
	process = '⏳'
	success = '✔️'
	fail = '❌'

class IconSet2(IconSetType):
	"""
	Second icon set.
	"""
	debug = '🐞'
	debug_performance = '⌛️'
	performance = '🚀'
	event = '🎉'
	audit = '🔒'
	metrics = '📈'
	user = '👥'
	message = '📝'
	info = '🔍'
	notice = '📎'
	warning = '⚡️'
	error = '🚫'
	critical = '🚨'
	process = '🔄'
	success = '🎉'
	fail = '🚫'

class IconSet3(IconSetType):
	"""
	Third icon set.
	"""
	debug = '🚧'
	debug_performance = '🔍'
	performance = '📊'
	event = '📣'
	audit = '📋'
	metrics = '📉'
	user = '🙋‍♂️'
	message = '🗒️'
	info = '📌'
	notice = '🔖'
	warning = '⛔️'
	error = '💔'
	critical = '⛔️'
	process = '⚙️'
	success = '👍'
	fail = '👎'

class IconSet4(IconSetType):
	"""
	Fourth icon set.
	"""
	debug = '🔬'
	debug_performance = '📈'
	performance = '⚡️'
	event = '🚨'
	audit = '🔐'
	metrics = '📄'
	user = '🙋‍♀️'
	message = '📨'
	info = '🔔'
	notice = '🚩'
	warning = '🔺'
	error = '🔴'
	critical = '🚒'
	process = '🕰️'
	success = '✅'
	fail = '❎'
