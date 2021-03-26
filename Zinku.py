import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def currently_played():
    scope = "user-read-recently-played"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
    results = sp.current_user_recently_played()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])


def take_command():
    try:
        with sr.Microphone() as source:
            print("Zinku is listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        print('InvalidSearchError. Try Again.')

    return command


def run():
    command = take_command()
    print("You: ", command)
    if "play" in command:
        talk("Your currently played songs have been listed on console: ")
        print("Zinku: Your currently played songs: ")
        currently_played()
    elif "hello" in command:
        print("Zinku: Hello!")
        talk("Hello!")
    elif "open" in command:
        video = command.replace('open', '')
        print("Zinku: Opening" + video)
        talk("Opening " + video)
        pywhatkit.playonyt(video)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Zinku: Current time is ' + time)
        talk('Current time is ' + time)
    elif "who is" in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print("Zinku: ", info)
        talk(info)
    elif "what is" in command:
        subject = command.replace('what is', '')
        info = wikipedia.summary(subject, 1)
        print("Zinku: ", info)
        talk(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "bye" in command:
        print("Zinku: See you later!")
        talk("See you later!")
    else:
        talk('Please say the command again.')


while True:
    run()