import unittest,requests
from util.util import Get_Info,BASEURL,Con_Mysql
url = BASEURL+'add_guest/'   # 获取接口地址
class TestAddGuest(unittest.TestCase):
    '''测试添加嘉宾接口'''
    data = {}
    rep = ''
    cm ,con, cur = '','',''
    def setUp(self):
        self.cm = Con_Mysql()
        self.con, self.cur = self.cm.con_mysql()  # 连接数据库
        gf = Get_Info()
        self.data['eid'] = 1002
        self.data['realname'] = gf.get_name()  # 生成用户名
        self.data['phone'] = gf.get_phone_no()  # 生成手机号
        self.data['email'] = gf.get_email()  # 生成邮箱

    def tearDown(self):
        self.cm.close(self.con,self.cur)  # 关闭数据库连接

    def testcase1(self):
        '''传入有效参数（手机号13开头），添加嘉宾成功'''
        self.data['phone'] = self.data['phone'].replace(self.data['phone'][1],'3') # 将电话号码的第二位替换为3
        self.rep = requests.post(url=url, data=self.data)   # 对接口发起请求
        self.assertEqual(10000,self.rep.json()['status'])   # 断言
        self.assertEqual('add guest success',self.rep.json()['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s" and event_id="%d" and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['realname'],self.data['phone'],self.data['eid']))
        self.assertEqual(1,n)

    def testcase2(self):
        '''传入有效参数（手机号15开头），添加嘉宾成功'''
        self.data['phone'] = self.data['phone'].replace(self.data['phone'][1],'5') # 将电话号码的第二位替换为3
        self.rep = requests.post(url=url, data=self.data)
        self.assertEqual(10000,self.rep.json()['status'])
        self.assertEqual('add guest success',self.rep.json()['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s" and event_id="%d" and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['realname'],self.data['phone'],self.data['eid']))
        self.assertEqual(1,n)
    def testcase3(self):
        '''传入有效参数（手机号17开头），添加嘉宾成功'''
        self.data['phone'] = self.data['phone'].replace(self.data['phone'][1],'7') # 将电话号码的第二位替换为3
        self.rep = requests.post(url=url, data=self.data)
        self.assertEqual(10000,self.rep.json()['status'])
        self.assertEqual('add guest success',self.rep.json()['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s" and event_id="%d" and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['realname'],self.data['phone'],self.data['eid']))
        self.assertEqual(1,n)
    def testcase4(self):
        '''传入有效参数（手机号18开头），添加嘉宾成功'''
        self.data['phone'] = self.data['phone'].replace(self.data['phone'][1],'8') # 将电话号码的第二位替换为3
        self.rep = requests.post(url=url, data=self.data)
        self.assertEqual(10000,self.rep.json()['status'])
        self.assertEqual('add guest success',self.rep.json()['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s" and event_id="%d" and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['realname'],self.data['phone'],self.data['eid']))
        self.assertEqual(1,n)
    def testcase5(self):
        '''嘉宾姓名为空，添加嘉宾失败'''
        self.data.pop('realname')
        self.rep = requests.post(url=url, data=self.data)
        self.assertEqual(10021,self.rep.json()['status'])
        self.assertEqual('parameter error',self.rep.json()['message'])
        sql = 'select * from sign_guest where  phone="%s" and event_id="%d" and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['phone'],self.data['eid']))
        self.assertEqual(0,n)
    def testcase6(self):
        '''传入有效参数（手机号19开头），添加嘉宾成功'''
        self.data['phone'] = self.data['phone'].replace(self.data['phone'][1],'9') # 将电话号码的第二位替换为3
        self.rep = requests.post(url=url, data=self.data)
        self.assertEqual(10000,self.rep.json()['status'])
        self.assertEqual('add guest success',self.rep.json()['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s" and event_id="%d" and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['realname'],self.data['phone'],self.data['eid']))
        self.assertEqual(1,n)
    def testcase7(self):
        '''发布会状态为0，添加嘉宾失败'''
        self.data['eid'] = 1001
        self.rep = requests.post(url=url, data=self.data)
        self.assertEqual(10023,self.rep.json()['status'])
        self.assertEqual('event status is not available',self.rep.json()['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s" and event_id="%d" and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['realname'],self.data['phone'],self.data['eid']))
        self.assertEqual(0,n)
    def testcase8(self):
        '''发布会id为空，添加嘉宾失败'''
        self.data.pop('eid')
        self.rep = requests.post(url=url, data=self.data)
        self.assertEqual(10021,self.rep.json()['status'])
        self.assertEqual('parameter error',self.rep.json()['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.cm.execute_sql(self.cur,sql %(self.data['realname'],self.data['phone']))
        self.assertEqual(0,n)



if __name__ == '__main__':
 unittest.main()