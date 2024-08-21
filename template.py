import os

from pathlib import Path  # Import the Path class from the pathlib module

# The 'pathlib' module provides an object-oriented interface for working with filesystem paths.
# The Path class can handle different operating systems' file path formats automatically.
# This means you can write code that works seamlessly on Windows (which uses backslashes) and 
# Unix-like systems like Linux and macOS (which use forward slashes) without worrying about
# the differences in path separators.

# import logging

# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

import logging  # Import the logging module for handling log messages

# Configure the basic settings for logging
logging.basicConfig(
    level=logging.INFO,                           # Set the logging level to INFO
                                                  # Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
                                                  # INFO level logs messages that are general information about the program's operation

    format='[%(asctime)s]: %(message)s:'          # Specify the format of the log messages
                                                  # '%(asctime)s' inserts the current timestamp into the log message
                                                  # '%(message)s' inserts the actual log message text
                                                  # The format string is enclosed in brackets for clarity in log output
)

# # Example usage:
# logging.info("This is an informational message.")  # Logs an informational message with a timestamp


# Define the name of the project
project_name = "mlProject"

# List of files and directories to be created in the project
list_of_files = [
    f"src/{project_name}/__init__.py",                # Package initialization file, makes the directory a Python package
    f"src/{project_name}/components/__init__.py",     # Initialization file for the components module, essential for organization
    f"src/{project_name}/utils/__init__.py",          # Initialization file for the utils module, contains utility functions
    f"src/{project_name}/utils/common.py",            # Common utility functions that can be reused across the project
    f"src/{project_name}/config/__init__.py",         # Initialization file for the config module, holds configuration-related code
    f"src/{project_name}/config/configuration.py",    # Configuration management code, handles project settings and parameters
    f"src/{project_name}/pipeline/__init__.py",       # Initialization file for the pipeline module, organizes data processing pipeline
    f"src/{project_name}/entity/__init__.py",         # Initialization file for the entity module, deals with structured data entities
    f"src/{project_name}/entity/config_entity.py",    # Definitions for configuration-related entities (classes, data structures)
    f"src/{project_name}/constants/__init__.py",      # Initialization file for the constants module, stores constant values
    "config/config.yaml",                             # YAML file for global configuration settings
    "params.yaml",                                    # YAML file for storing model parameters and hyperparameters
    "schema.yaml",                                    # YAML file for defining data schema and structure
    "main.py",                                        # Main entry point for running the project
    "app.py",                                         # Script for creating a web application or API interface (if applicable)
    "requirements.txt",                               # Text file listing all project dependencies for easy installation
    "setup.py",                                       # Setup script for packaging and distributing the project
    "research/trials.ipynb",                          # Jupyter notebook for experiments and research trials
    "templates/index.html"                            # HTML template for web interface, if the project includes a frontend
]

# Explanation:
# - `project_name` is a variable that stores the name of the project, which is used in the file paths.
# - `list_of_files` is a list containing the paths to files and directories needed for the project.
# - The `f"src/{project_name}/..."` syntax is an f-string, allowing for dynamic insertion of the project name into paths.
# - `__init__.py` files are used to mark directories as Python packages, enabling them to be imported elsewhere in the project.
# - The `.yaml` files are configuration files that store settings and parameters in a readable format.
# - `.py` files are Python scripts that contain the logic, utilities, and configurations for the project.
# - `requirements.txt` specifies the external libraries required to run the project.
# - `setup.py` is used for packaging the project, making it installable with tools like pip.
# - `trials.ipynb` is a notebook for experimentation and testing in a Jupyter environment.
# - `index.html` is a basic HTML template for the web interface if the project includes a web component.





# Iterate over each file path in the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object for better OS compatibility

    # Split the file path into directory (filedir) and file name (filename)
    filedir, filename = os.path.split(filepath)  # os.path.split() returns a tuple (directory, file name)

    # Check if the directory part of the path is not empty
    if filedir != "":
        # Create the directory if it doesn't exist, `exist_ok=True` means no error if directory already exists
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file doesn't exist or if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, "w") as f:
            pass  # The 'pass' statement means "do nothing"; it's a placeholder

        # Log that the file has been created
        logging.info(f"Creating empty file: {filepath}")

    else:
        # If the file already exists and is not empty, log that information
        logging.info(f"{filename} already exists")

# for filepath in list_of_files:
#     filepath = Path(filepath)

#     filedir, filename = os.path.split(filepath)

#     if filedir !="":
#         os.makedirs(filedir, exist_ok=True)
#         logging.info(f"Creating directory; {filedir} for the file: {filename}")

#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#         with open(filepath, "w") as f:
#             pass
#             logging.info(f"Creating empty file: {filepath}")


#     else:
#         logging.info(f"{filename} is already exists")