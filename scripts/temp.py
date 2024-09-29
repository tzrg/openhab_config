#!/usr/bin/env python2.7
import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 2

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:

    print('{0:0.1f}'.format(temperature))

else:

    print('Failed to get reading. Try again!')

sys.exit(1)
