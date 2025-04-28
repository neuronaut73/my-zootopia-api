X_API_KEY = "gmEqTVp4GLaYcXUIJLblRw==SQdua3MhJo7y3LkG"

import requests
import json


REQUEST_ANIMALS = f"https://api.api-ninjas.com/v1/animals?name=<ANIMAL_NAME>&X-Api-Key={X_API_KEY}"


def save_output(output:dict, filename: str):
    with open(filename, "w") as handle:
        handle.write(str(output))


def get_user_input() -> str:
    """Asks user to enter the name of an animal"""
    animal_name = input("Enter a name of an animal: ")
    request_url = REQUEST_ANIMALS.replace("<ANIMAL_NAME>", animal_name)
    return animal_name, request_url


def main():
    animal_name, request_url = get_user_input()

    raw = requests.get(request_url)
    text = raw.json()
    print(text)
    for item in text:
        print(item["name"])

    print(f"{animal_name}-Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()