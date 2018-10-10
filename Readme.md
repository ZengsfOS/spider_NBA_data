## 爬取NBA信息
- 通过这个网站来爬取[http://www.stat-nba.com/award/item14.html]()
- 用到requests和re库
- 返回的数据都是以列表里面嵌套多个字典的形式。

## py文件的介绍
> 1. stat_NBA_data.py文件是运行文件，返回出来的数据是一个大列表里面嵌套每页数据的小列表，小列表里面是以字典的形式存放值。
> 2. get_Url_Html.py文件是一个请求数据且将数据爬去出来的模块。
> 3. headers.py文件是存放多个请求头headers，这样在利用url取拿去html数据的时候，防止让服务器识别是爬虫。
> 4. data_ranking.py文件是爬取[https://nba.hupu.com/stats/players/pts/1]()下的数据，该py文件可以直接运行获取数据。
> 5. NBA_data.py爬取的是[http://china.nba.com/playerindex/]()网站下的所有球员信息。