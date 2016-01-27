
from setuptools import setup

setup(
  name = 'DSDownload',
  version = '1.4.2.0',
  description = 'Easily download files in the fastest speed possible. Up to 452% faster than traditional download using Multi-Threaded Downloads',
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