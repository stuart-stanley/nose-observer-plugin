import unittest
from infra_logging import *

class TestTwoLoggerTest(unittest.TestCase):
    def setUp(self):
        self.__lg = getTestRunLogger()
        super(TestOneLoggerTest, self).setUp()

    def test_one_of_two_to_run(self):
        self.__lg.warning('test_one_of_two_to_run')

    def test_two_of_two_to_run(self):
        self.__lg.warning('test_two_of_two_to_run')
