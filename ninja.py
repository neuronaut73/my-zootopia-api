X_API_KEY = "gmEqTVp4GLaYcXUIJLblRw==SQdua3MhJo7y3LkG"

import requests
import json


name = "fox"

REQUEST_ANIMALS = f"https://api.api-ninjas.com/v1/animals?name={name}&X-Api-Key={X_API_KEY}"


def save_output(output:dict, filename: str):
    with open(filename, "w") as handle:
        handle.write(str(output))


def main():
    raw = requests.get(REQUEST_ANIMALS)
    text = raw.json()
    print(text)
    for item in text:
        print(item["name"])
    # animals = text["countries"]
    # for country in countries:
    #     print(f"{country["name"]} ({country["codes"]["alpha-3"]})")
    # land = input("Please enter a country: ")
    # REQUEST_URL = f"https://holidayapi.com/v1/holidays?pretty&key={API_KEY}&format=json&year={year}&country={land}"
    # raw2 = requests.get(REQUEST_URL)
    # text2 = raw2.json()

    # print(text2)
    # print(f"List of holidays in the last year ({year}):")

    # for item in text2["holidays"]:
    #     print(f"{item["name"]} ({item["weekday"]["date"]["name"]}, {item["date"]})")


if __name__ == "__main__":
    main()