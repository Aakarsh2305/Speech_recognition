import speech_recognition as sr
import webbrowser
import os

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as source for input
with sr.Microphone() as source:
    print("Say something to search or open in the web browser!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # use the Google Speech Recognition API to convert speech to text
    query = r.recognize_google(audio)
    print("You said: " + query)

    # check if the query is a URL
    if query.startswith('http://') or query.startswith('https://'):
        # open the URL in a web browser
        webbrowser.open(query)
    else:
        # search for the query in a web browser
        search_url = 'https://www.google.com/search?q=' + query
        webbrowser.open(search_url)

    # return a response to the user
    os.system("say I have opened your query in the web browser")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))