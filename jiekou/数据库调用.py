import pymysql  # 引入pymysql模块


def mc(db):
    try:
        cn = pymysql.connect('localhost', 'root', 'root', db, charset='utf8')  # 创建连接对象
        cur = cn.cursor()  # 连接对象创建游标对象具体操作数据库
        # execute():执行单条sql语句
        a = cur.execute('select count(*) from sign_event WHERE id=1004')
        cur.close()  # 关闭游标对象
        cn.commit()  # 连接对象提交事务
    except Exception:
        print('连接失败，请检查数据库是否开启及连接参数')
    else:
        print('连接成功')
    if a == 1:
        print('成功')
        cn.close()
mc('learn')


