import redis
import re
import aiohttp
import asyncio
import pymysql
from lxml import etree
from fen.cunchu import CunChu


class Cong:
    def __init__(self):
        self.list = []
        self.final = []
        self.url = []
        self.AllData = []
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db="test")
        self.cursor = conn.cursor
        r = redis.StrictRedis(host='127.0.0.1', port=6380, db=0)
        pipe = r.pipeline()
        pipe.lrange('sina', 120, 130)
        result = pipe.execute()
        for AllUrl in result:
            for j in AllUrl:
                c = str(j, encoding='utf-8')
                print(c)
                self.list.append(c)

    async def send_request(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.103 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=headers, timeout=20) as resp:
                    if resp.status == 200:
                        print("ok")
                        self.url.append(url)
                        return await resp.text()
                    else:
                        raise Exception(f'Waring：链接超时{url}')
            except UnicodeError  as e:
                async with session.get(url, headers=headers, timeout=20) as resp:
                    if resp.status == 200:
                        self.url.append(url)
                        print("ok")
                        return await resp.text(encoding='gbk')


                    else:
                        raise Exception(f'Waring：链接超时{url}')
            except Exception as e:
                pass
                # sys.stdout.write(f'Waring：{e}\n')

    async def save_data(self, url):
        html = await self.send_request(url)
        if html is not None:
            str = etree.HTML(html)
            if str.xpath('//div[@class="main-content w1240"]'):

                title = str.xpath('//title/text()')
                # print(title, end=" ")
                keyword = str.xpath('//div[@class="keywords"]/@data-wbkey')
                all = {'title': title, 'key': keyword}
                self.all = {url: all}
                # a = Node(self.all, url, all)
                # b = a.add()
                self.AllData.append(self.all)
                print("解析页面完成")

            elif str.xpath('//div[@class="main"]') or str.xpath('//div[@class="blkContainerSblk"]'):
                title = []
                key = []
                r = re.compile('<title>(.*?)</title>')
                data = r.findall(html)
                title = title + data
                keywords = str.xpath('//p[@class="art_keywords"]/a')
                if not keywords:
                    keywords = str.xpath('//div[@class="art_keywords"]/a')
                for i in keywords:
                    a = i.xpath('./text()')
                    key = key + a
                all = {'title': title, 'key': key}
                self.all = {url: all}
                self.cursor.execute('insert into test value(%s,%s)'%(self.all,all))
                # a =Node(self.all,url,all)
                # b =a.add()
                self.AllData.append(self.all)
                print("解析页面完成")

            else:
                a = re.compile('href="(.*?)"')
                b = a.findall(html)
                # print(b)
                for i in b:
                    a = CunChu(i)
                    a.cunchu()
                print("存储页面完成")

    def save(self):
        print(self.AllData)
        return self.AllData

    async def main(self):

        await asyncio.gather(*[self.save_data(url) for url in self.list])
        self.save()


if __name__ == '__main__':
    a = Cong()
    asyncio.run(a.main())
