#! /bin/sh

python mqtt_pub.py -m 5 -l 10 -r 500
python mqtt_pub.py -m 10 -l 10 -r 500
python mqtt_pub.py -m 15 -l 10 -r 500
python mqtt_pub.py -m 20 -l 10 -r 500

exit