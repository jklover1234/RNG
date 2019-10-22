from zkhkj import get_data,get_database
import requests
import unittest
f = get_data()
i = get_database()
mark = 0

class Test_login(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        url = f.get_url()+f.get_urla()


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
        global mark
        mark+=1
        i.close()
    def test_case(self):
        '''添加发布会成功'''
        self.con, self.cur = i.con_mysql()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        select_result = i.execute_sql(sql % (self.data['eid'], self.data['name']))
        try:
            self.assertEqual(self.res['message'],'add event success')
            self.assertEqual(self.res['status'],10000)
            self.assertEqual(select_result,1)

        except:
            print('fail')
            raise Exception


    def test_case1(self):
        '''添加发布会成功'''
        self.con, self.cur = i.con_mysql()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        select_result = i.execute_sql(sql % (self.data['eid'], self.data['name']))
        try:
            self.assertEqual(self.res['message'],'add event success')
            self.assertEqual(self.res['status'],10000)
            self.assertEqual(select_result, 1)

        except:
            print('fail')
            raise Exception


if __name__ == '__main__':
    unittest.main()