from mighty_logger import Logger

if __name__ == "__main__":
	logger = Logger(program_name="Test", console_width=115)
	logger.message(message_text="Hello world!")
	logger.buffer().save("log.txt")
