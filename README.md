## 功能
- 连续获取一个或多个**微博关键词搜索**结果，并将结果写入文件（可选）、数据库（可选）等。所谓微博关键词搜索即：**搜索正文中包含指定关键词的微博**，可以指定搜索的时间范围。<br>
- 通过analyse.py对爬取的微博内容进行词云分析

## 输出
- 微博id：微博的id，为一串数字形式
- 微博bid：微博的bid
- 微博内容：微博正文
- 头条文章url：微博中头条文章的url，若某微博中不存在头条文章，则该值为''
- 原始图片url：原创微博图片和转发微博转发理由中图片的url，若某条微博存在多张图片，则每个url以英文逗号分隔，若没有图片则值为''
- 视频url: 微博中的视频url和Live Photo中的视频url，若某条微博存在多个视频，则每个url以英文分号分隔，若没有视频则值为''
- 微博发布位置：位置微博中的发布位置
- 微博发布时间：微博发布时的时间，精确到天
- 点赞数：微博被赞的数量
- 转发数：微博被转发的数量
- 评论数：微博被评论的数量
- 微博发布工具：微博的发布工具，如iPhone客户端、HUAWEI Mate 20 Pro等，若没有则值为''
- 话题：微博话题，即两个#中的内容，若存在多个话题，每个url以英文逗号分隔，若没有则值为''
- @用户：微博@的用户，若存在多个@用户，每个url以英文逗号分隔，若没有则值为''
- 原始微博id：为转发微博所特有，是转发微博中那条被转发微博的id，那条被转发的微博也会存储，字段和原创微博一样，只是它的本字段为空
- 结果文件：保存在当前目录“结果文件”文件夹下以关键词为名的文件夹里
- 微博图片：微博中的图片，保存在以关键词为名的文件夹下的images文件夹里
- 微博视频：微博中的视频，保存在以关键词为名的文件夹下的videos文件夹里

## 使用说明
本程序的所有配置都在setting.py文件中完成，该文件位于“weibo-search\weibo\settings.py”。
### 1.下载脚本
```bash
$ git clone https://github.com/dataabc/weibo-search.git
```
### 2.安装Scrapy
本程序依赖Scrapy，要想运行程序，需要安装Scrapy。如果系统中没有安装Scrapy，请根据自己的系统安装Scrapy，以Ubuntu为例，可以使用如下命令：
```bash
$ pip install scrapy
```
### 3.安装依赖
```
$ pip install -r requirements.txt
```

### 4.设置cookie
DEFAULT_REQUEST_HEADERS中的cookie是我们需要填的值，如何获取cookie详见[如何获取cookie](#如何获取cookie)，获取后将"your cookie"替换成真实的cookie即可。
### 5.设置搜索关键词
修改setting.py文件夹中的KEYWORD_LIST参数。
如果你想搜索一个关键词，如“迪丽热巴”：
```
KEYWORD_LIST = ['迪丽热巴']
```
如果你想分别搜索多个关键词，如想要分别获得“迪丽热巴”和“杨幂”的搜索结果：
```
KEYWORD_LIST = ['迪丽热巴', '杨幂']
```
如果你想搜索同时包含多个关键词的微博，如同时包含“迪丽热巴”和“杨幂”微博的搜索结果：
```
KEYWORD_LIST = ['迪丽热巴 杨幂']
```
如果你想搜索微博话题，即包含#的内容，如“#迪丽热巴#”：
```
KEYWORD_LIST = ['#迪丽热巴#']
```
也可以把关键词写进txt文件里，然后将txt文件路径赋值给KEYWORD_LIST，如：
```
KEYWORD_LIST = 'keyword_list.txt'
```
txt文件中每个关键词占一行。
### 6.设置搜索时间范围
START_DATE代表搜索的起始日期，END_DATE代表搜索的结束日期，值为“yyyy-mm-dd”形式，程序会搜索包含关键词且发布时间在起始日期和结束日期之间的微博（包含边界）。比如我想筛选发布时间在2020-06-01到2020-06-02这两天的微博：
```
START_DATE = '2020-06-01'
END_DATE = '2020-06-02'
```
### 7.运行程序
```bash
$ scrapy crawl search -s JOBDIR=crawls/search
```
其实只运行“scrapy crawl search”也可以，只是上述方式在结束时可以保存进度，下次运行时会在程序上次的地方继续获取。注意，如果想要保存进度，请使用“Ctrl + C”**一次**，注意是**一次**。按下“Ctrl + C”一次后，程序会继续运行一会，主要用来保存获取的数据、保存进度等操作，请耐心等待。下次再运行时，只要再运行上面的指令就可以恢复上次的进度。
## 如何获取cookie
1.用Chrome打开<https://passport.weibo.cn/signin/login>；<br>
2.输入微博的用户名、密码，登录，如图所示：
![](https://picture.cognize.me/cognize/github/weibospider/cookie1.png)
登录成功后会跳转到<https://m.weibo.cn>;<br>
3.按F12键打开Chrome开发者工具，在地址栏输入并跳转到<https://weibo.cn>，跳转后会显示如下类似界面:
![](https://picture.cognize.me/cognize/github/weibospider/cookie2.png)
4.依此点击Chrome开发者工具中的Network->Name中的weibo.cn->Headers->Request Headers，"Cookie:"后的值即为我们要找的cookie值，复制即可，如图所示：
![](https://picture.cognize.me/cognize/github/weibospider/cookie3.png)

##声明
- 本项目参考了以下项目：
https://github.com/dataabc/weibo-search
- 本项目禁止商用
- 如有问题，欢迎提出issues并与我取得联系：eeyushuli@gmail.com