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
from flask import Blueprint, render_template, make_response
import json
from flask import g,request
from models.data import Wendu,Shidu
from models.data import *
from flask_login import login_required
import os
from setting import CURRENT_SETTINGS, generate_settings, update_settings
from test_use_c import generate_now_frequency, generate_wav
bp = Blueprint("set", __name__)


@bp.route("/set_grade_frequency_form", methods=['GET', 'POST'])
def set_grade_frequency_form():
    new_settings = request.values.dicts[1].to_dict()
    update_settings(new_settings)
    wendu = Wendu.query.order_by(Wendu.save_time.desc()).first()
    #now_frequency = generate_now_frequency(int(wendu.data))
    #generate_wav(now_frequency)
    return make_response('保存成功！'), 200


@bp.route("/set_other_parameters", methods=['GET', 'POST'])
def set_other_parameters():
    new_settings = request.values.dicts[1].to_dict()
    update_settings(new_settings)
    com_audio_size = "sudo amixer -M set PCM " + str(new_settings['audio_size']) + "%" 
    os.system(com_audio_size)
    return make_response('保存成功！'), 200
