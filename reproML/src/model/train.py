from src.log import log
from src.model.io import save_model


@log
def main():
    """Builds a model and saves it to the file system."""
    model = None  # TODO implement training
    save_model(model, "model")
