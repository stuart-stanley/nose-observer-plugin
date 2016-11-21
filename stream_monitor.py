import logging
import os
from nose.plugins import Plugin
import sys

class StreamMonitorPlugin(Plugin):
    name = "stream-monitor"

    def options(self, parser, env=os.environ):
        print >>sys.stderr, "options"
        self.__log = logging.getLogger('nose.plugins.streammonitor')
        super(StreamMonitorPlugin, self).options(parser, env=env)

    def configure(self, options, conf):
        print >>sys.stderr, "configure"
        super(StreamMonitorPlugin, self).configure(options,conf)
        if not self.enabled:
            return

    def finalize(self, result):
        print >>sys.stderr, "finalize"
        self.__log.info('Stream Monitor Active')

    def begin(self):
        print >>sys.stderr, "begin"

    def beforeTest(self, test):
        print >>sys.stderr, "beforeTest", test

    def startTest(self, test):
        print >>sys.stderr, "startTest", test

    def stopTest(self, test):
        print >>sys.stderr, "stopTest", test

        
