from mighty_logger import Logger
from mighty_logger.src import LogEnvironments

if __name__ == "__main__":
	logger = Logger(program_name="Test", log_environment=LogEnvironments.HTML)
	logger.message(message_text="Hello world!")
	logger.buffer().save("log.html")
