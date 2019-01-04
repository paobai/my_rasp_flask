import os
import requests
from setting import CURRENT_SETTINGS
from creatapp import generate_settings, update_settings
import wave
import pyaudio
from pyaudio import PyAudio
import array
import math

def get_wendu_shidu():
    c_path = os.path.join(CURRENT_SETTINGS.root_path, "wenshidu_2")

    result = os.popen(c_path)
    #state,output = commands.getstatusoutput("./wenshidu_2")
    #print(state)
    #print(output)
    #* * * * * sleep 10; python3 /home/pi/github/my_rasp_flask/raspy_python/test_use_c.py
    data = int(result.read())
    
    shidu = int(data/1000)
    wendu = data%100 -10
    print(wendu)
    print(shidu)
    update_state(wendu,shidu)
    result.close()
    return wendu, shidu

def generate_now_frequency(wendu):
    i = int(wendu/5) + 2
    grade = 'grade' + str(i)
    print(grade)
    settings = generate_settings()
    now_frequency = settings[grade]
    update_settings(dict(now_frequency = now_frequency))
    return now_frequency

def update_state(wendu, shidu):
    up_data = dict()
    up_data['shidu'] = shidu
    up_data['wendu'] = wendu

    url = "http://127.0.0.1:5001/load/save_state"
    #requests.post(url,data=up_data)


def generate_wav(frequency):
    Fs = 16000
    T = 5
    n = Fs*T
    f = frequency
    p = PyAudio()
    y = []

    for x in range(n):
        y.append(int(math.sin(2 * math.pi * f / Fs * x) * 127 + 128))
    b = array.array('B', y).tobytes()

    music_path = os.path.join(CURRENT_SETTINGS.root_path, "music_frequency.wav")
    wf = wave.open(music_path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt8))
    wf.setframerate(16000)
    wf.writeframes(b)
    wf.close()
wendu,shidu = get_wendu_shidu()
now_frequency = generate_now_frequency(wendu)
generate_wav(now_frequency)