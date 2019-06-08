from bs4 import BeautifulSoup
import requests

def url_getting(stroka_egora):
    url = "https://vk.com/photo" + str(stroka_egora) + "?rev=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find('img')
    a = str(a)
    url_of_photo = a[32:-3]
return url_of_photo
