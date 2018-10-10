import requests
import re


def get_html_use_data():
    '''获取每个赛季中最好的球员'''
    url = "http://www.stat-nba.com/award/item14pr4.html"
    response = requests.get(url)
    html = response.text.encode("ISO-8859-1").decode("UTF-8")

    index = ['赛季', '球员', '联盟', '出场', '首发', '时间', '投篮', '命中', '出手', '三分',
             '三分命中', '三分出手', '罚球', '罚球命中', '罚球出手',
             '篮板', '前场', '后场', '助攻', '抢断', '盖帽',
             '失误', '犯规', '得分']
    ls = []
    for i in range(45):
        pattern = re.compile('<tr>.*?row{}.*?>(.*?)</td>.*?target.*?>(.*?)</a></td>.*?>(.*?)</td>'
                        '.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'
                        '.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'
                        '.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'
                        '.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'.format(i), re.S)
        result = re.search(pattern, html)
        d = {}
        l = []
        for x in result.groups():
            l.append(x)
        print(l)
        d['赛季'] = l[0]
        d['球员'] = l[1]
        d['联盟'] = l[2]
        d['出场'] = l[3]
        d['首发'] = l[4]
        d['时间'] = l[5]
        d['投篮'] = l[6]
        d['命中'] = l[7]
        d['出手'] = l[8]
        d['三分'] = l[9]
        d['三分命中'] = l[10]
        d['三分出手'] = l[11]
        d['罚球'] = l[12]
        d['罚球命中'] = l[13]
        d['罚球出手'] = l[14]
        d['篮板'] = l[15]
        d['前场'] = l[16]
        d['后场'] = l[17]
        d['助攻'] = l[18]
        d['抢断'] = l[19]
        d['盖帽'] = l[20]
        d['失误'] = l[21]
        d['犯规'] = l[22]
        d['得分'] = l[23]
        ls.append(d)
    print(ls)
    return ls




def main():
    data = get_html_use_data()
    print(data)


if __name__ == "__main__":
    main()
