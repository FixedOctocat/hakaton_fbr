import bs4 as bs4
import requests
import json
from download_img import download_image_func, download_image_func_1
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from face_compare import open_files

class VkBot:
    def __init__(self, user_id):
        print("Bot created")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["HELLO", "UPLOAD PHOTO", "FIND SOMEONE"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, event):
        message = event.text

        if message.upper() == self._COMMANDS[0]:
            return {"text": f"Hello, {self._USERNAME}! Me commands: 'UPLOAD PHOTO', 'FIND SOMEONE'", "keyboard": None}

        elif message.upper() == self._COMMANDS[1]:
            download_image_func(event.attachments['attach1'])
            return {"text": "Send me your photo", "keyboard": None}

        elif message.upper() == self._COMMANDS[2]:
            file = download_image_func_1(event.attachments['attach1'])
            open_files(file)
            return {"text": "Send somebodies photo", "keyboard": None}

        else:
            return {"text": "??????", "keyboard": None}

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
