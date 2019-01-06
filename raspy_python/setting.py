import os
import json
class DefaultSettings(object):
    DEBUG = True
    UPLOAD_FOLDER = 'upload'
    root_path = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:a821233789@127.0.0.1:3306/testdb?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'this is hard'
    settings_path = os.path.join(root_path, 'settings.json')
    #SESSION_TYPE = 'filesystem'


CURRENT_SETTINGS = locals()['DefaultSettings']


settings_path = CURRENT_SETTINGS.settings_path
def generate_settings():
    with open(settings_path, encoding='utf-8') as f:
        return json.load(f)


def update_settings(new_settings):
    my_settings = generate_settings()
    with open(settings_path, 'w', encoding='utf-8') as f:
        for key, value in new_settings.items():
            if 'grade' in key:
                new_settings[key] = int(value)
            elif 'ratio' in key:
                new_settings[key] = int(value)
            elif 'size' in key:
                new_settings[key] = int(value)
        my_settings.update(new_settings)
        f.write(json.dumps(my_settings))