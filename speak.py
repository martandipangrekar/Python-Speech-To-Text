import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak...")
    a=r.listen(source)
    try:
        text=r.recognize_google(a)
        print(f"you said,{text}")
    except:
        print("NOt recognized")


