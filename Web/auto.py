#coding= utf-8
from widget import Widget
import unittest
# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40), "size equal")
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))
    def tearDown(self):
        self.widget = None
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    return suite
if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')