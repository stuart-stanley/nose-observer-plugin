import unittest, os
from nose.plugins import PluginTester
from stream_monitor import StreamMonitorPlugin

class TestStreamMonitorPlugin(PluginTester, unittest.TestCase):
    activate = '--with-stream-monitor'
    plugins = [StreamMonitorPlugin()]
    def test_foo(self):
        for line in self.output:
            pass

        assert "ValueError" in self.output

    def test_boo(self):
        pass

    def makeSuite(self):
        class TC(unittest.TestCase):
            def runTest(self):
                raise ValueError("I hate foo")
        return [TC('runTest')]


if __name__ == '__main__':
    res = unittest.TestResult()
    case = TestStreamMonitorPlugin('test_foo')
    _ = case(res)
    print res.errors
    res.failures
    res.wasSuccessful()
    res.testsRun
