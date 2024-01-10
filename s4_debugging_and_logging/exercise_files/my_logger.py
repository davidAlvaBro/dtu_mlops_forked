import logging
import logging.config
import sys
from rich.logging import RichHandler

# path = "s4_debugging_and_logging/exercise_files/"
path = "" 

# Logging configuration
logging_config = {
    "version": 1,
    "formatters": { # 
        "minimal": {"format": "%(message)s"},
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
        },
    },
    "handlers": { # 
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": path + "logs_dir/info.log",
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": path + "logs_dir/error.log",
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
    },
    "root": {
        "handlers": ["console", "info", "error"],
        "level": logging.INFO,
        "propagate": True,
    },
}

# Create super basic logger
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__) # 


# logger.handlers[0] = RichHandler(markup=True)  # set rich handler

rich_handler = RichHandler(markup=True)
logger.addHandler(rich_handler)

# Logging levels (from lowest to highest priority)
logger.debug("Used for debugging your code.")
logger.info("Informative messages from your code.")
logger.warning("Everything works but there is something to be aware of.")
logger.error("There's been a mistake with the process.")
logger.critical("There is something terribly wrong and process may terminate.")