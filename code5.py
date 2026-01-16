from gtts import gTTS
from playsound import playsound

text = """
Hello, how are you?
This is a multi-line text to speech example.
Using Google Text to Speech.
"""

# Generate TTS audio
tts = gTTS(text=text, lang='en')

# Save as MP3 file
tts.save("speech.mp3")

# Play the audio file
playsound("speech.mp3")