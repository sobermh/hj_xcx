"""
@author:maohui
@time:2022/7/26 10:47
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
from pathlib import Path

import minium

from base import route


class BaseCase(minium.MiniTest):
    """BaseCase是测试用例基类，用于设置用例输出路径和清理工作，项目的测试用例都继承此类"""

    @classmethod
    def setUpClass(cls):
        super(BaseCase, cls).setUpClass()
        output_dir = Path(cls.CONFIG.outputs)
        if not output_dir.is_dir():
            output_dir.mkdir()

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()

    def setUp(self):
        super(BaseCase, self).setUp()     #回到首页，不需要可以pass
        self.page.wait_for(5)
        # self.app.wait_for_page(route.HomePage_addr)  # 等待首页加载出来

    def tearDown(self):
        super(BaseCase, self).tearDown()
