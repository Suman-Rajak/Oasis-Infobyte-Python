import speech_recognition as sr
from datetime import datetime
import webbrowser

# Function to recognize speech using Google Speech Recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to handle user commands
def handle_command(command):
    if "hello" in command:
        print("Hello! How can I assist you?")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        print("The current time is", current_time)
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        search_url = "https://www.google.com/search?q=" + search_query
        webbrowser.open(search_url)
    elif "exit" in command:
        print("Exiting...")
        return False
    else:
        print("Sorry, I don't understand that command.")

# Main function
def main():
    print("Welcome to the Basic Voice Assistant!")
    running = True
    while running:
        command = recognize_speech()
        if command:
            running = handle_command(command)

if __name__ == "__main__":
    main()
