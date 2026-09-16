import os
from dotenv import load_dotenv
import requests
import tkinter as tk

load_dotenv()
APP_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.youversion.com"
VERSE_OF_THE_DAY_PATH = "/v1/verse_of_the_days"
BIBLE_PASSAGE_PATH = "/v1/bibles/3034/passages/"

def get_day():
    from datetime import date

    day_of_year = date.today().timetuple().tm_yday

    return day_of_year

def get_verse_of_the_day_id():

    headers = {"X-YVP-App-Key": APP_KEY}
    url = BASE_URL + VERSE_OF_THE_DAY_PATH + f"/{get_day()}"
    response = requests.get(url, headers=headers)
    return response.json()['passage_id']

def get_bible_verse(passage_id):
    headers = {"X-YVP-App-Key": APP_KEY}
    url = BASE_URL + BIBLE_PASSAGE_PATH + f"{passage_id}"
    response = requests.get(url, headers=headers)
    return response.json()


verse_of_the_day = get_bible_verse(get_verse_of_the_day_id())

verse = verse_of_the_day["reference"]
reference = verse_of_the_day["content"]

root = tk.Tk()
root.title("Verse of the Day")

root.overrideredirect(True)
root.attributes("-topmost", False)
root.geometry("400x200+50+50")

label = tk.Label(
    root,
    text=f'"{verse}"\n\n— {reference}',
    font=("Arial", 14),
    wraplength=350,
    justify="center"
)

label.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()