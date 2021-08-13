import requests # pip install requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    print(str)
    speak.Speak(str)


if __name__ == '__main__':
    speak("News for today. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=9c4958575f6e427a96b5c434a58ba387"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news")
    speak("Thanks for listening")
