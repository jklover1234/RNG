from faker import Faker
import pymysql
class get_data():  #公共类
    fake = Faker(locale='zh_CN')
    def get_number(self,m,n):
        return self.fake.random_int(min=m,max=n)
    def get_string(self):
        return self.fake.sentence()[:-1]
    def get_address(self):
        return self.fake.province()+'-'+self.fake.city()
    def get_datetime(self):
        return self.fake.future_datetime()

class get_database():

    def con_mysql(self):
        try:
            self.con = pymysql.connect(host='localhost', user='root', password='root', database='learn', port=3306,
                                           charset='utf8')
        except:
            print('连接失败')
        else:
            print('成功连接')
            self.cur = self.con.cursor()
        return self.con, self.cur

    def execute_sql(self, sql):
        return self.cur.execute(sql)

    def close(self):
        self.cur.close()
        self.con.close()