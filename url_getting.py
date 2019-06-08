from bs4 import BeautifulSoup
import requests

def url_getting_func(str):
    url = "https://vk.com/photo" + str(str) + "?rev=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    a = soup.find('img')
    a = str(a)
    url_of_photo = a[32:-3]
return url_of_photo
