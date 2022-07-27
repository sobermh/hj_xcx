"""
@author:maohui
@time:2022/6/27 15:17
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
import os
import re
import time
import minium


class BasePage:
    """BasePage是页面基类，封装所有页面会用到的公用方法"""

    def __init__(self, page):
        self.page=page

    def wait(self, loc):
        self.page.wait_for(loc)

    # 元素定位返回为唯一的元素
    def locator(self, loc,inner_text=None):
        self.wait(loc)  # 等到元素的出现
        # self.page.wait_for(2)  # 当前页面等待2s
        return self.page.get_element(loc,inner_text=inner_text)

    #返回指定的第几个元素
    def locator_appoint_ele(self,loc,n):
        ele=self.page.get_elements(loc)
        return ele[n]

    #输入
    def input(self, loc,value, inner_text=None,index=None):
        self.wait(loc)
        try:
            self.locator(loc,inner_text=inner_text).trigger("input", {"value": value})
        except:
            self.locator_appoint_ele(loc,index).trigger("input", {"value": value})
    # 点击
    def click(self,loc, inner_text=None,index=None):
        self.wait(loc)
        try:
            self.locator(loc, inner_text=inner_text).click()
        except:
            self.locator_appoint_ele(loc, index).click()
    # 元素包含的文本
    def ele_text(self, loc):
        self.wait(loc)
        return self.locator(loc).inner_text

    # 元素的值
    def ele_value(self, loc):
        self.wait(loc)
        return self.locator(loc).value
