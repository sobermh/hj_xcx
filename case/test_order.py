"""
@author:maohui
@time:2022/7/27 11:36
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

from base.basecase import BaseCase
from base.basepage import BasePage

from page.home_page import HomePage
from page.my_page import MyPage
from page.order_page import OrderPage
class TestOrder(BaseCase):

    def test_01_add_order(self):
        """colonscr正常预约"""
        HomePage(self.page).click_my()
        MyPage(self.page).click_order()
        OrderPage(self.page).click_add_order()
        OrderPage(self.page).click_select_pro()
        OrderPage(self.page).click_colonscr()
        OrderPage(self.page).input_phone()
        OrderPage(self.page).input_name()
        OrderPage(self.page).click_order_org()
        OrderPage(self.page).click_zjcollege()
        OrderPage(self.page).select_order_time()
        OrderPage(self.page).click_confirm()
    def test_02_pre_arrive(self):
        """点击已到场"""
        HomePage(self.page).click_my()
        MyPage(self.page).click_order()
        OrderPage(self.page).click_pre_arrive()

    def test_03_pre_cancel(self):
        """点击已取消"""
        HomePage(self.page).click_my()
        MyPage(self.page).click_order()
        OrderPage(self.page).click_pre_cancel()





