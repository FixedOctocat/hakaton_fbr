from config import BOT_HOME
from bs4 import BeautifulSoup
import requests
import urllib.request


def url_getting(строка_егора):
    vk_user_data = []
    url = "https://vk.com/photo" + str(строка_егора) + "?rev=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    a = soup.find("img")
    a = str(a)
    print(a)
    print()
    url_of_photo = a[32:-3]
    idd = строка_егора[:-10]
    vk_user_data.append(url_of_photo)
    vk_user_data.append(idd)
    return vk_user_data


def download_image_func(vk_str):
    vk_user_data = url_getting(vk_str)
    path = f"{BOT_HOME}/registered_photos/"
    urllib.request.urlretrieve(vk_user_data[0], path + vk_user_data[1] + ".jpg")


def download_image_func_1(vk_str):
    vk_user_data = url_getting(vk_str)
    path = f"{BOT_HOME}/photos/"
    urllib.request.urlretrieve(vk_user_data[0], path + vk_user_data[1] + ".jpg")
    return f"{BOT_HOME}/photos/" + vk_user_data[1] + ".jpg"
