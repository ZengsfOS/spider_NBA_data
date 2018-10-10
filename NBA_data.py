import requests
import itertools
import time
from headers import header
import json

#通过ulr来获取到数据
def getData(x):
	url = "http://china.nba.com/static/data/league/playerlist_{}.json".format(chr(x))
	# url = "http://china.nba.com/static/data/league/playerlist_{}.json".format("A")
	headers = {'User-Agent': header()}
	response = requests.get(url, headers).text
	#	time.sleep(3)
	#	print(response.text)
	return response

def drawData(data):
	json_data = json.loads(data)      #将json数据装换为字典
	jsonlist = json_data["payload"]["players"]
	str_data = ""
	for i in jsonlist:
		playerProfile = i["playerProfile"]
		teamProfile = i["teamProfile"]
		datas = dict(playerProfile, **teamProfile)   #将两个字典合并成一个字典
		str_data += str(datas) + ","
	return str_data
#print(headers)

def main():
	str_datas = ""
	#itertools就是一个迭代器工具，这里取出65—90，然后转换成A—Z。
	for x in itertools.count(65):
		if x > 90:
			break
		data = getData(x)
		datas = drawData(data)
		str_datas += datas
	str_datas = str_datas.rstrip(",")    #将说有数据编程一个字符串
	# print(str_datas)
    # print(type(str_datas))
	str_datas = eval(str_datas)          #将其字符串转换为一个元组，因此好循环遍历
	print(str_datas)
	print(len(str_datas))
	print(type(str_datas))
	return str_datas


if __name__ == "__main__":
	main()
