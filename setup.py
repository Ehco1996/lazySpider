from setuptools import setup

setup(
    name='lazyspider',
    version='0.0.1',
    description='Powerful spider tools',
    long_description=''' 
    lazyspider is a powerful tools which can:
        help you get request header/cookie easily
        help you manipulate database in humanized way
    ''',
    url='https://github.com/Ehco1996/lazySpider',
    author='Ehco1996',
    author_email='zh19960202@gmial.com',
    license='GPLv3',
    keywords='spider headers mysql',
    zip_safe=False,
    install_requires=['pymysql'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: zh-cn',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['lazyspider'],
)
