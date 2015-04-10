#!/usr/bin/python
from phue import Bridge
from time import sleep

b = Bridge('192.168.1.26')

##Bulbs
# 1 Bedroom Dome 1 (Hue)
# 2 Bedroom Lamp  (Hue)
# 3 Bedroom Dome 2 (Hue)
# 4 
# 5 Closet 2 (Lux)
# 6 Closet 1 (Lux)
# 7 Bathroom 1 (Lux)
# 8 Bathroom 3 (Lux)
# 9 Bathroom 2 (Lux)
# 10 Bathroom Dome (Hue)
# 12 Couch (Hue)

##Groups
# 1 Bedroom Dome
# 2 Bathroom Mirror
# 3 Closet
# 4 Hues


Bulbs = [1,2,3,10,12]
#for x in Bulbs:
#	print x

#Set Target Bulbs and Groups

hue = [];
bri = [];
pwr = [];

for i in Bulbs:
	hue.append(b.get_light(i,'hue'))
	bri.append(b.get_light(i,'bri'))
	pwr.append(b.get_light(i,'on'))
	b.set_light(i,'on',True)


b.set_group(i,'bri',150)
ghue = b.get_group(4,'hue')
for x in range(0, 2):
	b.set_group(4,'hue',0)
        sleep(0.4)
	b.set_light(4,'hue',ghue)
	sleep(0.4)


index = 0
for i in Bulbs:
	b.set_light(i,'hue',hue[index])
        b.set_light(i,'bri',bri[index])
        b.set_light(i,'on',pwr[index])
	index = index+1
