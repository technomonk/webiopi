#!/bin/sh
cd python
python setup.py install
cd ..
rm -rf /usr/share/webiopi
mkdir /usr/share/webiopi
cp -v -r htdocs /usr/share/webiopi/htdocs
cp -v -r doc /usr/share/webiopi/doc