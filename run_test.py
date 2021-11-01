import unittest
import os
from common.handlepath import CASEDIR, REPORTDIR
from HTMLTestRunnerNew import HTMLTestRunner
# from BeautifulReport import BeautifulReport

import datetime


date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


# 第一步：创建套件
suite = unittest.TestSuite()

# 第二步：加载用例到套件
loader = unittest.TestLoader()

suite.addTest(loader.discover(CASEDIR))

# 第三步：执行用例
report_file = os.path.join(REPORTDIR, date+"report1.html")

runner = HTMLTestRunner(stream=open(report_file, "wb"),
                        description="收银测试报告最终版",
                        title="收银V5.1.1测试报告",
                        tester="fufu"
                        )

runner.run(suite)

# br = BeautifulReport(suite)
#
# br.report("前程贷项目用例",filename=date+"report1.html",report_dir=REPORTDIR)

# send_email(report_file,"py26测试报告最终版")


