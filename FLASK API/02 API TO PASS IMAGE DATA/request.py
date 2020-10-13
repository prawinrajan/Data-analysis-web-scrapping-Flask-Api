import requests
r=requests.post("http://127.0.0.1:5000/image",data={'HomeId':1,'image':open('/home/prawin/test.jpg','rb')})
print(r.status_code, r.reason)


'''
requests.post(url, files=files)
print(r.status_code, r.reason)

import requests
r = requests.post("http://127.0.0.1:5000/sensor_data",data={"HomeId":1,"time":13,"temperature":38,"Humidity":13,"ultrasonic_motion_sensor":1,"IR":1})

print(r.status_code, r.reason)'''
