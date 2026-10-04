from pathlib import Path
import yaml

def load_database(filename):
    path = Path(__file__).parent / filename

    with open(path, "r") as file:
        return yaml.safe_load(file)