import os        # Import the os module to interact with the operating system (e.g., file paths, directories).
import sys       # Import the sys module to interact with the Python runtime environment (e.g., standard input/output).
import logging   # Import the logging module to enable logging of messages for tracking and debugging.
#The logging module is used to track events that happen during program execution. 
# It's helpful for debugging and understanding program flow.

# Define the format of the log messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where log files will be stored
log_dir = "logs"

# Create the full path for the log file
log_filepath = os.path.join(log_dir, "running_log.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,                 # Set the logging level to INFO (only log messages with INFO level or higher).
    format=logging_str,                 # Use the specified format for all log messages.
    
    # Specify the handlers that determine where log messages are output
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages will be written to the file at log_filepath. means create a log file in local system and we can see inside log folder  
        logging.StreamHandler(sys.stdout)   # Log messages will also be printed to the console (standard output). means created log file we  see on terminal output same as above 
    ] # show streamhandler used to show log file in terminal or output and filehandler use to crate file 
)

# Create a logger object with a specific name for this project
logger = logging.getLogger("mlProjectLogger")
