import requests
import re


def get_Data():
    try:
        url = "https://nba.hupu.com/stats/players/pts/1"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None


def get_Data_Parse(html):
    # pattern = re.compile('<tr.*?bg_a">.*?width="46">(.*?)</td>.*?class="left">(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'
    #                     '.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'
    #                     '.*?>(.*?)</td>.*?>(.*?)</td>', re.S)
    pattern = re.compile('<tr.*?width="46">(.*?)</td>.*?class="left">(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'
                         '.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)</td>'
                         '.*?>(.*?)</td>.*?>(.*?)</td>', re.S)
    print(pattern)
    result = re.findall(pattern, html)
    for i in result:
            print(i)
    return result


def main():
    html = get_Data()
    print(html)
    data = get_Data_Parse(html)
    print(data)


if __name__ =="__main__":
    main()
