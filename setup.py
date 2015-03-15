try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

setup(name='pyThreadPool',
      version='0.1',
      description='Threadpool library for humans.',
      url='http://github.com/srirams6/py-threadpool',
      author='Sriram Sundarraj',
      author_email='sriram.s.1994@gmail.com',
      license='MIT',
      packages=['py_threadpool'],)