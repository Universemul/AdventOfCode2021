import getopt
import sys
import os
import requests
import datetime
import shutil
import subprocess

URL = "https://adventofcode.com/{year}/day/{day}/input"
PWD = os.getcwd()
COOKIE_SESSION=os.getenv("AOC_SESSION") # See https://github.com/wimglenn/advent-of-code-data/tree/ed7cd3ff807228d5e78abbde02276231182ce986
TEMPLATE=f"{PWD}/templates/main.rs"
TEMPLATE_LIB=f"{PWD}/templates/lib.rs"
TEMPLATE_UTIL=f"{PWD}/templates/util.rs"


def current_day():
    now = datetime.datetime.now()
    day = min(now.day, 25)
    return day

def current_year():
    now = datetime.datetime.now()
    return now.year

def create_context(url: str, day_number: int):
    r = requests.get(url, cookies={"session": COOKIE_SESSION})
    directory = f"{PWD}/day{day_number}"
    if not os.path.exists(directory):
        subprocess.run(["cargo", "new", f"day{day_number}"])
    with open(f"{directory}/input.txt", 'wb') as f:
        f.write(r.content)
    if os.path.exists(TEMPLATE): #Copy template in directory
        with open(TEMPLATE, "r") as main_file:
            data = main_file.read().replace("{{day}}", f"day{day_number}")
            with open(f"{directory}/src/main.rs", "w") as f:
                f.write(data)
    for file in [TEMPLATE_LIB, TEMPLATE_UTIL]:
        if os.path.exists(file): #Copy template in directory
            name = file.split("/")[-1]
            shutil.copyfile(file, f"{directory}/src/{name}") 

def usage():
    print('start.py')
    exit(1)

def main():
    day = current_day()
    year = current_year()
    create_context(URL.format(day=day, year=year), day)


if __name__ == "__main__":
    main()
