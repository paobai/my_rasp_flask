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
import time
from setting import CURRENT_SETTINGS,generate_settings, update_settings
music_path = os.path.join(CURRENT_SETTINGS.root_path, "music_frequency.wav")
pygame.mixer.init(frequency=16000,  channels=1)
# n=2
while True:
    #com_audio_size = "sudo amixer -M set PCM " + str(settings['audio_size']) + "%" 
    #os.system(com_audio_size)
    #p = PyAudio()

    # settings = generate_settings()
    # if settings['open']:
    #     for x in range(3):
    #         print(x)
    #         #pygame.mixer.music.stop()
    #         pygame.mixer.music.load(music_path)
    #         pygame.mixer.music.play()
    #         pygame.time.wait(4700)
    # else:
    #     pygame.time.wait(5000)
        
    # n=n-1
    # settings = generate_settings()
    # if settings['open']:
    #     pygame.mixer.music.load(music_path)
    #     pygame.mixer.music.play()
    #     pygame.time.wait(3500)
    #     pygame.mixer.music.stop()
    # else:
    #     pygame.time.wait(4700)

    # n-=1
    import datetime
    print(datetime.datetime.now())
    settings = generate_settings()
    if settings['open']:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(5)
        settings = generate_settings()
        time.sleep(5)
        for i in range(2):
            settings = generate_settings()
            if settings['open']:
                time.sleep(5)
            else:
                pygame.mixer.music.stop()
        print(datetime.datetime.now())
    else:
        time.sleep(5)
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load(music_path)
    # pygame.mixer.music.play()
    # print(datetime.datetime.now())
    # pygame.time.wait(2000)
    # print(datetime.datetime.now())
