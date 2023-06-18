"""
A module with a list of environment options in which the modules work
and entry types that can be passed to an entry in Progress bar.
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

class LogEnvironments:
	"""
	Environments of Logger.
	"""
	CONSOLE = 'console'
	HTML = 'html'

class TypesEntries:
	"""
	Entries types of Logger.
	Use for Logger.note_process().
	"""
	DEBUG = 'debug'
	DEBUG_PERFORMANCE = 'debug_performance'
	PERFORMANCE = 'performance'
	EVENT = 'event'
	AUDIT = 'audit'
	METRICS = 'metrics'
	USER = 'user'
	MESSAGE = 'message'
	INFO = 'info'
	NOTICE = 'notice'
	WARNING = 'warning'
	ERROR = 'error'
	CRITICAL = 'critical'
	RESOLVED = 'resolved'
	UNRESOLVED = 'unresolved'
	ACHIEVEMENT = '_achievement'
	MILESTONE = '_milestone'
	START_TIMER = 'start_timer'
	TIMER_MARK = 'timer_mark'
	STOP_TIMER = 'stop_timer'
