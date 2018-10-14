# -*- coding:utf-8 -*-
import requests
import re
from nba.get_Url_Html import get_html_use_data
from nba.getRequestData import get_Data


def get_Data_Parse(html):
    '''将html中所要的数据提取出来,提取出来的数据是各项数据王中的网络url'''
    pattern = re.compile('<div.*?2px.*?>.*?class="chooserinlittle" href="(.*?)"><div>(.*?)</div>'
                         '.*?class="chooserlittle" href="(.*?)"><div>(.*?)</div>'
                         '.*?class="chooserlittle" href="(.*?)"><div>(.*?)</div>'
                         '.*?class="chooserlittle" href="(.*?)"><div>(.*?)</div>'
                         '.*?class="chooserlittle" href="(.*?)"><div>(.*?)</div>', re.S)
    print(pattern)
    result = re.search(pattern, html)
    l = []    # 将查找出来的数据存入列表中
    for i in result.groups():
        l.append(i)
    print(l)
    return l


def tidy_data(data):
    '''将解析出来的url的数据进行整理
    {'0': '/award/item14pr0.html', '1': '/award/item14pr1.html', '2': '/award/item14pr2.html', '3': '/award/item14pr3.html', '4': '/award/item14pr4.html'}
    {'0': '得分王', '1': '篮板王', '2': '助攻王', '3': '盖帽王', '4': '抢断王'}'''
    d = {}
    d1 = {}
    for i in range(0,5):
        d["{}".format(i)] = data[i*2]
        d1["{}".format(i)] = data[i*2+1]
    print(d)
    print(d1)
    return d, d1


def thread_get_data(visit_url, visit_name):
    '''利用线程，获取各项数据王的所有数据'''
    all_data = []
    for x in visit_url:
        url_end = "http://www.stat-nba.com" + visit_url["{}".format(x)]
        print(x)
        print(visit_url["{}".format(x)])
        datas = get_html_use_data(str(x), url_end, visit_name)
        all_data.append(datas)
    return all_data


def main():
    url = "http://www.stat-nba.com/award/item14.html"
    html = get_Data(url)
    print(html)
    data = get_Data_Parse(html)
    print(data)
    visit_url, visit_name = tidy_data(data)
    print(visit_url, visit_name)
    datas = thread_get_data(visit_url, visit_name)
    print(datas)


if __name__ == "__main__":
    main()
