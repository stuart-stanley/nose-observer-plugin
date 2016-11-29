import unittest
from infra_logging import *

class TestOneLoggerTest(unittest.TestCase):
    def setUp(self):
        self.__lg = getTestRunLogger()
        super(TestOneLoggerTest, self).setUp()

    def test_single_log_to_run(self):
        self.__lg.warning('test_single_log_to_run')
