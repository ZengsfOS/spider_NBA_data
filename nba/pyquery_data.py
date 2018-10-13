from pyquery import PyQuery as pq
import requests
from nba.getRequestData import get_Data

def get_chooser_url():
    '''获取首页所有的名字与url以字典形式保存，全部放在一个大字典里面'''

    doc = pq(get_Data("http://www.stat-nba.com/award/item14.html"))
    a = doc(".chooserin")
    a.remove_class("chooserin")
    a.add_class("chooser")

    datas = doc(".chooser").items()
    ls = []
    urls = []
    for data in datas:
        ls.append(data.text())
        urls.append(data.attr("href"))
    lengths = len(ls)
    L = []
    for length in range(lengths):
        d = {}
        d[ls[length]] = urls[length]
        L.append(d)
    return L


def get_chooserlittle_url(url):
    doc = pq(get_Data(url))
    #url = "http://www.stat-nba.com/award/item19isnba0season2016.html"     #球员
    #doc = pq(get_Data("http://www.stat-nba.com/award/item19.html"))      #球队
    #修改查找到标签里面的class的内容
    a = doc(".chooserinlittle")
    a.remove_class("chooserinlittle")
    a.add_class("chooserlittle")

    datas = doc(".chooserlittle").items()
    ls = []
    urls = []
    for data in datas:
        ls.append(data.text())
        urls.append(data.attr("href"))
    #print(ls)
    #print(urls)
    lengths = len(ls)
    L = []
    for length in range(lengths):
        d = {}
        d[ls[length]] = urls[length]
        L.append(d)
    #print(L)
    #这里还要进行url判断，进行删除球员为键的字典还是球队为键的字典
    # if url == "http://www.stat-nba.com/award/item19isnba0season2016.html":
    #     del L[0]
    #     #print(L)
    # elif url == "http://www.stat-nba.com/award/item19.html":
    #     del L[1]
        #print(L)
    return L


def pyquery_get_all_datas(url):
    '''利用PyQuery来查询数据球队的薪金排名'''

    #发送请求，获取html文本
    #doc = pq(requests.get("http://www.stat-nba.com/award/item19.html").text.encode("ISO-8859-1").decode("UTF-8"))
    #doc = pq(requests.get("http://www.stat-nba.com/award/item19isnba0season2016.html").text.encode("ISO-8859-1").decode("UTF-8"))
    #doc = pq(get_Data("http://www.stat-nba.com/award/item19isnba0season2016.html"))
    doc = pq(get_Data(url))
    #得到thead tr th中的文本信息，以字符串的格式返回，这里把它变成了列表
    title = doc("thead tr th").text().split()
    #print(title)
    #得到tbody tr标签下面的所有标签，得到一个生成器对象
    trs = doc("tbody tr").items()
    ls = []
    #这里是循环遍历tr中所有td的文本信息，但由于会有空文本，因此做了处理，如果是空文本，则返回""
    for tr in trs:
        tds = tr("td").items()
        datas = []
        for td in tds:
            if td.text():
                datas.append(td.text())
            else:
                datas.append("")
        ls.append(datas)
    datalists = []
    #这里是每条记录以字典的形式返回。最后返回的是一个大列表集合
    for l in ls:
        dataline = {}
        for record_length in range(len(l)):
            dataline[title[record_length]] = l[record_length]
        datalists.append(dataline)
    #print(datalists)
    return datalists


def select_chooser_url(chooser, name):
    '''获取某个相对应的url'''
    for chooser_dict in chooser:
        for chooser_name, url in chooser_dict.items():
            if chooser_name == name:
                return "http://www.stat-nba.com" + url


def get_team_or_player_url(team_and_player):
    l = []
    for d in team_and_player:
        for name, url in d.items():
            d = {}
            d[name] = get_chooserlittle_url("http://www.stat-nba.com" + url)[2:]
        l.append(d)
    return l

def get_all_datas(all_url):
    ls = []
    ds = {}
    for x in all_url:
        for team_or_player, urls in x.items():
            #print(urls)
            l = []
            for y in urls:
                for name, url in y.items():
                    d = {}
                    datas = pyquery_get_all_datas("http://www.stat-nba.com" + url)
                    d[name] = datas
                    l.append(d)
            ds[team_or_player] = l
            ls.append(ds)
    return ls



def main():
    chooser = get_chooser_url()
    print(chooser)
    name = "薪金排名"
    chooser_url = select_chooser_url(chooser, name)
    print(chooser_url)
    team_and_player = get_chooserlittle_url(chooser_url)[0:2]
    print(team_and_player)
    all_url = get_team_or_player_url(team_and_player)
    datas = get_all_datas(all_url)
    print(datas)


if __name__ == "__main__":
    main()