"""Installation setup of the frbcat python package."""
import os
from setuptools import setup

with open(os.path.join('frbcat', '__version__.py')) as f:
    version = {}
    exec(f.read(), version)
    project_version = version['__version__']


setup(name='frbcat',
      version=project_version,
      description='Query the FRB catalogue',
      url='http://github.com/davidgardenier/frbcat',
      author='David Gardenier',
      author_email='davidgardenier@gmail.com',
      license='MIT',
      packages=['frbcat'],
      install_requires=['pandas', 'requests', 'numpy'],
      zip_safe=False)
