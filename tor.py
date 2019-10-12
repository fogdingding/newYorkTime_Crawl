import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent

class tor():
    def __init__(self):
        tmp = requests.get("https://ident.me", proxies=self.get_proxies(), headers=self.get_header()).text
        print('check ip is {}'.format(tmp))
        
    def get_header(self):
        headers = {
            'user-agent': '',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'method': 'GET',
            'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        headers['user-agent'] = UserAgent().random 
        return headers

    def get_proxies(self):
        proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
        return proxies

    def renew_connection(self):
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password = '16:DAA655A9FB381627606670D17E4851EE1B690DB2B4759062EA5D27E993')
            controller.signal(Signal.NEWNYM)
            controller.close()

    def get_soup_with_tor(self, url, type_r = False):
        flag = 1
        while(flag == 1):
            try :
                result = requests.get(url, proxies=self.get_proxies(), headers=self.get_header(), timeout=30)
            except requests.exceptions.ConnectTimeout:
                self.renew_connection()
                flag = 1
            except requests.exceptions.ProxyError:
                print("requests.exceptions.ProxyError")
                self.renew_connection()
                flag = 1
            except requests.exceptions.ReadTimeout:
                print("requests.exceptions.ReadTimeout")
                self.renew_connection()
                flag = 1
            except requests.exceptions.SSLError:
                print("requests.exceptions.SSLError")
                self.renew_connection()
                flag = 1
            except requests.exceptions.ConnectionError:
                print("requests.exceptions.ConnectionError")
                self.renew_connection()
                flag = 1
            else:
                flag = 0
        if type_r == True:
            return result
        else:
            soup = BeautifulSoup(result.text, 'html.parser')
            return soup