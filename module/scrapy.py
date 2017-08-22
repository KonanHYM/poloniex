import requests
import lxml.etree

WEB_URL = {
    'detail':['http://theme.npm.edu.tw/opendata/DigitImageSets.aspx?pageNo={0}'.format(i) for i in range(1, 300)]
    }

class Crawl():
    def __init__(self):
        self.web_urls = WEB_URL['detail']

    def run(self):
        headers = {
            'Host':"map.baidu.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        for url in self.web_urls:
            print url
            response = requests.get(url, headers=headers)
            tree = lxml.etree.HTML(response.content)
            img_urls = tree.xpath('//div[@class="photobg"]/img/@src')
            for img_url in img_urls:
                print img_url

if __name__ == '__main__':
    crawl = Crawl()
    crawl.run()
