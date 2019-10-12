import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent

def get_header():
    headers = {
        'user-agent': '',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'method': 'GET',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    headers['user-agent'] = UserAgent().random 
    return headers

def get_proxies():
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    return proxies

def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password = '16:DAA655A9FB381627606670D17E4851EE1B690DB2B4759062EA5D27E993')
        controller.signal(Signal.NEWNYM)
        controller.close()

def get_soup_with_tor(url):
    flag = 1
    while(flag == 1):
        try :
            result = requests.get(url, proxies=get_proxies(), headers=get_header(), timeout=10)
        except requests.exceptions.ConnectTimeout:
            renew_connection()
            flag = 1
        except requests.exceptions.ProxyError:
            print("requests.exceptions.ProxyError")
            renew_connection()
            flag = 1
        except requests.exceptions.ReadTimeout:
            print("requests.exceptions.ReadTimeout")
            renew_connection()
            flag = 1
        except requests.exceptions.SSLError:
            print("requests.exceptions.SSLError")
            renew_connection()
            flag = 1
        except requests.exceptions.ConnectionError:
            print("requests.exceptions.ConnectionError")
            renew_connection()
            flag = 1
        else:
            flag = 0
    soup = BeautifulSoup(result.text, 'html.parser')
    return soup

# testing
tmp = requests.get('https://ident.me', headers=get_header()).text
print(tmp)

tmp = requests.get("https://ident.me", proxies=get_proxies(), headers=get_header()).text
print(tmp)

renew_connection()
tmp = requests.get("https://ident.me", proxies=get_proxies(), headers=get_header()).text
print(tmp)

url = 'https://www.nytimes.com/2019/10/11/world/middleeast/turkey-syria-kurds.html'
tmp = get_soup_with_tor(url)
print(type(tmp))