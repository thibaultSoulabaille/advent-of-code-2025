import os
import json
import requests
from typing import Any


def fetch_input(day: int) -> str:
    with open("config/config.json") as config_file:
        config = json.load(config_file)

    req = requests.get(
        url=f"https://adventofcode.com/2025/day/{day}/input",
        cookies=config["cookies"],
    )

    if req.status_code == 200:
        return req.text

    raise Exception(f"Error while fetching day {day} input")


def download_input(day: int, base_folder: str = "inputs") -> bool:
    try:
        input_path = f"{base_folder}/day-{day}/input.txt"
        if not os.path.exists(input_path):
            os.makedirs(f"{base_folder}/day-{day}", exist_ok=True)
            input_ = fetch_input(day)
            with open(input_path, "w+") as input_file:
                input_file.write(input_)
        return True
    except Exception as e:
        print(f"Could not download day {day} input >> {e}")
        return False


def open_input(day: int, test: bool = False, as_list: bool = True) -> Any:
    if test:
        f_name = f"inputs/day-{day}/test.txt"
    else:
        download_input(day)
        f_name = f"inputs/day-{day}/input.txt"
    if as_list:
        return open(f_name).read().splitlines()
    return open(f_name).read()
