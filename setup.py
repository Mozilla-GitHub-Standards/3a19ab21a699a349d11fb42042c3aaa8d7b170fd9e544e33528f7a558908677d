
from setuptools import setup, find_packages

setup(name='snippets-stats',
      version='0.0.1',
      description='Python script for parsing snippets-stats logs',
      python_requires='>=3.4',
      author='Chris Valaas',
      author_email='cvalaas@mozilla.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      scripts=['get_snippets_logs.py','snippets.py'],
      install_requires=[
        'geoip2',
        'pyodbc',
        'httpagentparser'
      ]
    )
