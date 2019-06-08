import bs4 as bs4
import requests
import json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class VkBot:
    def __init__(self, user_id):
        print("Bot created")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["Hello", "Upload photo", "Find someone"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, message):
        if message.upper() == self._COMMANDS[0]:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('Upload photo', color=VkKeyboardColor.DEFAULT)
            keyboard.add_button('Find someone', color=VkKeyboardColor.DEFAULT)
            return {"text": f"Hello, {self._USERNAME}!", "keyboard": keyboard.get_keyboard()}

        elif message.upper() == self._COMMANDS[1]:
            weather = self._get_weather()
            return {"text": wait for your photo, "keyboard": None}
