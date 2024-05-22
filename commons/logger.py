import logging
from logging.handlers import TimedRotatingFileHandler

# Create a custom logger
logger = logging.getLogger(__name__)

# Set the log level of the logger to DEBUG
logger.setLevel(10)


# Create a TimedRotatingFileHandler
handler = TimedRotatingFileHandler(
    "my_log.log",              # Path to the log file
    when="midnight",           # Rotate the log at midnight
    interval=1,                # Interval indicates the log rotation frequency. '1'
                               # in combination with 'when="midnight"' means daily rotation.
    backupCount=10,            # Keep 10 backup log files
    encoding="utf-8",          # Use utf-8 encoding for the log files
    delay=False,               # Do not delay the creation of the log file
    utc=False                  # Use local time for the log rotation schedule
)
console_handler = logging.StreamHandler()
# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)
logger.addHandler(console_handler)
