
#### Load Library ####

from email.mime import audio
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import requests
import yfinance as yf
import wolframalpha
import translators as ts
import wikipedia
import datetime

#### Load Tokens ####

from VA_Tokens import crypto_api
from VA_Tokens import wolframalpha_api
from VA_Tokens import news_url
from VA_Tokens import weather_api


#### Voice Assistant Main Logic ####

## Wikipedia
def wikipedia_info():
    mily_talk('Happy to help. What would you like to search in Wikipedia?')
    wiki_listen = mily_listen()
    wiki_results = wikipedia.summary(wiki_listen, sentences = 2)
    print(wiki_results)
    mily_talk(wiki_results)

## Date / Time
def time_now():
    today_date = datetime.datetime.now()
    hour = today_date.strftime("%I")
    minute = today_date.strftime("%M")
    meridiem = today_date.strftime("%p")
    time_now = 'The current time is ' + hour + ':' + minute + ' ' + meridiem
    print(time_now)
    mily_talk(time_now)

## Week now
def weekday_now():
    week_today = datetime.datetime.now().strftime("%A")
    print(week_today)
    mily_talk(week_today)

## Get top US news
def get_news():
    news = requests.get(news_url).json()
    articles = news['articles']

    news_headlines = []
    for a in articles:
        news_headlines.append(a['title'])

    for i in range(5):
        print(news_headlines[i])
        mily_talk(news_headlines[i])

## Get weather
def get_weather():
    mily_talk('Sure. What city are you interested on?')
    weather_city = mily_listen()
    print(weather_city)
    weather_url = 'https://api.weatherbit.io/v2.0/current?city=' + weather_city + '&key=' + weather_api + '&units=I'
    weather = requests.get(weather_url).json()
    temperature = weather['data'][0]['temp']
    description = weather['data'][0]['weather']['description']

    weather_result = 'The current temperature in ' + weather_city + ' is ' + str(temperature) + ' degrees Fahrenheit with ' + str(description)
    print(weather_result)
    mily_talk(weather_result)

## Convert Speech to Txt
def mily_listen():
    # recognize microphone
    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.3)

        audio = r.listen(source)
        text = ''

        try:
            text = r.recognize_google(audio)

        except sr.RequestError as re:
            print(re)

        except sr.UnknownValueError as uve:
            print(uve)

        except sr.WaitTimeoutError as wte:
            print(wte)

    text = text.lower()

    return text

## Convert Txt to Speech (English)
def mily_talk(text):
    # creates an audio file to store talk
    file_raw = 'audio_raw.mp3'

    tts = gTTS(text = text, lang = 'en')
    tts.save(file_raw)

    playsound.playsound(file_raw)
    os.remove(file_raw)

## Convert Txt to Speech (Spanish)
def mily_talk_es(text):
    # creates an audio file to store talk
    file_raw = 'audio_raw.mp3'

    tts = gTTS(text = text, lang = 'es')
    tts.save(file_raw)

    playsound.playsound(file_raw)
    os.remove(file_raw)

## Create a reply function based on text (user request)
def mily_reply(text):

    # Normal talk
    if 'what' in text and 'name' in text:
        mily_talk('My name is Milagros and I am your personal asistant')

    elif 'stop' in text:
        mily_talk('It was a pleasure. Have a great rest of your day')

    # Bitcoin talk
    elif 'bitcoin' in text:
        response = requests.get(crypto_api)
        crypto_json = response.json()
        mily_talk('The current price for Bitcoin is' + str(crypto_json['bitcoin']['usd']) + ' US Dollars')

    elif 'dogecoin' in text:
        response = requests.get(crypto_api)
        crypto_json = response.json()
        mily_talk('The current price for Dogecoin is' + str(crypto_json['dogecoin']['usd']) + ' US Dollars')

    elif 'solana' in text:
        response = requests.get(crypto_api)
        crypto_json = response.json()
        mily_talk('The current price for Bitcoin is' + str(crypto_json['solana']['usd']) + ' US Dollars')

    # Stock talk
    elif 'tesla' in text and ('stock' in text or 'price' in text):
        tesla_stock = yf.Ticker('TSLA')
        mily_talk('The current share price for Tesla is' + str(tesla_stock.info['regularMarketPrice']) + ' US Dollars')
    
    elif 'facebook' in text and ('stock' in text or 'price' in text):
        facebook_stock = yf.Ticker('FB')
        mily_talk('The current share price for Tesla is' + str(facebook_stock.info['regularMarketPrice']) + ' US Dollars')

    elif 'apple' in text and ('stock' in text or 'price' in text):
        apple_stock = yf.Ticker('AAPL')
        mily_talk('The current share price for Tesla is' + str(apple_stock.info['regularMarketPrice']) + ' US Dollars')
    
    # Open questions
    elif 'question' in text:
        mily_talk('Please tell me your question')
        question = mily_listen()
        client = wolframalpha.Client(wolframalpha_api)
        result =  client.query(question)
        answer = next(result.results).text
        #answer_split = answer.split()
        mily_talk('The answer to your question is the following. ' + answer)
        #print(answer)
        #answer_split = answer.split()
        #print(answer_split)

    # Translator
    elif 'translate' in text:
        
        while True:

            mily_talk('Would you like to translate from English to Spanish or Spanish to English?')
            question_translate = mily_listen()
            if 'english to spanish' in question_translate:
                mily_talk('What would you like to translate?')
                sentence_translate = mily_listen()
                mily_talk_es(ts.google(sentence_translate, from_language='en', to_language='es'))

            elif 'spanish to english' in question_translate:
                mily_talk('What would you like to translate?')
                sentence_translate = mily_listen()
                mily_talk(ts.google(sentence_translate, from_language='es', to_language='en'))

            elif 'stop' in question_translate:
                mily_talk('I will stop translating now.')
                break

    # News
    elif 'news' in text:
        mily_talk('Ok, these are the top 5 headlines in US')
        get_news()

    # Weather
    elif 'weather' in text:
        get_weather()

    # Wikipedia    
    elif 'wikipedia' in text:
        wikipedia_info()

    # Time now
    elif 'time' in text:
        time_now()

    elif 'weekday' or 'day of the week' or 'day' in text:
        weekday_now()

    # Exit talk
    else:
        mily_talk('I am sorry, would you be able to repeat your request?')


#### Voice Assistant Execution ####

def execute_app():
    
    mily_talk('Hello, may I ask what is your name?')
    listen_name = mily_listen()
    mily_talk('Hi ' + listen_name + ' what can I do for you?')

    while True:
        listen_mily = mily_listen()
        print(listen_mily)

        mily_reply(listen_mily)

        if 'stop' in listen_mily:
            break

# Execute assistant
execute_app()

#### Test Area ####
