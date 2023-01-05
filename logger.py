import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the log level
logger.setLevel(logging.DEBUG)

# Create a handler to write the log to a file
file_handler = logging.FileHandler("logs.log")

# Create a handler to write the log to the console
console_handler = logging.StreamHandler()

# Set the log level of the file and console handlers
file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Use the logger
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

