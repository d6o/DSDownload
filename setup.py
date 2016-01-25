from distutils.core import setup
setup(
  name = 'mdownload',
  packages = ['mdownload'], # this must be the same as the name above
  version = '0.2',
  description = 'It is a small library to multi-threaded downloads.',
  author = 'Diego Siqueira',
  author_email = 'dieg0@live.com',
  url = 'https://github.com/DiSiqueira/mdownload', # use the URL to the github repo
  download_url = 'https://github.com/DiSiqueira/mdownload/tarball/0.2', # I'll explain this in a second
  keywords = ['download', 'thread', 'speed', 'resume', 'multi', 'simple'], # arbitrary keywords
  classifiers = [],
  scripts=["mdownload/mdownload.py"],
)