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
