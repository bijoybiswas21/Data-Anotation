from gtts import gTTS
import os
import tempfile
import platform

# Take input from user
text = input("Enter text to speak: ")

# Create a gTTS object (language='en' for English)
tts = gTTS(text=text, lang='en', slow=False)

# Use a temporary file to save the audio
with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
    temp_file = fp.name

# Save the speech to the temporary file
tts.save(temp_file)

# Play the audio file
system = platform.system()
if system == "Windows":
    os.system(f"start {temp_file}")
elif system == "Darwin":  # macOS
    os.system(f"afplay {temp_file}")
else:  # Linux
    os.system(f"mpg123 {temp_file}")  # or use 'ffplay', 'vlc', etc.

# Optional: delete the file after playing (or keep it if needed)
# os.remove(temp_file)