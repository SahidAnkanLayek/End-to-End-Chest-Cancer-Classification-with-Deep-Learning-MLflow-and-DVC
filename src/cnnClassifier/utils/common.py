# src/cnnClassifier/utils/common.py

import os
import json
import joblib
import base64
import random
import numpy as np
import tensorflow as tf
import yaml

from pathlib import Path
from typing import Any, List, Optional, Union
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError

from cnnClassifier.utils.logger import get_logger

logger = get_logger(__name__)


@ensure_annotations
def read_yaml(path_to_yaml: Path, default: Optional[dict] = None) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.
        default (Optional[dict]): Value to return if YAML is empty.

    Raises:
        ValueError: If the YAML file is empty and no default is provided.

    Returns:
        ConfigBox: Parsed YAML content with attribute-style access.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                if default is not None:
                    logger.warning(f"YAML file {path_to_yaml} is empty. Returning default.")
                    return ConfigBox(default)
                raise ValueError(f"YAML file {path_to_yaml} is empty")
            logger.info(f"YAML file loaded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file {path_to_yaml} is invalid/empty")
    except Exception as e:
        logger.error(f"Error reading YAML file {path_to_yaml}: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: List[Path], verbose: Optional[bool] = True) -> None:
    """Creates directories from a list of paths."""
    for path in path_to_directories:
        path.mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """Save a Python dictionary as a JSON file."""
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except Exception as e:
        logger.error(f"Failed to save JSON file at {path}: {e}")
        raise e


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON file content as ConfigBox."""
    try:
        with open(path, "r") as f:
            content = json.load(f)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Failed to load JSON file from {path}: {e}")
        raise e


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Save data as a binary file using joblib."""
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Failed to save binary file at {path}: {e}")
        raise e


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from a binary file using joblib."""
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data
    except Exception as e:
        logger.error(f"Failed to load binary file from {path}: {e}")
        raise e


@ensure_annotations
def get_size(path: Path) -> str:
    """Get file size in KB as a string."""
    try:
        size_in_kb = round(path.stat().st_size / 1024)
        logger.info(f"File {path} size: ~ {size_in_kb} KB")
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(f"Failed to get size for file {path}: {e}")
        raise e


@ensure_annotations
def decode_image(imgstring: str, file_name: Path) -> None:
    """Decode a base64 string and save it as a binary file."""
    try:
        imgdata = base64.b64decode(imgstring)
        with open(file_name, "wb") as f:
            f.write(imgdata)
        logger.info(f"Image decoded and saved at: {file_name}")
    except Exception as e:
        logger.error(f"Failed to decode/save image to {file_name}: {e}")
        raise e


@ensure_annotations
def encode_image_into_base64(cropped_image_path: Path) -> str:
    """Encode an image file into a base64 string."""
    try:
        with open(cropped_image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        logger.info(f"Image encoded to base64 from: {cropped_image_path}")
        return encoded
    except Exception as e:
        logger.error(f"Failed to encode image {cropped_image_path} to base64: {e}")
        raise e


@ensure_annotations
def set_seed(seed: int = 42) -> None:
    """Set global random seeds for reproducibility."""
    try:
        os.environ["PYTHONHASHSEED"] = str(seed)
        random.seed(seed)
        np.random.seed(seed)
        tf.random.set_seed(seed)
        logger.info(f"Global seed set to {seed}")
    except Exception as e:
        logger.error(f"Failed to set seed: {e}")
        raise e
