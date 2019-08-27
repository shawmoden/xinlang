import asyncio

from fen.bing import Fruit

from fen.sl import Cong


item ={"巨坑":'http://baidu.com'}
a ={
    'http://www.sina.com.cn/midpage/mobile/index.d.html?docID=htxyzsk9503601&url=news.sina.cn/gn/2019-03-22/detail'
    '-ihtxyzsk9503601.d.html': {'title': ['江苏盐城化工厂爆炸厂区被完全摧毁 核心区现巨坑_新浪网'], 'key': ['化工厂爆炸', '巨坑', '盐城', '核心区', '厂区']}}
AllList =[]
a = Cong()
asyncio.run(a.main())
li =a.save()
print(li)
'''
li = [
    {'http://finance.sina.com.cn/zl/international/2019-03-06/zl-ihrfqzkc1609472.shtml': {'title': ['霍华德·戴维斯：科技巨头何以搅动金融市场？|金融科技|苹果|谷歌_新浪财经_新浪网'], 'key': ['金融科技', '苹果', '谷歌']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-11/zl-ihsxncvh1643257.shtml': {'title': ['魏欣：美国能否保持科技人才优势|美国|人才|科技人才_新浪财经_新浪网'], 'key': ['美国', '人才', '科技人才','谷歌']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-13/zl-ihrfqzkc3570388.shtml#J_Comment_Wrap': {'title': ['菲尔普斯：经济学需要三场革命|经济学|菲尔普斯|经济学革命_新浪财经_新浪网'], 'key': ['经济学', '菲尔普斯', '经济学革命']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-15/zl-ihsxncvh2710577.shtml#J_Comment_Wrap': {'title': ['魏欣：招生腐败案之外美国大学还存在哪些问题|美国高校|招生腐败案_新浪财经_新浪网'], 'key': ['美国高校', '招生腐败案']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-21/zl-ihtxyzsk9249344.shtml#J_Comment_Wrap': {'title': ['约瑟夫·斯蒂格利茨：市场集中正在威胁美国经济|金融科技|美国|经济_新浪财经_新浪网'], 'key': ['金融科技', '美国', '经济']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-11/zl-ihsxncvh1643257.shtml#J_Comment_Wrap': {'title': ['魏欣：美国能否保持科技人才优势|美国|人才|科技人才_新浪财经_新浪网'], 'key': ['美国', '人才', '科技人才']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-13/zl-ihrfqzkc3570388.shtml': {'title': ['菲尔普斯：经济学需要三场革命|经济学|菲尔普斯|经济学革命_新浪财经_新浪网'], 'key': ['经济学', '菲尔普斯', '经济学革命']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-15/zl-ihsxncvh2710577.shtml': {'title': ['魏欣：招生腐败案之外美国大学还存在哪些问题|美国高校|招生腐败案_新浪财经_新浪网'], 'key': ['美国高校', '招生腐败案']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-06/zl-ihrfqzkc1609472.shtml#J_Comment_Wrap': {'title': ['霍华德·戴维斯：科技巨头何以搅动金融市场？|金融科技|苹果|谷歌_新浪财经_新浪网'], 'key': ['金融科技', '苹果', '谷歌']}},
    {'http://finance.sina.com.cn/zl/international/2019-03-21/zl-ihtxyzsk9249344.shtml': {'title': ['约瑟夫·斯蒂格利茨：市场集中正在威胁美国经济|金融科技|美国|经济_新浪财经_新浪网'], 'key': ['金融科技', '美国', '经济']}}]
'''

for i in li:
    c =i.keys()
    b = list(i.values())[0].get('key')

    c =list(c)
    list1 =[]
    for i in range(9):
        list1=list1+c

    d =dict(zip(b,list1))

    AllList.append(d)
#print(AllList)

List1 =[]
for i in AllList:

    for j,k in i.items():

        List1.append({j:[k]})

KK =[]
i =1
while i<len(List1):
    y=0
    if y!=0:

        x =y+Fruit(List1[i])
        y =x.mydict
        i+=1
    else:
        y = Fruit(List1[0])
        x = y + Fruit(List1[i])
        y = x.mydict
        i+=1
KK.append(y)
print(KK)
for i in KK:
    print(i.keys())

