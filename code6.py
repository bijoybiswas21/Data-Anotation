from gtts import gTTS
import os

# Optional: Use playsound only if available and working
try:
    from playsound import playsound
    USE_PLAYSOUND = True
except ImportError:
    USE_PLAYSOUND = False

text = """প্রিয় পাঠক, শুভেচ্ছা নিন। আমি ময়নুল ইসলাম শাহ্‌, আপনাদের জন্য নেতাজি সুভাষচন্দ্র বসুকে নিয়ে এই ব্লগে লিখছি। ২৩ জানুয়ারি, ভারতের অন্যতম গর্বের দিন, যা নেতাজি দিবস হিসেবে পালিত হয়। ভারতের স্বাধীনতা সংগ্রামে নেতাজি সুভাষচন্দ্র বসুর ভূমিকা চিরস্মরণীয়। আশা করি এই লেখা আপনাদের উপকারে আসবে।
"""

# Generate TTS audio
tts = gTTS(text=text, lang='bn', slow=False)
tts.save("speech.mp3")

# Play the audio
if USE_PLAYSOUND:
    try:
        playsound("speech.mp3")
    except Exception as e:
        print(f"playsound failed: {e}")
        # Fallback to system player
        os.system("start speech.mp3" if os.name == "nt" else "afplay speech.mp3" if os.name == "posix" and os.uname().sysname == "Darwin" else "mpg123 speech.mp3")
else:
    # Fallback playback
    if os.name == "nt":  # Windows
        os.startfile("speech.mp3")
    elif os.name == "posix":
        import platform
        if platform.system() == "Darwin":  # macOS
            os.system("afplay speech.mp3")
        else:  # Linux
            os.system("mpg123 speech.mp3")