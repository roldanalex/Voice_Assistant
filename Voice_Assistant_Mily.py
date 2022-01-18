
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


#### Load Tokens ####

from VA_Tokens import crypto_api
from VA_Tokens import wolframalpha_api
from VA_Tokens import news_url


#### Voice Assistant Main Logic ####

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
