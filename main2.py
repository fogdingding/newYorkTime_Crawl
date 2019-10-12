import sys
from newYorkCrawl import newYorkCrawl
from BaseThread import BaseThread
import threading
import json
import time
from filelock import FileLock

def get_type(url):
    tmp_url = url.replace("https://www.nytimes.com/",'')
    tmp = tmp_url.split("/")
    try:
        return tmp[3]
    except:
        with open("error",'a+',encoding='utf8') as f:
            f.write(url)
            f.write("\n")
lock = threading.Lock()
def append_data(append_fileName,data):
    lock.acquire()
    with open(append_fileName, 'a+', encoding='utf8') as f:
        try:
            
            json.dump(data,f)
            f.write("\n")
        except:
            print("append_data error")
    lock.release()

# 多執行緒的前工作
def my_thread_job():
    return True
# 多執行緒的後工作
def cb(tmp,childNumber):
    with sem:
        data = {}
        url = tmp['web_url']
        news_type = get_type(tmp['web_url'])
        title = tmp['headline']['main']
        keywords = tmp['keywords']
        date = tmp['pub_date']
        try:
            content = nYC.get_newsContent(url)
            data = {
                'url':url,
                'news_type':news_type,
                'title':title,
                'keywords':keywords,
                'date':date,
                'content':content
            }
            append_data(append_fileName,data)
        except:
            with open("error_content",'a+',encoding='utf8') as f:
                f.write(url)
                f.write("\n")
            print("error")
        else:
            print("{} done".format(childNumber))


nYC = newYorkCrawl()
year = sys.argv[1]
month = sys.argv[2]

fileName = "NYC_{}_{}.json".format(year,month)
append_fileName = "NYC_{}_{}.txt".format(year,month)

data = nYC.openJson(fileName)
print('{},{},{}'.format(year,month,data['response']['meta']['hits']))
print('{},{},{}'.format(year,month,len(data['response']['docs'])))
maxItem = len(data['response']['docs'])

sem = threading.Semaphore(100)
for child in range(0,maxItem):
    if child != 0 and child%1000==0:
        time.sleep(200)
    tmp = data['response']['docs'][child]
    BaseThread(
        name = 'test',
        target=my_thread_job,
        callback=cb,
        callback_args=(tmp,child)
    ).start()