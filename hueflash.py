#!/usr/bin/python
from time import sleep
from phue import Bridge

b = Bridge('192.168.1.26')

hue = b.get_light(2,'hue')
bri = b.get_light(2,'bri')
pwr = b.get_light(2,'on')

# b.set_light(2,'on',True)
if pwr == 'False':
	b.set_light(2,'on',True)

for x in range(0, 2):
	b.set_light(2,'hue',0)
	sleep(0.4)
	b.set_light(2,'hue',hue)
	sleep(0.4)

b.set_light(2,'on',pwr)

#b.set_light(2,'bri',bri)
#b.set_light(2,'hue',hue)
