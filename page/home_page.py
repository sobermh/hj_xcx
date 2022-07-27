"""
@author:maohui
@time:2022/6/28 8:58
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
import minium

from base.basepage import BasePage
class HomePage(BasePage):
    search_btn_loc='.van-icon-search'
    colon_loc='/*[@id="home"]/view/view[2]/image[1]'
    lungscr_loc='/*[@id="home"]/view/view[2]/image[2]'
    index_loc='.van-icon-wap-home-o'
    shopcart_loc='.van-icon-qr'
    my_loc='.van-icon-user-circle-o'

    #搜索框输入
    def input_search(self,loc,value):
        self.input(loc,value)

    #点击colon
    def click_colon(self):
        self.click(self.colon_loc)

    #点击lungscr
    def click_lungscr(self):
        self.click(self.lungscr_loc)

    #点击wode
    def click_my(self):
        self.click(self.my_loc)



