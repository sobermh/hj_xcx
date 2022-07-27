"""
@author:maohui
@time:2022/6/27 15:53
  　　　　　　　 ┏┓    ┏┓+ +
  　　　　　　　┏┛┻━━━━┛┻┓ + +
  　　　　　　　┃        ┃ 　 
  　　　　　　　┃     ━  ┃ ++ + + +
  　　　　　 　████━████ ┃+
  　　　　　　　┃        ┃ +
  　　　　　　　┃   ┻    ┃
  　　　　　　　┃        ┃ + +
  　　　　　　　┗━┓   ┏━━┛
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃ + + + +
  　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
  　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃　　+
  　　　　　　　  ┃   ┗━━━━━━━┓ + +     
  　　　　　　　  ┃           ┣┓
  　　　　　　　  ┃           ┏┛
  　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
  　　　　　　　   ┃┫┫     ┃┫┫
  　　　　　　　   ┗┻┛     ┗┻┛+ + + +
"""

# import minium

# #!/usr/bin/env python3
# import minium
# class FirstTest(minium.MiniTest):
#     def test_get_system_info(self):
#         sys_info = self.mini.get_system_info()
#         self.logger.info(f'SDKVersion is: {sys_info.get("SDKVersion")}')
#         self.assertIn("SDKVersion", sys_info)
#
# if __name__ == "__main__":
#     import unittest
#     loaded_suite = unittest.TestLoader().loadTestsFromTestCase(FirstTest)
#     result = unittest.TextTestRunner().run(loaded_suite)
#     print(result)
import minium
from base.basepage import BasePage
from page.my_page import MyClass

# mini = minium.Minium({
#      "dev_tool_path": "E:\\微信web开发者工具\\cli.bat",
#   "project_path": "C:\\Users\\PC\\Desktop\\mp-weixin",
# })
# print(mini.get_system_info())
class TestLogin(minium.MiniTest):

    def test_01(self):
        """正确授权登录"""
        # # 弹出的授权看框没法点
        # self.page.wait_for(2)
        # self.page.get_element('.van-icon-user-circle-o').click()  # 点击我的
        # MyClass(self.page).click_login_out()
        # BasePage(self.page).click('.authBtn')
        # self.page.get_element('.authBtn',max_timeout=2).click()  # 点击授权登录
        # self.page.wait_for(3)  # 当前页面等待3s
        # # self.assertEqual('/pages/main/index', self.mini.app.current_page.path, msg='登录失败')
        # # 断言登录后是否跳转到首页，如果断言失败，则返回mgs"登录失败"
        # self.native.allow_authorize(answer=True)
        pass