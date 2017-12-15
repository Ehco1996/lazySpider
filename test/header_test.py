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

test_raw_headers = '''
GET /requests/requests/tree/master/requests HTTP/1.1
Host: github.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://github.com/requests/requests/blob/master/requests/models.py
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,mt;q=0.7
Cookie: logged_in=no; _octo=GH1.1.1774715580.1513235009; _ga=GA1.2.600936162.1513235009; tz=Asia%2FShanghai; _gh_sess=eyJzZXNzaW9uX2lkIjoiMjBhMzVlYzU0NzRiZjA5YzM0NmRlZjllZDQzNGNiYzgiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUxMzI0NTQ0MzcwMSwicmVmZXJyYWxfY29kZSI6Imh0dHBzOi8vY24uYmluZy5jb20vIiwiX2NzcmZfdG9rZW4iOiJJcnBBK2YxTHM1ZEQ2a2E5bEFnUVpmWm9vMERHRkk0eGVkVmhsRStDNDkwPSIsInNweV9yZXBvIjoicmVxdWVzdHMvcmVxdWVzdHMiLCJzcHlfcmVwb19hdCI6MTUxMzI0NTQ0M30%3D--a63379870b546ca33ec0a8c1e3629013ba77b42c
'''


def test_lazy_header():
    '''
    测试header/cookies是否被正确的传入
    '''
    lzh = LazyHeaders(test_raw_headers)
    headers = lzh.getHeaders()
    cookies = lzh.getCookies()
    r = requests.get('https://github.com/requests/requests/tree/master/requests',
                     headers=headers, cookies=cookies)
    assert r.status_code == 200


if __name__ == '__main__':
    pytest.main()
