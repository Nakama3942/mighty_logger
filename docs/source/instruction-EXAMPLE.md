## Example

```python
from time import sleep

from mighty_logger import Logger
from mighty_logger.src.lib_types_collection import LoggerEntryTypes, ProcessEntryTypes, LogEnvironments, SortingKeys, SelectionTypes
from mighty_logger.src import IndefiniteAnimations, DefiniteAnimations

if __name__ == "__main__":
	logger = Logger(program_name="Installer", log_environment=LogEnvironments.CONSOLE, console_width=115, global_background=True)
	logger.might().publish_author()

	logger.might().start_timer("Timer started")
	logger.message("Program installation started")

	sleep(1)
	logger.might().start_indefinite_process("File upload", IndefiniteAnimations.SuperSpace)
	sleep(2)
	logger.might().note_process(ProcessEntryTypes.achievement, "Files downloaded")
	sleep(3)
	logger.might().progress_rise(100)
	logger.might().stop_process("Files unzipped")

	logger.warning("Newer version found")
	logger.might().timer_mark("Timer mark")

	logger.might().separator()

	data = logger.might().getty("Enter password: ")

	sleep(1)
	logger.might().start_definite_process("Installing files", DefiniteAnimations.Arrow)
	sleep(0.6)
	logger.might().progress_rise(3)
	sleep(0.4)
	logger.might().progress_rise(7)
	sleep(0.3)
	logger.might().progress_rise(14)
	sleep(0.5)
	logger.might().progress_rise(16)
	sleep(1.1)
	logger.might().progress_rise(19)
	sleep(1.5)
	logger.might().progress_rise(25)
	sleep(1.4)
	logger.might().progress_rise(35)
	sleep(1.4)
	logger.might().progress_rise(45)
	sleep(1.6)
	logger.might().progress_rise(46)
	sleep(1.1)
	logger.might().progress_rise(47)
	logger.might().note_process(ProcessEntryTypes.milestone, "Files prepared")
	sleep(3.7)
	logger.might().progress_rise(76)
	sleep(1.5)
	logger.might().progress_rise(77)
	sleep(1.4)
	logger.might().progress_rise(79)
	sleep(1.1)
	logger.might().progress_rise(81)
	sleep(1.2)
	logger.might().progress_rise(82)
	sleep(1.3)
	logger.might().progress_rise(85)
	sleep(0.8)
	logger.might().note_process(LoggerEntryTypes.error, "Incompatibility found")
	sleep(1.3)
	logger.might().note_process(LoggerEntryTypes.resolved, "Incompatibility eliminated")
	sleep(1.1)
	logger.might().progress_rise(86)
	sleep(0.6)
	logger.might().progress_rise(87)
	sleep(0.9)
	logger.might().progress_rise(88)
	sleep(0.9)
	logger.might().progress_rise(89)
	sleep(0.9)
	logger.might().progress_rise(90)
	sleep(1.4)
	logger.might().progress_rise(91)
	sleep(1.8)
	logger.might().progress_rise(97)
	sleep(1.5)
	logger.might().progress_rise(100)
	sleep(1.3)
	logger.might().stop_process("Program installed")

	logger.might().stop_timer("Timer completed")
	logger.might().empty(data)

	logger.might().sort(SortingKeys.SORT_ON_TYPE)
	# logger.sort_with_save(SortingKeys.SORT_ON_TYPE)
	# logger.search("o", True)
	# logger.search_with_save("o", True)
	# logger.select(SelectionTypes.initiation)
	# logger.select_with_save(SelectionTypes.initiation)
	logger.info("Logger sorted")

	logger.might().export_to_csv("export_logs")

	logger.might().savy("log", False)
```