from os import path

from cloudpickle import dump, load
from src.log import log


@log
def save_model(model: object, model_name: str) -> None:
    """Saves a model artefact to the file system..

    Args:
        model (object): Model to be saved
        model_name (str): Name under which the model should be saved.
    """
    outfile_path = get_path(model_name=model_name)
    with open(outfile_path, "wb") as outfile:
        dump(model, outfile)


@log
def load_model(model_name: str) -> object:
    """Loads a model from the file system.

    Args:
        model_name (str): Name given to the model when saved.

    Returns:
        object: Model
    """
    infile_path = get_path(model_name=model_name)
    with open(infile_path, "rb") as infile:
        return load(infile)


@log
def get_path(model_name: str) -> str:
    """Constructs path for a model artefact.

    Args:
        model_name (str): Name given to the model

    Returns:
        str: Model artefact path
    """
    return path.join("models", f"{model_name}.cldpkl")
