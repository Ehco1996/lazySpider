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
    :param cRUL_str: str form chrome dev tools ->  Copy as cURL
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
        self.data = self._stripStrList(
            raw_str, [' ', "'"]).split('-H')

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

    def _judeNOtIn(self, raw_str, ele_list):
        '''
        判断ele是否在原始字符串中
        args：
            raw_str 源字符串
            ele_list  待检查的列表
        return
            boolean
        '''
        for ele in ele_list:
            if ele in raw_str:
                return False
        return True

    def getCookies(self):
        '''
        从字符串中格式化出字典形式的Cookies
        '''
        items = self.data
        for item in items:
            if 'cookie' in item or 'Cookie' in item:
                cookies = SimpleCookie(item[7:])
                return {i.key: i.value for i in cookies.values()}
        return {}

    def getHeaders(self):
        '''
        从字符串中格式化出字典形式的Headers
        '''
        items = self.data
        headers = {}
        for item in items:
            if len(item) > 0 and self._judeNOtIn(item, ['curl', 'GET', 'Cookie', 'cookie']):
                sp = item.split(':')
                headers[sp[0]] = sp[1]
        return headers
