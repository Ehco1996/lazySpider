'''
lazyspider.lazyheades
str -> dict 
~~~~~~~~~~~~~~~~~~~~~

将header字符串转换为字典格式
'''

from http.cookies import SimpleCookie


class LazyHeaders(object):
    """
    将requests headers <str> 格式化为对应的dict
    返回一个转换后的heaers
    :param raw_str: str form chrome dev tools -> Copy request headers / Copy as cURL
    Usage::
      >>> from lazyspider import lazyheaders
      >>> lzay = LazyHeaders(raw_str)  
      >>> headers = lzay.getHeaders()
      >>> cookies = lazy.getCookies()
      >>> r = requests.get(url,headers=headers, cookies=cookies)
    """

    def __init__(self, raw_str):
        '''
        判断输入的字符串是request headers 还是 curl
        '''
        if '\n' in raw_str:
            self.data = self._stripStr(raw_str, ' ').split('\n')
        elif '-H' in raw_str:
            self.data = self._stripStrList(
                raw_str, ['"', ' ', "'"]).split('-H')

    def _stripStr(self, raw_str, stop_str):
        '''
        去除字符串中的所有指定字符串
        args：
            raw_str 源字符串
            stop_str 指定字符串
        return
            str 筛选后的字符串
        '''
        try:
            return raw_str.replace(stop_str, '')
        except:
            raise Exception('error input must be headers string')

    def _stripStrList(self, raw_str, stop_strs):
        '''
        去除字符串中的所有指定字符串
        args：
            raw_str 源字符串
            stop_strs 指定字符串 列表
        return
            str 筛选后的字符串
        '''
        if type(stop_strs) == list:
            for word in stop_strs:
                raw_str = self._stripStr(raw_str, word)
            return raw_str
        else:
            raise Exception('stop_words must be list!')

    def getCookies(self):
        '''
        从字符串中格式化出字典形式的Cookies
        '''
        items = self.data
        for item in items:
            if item[:6] == 'Cookie':
                cookies = SimpleCookie(item[7:])
                return {i.key: i.value for i in cookies.values()}
        return cookies

    def getHeaders(self):
        '''
        从字符串中格式化出字典形式的Headers
        '''
        raw_headers = self.data
        headers = {}
        for item in raw_headers:
            if len(item) > 0 and item[:4] != 'curl' and item[:3] != 'GET' and item[:6] != 'Cookie':
                sp = item.split(':')
                headers[sp[0]] = sp[1]
        return headers
