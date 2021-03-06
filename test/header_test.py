'''
测试LazyHeaders是否运行正确
'''
import pytest
import requests
import os
import sys
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

from lazyspider.lazyheaders import LazyHeaders


from lazyspider.lazyheaders import LazyHeaders


test_raw_headers_curl = '''curl 'https://github.com/requests/requests/tree/master/requests' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,mt;q=0.7' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Cookie: _octo=GH1.1.301629262.1507796673; logged_in=yes; dotcom_user=Ehco1996; _ga=GA1.2.1257895217.1507796673; user_session=QUSFvf0-4hcyheR99vGbP0LVjiIbE5sa9lA0SLa6UZUorG8_; __Host-user_session_same_site=QUSFvf0-4hcyheR99vGbP0LVjiIbE5sa9lA0SLa6UZUorG8_; tz=Asia%2FShanghai; _gat=1; _gh_sess=eyJzZXNzaW9uX2lkIjoiMDM2OWE5YWJmNDc0YjY2ZWZiN2I0YTc4ZWE2ZWIxZTUiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUxMzQyMzM1MDAyNCwic3B5X3JlcG8iOiJyZXF1ZXN0cy9yZXF1ZXN0cyIsInNweV9yZXBvX2F0IjoxNTEzNDIzMzQ5fQ%3D%3D--cde3b6da4263f6f19e5ea0631ad90f1b05a373e3' -H 'Connection: keep-alive' --compressed'''


def test_lazy_header_curl():
    '''
    测试header/cookies是否被正确的传入
    '''
    lzh = LazyHeaders(test_raw_headers_curl)
    headers = lzh.getHeaders()
    cookies = lzh.getCookies()
    r = requests.get('https://github.com/requests/requests/tree/master/requests',
                     headers=headers, cookies=cookies)
    assert r.status_code == 200


if __name__ == '__main__':
    pytest.main()
