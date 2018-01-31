from setuptools import setup

VERSION = '0.0.3'
URL = 'https://github.com/Ehco1996/lazySpider'
KEYWORDS = 'spider headers mysql'
EMAIL = 'zh19960202@gmial.com'
DESCRIPTION = "Powerful spider tools"
LONG_DESCRIPTION = '''
                    lazyspider is a powerful tools which can: 
                    help you get request header/cookie easily
                    help you manipulate database in humanized way
                    '''
REQUIRES = ['pymysql']
PACKAGES = ['lazyspider']

setup(
    name='lazyspider',
    author='Ehco1996',
    license='GPLv3',
    zip_safe=False,
    url=URL,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author_email=EMAIL,
    keywords=KEYWORDS,
    install_requires=REQUIRES,
    packages=PACKAGES,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
