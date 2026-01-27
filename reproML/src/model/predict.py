from src.log import log
from src.model.io import load_model


@log
def main():
    """Generates predictions based on the previously trained model."""
    model = load_model("model")
    print(model.__class__.__name__)
    # TODO implement prediction


if __name__ == "__main__":
    main()
