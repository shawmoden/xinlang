import hashlib
import redis

class CunChu:
    def __init__(self,url):
        self.pipe =redis.StrictRedis()
        self.url =url

    def cunchu(self):    
        a = hashlib.md5()
        a.update(bytes(self.url, encoding='utf-8'))
        result = a.hexdigest()
        if not self.pipe.sismember('visited', result):
            self.pipe.sadd('visited', result)  # 去重
            if 'qq' in self.url:
                self.pipe.lpush('qq', self.url)
            if 'sina' in self.url:
                self.pipe.lpush('sina', self.url)
            if '163' in self.url:
                self.pipe.lpush('163', self.url)
            if 'baidu' in self.url:
                print("ok")
