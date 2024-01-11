from setuptools import setup, find_packages

setup(name='cot',
      version='0.2',
      description='cot',
      packages=['cot', 'cot.core', 'cot.prompt'],
      install_requires=['openai', 'python-dateutil'],
      )
