# sds011

This repository contain a basic http server used to feed the output of an [sds011 sensor](https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf) into a telegraf measure.

## Usage

```
$ git clone https://github.com/OneBlue/sds011
$ pip3 install .
$ sds011 127.0.0.1 80 /dev/ttyUSB0
```
