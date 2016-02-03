
from setuptools import setup

setup(
  name = 'DSDownload',
  version = '1.6.0.1',
  description = 'Program and module for download queue optimization using multi-thread.',
  url = 'https://github.com/DiSiqueira/DSDownload',
  author = 'Diego Siqueira',
  author_email = 'dieg0@live.com',
  license = 'MIT',
  package_dir = { 'DSDownload' : 'src' },
  packages = [ 'DSDownload' ],
  zip_safe = False, 
  keywords = ['download', 'thread', 'speed', 'resume', 'multi', 'simple'],
  entry_points = 
  {
      'console_scripts': 
      [
          'dsdownload = DSDownload:main',
      ],
  },
)