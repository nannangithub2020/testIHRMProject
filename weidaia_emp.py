import requests
#发送登录的接口请求
response = requests.post(url="http://ihrm-test.itheima.net"+"/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
#打印登录的结果
print("登录的结果为：",response.json())
#提取登录返回的令牌
token = ('登录的结果为：',response.json())
#发送添加员工的接口
token='Bearer '+response.json().get("data")
print("提取的令牌为：",token)
#打印添加员工的接口

headers = {"Content-Type":"application/json","Authorization":token}
response =requests.post(url="http://ihrm-test.itheima.net"+"/api/sys/user",
                        json={
                            "username":"他爷爷9999tututu",
                            "mobile":"17834420909",
                            "timeOfEntry":"2020-05-05",
                            "formOfEmployment":1,
                            "departmentName":"测试部",
                            "departmentId":"1063678149528784896",
                            "correctionTime":"2020-05-30T16:00:00.000Z"
                        },headers=headers)
print("添加员工的接口返回数据为：" , response.json())
#提取添加员工接口返回的员工id
emp_id = response.json().get('data').get('id')
print("提取的员工id为：" ,emp_id)

#拼接查询员工的接口的url
query_url = "http://ihrm-test.itheima.net"+"/api/sys/user" + "/" + emp_id
print("拼接查询员工的接口的url为：",query_url)
#发送查询员工的接口的请求
response=requests.get(url=query_url,headers=headers)
print("打印查询员工的结果为：",response.json())
#拼接修改员工的url
modify_url = "http://ihrm-test.itheima.net"+"/api/sys/user" + "/" + emp_id
response =requests.put(url=modify_url,json={"username":"爱因斯坦"},headers=headers)
print("修改员工的结果为：",response.json())

#拼接删除员工的url
delete_url = "http://ihrm-test.itheima.net"+"/api/sys/user" + "/" + emp_id
response=requests.delete(url=delete_url,headers=headers)
print("删除员工的结果为：",response.json())