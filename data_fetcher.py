import json
import requests


X_API_KEY = "gmEqTVp4GLaYcXUIJLblRw==SQdua3MhJo7y3LkG"
REQUEST_ANIMALS = f"https://api.api-ninjas.com/v1/animals?name=<ANIMAL_NAME>&X-Api-Key={X_API_KEY}"


def get_user_input() -> str:
    """Asks user to enter the name of an animal"""
    animal_name = input("Enter a name of an animal: ")
    request_url = REQUEST_ANIMALS.replace("<ANIMAL_NAME>", animal_name)
    return animal_name, request_url

    animal_name, request_url = get_user_input()


def fetch_data():
    raw = requests.get(request_url)
    animals_data = raw.json()


def load_data(filename = FILENAME):
    # Highscore-Daten (Beispiel)
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def save_data(highscore_dict, filename = FILENAME):
    """Writes the updated highscore data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as fileobj:
        json.dump(highscore_dict, fileobj,  ensure_ascii=False, indent = 4)

    print(f"The highscores were saved successfully in {filename}.")

