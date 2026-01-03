from src.model.io import save_model


def main():
    """Builds a model and saves it to the file system."""
    model = None  # TODO implement training
    save_model(model, "model")


if __name__ == "__main__":
    main()
