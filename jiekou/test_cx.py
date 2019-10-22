from zkhkj import get_data,get_database
import requests
import unittest

f = get_data()
i = get_database()

class Test_login1(unittest.TestCase):
    '''添加嘉宾'''
    def setUp(self):
        self.url = f.get_url()+f.get_urlc()

    def tearDown(self):

        i.close()
    def test_case1(self):
        '''添加嘉宾成功'''
        self.data = {}
        self.data['eid'] = 1004
        self.data['phone'] = f.get_number(18000000000, 18999999999)
        self.data['realname'] = f.get_string()

        print(self.data)

        r = requests.post(self.url, self.data)

        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        sql = 'select * from sign_guest where phone="%s";'
        select_result = i.execute_sql(sql % (self.data['phone']))
        try:
            self.assertEqual(self.res['message'], 'add guest success')
            self.assertEqual(self.res['status'], 10000)
            self.assertEqual(select_result,1)

        except:
            print('fail')
            raise Exception

    def test_case2(self):
        '''不输入ID添加失败'''
        self.data = {}

        self.data['phone'] = 13558587795
        self.data['realname'] = '李某'

        print(self.data)
        r = requests.post(self.url, self.data)
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        # sql = 'select * from sign_guest where realname="李某";'
        # select_result = i.execute_sql(sql)
        try:

            self.assertEqual(self.res['message'], 'parameter error')
            self.assertEqual(self.res['status'], 10021)


        except:
            print('fail')
            raise Exception

    def test_case3(self):
        '''关联无效ID添加失败'''
        self.data = {}
        self.data['eid'] = 100
        self.data['phone'] = 13558587795
        self.data['realname'] = '李某'

        print(self.data)
        r = requests.post(self.url, self.data)
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        # sql = 'select * from sign_guest where realname="李某";'
        # select_result = i.execute_sql(sql)
        try:

            self.assertEqual(self.res['message'], 'event id null')
            self.assertEqual(self.res['status'], 10022)


        except:
            print('fail')
            raise Exception

    def test_case4(self):
        '''关联ID状态不可用添加失败'''
        self.data = {}
        self.data['eid'] = 1003
        self.data['phone'] = 13558587795
        self.data['realname'] = '张某'

        print(self.data)
        r = requests.post(self.url, self.data)
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        # sql = 'select * from sign_guest where realname="李某";'
        # select_result = i.execute_sql(sql)
        try:

            self.assertEqual(self.res['message'], 'event status is not available')
            self.assertEqual(self.res['status'], 10023)

        except:
            print('fail')
            raise Exception

    def test_case5(self):
        '''邀请人数已满，添加失败'''
        self.data = {}
        self.data['eid'] = 1001
        self.data['phone'] = 13558587795
        self.data['realname'] = '张某'

        print(self.data)
        r = requests.post(self.url, self.data)
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        # sql = 'select * from sign_guest where realname="李某";'
        # select_result = i.execute_sql(sql)
        try:

            self.assertEqual(self.res['message'], 'event number is full')
            self.assertEqual(self.res['status'], 10024)

        except:
            print('fail')
            raise Exception

    def test_case6(self):
        '''电话号码重复，添加失败'''
        self.data = {}
        self.data['eid'] = 1002
        self.data['phone'] = 18328155243
        self.data['realname'] = '张某'

        print(self.data)
        r = requests.post(self.url, self.data)
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        # sql = 'select * from sign_guest where realname="李某";'
        # select_result = i.execute_sql(sql)
        try:

            self.assertEqual(self.res['message'], 'the event guest phone number repeat')
            self.assertEqual(self.res['status'], 10026)

        except:
            print('fail')
            raise Exception

    def test_case7(self):
        '''发布会已经开始，添加失败'''
        self.data = {}
        self.data['eid'] = 1000
        self.data['phone'] = 18328155240
        self.data['realname'] = '1某'

        print(self.data)
        r = requests.post(self.url, self.data)
        self.res = r.json()
        print(self.res)
        self.con, self.cur = i.con_mysql()
        # sql = 'select * from sign_guest where realname="李某";'
        # select_result = i.execute_sql(sql)
        try:

            self.assertEqual(self.res['message'], 'event has started')
            self.assertEqual(self.res['status'], 10025)

        except:
            print('fail')
            raise Exception
if __name__ == '__main__':
    unittest.main()