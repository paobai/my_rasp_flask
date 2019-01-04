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
from settings import generate_settings, update_settings

pygame.mixer.init(frequency=16000,  channels=1)
while True:
    #com_audio_size = "sudo amixer -M set PCM " + str(settings['audio_size']) + "%" 
    #os.system(com_audio_size)
    #p = PyAudio()
    for x in range(3):
        print(x)
        #pygame.mixer.music.stop()
        pygame.mixer.music.load("music_frequency.wav")
        pygame.mixer.music.play()
        pygame.time.wait(4700)
        
