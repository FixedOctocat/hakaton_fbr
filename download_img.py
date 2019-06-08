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
    url_of_photo = a[32:-3]
    idd = stroka_egora[:-10]
    vk_user_data.append(url_of_photo)
    vk_user_data.append(idd)
    return vk_user_data
    

def download_image(vk_user_data):
    path = "/home/maska/Downloads/photos/"
    urllib.request.urlretrieve(vk_user_data[0],path+'.jpg')  
    file = open(path+".txt", 'w')
    file.write(vk_user_data[1])


stroka_egora = "50210887_456239258"
url = url_getting(stroka_egora)
download_image(url) 