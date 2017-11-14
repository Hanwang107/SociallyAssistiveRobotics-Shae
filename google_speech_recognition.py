import speech_recognition as sr

def speech():
	# Record Audio
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Doctor, am listening!")
	    audio = recognizer.listen(source)
	 
	# Speech recognition using Google Speech Recognition
	try:
	    # Using the default API key
	    print("You said: " + recognizer.recognize_google(audio))
	    return recognizer.recognize_google(audio)
	except sr.UnknownValueError:
	    # Google Speech Recognition could not understand the audio
	    return "Counld not understand the audio"
	except sr.RequestError as e:
	    # Could not request results from Google Speech Recognition service
	    return "Could not request results from Google Speech Recognition service; {0}".format(e)



