'''
lazyspider.lazyheades
str -> dict 
~~~~~~~~~~~~~~~~~~~~~

将header字符串只能转换为字典格式
方便调用 
'''

from http.cookies import SimpleCookie


class LazyHeaders(object):
    """
    将requests headers <str> 格式化为对应的dict
    返回一个转换后的heaers
    :param raw_str: str form chrome dev tools : Copy request headers
    Usage::
      >>> from lazyspider import lazyheaders
      >>> lzay = LazyHeaders(raw_str)  
      >>> headers = lzay.getHeaders()
      >>> cookies = lazy.getCookies()
      >>> r = requests.get(url,headers=headers, cookies=cookies)
    """

    def __init__(self, raw_str):
        self.data = self._stripStr(raw_str)

    def _stripStr(self, raw_str):
        '''
        去除字符串中的所有空格
        '''
        try:
            return raw_str.replace(' ', '')
        except:
            raise Exception('error input must be headers string')

    def getCookies(self):
        items = self.data.split('\n')
        for item in items:
            if item[:6] == 'Cookie':
                cookies = SimpleCookie(item[7:])
                return {i.key: i.value for i in cookies.values()}
        return cookies

    def getHeaders(self):
        raw_headers = self.data.split('\n')
        headers = {}
        for item in raw_headers:
            if len(item) > 0 and item[:3] != 'GET' and item[:6] != 'Cookie':
                sp = item.split(':')
                headers[sp[0]] = sp[1]
        return headers
