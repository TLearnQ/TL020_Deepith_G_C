import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "time": self.formatTime(record)
        }
        return json.dumps(log_record)

def setup_logger():
    logger = logging.getLogger("3gpp_parser")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("logs/app.log")
    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)
    return logger
