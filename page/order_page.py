"""
@author:maohui
@time:2022/7/27 11:47
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
# import minium  #调试

import time

from base.basepage import BasePage

class OrderPage(BasePage):

    order_list_loc='.van-ellipsis'



    add_order_loc='.van-button--normal'
    select_pro_loc='.van-field__label'
    select_prolist_loc='.list'
    input_phone_loc='.van-field__control'    #4
    input_name_loc='.van-field__control'     #6
    order_org_loc='.van-field__control'      #8
    order_orglist_loc='.address'
    order_time_loc='.van-field__control'    #10
    order_timelist_loc='.van-ellipsis'
    confirm_loc='.van-button--block'
    #点击已预约
    def click_pre_order(self):
        self.click(self.order_list_loc,inner_text='已预约')

    #点击已到场

    def click_pre_arrive(self):
        self.click(self.order_list_loc,inner_text="已到场")

    #点击已取消
    def click_pre_cancel(self):
        self.click(self.order_list_loc, inner_text="已取消")

    #点击新增预约
    def click_add_order(self):
        self.click(self.add_order_loc)

    #点击选择项目
    def click_select_pro(self):
        self.click(self.select_pro_loc,inner_text='选择项目')

    #点击ColonScr项目
    def click_colonscr(self):
        self.click(self.select_prolist_loc,inner_text='汇健科技 爱可现-ColonScr 肠癌早期检测 血清肽谱检测 中老年')

    #点击LungScr项目
    def click_lungscr(self):
        self.click(self.select_prolist_loc, inner_text='汇健科技 常津采-LungScr 肺癌早期检测 唾液代谢谱检测')

    #输入患者手机号
    def input_phone(self):
        # ele=self.page.get_elements(self.input_phone_loc)
        # ele[3].trigger("input", {"value": 19357665827})
        self.input(self.input_phone_loc,index=4,value=19357665827)

    #输入患者姓名
    def input_name(self):
        self.input(self.input_name_loc,index=6,value='sober万森')

    #点击预约机构
    def click_order_org(self):
        self.click(self.order_org_loc,index=8)

    #选择浙江大学校医院
    def click_zjcollege(self):
        self.click(self.order_orglist_loc)

    #点击预约时间
    def select_order_time(self):
        day=time.localtime().tm_mday+1
        self.click(self.order_time_loc,index=10)
        self.click(self.order_timelist_loc,inner_text=str(day)+'日')

    #点击确认
    def click_confirm(self):
        self.click(self.confirm_loc)

