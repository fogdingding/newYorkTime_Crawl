import json
from tor import tor
from MyJsonDecoder import MyJsonDecoder

class newYorkCrawl():
    '''
    newYorkCrawl 的說明
    newYorkCrawl https://www.nytimes.com 爬曲紐約時報的新聞
    Attributes(相關函數說明)
    ----------
    __init__
        : 初始化
    get_monthData()
        : 獲得一整月的新聞網址資料,return json
    write_monthData(fileName, monthData)
        : 寫檔案，把整月的新聞網址資料寫入一個檔案
    openJson(filePath):
        : 讀取json檔案並回傳檔案資料,return dict
    

    Methods(如何使用說明)
    ----------
    EX:
    '''
    def __init__(self):
        self.password = 'JRghpSmkijJCRD6gCJvZRHgKvEqYOGno'
        self.apiUrl = 'https://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}'
        self.tor = tor()
        self.MD = MyJsonDecoder()

    def get_monthData(self,year,month):
        url = self.apiUrl.format(year,month,self.password)
        monthData_text = self.tor.get_soup_with_tor(url = url, type_r = True).text
        monthData_json = self.MD.decode(monthData_text)
        return monthData_json

    def write_monthData(self,fileName, monthData):
        with open(fileName, 'w', encoding='utf8') as f:
            try:
                json.dump(monthData,f)
            except:
                print("write_monthData error")
            else:
                print("write_monthData {} done".format(fileName))

    def openJson(self,filePath):
        with open(filePath, 'r', encoding='utf8') as f:
            try:
                return json.load(f)
            except:
                print("openJson error")
            else:
                print("openJson {} done".format(filePath))

    def get_newsContent(self,url):
        newsSoup = self.tor.get_soup_with_tor(url = url, type_r = False)
        articleBody = newsSoup.find("section", {"name":"articleBody"})
        return articleBody.get_text()




