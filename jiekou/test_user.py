from zkhkj import get_data,get_database
import requests
import unittest
f = get_data()
i = get_database()
class Test_login(unittest.TestCase):
    '''查询发布会'''
    def setUp(self):
        self.url = f.get_url()+f.get_urlb()


    def tearDown(self):
        i.close()
    def test_case(self):
        '''ID查询发布会成功'''
        data = {}
        data['eid'] = 1000

        r = requests.get(self.url, data, auth=('Q1', 'sys123456'))
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        sql = 'select * from sign_event where id=1000;'
        select_result = i.execute_sql(sql)
        try:

            self.assertEqual(self.res['message'], 'success')
            self.assertEqual(self.res['status'], 200)
            self.assertEqual(select_result,1)

        except:
            print('fail')
            raise Exception

    def test_case1(self):
        '''name查询发布会成功'''
        data = {}
        data['name'] = '移动'

        r = requests.get(self.url, data, auth=('Q1', 'sys123456'))
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        sql = 'select * from sign_event where name="移动";'
        select_result = i.execute_sql(sql)

        try:

            self.assertEqual(self.res['message'], 'success')
            self.assertEqual(self.res['status'], 200)
            self.assertEqual(select_result, 1)

        except:
            print('fail')
            raise Exception

    def test_case2(self):
        '''不存在的账户信息，登录失败'''
        data = {}
        data['name'] = '移动'

        r = requests.get(self.url, data)
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()

        try:

            self.assertEqual(self.res['message'], 'user auth null')
            self.assertEqual(self.res['status'], 10011)


        except:
            print('fail')
            raise Exception

    def test_case3(self):
        '''错误的密码，登录失败'''
        data = {}
        data['name'] = '移动'

        r = requests.get(self.url, data, auth=('Q1', 'sys123457'))
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()

        try:

            self.assertEqual(self.res['message'], 'user auth fail')
            self.assertEqual(self.res['status'], 10012)

        except:
            print('fail')
            raise Exception

    def test_case4(self):
        '''不输入标题ID，查询失败'''
        data = {}


        r = requests.get(self.url, data, auth=('Q1', 'sys123456'))
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()

        try:

            self.assertEqual(self.res['message'], 'parameter error')
            self.assertEqual(self.res['status'], 10021)

        except:
            print('fail')
            raise Exception

    def test_case5(self):
        '''使用不存在的ID，查询失败'''
        data = {}
        data['eid'] = 111

        r = requests.get(self.url, data, auth=('Q1', 'sys123456'))
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()

        try:

            self.assertEqual(self.res['message'], 'query result is empty')
            self.assertEqual(self.res['status'], 10022)

        except:
            print('fail')
            raise Exception



if __name__ == '__main__':
    unittest.main()