'''
lazyspider.lazystore
data -> database
~~~~~~~~~~~~~~~~~~~~~

封装操纵数据库方法
'''

import pymysql.cursors


class LazyMysql():
    """
    封装操作mysql数据的方法
    做到了基本的增删改查
    :param configs <dict>
        TEST_DB = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'xxx',
            'db': 'EhcoTestDb'
            }
    Usage::
      >>> from lazyspider.lazystore import LazyMysql
      >>> store = LazyMysql(TEST_DB)
      >>> data <dict> {'id':1,'name':'ehco','age',20}
      >>> store.save_one_data(data,table_name)
    """

    def __init__(self, configs):
        '''
        初始化与数据库的连接
        '''
        self.configs = configs
        self.connect()

    def connect(self):
        self.con = pymysql.connect(
            host=self.configs['host'],
            user=self.configs['user'],
            password=self.configs['password'],
            db=self.configs['db'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def close(self):
        '''关闭数据库链接'''
        self.con.close()

    def query(self, sql):
        '''
        根据sql查询
        Args:
            sql: sql 语句 str
        return:
            成功： [dict] 保存的记录            
            失败： -1 并打印返回报错信息 
        '''
        try:
            self.connect()
            with self.con.cursor() as cursor:
                cursor.execute(sql)
                self.con.commit()
                res = cursor.fetchall()
                return res
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

    def save_one_data(self, data, table):
        '''
        将一条记录保存到数据库
        Args:
            table: 表名字 str
            data:  记录 dict
        return:
            成功： dict 保存的记录
            失败： -1 并打印返回报错信息            
        每条记录都以一个字典的形式传进来
        '''
        key_map = {}
        if len(data) == 0:
            print('请确保data被正确传入了')
            return -1
        fields = ''
        values = ''
        datas = {}
        for k, v in data.items():
            # 防止sql注入
            datas.update({k: pymysql.escape_string(v)})
        for d in datas:
            fields += "`{}`,".format(str(d))
            values += "'{}',".format(str(datas[d]))
        if len(fields) <= 0 or len(values) <= 0:
            return -1
        # 生成sql语句
        sql = "insert ignore into {}({}) values({})".format(
            table, fields[:-1], values[:-1])
        try:
            self.connect()
            with self.con.cursor() as cursor:
                # 执行语句
                cursor.execute(sql)
                self.con.commit()
                res = cursor.fetchone()
                return res
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

    def update_one_data(self, data, table, field):
        '''
        将一条记录更新到数据库
        Args:
            table: 表名字 str
            data:  记录 dict
            field: 用于检索更新的唯一字段 列如Id
        return:
            成功： 更新记录的id
            失败： -1 并打印返回报错信息
        每条记录都以一个字典的形式传进来
        '''
        key_map = {}
        if len(data) == 0:
            print('请确保data被正确传入了')
            return -1
        datas = {}
        updates = ''
        for k, v in data.items():
            # 防止sql注入
            datas.update({k: pymysql.escape_string(v)})
        for d in datas:
            if d == field:
                field_value = str(datas[d])
            updates += "{}='{}',".format(str(d), str(datas[d]))
        if len(updates) <= 0 or field_value == None:
            return -1
        # 生成sql语句
        sql = "update {} set {} where {} = '{}'".format(
            table, updates[:-1], field, field_value)
        try:
            self.connect()
            with self.con.cursor() as cursor:
                # 执行语句
                cursor.execute(sql)
                self.con.commit()
                res = cursor.fetchone()
                return cursor.rownumber
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

    def find_all(self, table, limit):
        '''
        从数据库里查询所有记录
        Args:
            table: 表名字 str
            limit: 限制数量
        return:
            成功： [dict] 保存的记录
            失败： -1 并打印返回报错信息            
        '''
        try:
            self.connect()
            with self.con.cursor() as cursor:
                sql = "select * from {} limit 0,{}".format(table, limit)
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

    def find_by_field(self, table, field, field_value):
        '''
        从数据库里查询指定条件的记录
        Args:
            table: 表名字 str
            field: 字段名
            field_value: 字段值
        return:
            成功： [dict] 保存的记录
            失败： -1 并打印返回报错信息                      
        '''
        try:
            self.connect()
            with self.con.cursor() as cursor:
                sql = "select * from {} where {} = '{}'".format(
                    table, field, field_value)
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

    def find_by_fields(self, table, queryset={}):
        '''
        从数据库里查询 符合多个条件的记录 
        Args:
            table: 表名字 str
            queryset : key 字段 value 值 dict
        return:
            成功： [dict] 保存的记录
            失败： -1 并打印返回报错信息                      
        '''
        try:
            self.connect()
            with self.con.cursor() as cursor:
                querys = ""
                for k, v in queryset.items():
                    querys += "{} = '{}' and ".format(k, v)
                sql = "select * from {} where {} ".format(
                    table, querys[:-4])
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

