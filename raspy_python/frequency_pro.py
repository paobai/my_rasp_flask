#!/usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------#
#   Srit Software LTD Corporation Confidential                      #
#   All Rights Reserved.                                            #
#                                                                   #
#   NOTICE:  All information contained herein is, and remains       #
#   the property of  Srit Software LTD Corporation. The             #
#   intellectual and technical concepts contained herein are        #
#   proprietary to Srit Software LTD Corporation, and are           #
#   protected by trade secret or copyright law. Dissemination of    #
#   this information or reproduction of this material is strictly   #
#   forbidden unless prior written permission is obtained           #
#   Srit Software LTD Corporation.                                  #
#-------------------------------------------------------------------#
import json
import math
from pyaudio import PyAudio
import pygame
import pyaudio
import wave
import os
import array
from api.set import generate_settings, update_settings

pygame.mixer.init(frequency=16000,  channels=1)

Fs = 16000
T = 3
n = Fs*T
f = 1000
settings = generate_settings()
f = settings['now_frequency']

y = []
for x in range(n):
    y.append(int(math.sin(2 * math.pi * f / Fs * x) * 127 + 128))
b = array.array('B', y).tobytes()

for i in range(6):
    settings = generate_settings()
    if f != settings['now_frequency']:
        f = settings['now_frequency']
        #print('change frequency!'+'-'+str(i) + '-'+str(f) + '-'+str(settings['now_frequency']))
        y = []
        for x in range(n):
            y.append(int(math.sin(2*math.pi*f/Fs*x)*127 + 128))
        b = array.array('B', y).tobytes()
    com_audio_size = "sudo amixer -M set PCM " + str(settings['audio_size']) + "%" 
    os.system(com_audio_size)
    p = PyAudio()
    '''
    stream = p.open(
        format=p.get_format_from_width(1),
        channels=1,
        rate=44000,
        output=True,
        )
    stream.write(b)
    stream.stop_stream()
    stream.close()
    p.terminate()
    '''
    wf = wave.open('test5.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt8))
    wf.setframerate(16000)
    wf.writeframes(b)
    wf.close()
    for x in range(10):
        pygame.mixer.music.load("test5.wav")
        pygame.mixer.music.play()
        pygame.time.wait(1500)
