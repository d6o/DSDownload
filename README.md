# mdownload
It is a small library to multi-threaded downloads. This means that it can generate a queue and download several files simultaneously

## Requirements

* [Python](https://www.python.org)

## Usage

```bash
mdownload.py [-h] [--threads THREADS] [--output OUTPUT] urls [urls ...]

It is a small library to multi-threaded downloads.This means that it can
generate a queue and download several files simultaneously

positional arguments:
  urls               URLs to be downloaded

optional arguments:
  -h, --help         show this help message and exit
  --threads THREADS  Number of parallel downloads. The default is 5.
  --output OUTPUT    Output folder
```

###Example 1
```bash
 python mdownload.py https://i.imgur.com/eUrbKtO.jpg
```
###Example 2
```bash
 python mdownload.py --threads 2 https://i.imgur.com/eUrbKtO.jpg https://i.imgur.com/9am20SK.jpg https://i.imgur.com/KR06C.jpg
```
###Example 3
```bash
 python mdownload.py --threads 2 --output myimages https://i.imgur.com/eUrbKtO.jpg https://i.imgur.com/9am20SK.jpg https://i.imgur.com/KR06C.jpg
```

## Find a bug/issue or simply want to request a new feature?

[Create a Github issue/feature request!](https://github.com/DiSiqueira/mdownload/issues/new)