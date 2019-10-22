from faker import Faker
import pymysql

class get_data():  #公共类
    fake = Faker(locale='zh_CN')
    def get_number(self,m,n): #ID
        return self.fake.random_int(min=m,max=n)
    def get_string(self): #name
        return self.fake.name()
    def get_address(self): #地址
        return self.fake.province()+'-'+self.fake.city()
    def get_datetime(self):  #时间
        return self.fake.future_datetime()
    def get_url(self):
        url = 'http://127.0.0.1:8000/api/'
        return url
    def get_urla(self):
        urla = 'add_event/' #添加发布会
        return urla
    def get_urlb(self):
        urlb = 'sec_get_event_list/' #查询发布会
        return urlb
    def get_urlc(self):
        urlc = 'add_guest/' #添加嘉宾
        return urlc




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

