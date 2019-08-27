# -*- coding:utf-8 -*-
import re

import jieba
class Rank:
    def __init__(self,str):
        self.str =str
        self.li =[]
        self.item ={}
    def index(self):
        temp = []
        a =jieba.cut(self.str,cut_all=False)
        b =' '.join(a)
        b=b.split()

        for i in b:

            if len(i)>=2 and not i.isdigit():

                self.li.append(i)
        for i in self.li:
            chudu =set()
            if i not in self.item.keys():
                self.item[i]=chudu
            if len(temp)>=5:
                del temp[0]
            for j in temp:
                if(j== i):
                    continue
                else:
                    self.item.get(i).add(j)
                    self.item.get(j).add(i)
            temp.append(i)
        print(self.item)


    def rank(self):
        self.index()
        d =0.85
        score ={}
        for i in range(500):
            m ={}
            a =0.00
            for i,j in self.item.items():
                key =i
                value =j
                m[key] =1-d
                for k in value:
                    size =len(self.item[k])
                    if (key==k) or (size)==0:
                        continue
                    else:
                        m[key]=m[key]+d/size*(0 if score.get(k) == None  else score.get(k));
                a =max(a,abs(m.get(key)-(0 if score.get(key) == None  else score.get(key))))
            score=m
            if (a<=0.00001):
                break
        final =sorted(score.items(),key=lambda x:x[1],reverse=True)
        return final
str1="中国台湾网5月21日讯 据台湾“中时电子报”报道，“台湾大选”近日几份民调显示，高雄市长韩国瑜支持度下滑，尽管他仍是国民党最强王牌，但鸿海董事长郭台铭声势上扬，以差距2%紧追在后，他最后能否胜出代表国民党参选，已在未定之天。桃园新科议员谢美英分析，韩国瑜想保持高声势选台湾地区领导人，应直接宣布参选。2020台湾地区领导人初选战局，目前蓝绿都碰到状况，让尚未宣布参选的台北市长柯文哲坐收渔翁之利。从台湾“联合报”日前民调显示，韩国瑜支持度约下滑5%，他在国民党支持度仍最高，但郭台铭已急起直追。在面临柯文哲加入的“三脚督”对战，韩、郭两人都输柯文哲，曝露韩国瑜不再一枝独秀。更令外界意外的是，若是蓝绿对战，郭台铭的优势更胜韩国瑜。国民党初选要到7月5日才进行民调，眼见韩国瑜声势下滑，国民党挺韩同志倡议，国民党的提名时程宜提早进行，再拖下去会对韩国瑜参选不利。不过，韩国瑜日前表示，若国民党五人征询小组征召他初选，他说“yes,I do”，但现在高雄议会正在进行总质询，目前暂订见面时间是在总质询后的6月上旬。“中评社”报导，新科桃园市议员谢美英表示，韩国瑜刚选上高雄市长，民调冲很高，就好比当年的蔡英文跟马英九，声势最高、一举到达山顶，接着就开始下滑。除了有所谓的“打韩”、“黑韩”势力，韩国瑜到高雄市议会接受总质询，很多选民开始从“情感面”回到“理性面”，毕竟当初认为的“救世主”，还是要拿出真本事。她分析，目前韩国瑜民调最高，也最被蓝军看好，但随着韩民调开始下滑，蓝军也要重新评估，手上这张牌是否还是王牌？韩不如趁气势最旺直接宣布参选，真正营造胜选气势。"

a =Rank(str1)
b =a.rank()
print(b)
