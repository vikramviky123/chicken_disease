import logging
import os
import sys
from datetime import datetime

# Log Folder name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path for Logs folder
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Creating folder for LOG_FILE
os.makedirs(logs_path, exist_ok=True)

# Name of text log file in logs_path folder
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Creates text log file with LOG_FILE name in logs_path
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)
