import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import speech_recognition as sr
fs = 44100
seconds = 5
output_file = "audio.wav"
print("Recording...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

myrecording = (myrecording * 32767).astype(np.int16)
write(output_file, fs, myrecording)
print(f"Recording saved as '{output_file}'")


recognizer = sr.Recognizer()

try:
    with sr.AudioFile(output_file) as source:
        print("Processing audio for transcription...")
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)

        with open("transcription.txt", "w") as text_file:
            text_file.write(text)
            print("Transcription saved as 'transcription.txt'")
except sr.UnknownValueError:
    print("Speech was not understood.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
except FileNotFoundError:
    print("The audio file was not found.")
