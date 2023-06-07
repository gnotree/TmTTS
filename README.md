IBM Watson Text-to-Speech Python Script
This repository contains a Python script which demonstrates how to use IBM Watson's Text-to-Speech API.

The script allows a user to select a voice from the available options, enter a custom text/prompt, and have it converted to an audio file (.wav) using IBM's TTS API.

Users are also given the option to specify the name of the output audio file. If no name is specified, the file will be saved as output.wav by default. If a file with the same name already exists in the directory, the program will automatically add a numerical suffix to the new file to prevent overwriting. For example, if output.wav and output(2).wav already exist, the new file will be saved as output(3).wav.

The script continues to run until the user decides to exit by entering -1.

Requirements
To run this script, you need:

Python 3.6 or later
IBM Watson's Text-to-Speech API key and URL
requests and playsound libraries for Python
How to Run
Clone the repository to your local machine.
Open terminal/command prompt and navigate to the directory where the script is located.
Run the script using python scriptname.py.
Follow the prompts in the terminal to use the text-to-speech function.
This script is a simple demonstration of the powerful capabilities of IBM's Watson Text-to-Speech API and can be extended or modified to suit more specific needs.

Note
Make sure to replace the api_key and url variables with your actual API key and URL obtained from IBM Cloud.

To play the .wav files from the terminal, you can use the appropriate command for your operating system (for example, aplay filename.wav on Linux, afplay filename.wav on MacOS, start filename.wav on Windows).





Regenerate response
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set up service.
authenticator = IAMAuthenticator('API_KEY')
text_to_speech = TextToSpeechV1(authenticator=authenticator)

# Set the service URL.
text_to_speech.set_service_url('YOUR_URL')

# Get list of voices.
voices = text_to_speech.list_voices().get_result()
voice_names = [voice['name'] for voice in voices['voices']]

# Print out voice names.
print("Available voices:")
for index, voice_name in enumerate(voice_names):
    print(f"{index + 1}. {voice_name}")

# Ask user to choose a voice.
voice_choice = int(input("Choose a voice by typing its number: ")) - 1
voice = voice_names[voice_choice]

# Ask user for text to convert to speech.
text = input("Enter the text to convert to speech: ")

# Convert text to speech.
response = text_to_speech.synthesize(
    text=text,
    voice=voice,
    accept='audio/wav'
).get_result()

# Write the speech to an audio file.
with open('output.wav', 'wb') as audio_file:
    audio_file.write(response.content)

print("The speech has been saved to 'output.wav'.")


ChatGPT may produce inaccurate information about people, places, or facts. ChatGPT May 24 Version
