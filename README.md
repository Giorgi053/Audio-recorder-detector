# Audio-recorder-detector
PyTranscribe – Simple Audio to Text Converter
PyTranscribe is a Python script that records audio, saves it as a WAV file, and transcribes the speech into text using Google Speech Recognition API
Libaries which is used sounddevice, numpy, scipy, SpeechRecognition
Features: 
      Records audio (default: 5 seconds)
      Saves the recording as audio.wav
      Converts speech to text
      Saves the transcription in transcription.txt
      Handles errors gracefully
How It Works:
      ecords 5 seconds of audio using sounddevice 
      Saves the recording as audio.wav 
      Uses speech_recognition to transcribe speech into text 
      Saves the text in transcription.txt 
