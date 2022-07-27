"""
@author:maohui
@time:2022/7/26 9:02
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

class ProductDetailsPage(BasePage):
    select_loc='//*[@id="productDetails"]/view[1]/van-cell[1]/view/view'
    view_loc='//*[@id="productDetails"]/view[1]/van-cell[2]/view/view'
    kefu_loc='//*[@id="productDetails"]/view[2]/view[1]/view[1]/button'
    shopcar_loc='//*[@id="productDetails"]/view[2]/view[1]/view[2]/button'
    add_shopcar_loc = '//*[@id="productDetails"]/view[2]/view[2]/van-button[1]//button'
    buynow_loc='//*[@id="productDetails"]/view[2]/view[2]/van-button[2]//button'



    add_count_loc=".van-stepper__plus"
    confirm_loc='.van-button--block'

    #点击进入购物车
    def click_shopcar(self):
        self.click(self.shopcar_loc)

    #点击添加购物车
    def click_add_to_car(self):
        self.click(self.add_shopcar_loc)

    #点击立即购买
    def click_buynow(self):
        self.click(self.buynow_loc)

    #数量加
    def click_add_count(self):
        self.click(self.add_count_loc)

    #点击确定
    def click_confirm(self):
        self.click(self.confirm_loc)