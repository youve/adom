#!/usr/bin/python
#generates random character names, based on the day of the year and the current time
import random
import time
import readline

nums = time.strftime('%j%H%M')
vowels = ['a','e','i','o','u','y', ' ', '']

name = ''

#this is taken from the Major System. it's good for memorising stuff.
for num in nums:
	if '0' == num:
		name = name + random.choice(['s','z'])
	elif '1' == num:
		name = name + random.choice(['t','d','th'])
	elif '2' == num:
		name = name + 'n'
	elif '3' == num:
		name = name + 'm'
	elif '4' == num:
		name = name + 'r'
	elif '5' == num:
		name = name + 'l'
	elif '6' == num:
		name = name + random.choice(['j','ch','sh','zh'])
	elif '7' == num:
		name = name + random.choice(['g','k'])
	elif '8' == num:
		name = name + random.choice(['f','v'])
	else:
		name = name + random.choice(['b','p'])
	name = name + random.choice(vowels)

print(random.choice([random.choice(vowels)+name,name[0:-1], name]).title())
