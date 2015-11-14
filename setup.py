try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='SimplePool',
      version='0.1',
      description='Threadpool library for humans.',
      long_description=open('README.rst').read(),
      url='http://github.com/ssundarraj/py-threadpool',
      author='Sriram Sundarraj',
      author_email='ssundarraj@gmail.com',
      license='GPL v3',
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
                  'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                  ],
      )
