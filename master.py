import re
import sys
import redis
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from fen.cunchu import CunChu


class Master:
    def __init__(self, list):
        self.pipe = redis.StrictRedis()
        self.list = list
        self.visited = set()  # visit url的列表
        self.url = set()  # 去除重复
        self.firsturl = []  # 列表使用方便
        self.sinaurl = set()
        self.neteasyurl = set()
        self.sohu = set()
        self.web = []

    async def get_url(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.103 Safari/537.36'}

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=headers, timeout=5) as resp:
                    if resp.status == 200:
                        self.pipe.sadd('visited',url)
                        self.visited.add(url)

                        try:
                            return await resp.text()
                        except:
                            return await resp.text(encoding='gbk')
                    else:
                        raise Exception(f'Waring：链接超时{url}')
            except Exception as e:
                sys.stdout.write(f'Waring：{e}\n')

    async def get_html(self, url):
        response = await self.get_url(url)
        html = BeautifulSoup(response, 'lxml')
        if html.find('div', {'class': 'main'}) is not None:
            main = html.find('div', {'class': 'main'})
        elif html.find('div', {'class': 'ne_area ne_index_area'}) is not None:
            main = html.find('div', {'class': 'ne_area ne_index_area'})
        elif html.find('div', {'class': 'global'}) is not None:
            main = html.find('div', {'class': 'global'})
        if main:
            if html.find('div', {'class': 'mod-02'}):
                html.find('div', {'class': 'mod-02'}).decompose
            if html.find('div', {'class': 'part-d-l'}):
                html.find('div', {'class': 'part-d-l'}).decompose
            if html.find('div', {'class': 'part-e uni-blk'}):
                html.find('div', {'class': 'part-e uni-blk'}).decompose
            if html.find('div', {'class': 'footer'}):
                html.find('div', {'class': 'footer'}).decompose
            if html.find('div', {'class': 'sidebar right'}):
                html.find('div', {'class': 'sidebar right'}).decompose
            if html.find('div', {'class': 'col_r'}):
                html.find('div', {'class': 'col_r'}).decompose
            # if html.find('div', {'class': 'layout qq-top cf'}):
            # html.find('div', {'class': 'layout qq-top cf'}).decompose
            # request请求可以出来，但是不知道为什么aiohttp不可以

            for link in main.find_all('a', {'href': re.compile('163|sina|qq')}):
                if "#" not in link:
                    a = CunChu(link.get('href'))
                    a.cunchu()

    async def run(self):
        await asyncio.gather(*[self.get_html(url) for url in self.list])


if __name__ == '__main__':
    list = ['https://www.sina.com.cn/', 'https://www.163.com/', 'https://www.qq.com/']
    master = Master(list)
    asyncio.run(master.run())
    print("ok")