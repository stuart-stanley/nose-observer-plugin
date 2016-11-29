"""
todo: add
"""
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='stream monitors',
    version='0.1',
    author='Stuart Stanley',
    author_email = 'stuart.stanley@dell.com',
    description = 'Example nose plugin',
    license = 'Apache 2.0',
    py_modules = ['stream_monitor', 'infra_logging'],
    packages = ['stream_sources'],
    entry_points = {
        'nose.plugins.0.10': [
            'stream_monitor = stream_monitor:StreamMonitorPlugin'
            ]
        }
    )
