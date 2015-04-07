try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='SimplePool',
      version='0.1',
      description='Threadpool library for humans.',
      long_description=open('README.rst').read(),
      url='http://github.com/srirams6/py-threadpool',
      author='Sriram Sundarraj',
      author_email='sriram.s.1994@gmail.com',
      license=open('LICENSE').read(),
      packages=['SimplePool'],
      classifiers=[
                  'Operating System :: POSIX',
                  'Topic :: Software Development :: Libraries :: Application Frameworks',
                  'Intended Audience :: Developers',
                  'Programming Language :: Python',
                  'Programming Language :: Python :: 2',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.2',
                  'Programming Language :: Python :: 3.3',
                  ],
      )
