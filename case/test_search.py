"""
@author:maohui
@time:2022/7/25 14:38
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

from base import route
from base.basepage import BasePage
from page.home_page import HomePage

class TestSearch(minium.MiniTest):
    def test_01_search(self):
        """输入lungscr搜索"""
        self.app.wait_for_page(route.HomePage_addr)      #等待首页加载出来
        print(self.page.element_is_exists(('//*[@id="home"]/view/view[2]/image[2]')))
        es=self.page.get_elements(".van-field__control")
        # es[1].click()
        es[1].trigger("input", {"value": "lungscr"})
        self.page.wait_for(1)
        self.assertEqual(False, self.page.element_is_exists('//*[@id="home"]/view/view[2]/image[2]', max_timeout=2)) #本来可以定位到的元素定位不到了