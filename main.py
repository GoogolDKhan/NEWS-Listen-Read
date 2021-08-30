import requests
import json

# Environment variables
import os
from dotenv import load_dotenv

load_dotenv()

# Text to speak function
def speak(string):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    print(string)
    speak.Speak(string)


if __name__ == "__main__":
    speak("News for today. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + os.getenv("API_KEY")
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    articles = news_dict["articles"]
    for article in articles:
        speak(article["title"])
        speak("Moving on to the next news")
    speak("Thanks for listening")
