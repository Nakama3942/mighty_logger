"""
A module with implementation of entry status messages.
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

from mighty_logger.basic.lib_types.status_message_type import StatusMessageType

class StatusMessagePatterns:
	"""
	A class that emits the desired status message templates.
	"""
	@staticmethod
	def completed() -> StatusMessageType:
		return StatusMessageType("Completed")

	@staticmethod
	def failed() -> StatusMessageType:
		return StatusMessageType("Failed")

	@staticmethod
	def skipped() -> StatusMessageType:
		return StatusMessageType("Skipped")

	@staticmethod
	def lost() -> StatusMessageType:
		return StatusMessageType("Lost")

	@staticmethod
	def removed() -> StatusMessageType:
		return StatusMessageType("Removed")

	@staticmethod
	def created() -> StatusMessageType:
		return StatusMessageType("Created")

	@staticmethod
	def updated() -> StatusMessageType:
		return StatusMessageType("Updated")

	@staticmethod
	def loaded() -> StatusMessageType:
		return StatusMessageType("Loaded")

	@staticmethod
	def imported() -> StatusMessageType:
		return StatusMessageType("Imported")

	@staticmethod
	def exported() -> StatusMessageType:
		return StatusMessageType("Exported")

	@staticmethod
	def sent() -> StatusMessageType:
		return StatusMessageType("Sent")

	@staticmethod
	def received() -> StatusMessageType:
		return StatusMessageType("Received")

	@staticmethod
	def done() -> StatusMessageType:
		return StatusMessageType("Done")

	@staticmethod
	def canceled() -> StatusMessageType:
		return StatusMessageType("Canceled")

	@staticmethod
	def rejected() -> StatusMessageType:
		return StatusMessageType("Rejected")

	@staticmethod
	def activated() -> StatusMessageType:
		return StatusMessageType("Activated")

	@staticmethod
	def deactivated() -> StatusMessageType:
		return StatusMessageType("Deactivated")

	@staticmethod
	def awaiting() -> StatusMessageType:
		return StatusMessageType("Awaiting")

	@staticmethod
	def locked() -> StatusMessageType:
		return StatusMessageType("Locked")

	@staticmethod
	def unlocked() -> StatusMessageType:
		return StatusMessageType("Unlocked")

	@staticmethod
	def saved() -> StatusMessageType:
		return StatusMessageType("Saved")

	@staticmethod
	def moved() -> StatusMessageType:
		return StatusMessageType("Moved")

	@staticmethod
	def copied() -> StatusMessageType:
		return StatusMessageType("Copied")

	@staticmethod
	def restored() -> StatusMessageType:
		return StatusMessageType("Restored")

	@staticmethod
	def checked() -> StatusMessageType:
		return StatusMessageType("Checked")

	@staticmethod
	def verified() -> StatusMessageType:
		return StatusMessageType("Verified")

	@staticmethod
	def approved() -> StatusMessageType:
		return StatusMessageType("Approved")

	@staticmethod
	def confirmed() -> StatusMessageType:
		return StatusMessageType("Confirmed")

	@staticmethod
	def changed() -> StatusMessageType:
		return StatusMessageType("Changed")

	@staticmethod
	def reloaded() -> StatusMessageType:
		return StatusMessageType("Reloaded")

	@staticmethod
	def launched() -> StatusMessageType:
		return StatusMessageType("Launched")

	@staticmethod
	def stopped() -> StatusMessageType:
		return StatusMessageType("Stopped")

	@staticmethod
	def suspended() -> StatusMessageType:
		return StatusMessageType("Suspended")

	@staticmethod
	def renewed() -> StatusMessageType:
		return StatusMessageType("Renewed")

	@staticmethod
	def included() -> StatusMessageType:
		return StatusMessageType("Included")

	@staticmethod
	def exclude() -> StatusMessageType:
		return StatusMessageType("Exclude")

	@staticmethod
	def installed() -> StatusMessageType:
		return StatusMessageType("Installed")

	@staticmethod
	def reset() -> StatusMessageType:
		return StatusMessageType("Reset")

	@staticmethod
	def connected() -> StatusMessageType:
		return StatusMessageType("Connected")

	@staticmethod
	def disconnected() -> StatusMessageType:
		return StatusMessageType("Disconnected")

	@staticmethod
	def enabled() -> StatusMessageType:
		return StatusMessageType("Enabled")

	@staticmethod
	def disabled() -> StatusMessageType:
		return StatusMessageType("Disabled")

	@staticmethod
	def inserted() -> StatusMessageType:
		return StatusMessageType("Inserted")

	@staticmethod
	def extracted() -> StatusMessageType:
		return StatusMessageType("Extracted")

	@staticmethod
	def open() -> StatusMessageType:
		return StatusMessageType("Open")

	@staticmethod
	def closed() -> StatusMessageType:
		return StatusMessageType("Closed")

	@staticmethod
	def empty() -> StatusMessageType:
		return StatusMessageType("...")

	@staticmethod
	def custom(custom_status_message: str) -> StatusMessageType:
		return StatusMessageType(custom_status_message)
