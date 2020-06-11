import requests

# # 获取验证码：
# response_code = requests.get(url="http://localhost/index.php/Home/User/verify/type/user_reg.html")
# # 提取cookie并打印：
# cookie = response_code.cookies
# print("获取的cookie是：", cookie)
# # 使用cookie进行注册：
# response_login = requests.post(url="http://localhost/index.php/Home/User/reg.html", data={
#     "username": "18994130602", "verify_code":"8888","password": "123456","password2": "123456"},
#                                cookies=cookie,headers={"Content-Type": "application/x-www-form-urlencoded"})
# #打印注册结果：
# print("输出注册结果：", response_login.json())
# 3.请使用requests模块编写代码访问员工管理模块用户资料查询接口，并输出该接口返回响应数据中的
# url，encoding，cookies，headers，以及响应数据
# 建议使用requests来实现