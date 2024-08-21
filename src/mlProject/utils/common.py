# inside this we write utili function 
# use frequently 
# writing again and again as we do moduler coding 
# so we use util inside common.py and import function from here eg read.yaml, write.yaml, load_object() . save_object()

import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


# Reads a YAML file from the specified path and returns its content as a ConfigBox object, 
# which allows for accessing the data with attribute-style access.
# This function ensures that the YAML file is not empty, raising an error if it is.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

# Creates directories given in a list of paths. If the directories already exist, they are not recreated.
# Optionally logs the creation of each directory, useful for tracking directory setup in larger projects.
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")




# Saves a dictionary as a JSON file at the specified path. 
# This function is useful for exporting configurations or results in a standardized format.
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




# Loads data from a JSON file and returns it as a ConfigBox object, 
# allowing for easy attribute-style access to the data.
# This is helpful for loading configurations or structured data in a flexible way.
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


# Saves data in a binary format using joblib. 
# This is useful for saving models or large datasets efficiently, 
# preserving their state for later use.
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


# Loads binary data from the specified file using joblib. 
# Typically used for loading machine learning models or large datasets that were saved in binary format.
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

# Returns the size of a file in kilobytes (KB). 
# This is useful for checking file sizes, particularly when working with large datasets or ensuring files are correctly generated.
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"





