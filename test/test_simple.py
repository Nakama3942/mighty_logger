from mighty_logger import SimpleLogger

if __name__ == "__main__":
	logger = SimpleLogger("Installer")
	logger.message("Program installation started")
	logger.warning("Newer version found")
	logger.separator()
	data = logger.input("Enter password: ")
	logger.error("Incompatibility found")
	logger.fail("Program not installed")
	logger.print(data)
	logger.get_buffer().save("log")