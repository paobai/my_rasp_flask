from picamera import PiCamera
from setting import CURRENT_SETTINGS
import os
import datetime

"""set camera"""
def save_pigture():
    pic_file_path = os.path.join(CURRENT_SETTINGS.root_path,"save_picture")
    time = datetime.datetime.now()
    name = str(time.year).zfill(4)+str(time.month).zfill(2)+str(time.day).zfill(2)+".png"
    pic_path = os.path.join(pic_file_path,name)
    with PiCamera() as camera:
        camera.resolution = (1920,1080)
        camera.framerate = 60

        # 打开预览
        camera.start_preview()
        camera.capture(pic_path)
        camera.stop_preview()
save_pigture()
