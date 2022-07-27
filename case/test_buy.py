"""
@author:maohui
@time:2022/7/26 8:55
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



from base import route
from base.basecase import BaseCase
from base.basepage import BasePage


from page.home_page import HomePage
from page.productdetails_page import ProductDetailsPage
from page.shopcar_page import ShopCarPage
class TestBuyColon(BaseCase):

    def test_01_buynow_colonscr(self):
        """直接购买colonscr居家采样流程"""

        HomePage(self.page).click_colon()
        ProductDetailsPage(self.page).click_buynow()
        BasePage(self.page).click('.van-stepper__plus')
        ProductDetailsPage(self.page).click_confirm()
        # self.page.get_element('.van-button__text',inner_text='提交订单').click()

    def test_02_buynow_lungscr_home(self):
        """直接购买lungscr居家采样"""

        HomePage(self.page).click_lungscr()
        ProductDetailsPage(self.page).click_buynow()
        ProductDetailsPage(self.page).click_add_count()
        ProductDetailsPage(self.page).click_confirm()
        # LungScrPage(self.page).click_select_addr()
        # self.native.handle_modal("确定")  # 点击弹窗的"确定"按钮
        # self.page.get_element('.van-button__text', inner_text='提交订单').click()

    def test_03_buynow_lungscr_hospital(self):
        """直接购买lugnscr采血点采样"""

        HomePage(self.page).click_lungscr()
        ProductDetailsPage(self.page).click_buynow()
        self.page.get_element('.van-radio__label', inner_text="采血点采样").click()
        ProductDetailsPage(self.page).click_add_count()
        ProductDetailsPage(self.page).click_confirm()
        # self.native.handle_modal("确定")  # 点击弹窗的"确定"按钮
        # self.page.get_element('.van-button__text', inner_text='提交订单').click()

    def test_04_buycar_colonscr(self):
        """colonscr添加到购物车后购买"""

        HomePage(self.page).click_colon()
        ProductDetailsPage(self.page).click_add_to_car()
        ProductDetailsPage(self.page).click_add_count()
        ProductDetailsPage(self.page).click_confirm()
        ProductDetailsPage(self.page).click_shopcar()
        ShopCarPage(self.page).click_first_sigle_select()
        ShopCarPage(self.page).click_account()
        # self.page.get_element('.van-button__text',inner_text='提交订单').click()

    def test_05_buycar_lungscr_home(self):
        """lungscr居家采样添加到购物车后购买"""
        HomePage(self.page).click_lungscr()
        ProductDetailsPage(self.page).click_add_to_car()
        ProductDetailsPage(self.page).click_add_count()
        ProductDetailsPage(self.page).click_confirm()
        ProductDetailsPage(self.page).click_shopcar()
        ShopCarPage(self.page).click_first_sigle_select()
        ShopCarPage(self.page).click_account()
        # LungScrPage(self.page).click_select_addr()
        # self.native.handle_modal("确定")  # 点击弹窗的"确定"按钮
        # self.page.get_element('.van-button__text', inner_text='提交订单').click()

    def test_06_buycar_lungscr_hospital(self):
        """lungscr采血点采样添加到购物车后购买"""
        HomePage(self.page).click_lungscr()
        ProductDetailsPage(self.page).click_add_to_car()
        self.page.get_element('.van-radio__label', inner_text="采血点采样").click()
        ProductDetailsPage(self.page).click_add_count()
        ProductDetailsPage(self.page).click_confirm()
        ProductDetailsPage(self.page).click_shopcar()
        ShopCarPage(self.page).click_first_sigle_select()
        ShopCarPage(self.page).click_account()
        # LungScrPage(self.page).click_select_addr()
        # self.native.handle_modal("确定")  # 点击弹窗的"确定"按钮
        # self.page.get_element('.van-button__text', inner_text='提交订单').click()
