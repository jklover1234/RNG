import unittest
import time
from HTMLTestReportCN import HTMLTestRunner


def get_time():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
distime = get_time()
tests = unittest.defaultTestLoader.discover('')
f = open(distime + '.html', 'wb')
runner = HTMLTestRunner(stream=f, title='接口自动化报告', tester='蔡某人')
runner.run(tests)
f.close()