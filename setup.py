from setuptools import setup

exec(open("./_version.py").read())

setup(name="log-parser-rpt",
      version=__version__,
      author="Manoj Thakkar",
      author_email="writetomanoj@gmail.com",
      packages=['log-parser-rpt'],
      install_requires = [
        'user-agents',
        'pandas',
      ],
      description = "Parse lines and results of a log file",
      test_suite='sample-parser.tests',
      classifiers=[
        'Development Status :: 1 - Testing/Alpha',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ],
)
