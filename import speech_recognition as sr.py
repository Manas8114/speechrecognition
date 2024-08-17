import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    """
    Function to capture audio input from the user
    """
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

def speak(text):
    """
    Function to convert text into speech
    """
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def process_command(text):
    """
    Function to process user commands and provide appropriate responses
    """
    if "hello" in text:
        speak("Hello! How can I assist you today?")
    elif "what is the time" in text:
        # Implement time retrieval logic here
        speak("The current time is 12:00 PM")
    elif "thank you" in text:
        speak("You're welcome!")
    else:
        speak("I'm sorry, I didn't understand that.")

# Main loop
while True:
    user_input = input("Enter 't' for text input or 'v' for voice input: ")

    if user_input == "t":
        text_input = input("Enter your command: ")
        process_command(text_input)
    elif user_input == "v":
        text_input = listen()
        process_command(text_input)
    else:
        print("Invalid input. Please try again.")
