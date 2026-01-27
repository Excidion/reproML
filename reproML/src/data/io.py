from os import path

from src.log import log


@log
def get_path(stage: str, filename: str) -> str:
    """Constructs path for file in the dataset.

    Args:
        stage (str): Stage of data processing
        filename (str): File name within that stage.

    Raises:
        FileNotFoundError: If there is not directory named `stage`.

    Returns:
        str: Dataset path
    """
    directory = path.join("data", stage)
    if not path.exists(directory):
        raise FileNotFoundError(f"'{directory=}' does not exist.")
    return path.join(directory, filename)
