import requests
# # 1.请使用python的requests模块编写对百度进行搜索的代码，搜索关键字：接口测试
# # 使用requests模块发送get请求，访问百度首页，并获取返回的响应数据
# response=requests.get(url="http://www.baidu.com/S",params={"wd":"接口测试"})
# # 打印返回的结果
# print("返回的结果为：",response.text)


# url= "http://ihrm-test.itheima.net/api/sys/login"
# data = {"mobile":"13800000002","password":"123456"}
# response=requests.post(url=url,json=data)
# print(response.json())

# import  unittest,requests
# #创建测试类
# class UnittestTestIHRM(unittest.TestCase):
#     #初始化unittest
#     def setUp(self):
#         self.login_url ="http://ihrm-test.itheima.net/api/sys/login"
#     def tearDown(self):
#         pass
#     #编写测试函数
#     def test_01_login(self):
#         data = {"mobile":"13800000002","password":"123456"}
#         response = requests.post(url=self.login_url, json=data)
#         print(response.json())
#         #断言
#         self.assertIn("操作成功",response.json().get("message"))

# 2.请使用python的requests模块编写代码来访问tpshop商城的注册接口，并注册成功获取到注册结
# 果。
# 建议：使用session来实现。
# 前置条件：tpshop商城没有开启手机验证码，图片验证码已经mock成万能验证码
# 实现流程：先调用【注册的获取验证码接口】->然后调用【注册接口】
# 注意：代码操作需要保存cookie，或者使用session自动管理功能保存cookie
#导包

