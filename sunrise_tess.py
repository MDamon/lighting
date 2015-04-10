#!/usr/bin/python
from phue import Bridge
from time import sleep

b = Bridge('192.168.1.26')

##Bulbs
# 1 Bedroom Dome 1
# 2 Bedroom Lamp
# 3 Bedroom Dome 2
# 4 
# 5 Closet 2
# 6 Closet 1
# 7 Bathroom 1
# 8 Bathroom 3
# 9 Bathroom 2
# 10 Bathroom Dome
# 12 Couch

##Groups
# 1 Bedroom Dome
# 2 Bathroom Mirror
# 3 Closet

#Set Target Bulbs and Groups
b1 = 2
b2 = 10
b3 = 12
g1 = 2
g2 = 3

#Get Current Status of Bulbs and Groups
h1 = b.get_light(b1,'hue')
h2 = b.get_light(b2,'hue')
h3 = b.get_light(b3,'hue')

br1 = b.get_light(b1,'bri')
br2 = b.get_light(b2,'bri')
br3 = b.get_light(b3,'bri')
brg1 = b.get_group(g1,'bri')
brg2 = b.get_group(g2,'bri')

p1 = b.get_light(b1,'on')
p2 = b.get_light(b2,'on')
p3 = b.get_light(b3,'on')
pg1 = b.get_group(g1,'on') 
pg2 = b.get_group(g2,'on')

#Turn Bulbs on and Quickly Set Brightness to 0
b.set_light(b1,'on',True)
b.set_light(b1,'bri',0)

b.set_light(b2,'on',True)
b.set_light(b2,'bri',0)

b.set_light(b3,'on',True)
b.set_light(b3,'bri',0)

#Set Colors to Warm and Start 7 Minute Sunrise
newbri = 0
b.set_light(b1,'hue',13088)
b.set_light(b2,'hue',13088)
b.set_light(b3,'hue',13088)

while (newbri <= 150):
	b.set_light(b2,'bri',newbri,transitiontime=300)
	b.set_light(b3,'bri',newbri,transitiontime=300)
        if newbri <=100:
                b.set_light(b1,'bri',newbri,transitiontime=300)
		b.set_light(b3,'bri',newbri,transitiontime=300)
	newbri = newbri + 10
	sleep(30)

print 'Colored Lights Done'

#Turn on Lux Groups
b.set_group(g1,'on',True)
b.set_group(g1,'bri',0)

b.set_group(g2,'on',True)
b.set_group(g2,'bri',0)

#Start Brightness on Lux
newbri = 0
while (newbri <= 150):
        b.set_group(g1,'bri',newbri,transitiontime=300)
	if newbri <=100:
		b.set_group(g2,'bri',newbri,transitiontime=300)
        newbri = newbri + 10
        sleep(30)

print 'Lux Done'

#Wait 40 Mins Before Returning to Original State
#sleep(30*60)
sleep(30*60)

b.set_light(b1,'hue',h1)
b.set_light(b2,'hue',h2)
b.set_light(b3,'hue',h3)

b.set_light(b1,'bri',br1)
b.set_light(b2,'bri',br2)
b.set_light(b3,'bri',br3)
b.set_group(g1,'bri',brg1)
b.set_group(g2,'bri',brg2)

b.set_light(b1,'on',p1)
b.set_light(b2,'on',p2)
b.set_light(b3,'on',p3)
b.set_group(g1,'on',pg1)
b.set_group(g2,'on',pg2)
