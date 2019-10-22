import requests
import pymysql
from faker import Faker

class get_data():
    fake = Faker(locale='zh_CN')
    def get_number(self,m,n):
        return self.fake.random_int(min=m,max=n)
    def get_string(self):
        return self.fake.sentence()[:-1]
    def get_address(self):
        return self.fake.province()+'-'+self.fake.city()
    def get_datetime(self):
        return self.fake.future_datetime()

def con_mysql():
    try:
        con = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'learn', port = 3306, charset = 'utf8')
    except:
        print('连接失败')
    else:
        print('成功连接')
        cur = con.cursor()
    return con,cur
def execute_sql(cur,sql):
    return cur.execute(sql)
def close(con,cur):
    cur.close()
    con.close()

url = 'http://127.0.0.1:8000/api/add_event/'
f = get_data()
data = {}
data['eid'] = f.get_number(100,200)
data['name'] = '华为'+str(f.get_number(1,10))+'发布会'
data['status'] = f.get_number(0,1)
data['limit'] = f.get_number(1,100)
data['address'] = f.get_address()
data['start_time'] = f.get_datetime()
r = requests.post(url,data)
res = r.json()
print(res)
con,cur = con_mysql()
sql = 'select * from sign_event where id="%d" and name="%s";'
select_result = execute_sql(cur,sql %(data['eid'],data['name']))
if res['message'] == 'add event success' and res['status'] == 10000 and select_result == 1:
    print('pass')
else:
    print('fail')
close(con,cur)

