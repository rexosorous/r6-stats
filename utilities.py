import json
import pickle
from os import path

def load_file(file_name: str) -> dict:
    with open(file_name) as file:
        return json.load(file)


def write_file(file_name: str, rewrite):
    with open(file_name, 'w') as file:
        json.dump(rewrite, file, indent=4)


def pickle_load(file_name: str) -> list:
    with open(file_name, 'rb') as file:
        return pickle.load(file)


def pickle_write(file_name: str, rewrite):
    with open(file_name, 'wb') as file:
        pickle.dump(rewrite, file)


def file_exists(file_name: str) -> bool:
    return path.exists(file_name)