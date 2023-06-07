from mighty_logger import Logger
from mighty_logger.src import LogEnvironments
from mighty_logger.src import StatusMessagePatterns
from mighty_logger.text import IconSet

if __name__ == "__main__":
	logger = Logger(program_name="Test", log_environment=LogEnvironments.HTML)
	logger.debug(status_message=StatusMessagePatterns.activated(), message_text="Hello world!")
	logger.debug_performance(message_text="Hello world!")
	logger.performance(message_text="Hello world!")
	logger.event(message_text="Hello world!")
	logger.audit(message_text="Hello world!")
	logger.metrics(message_text="Hello world!")
	logger.user(message_text="Hello world!")
	logger.message(message_text="Hello world!")
	logger.info(icon=IconSet.info3, message_text="Hello world!")
	logger.notice(message_text="Hello world!")
	logger.warning(message_text="Hello world!")
	logger.error(message_text="Hello world!")
	logger.critical(message_text="Hello world!")
	logger.start_process(message_text="Hello world!")
	logger.success(message_text="Hello world!")
	logger.fail(message_text="Hello world!")
	logger.buffer().save("log.html")
