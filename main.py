import sys
from newYorkCrawl import newYorkCrawl
from BaseThread import BaseThread
import threading

# 多執行緒的前工作
def my_thread_job():
    with sem:
        print("work")
# 多執行緒的後工作
def cb(year, month):
    with sem:
        fileName = 'NYC_{}_{}.json'.format(year,month)
        filePath = 'NYC_{}_{}.json'.format(year,month)
        monthData = nYC.get_monthData(year,month)
        nYC.write_monthData(fileName,monthData)
        data = nYC.openJson(fileName)
        print('{},{},{}'.format(year,month,data['response']['meta']['hits']))
        print('{},{},{}'.format(year,month,len(data['response']['docs'])))

# testing

nYC = newYorkCrawl()
year = sys.argv[1]
maxMonth = sys.argv[2]
maxMonth = int(maxMonth)

sem = threading.Semaphore(4)
for month in range(1,maxMonth):
    BaseThread(
        name = 'test',
        target=my_thread_job,
        callback=cb,
        callback_args=(year,month)
    ).start()