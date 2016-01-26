
from config import version, description, name
from distutils.core import setup

setup(
  name = name,
  packages = [name], 
  version = version,
  description = description,
  author = 'Diego Siqueira',
  author_email = 'dieg0@live.com',
  url = 'https://github.com/DiSiqueira/DSDownload', 
  download_url = 'https://github.com/DiSiqueira/DSDownload/tarball/'+version, 
  keywords = ['download', 'thread', 'speed', 'resume', 'multi', 'simple'],
  classifiers = [],
  license='MIT',
  entry_points = {
          'console_scripts': [
              'dsdownload = DSDownload.DSDownload:main',                  
          ],              
      },
)