from page.zkhkj import get_data,get_database


import requests
import pymysql
import unittest
f = get_data()
i = get_database()
class Test_login(unittest.TestCase):
    def setUp(self):
        url = 'http://127.0.0.1:8000/api/add_event/'
        # f = get_data()
        # i = get_database()

        self.data = {}
        self.data['eid'] = f.get_number(100, 200)
        self.data['name'] = '华为' + str(f.get_number(1, 10)) + '发布会'
        self.data['status'] = f.get_number(0, 1)
        self.data['limit'] = f.get_number(1, 100)
        self.data['address'] = f.get_address()
        self.data['start_time'] = f.get_datetime()
        r = requests.post(url,self.data)
        self.res = r.json()
        print(self.res)

    def tearDown(self):
        i.close()
    def test_case(self):
        con, cur = i.con_mysql()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        select_result = i.execute_sql(sql % (self.data['eid'], self.data['name']))
        if self.res['message'] == 'add event success' and self.res['status'] == 10000 and select_result == 1:
            print('pass')
        else:
            print('fail')


if __name__ == '__main__':
    unittest.main()