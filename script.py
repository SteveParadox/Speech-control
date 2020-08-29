from imports import *

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
Query=''
try:
    Query = r.recognize_google(audio)
    print(Query)
    print("I thinks you said '" + str(r.recognize_google(audio)) + "'")
    with sr.Microphone() as source:
        if Query == "today's date":
            engine.say("Today's date is '" + str(datetime.now().strftime("%d%B%Y")) + "'")
            engine.runAndWait()
        else:
            engine.say("I thinks you said '" + str(r.recognize_google(audio)) + "'")
            engine.runAndWait()
        f_text='https://www.google.co.in/search?q=' + Query
        print(f_text)
        wb.get(chrome_path).open(f_text)

#except sr.UnknownValueError:
#  print("I could not understand audio")
except sr.RequestError as e:
   print("error; {0}".format(e))

except Exception as e:
   print (e)

# Run Application with Voice Command Function
def get_app(Q):
    if Q == "time":
        print(datetime.now())

    elif Q == '':
        engine.say("Sorry Try Again")
        engine.runAndWait()

    return


# Call get_app(Query) Func.
get_app(Query)
