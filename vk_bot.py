import bs4 as bs4
import requests
import json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class VkBot:
    def __init__(self, user_id):
        print("РЎРѕР·РґР°РЅ РѕР±СЉРµРєС‚ Р±РѕС‚Р°!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["Привет"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, message):
        if message.upper() == self._COMMANDS[0]:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('Р”РµР»Р°', color=VkKeyboardColor.DEFAULT)
            keyboard.add_button('РџРѕРіРѕРґР°', color=VkKeyboardColor.DEFAULT)
            return {"text": f"РџСЂРёРІРµС‚, {self._USERNAME}!", "keyboard": keyboard.get_keyboard(), "thread": None}

        elif message.upper() == self._COMMANDS[1]:
            weather = self._get_weather()
            return {"text": weather, "keyboard": None, "thread": None}
        
    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-tod54РєСѓay")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

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

    @staticmethod
    def _get_weather(city: str = "РјРѕСЃРєРІР°") -> list:

        request = requests.get("https://sinoptik.com.ru/РїРѕРіРѕРґР°-" + city)
        b = bs4.BeautifulSoup(request.text, "html.parser")

        p3 = b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = b.select('.temperature .p6')
        weather4 = p6[0].getText()

        result = ''
        result = result + ('РЈС‚СЂРѕРј :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Р”РЅС‘Рј :' + weather3 + ' ' + weather4) + '\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result
