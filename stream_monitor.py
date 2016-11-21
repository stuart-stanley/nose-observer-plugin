import logging
import os
from nose.plugins import Plugin
import sys

class StreamMonitorPlugin(Plugin):
    name = "stream-monitor"
    def __init__(self, *args, **kwargs):
        self.__save_call_sequence = None
        self.__print_to = None
        # Uncomment next line to view steps to console live
        # self.__print_to = sys.stderr   
        super(StreamMonitorPlugin, self).__init__(*args, **kwargs)

    def _self_test_print_step_enable(self):
        self.__save_call_sequence = []

    def _self_test_sequence_seen(self):
        rl = self.__save_call_sequence
        self.__save_call_sequence = []
        return rl

    def __take_step(self, name, **kwargs):
        if self.__save_call_sequence is not None:
            self.__save_call_sequence.append((name, kwargs))

        if self.__print_to is not None:
            print >>self.__print_to, 'ESTEP: {0} {1}'.format(name, kwargs)

    def options(self, parser, env=os.environ):
        self.__take_step('options', parser=parser, env=env)
        self.__log = logging.getLogger('nose.plugins.streammonitor')
        super(StreamMonitorPlugin, self).options(parser, env=env)

    def configure(self, options, conf):
        self.__take_step('configure', options=options, conf=conf)
        super(StreamMonitorPlugin, self).configure(options,conf)
        if not self.enabled:
            return

    def finalize(self, result):
        self.__take_step('finalize', result=result)
        self.__log.info('Stream Monitor Active')

    def begin(self):
        self.__take_step('begin')

    def beforeTest(self, test):
        self.__take_step('beforeTest', test=test)

    def afterTest(self, test):
        self.__take_step('afterTest', test=test)

    def startTest(self, test):
        self.__take_step('startTest', test=test)

    def stopTest(self, test):
        self.__take_step('stopTest', test=test)

        
