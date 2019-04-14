import os
import requests
from setting import CURRENT_SETTINGS, generate_settings, update_settings
import wave
import pyaudio
from pyaudio import PyAudio
import array
import math
import dateutil.parser as date_parser
import time
from sht20 import generate as generate_wendu_shidu

def get_wendu_shidu_old():
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

def get_wendu_shidu():
    result = generate_wendu_shidu()
    return result['temp'], result['humi']


def fix_frequency(base_freqency,now_temp,base_temp,temp_ratio,now_hum,base_hum,hum_ratio):
    print(base_freqency,now_temp,base_temp,temp_ratio,now_hum,base_hum,hum_ratio)
    final_frequency = base_freqency*(1+ (now_temp - base_temp) * temp_ratio/100 + (now_hum - base_hum) * hum_ratio/100)
    print(final_frequency,base_freqency)
    return int(final_frequency)



def generate_now_frequency_old(wendu,shidu):
    i = int(wendu/5) + 2
    grade = 'grade' + str(i)
    print(grade)
    settings = generate_settings()
    base_frequency = settings[grade]
    base_temp = -2.5 + (i-1)*5

    now_frequency = fix_frequency(base_freqency=base_frequency, now_temp=wendu, base_temp=base_temp,temp_ratio=settings['temp_ratio'], now_hum=shidu,base_hum=50,hum_ratio=settings['hum_ratio'])
    update_settings(dict(now_frequency = now_frequency))
    
    return now_frequency

def generate_now_frequency(wendu,shidu):
    i = int(wendu/5) + 2
    grade = 'grade' + str(i)
    print(grade)
    settings = generate_settings()
    base_frequency = settings[grade]
    #base_temp = -2.5 + (i-1)*5

    #now_frequency = fix_frequency(base_freqency=base_frequency, now_temp=wendu, base_temp=base_temp,temp_ratio=settings['temp_ratio'], now_hum=shidu,base_hum=50,hum_ratio=settings['hum_ratio'])
    now_frequency = base_frequency
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

def check_time():
    settings = generate_settings()
    start_time = date_parser.parse(settings['start_time']).timestamp()
    end_time = date_parser.parse(settings['end_time']).timestamp()
    now_time = time.time()
    print(start_time,end_time,now_time)
    if now_time >start_time and now_time<end_time:
        a=dict(open=True)
        update_settings(a)
    else:
        a=dict(open=False)
        update_settings(a)


if __name__ =='__main__':
    wendu,shidu = get_wendu_shidu()
    now_frequency = generate_now_frequency(wendu,shidu)
    print(now_frequency,wendu,shidu)
    generate_wav(now_frequency)
    check_time()
