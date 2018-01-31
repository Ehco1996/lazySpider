# lazySpider
爬虫的各种坑 我来填 :)

# LazySpider 发布啦！

lazyspider 并不是一个爬虫框架
他只是一个写爬虫时经常会用到的小工具

> 这是我实习的时候写了一个多月爬虫，期间遇到的一些坑  
> 想着有没有比较好的方式来解决  
> 于是`lazyspider`就诞生啦！名字是女票给起的，感觉还不错hhh~

### 功能介绍

其实目前也就实现了两个功能

* 将chrome浏览器的里`cookie/header`格式化为`dict`格式，方便调用
* 将`pymysql`再次封装了一层,做到了基本的增删改查
* random user-agent的支持

所以目前lazy里也只有三个小模块：

* lazyheaders
* lazystore
* lazyagent

### 安装

直接用pip安装就可以
仅支持py3~

```bash
pip install lazyspier
```

### 使用说明
`lazyspider`用起来十分简单

### lazyheaders

> 主要用于格式化cookies 和headers

源字符串来自chrome开发工具页面请求的 `Copy -> Copy as cURL`：

![](http://opj9lh0x4.bkt.clouddn.com/17-12-19/33196220.jpg)

复制好**原始字符串**之后：

```python
from lazyspider.lazyheaders import LazyHeaders

# 注意！字符串要包裹在 三引号 或 双引号 里
curl = "curl 'https://pypi.python.org/pypi' -H 'cookie: .....balabala...."

lh = LazyHeaders(curl)

headers = lh.getHeaders()
cookies = lh.getCookies()

print('*' * 40)
print('Headers: {}'.format(headers))
print('*' * 40)
print('Cookies: {}'.format(cookies))
print('*' * 40)

import requests
r = requests.get('https://pypi.python.org/pypi',
                 headers=headers, cookies=cookies)
print(r.status_code)

```
输出如下:

```bash
****************************************
Headers: {'origin': 'https', 'accept-encoding': 'gzip,deflate,br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,mt;q=0.7', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_13_2)AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.84Safari/537.36', 'content-type': '', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'cache-control': 'max-age=0', 'authority': 'pypi.python.org', 'referer': 'https'}
****************************************
Cookies: {'__utma': '32101439.146958433.1508462081.1509339065.1512998855.2', '__utmz': '32101439.1512998855.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', '_ga': 'GA1.2.146958433.1508462081', '_gid': 'GA1.2.555764366.1513659919', 'login_nonce': 'V649T4tBPTqQmg87ElGoHXQFviJkoz', 'pypi': '520cfc4475316b0c3fc41091af563886'}
****************************************
200
```
是不是很方便呢？


### lazystore

目前只封装了`mysql`的操作，用法也简单

**初始化数据库连接**

```python
from lazyspider.lazystore import LazyMysql

# 数据库配置
TEST_DB = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'xxx',
    'db': 'EhcoTestDb'
}
# 初始化数据库链接
store = LazyMysql(TEST_DB)
```

**保存数据**

```python
# 将要保存的数据以字典格式存储
data = {'id': 1, 'name': 'ehco', 'age': 20}
# 新增数据的方法
# 只需要传入 数据<dict> 表名 两个参数
state = store.save_one_data(data, 'testtable')
print(state)
# 数据保存成功会返回1
# 保存失败会返回-1 并打印错误堆栈
>>1
```

**删除数据**

```python
# 这里我将id为1的数据删除
state = store.delete_by_field('testtable','id','1')
print (state)
>>1
```

**更新数据**

```python
# 这里我更新id为1的name字段
data = {'id': 1, 'name': 'superehco', 'age': 20}
state = store.update_by_id(data, 'testtable', '1')
print(state)
>>1
```

**查询数据**

```python
# 这里我更新id为1的name字段
res = store.find_by_field('testtable', 'age', '20')
print(res)
# 返回的是一个列表，每条查询记录都以字典格式返回
'''
[{'id': 1, 'name': 'superehco', 'age': 20}, {'id': 2, 'name': 'lurenjia', 'age': 20}]
'''
```

**SQL语句查询**

```python
# 手撸sql也是必备的
sql = "select * from testtable"
res = store.query(sql)
print(res)
'''
[{'id': 1, 'name': 'superehco', 'age': 20}, {'id': 2, 'name': 'lurenjia', 'age': 20}]
'''
```

### lazyagent

可以随机获取到一些常用的ua

```python
from lazyspider.lazyagent import LazyAgent

ua = LazyAgent()

print(ua.mac)
# Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)

print(ua.linux)
# Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1

print(ua.win)
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)

print(ua.opera)
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11

print(ua.google)
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13

print(ua.firefox)
# Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1

print(ua.safari)
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57

print(ua.edge)
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586

print(ua.getRandomUa())
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)
