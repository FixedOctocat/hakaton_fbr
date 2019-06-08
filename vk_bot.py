import bs4 as bs4
import requests
import json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class VkBot:
    def __init__(self, user_id):
        print("Создан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["ПРИВЕТ", "ПОГОДА", "ДЕЛА", "РАБОТАТЬ", "15 МИНУТ", "30 МИНУТ", "45 МИНУТ", "ЧАС?!"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, message):
        if message.upper() == self._COMMANDS[0]:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('Дела', color=VkKeyboardColor.DEFAULT)
            keyboard.add_button('Погода', color=VkKeyboardColor.DEFAULT)
            return {"text": f"Привет, {self._USERNAME}!", "keyboard": keyboard.get_keyboard(), "thread": None}

        elif message.upper() == self._COMMANDS[1]:
            weather = self._get_weather()
            return {"text": weather, "keyboard": None, "thread": None}
        
        elif message.upper() == self._COMMANDS[2]:
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Работать', color=VkKeyboardColor.DEFAULT)
            return {"text": f"Что будешь делать, {self._USERNAME}?", "keyboard": keyboard.get_keyboard(), "thread": None}

        elif message.upper() == self._COMMANDS[3]:
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('15 минут', color=VkKeyboardColor.DEFAULT)
            keyboard.add_button('30 минут', color=VkKeyboardColor.DEFAULT)
            keyboard.add_button('45 минут', color=VkKeyboardColor.DEFAULT)
            keyboard.add_button('Час?!', color=VkKeyboardColor.DEFAULT)
            return {"text": f"Сколько хочешь поработать?", "keyboard": keyboard.get_keyboard(), "thread": None}

        elif message.upper() == self._COMMANDS[4]:
            return {"text": f"Жду тебя через 15 минут)", "keyboard": None, "thread": "work", "time": 15}

        elif message.upper() == self._COMMANDS[5]:
            return {"text": f"Заходи через полчасика", "keyboard": None, "thread": "work", "time": 30}

        elif message.upper() == self._COMMANDS[6]:
            return {"text": f"У тебя есть один академический час", "keyboard": None, "thread": "work", "time": 45}

        elif message.upper() == self._COMMANDS[7]:
            return {"text": f"Ты безумец, лучше не пользуйся мной больше", "keyboard": None, "thread": "work", "time": 60}    

        else:
            return {"text": "Не понимаю о чем ты...", "keyboard": None, "thread": None}

    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-tod54куay")
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
    def _get_weather(city: str = "москва") -> list:

        request = requests.get("https://sinoptik.com.ru/погода-" + city)
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
        result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result
