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

b1 = 1
g1 = 2

b.set_light(10,'hue',0)
