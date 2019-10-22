import requests
url = 'http://127.0.0.1:8000/api/get_event_list/'
data = {'eid':1001}
r = requests.get(url,data)
print(r.text)
res = r.json()
print(res)
print(r.status_code)
if res['status'] == 10000:
    print('pass')
else:
    print('fail')


url = 'http://127.0.0.1:8000/api/add_event/'
data = {'eid':1004 , 'name':'红魔' , 'status':1 , 'limit':100 , 'address':'成都东站' , 'start_time':'2019-12-12 12:00:00'}
r = requests.post(url,data)
res = r.json()
print(res)
if res['message'] == 'add event success' and res['status'] == 10000:
    print('pass')
else:
    print('fail')

