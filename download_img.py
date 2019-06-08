from bs4 import BeautifulSoup
import requests
import urllib.request

def url_getting(stroka_egora):
    vk_user_data = []
    url = "https://vk.com/photo" + str(stroka_egora) + "?rev=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find('img')
    a = str(a)
    print(a)
    print()
    url_of_photo = a[32:-3]
    idd = stroka_egora[:-10]
    vk_user_data.append(url_of_photo)
    vk_user_data.append(idd)
    return vk_user_data

def download_image_func(vk_str):
    vk_user_data = url_getting(vk_str)
    path = "/home/fixed/Documents/hakaton_fbr/registered_photos/"
    urllib.request.urlretrieve(vk_user_data[0],path+ vk_user_data[1] +'.jpg')