"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
from dotenv import find_dotenv
from dotenv import load_dotenv
load_dotenv(find_dotenv(), override=True)
import os
CHUNK = int(os.environ.get("CHUNK"))
FORMAT = eval(os.environ.get("FORMAT"))
CHANNELS = int(os.environ.get("CHANNELS"))
RATE = int(os.environ.get("RATE"))
RECORD_SECONDS = int(os.environ.get("RECORD_SECONDS"))
WAVE_OUTPUT_FILENAME = os.environ.get("WAVE_OUTPUT_FILENAME")

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()