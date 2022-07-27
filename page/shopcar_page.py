"""
@author:maohui
@time:2022/7/27 10:09
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

from base.basepage import BasePage

class ShopCarPage(BasePage):
    first_sigle_select_loc='//*[@id="shoppingCart"]/view/view[1]/view/view[1]'
    all_select_loc='//*[@id="shoppingCart"]/view/view[2]/van-checkbox'
    delect_loc='.van-button--plain'
    account_loc='.van-button--round'

    #点击第一个单元框
    def click_first_sigle_select(self):
        self.click(self.first_sigle_select_loc)

    #点击全选


    #点击删除按钮
    def click_delete(self):
        self.click(self.delect_loc)

    #点击结算
    def click_account(self):
        self.page.get_element(self.account_loc, inner_text="结算").click()