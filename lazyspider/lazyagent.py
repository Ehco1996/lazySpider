'''
lazyspider.lazyagent
get random user-agent
~~~~~~~~~~~~~~~~~~~~~
提供random user-agent
'''


from random import choices


class LazyAgent():

    RUA = {
        'mac': 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
        'linux': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        'win': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
        'opera': 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
        'google': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
        'firefox': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
        'edge': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'safari': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57'
    }

    def __init__(self):
        # 系统
        self.mac = self.RUA['mac']
        self.linux = self.RUA['linux']
        self.win = self.RUA['win']
        # 浏览器
        self.opera = self.RUA['opera']
        self.google = self.RUA['google']
        self.firefox = self.RUA['firefox']
        self.safari = self.RUA['safari']
        self.edge = self.RUA['edge']

    def getRandomUa(self):
        '''
        随机获取一个user-agent
        '''
        ua = choices(list(self.RUA.values()))[0]
        return ua
