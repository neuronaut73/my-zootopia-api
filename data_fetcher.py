import json
import requests


X_API_KEY = "gmEqTVp4GLaYcXUIJLblRw==SQdua3MhJo7y3LkG"
REQUEST_ANIMALS = f"https://api.api-ninjas.com/v1/animals?name=<ANIMAL_NAME>&X-Api-Key={X_API_KEY}"
FILENAME = "animals_data.json"


def get_user_input() -> tuple:
    """Asks user to enter the name of an animal"""
    animal_name = input("Enter a name of an animal: ")
    request_url = REQUEST_ANIMALS.replace("<ANIMAL_NAME>", animal_name)
    return animal_name, request_url


def fetch_data() -> tuple:
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics': {
        ...
        }
    },
    """
    animal_name, request_url = get_user_input()
    raw = requests.get(request_url)
    animals_data = raw.json()
    return animal_name, animals_data
