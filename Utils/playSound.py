import os
import pyaudio
import wave

def play_sound(animal):

    script_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(script_dir, "..", "AnimalSounds", f"{animal}.wav")
    path = os.path.abspath(path)
    
    wf = wave.open(path, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    chunk_size = 1024
    data = wf.readframes(chunk_size)
    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)

    stream.stop_stream()
    stream.close()
    p.terminate()