#!/usr/bin/python
# Generates a random adom character, weighted partially on starsign and difficulty. 


import random, readline, getopt, sys

verbose = False

if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
		for o, a in opts:
			if o in ("-v", "--verbose"):
				verbose = True
	except:
		pass

def resetValues(): #races, #classes, #starsigns
	# these get modified by star signs and whatnot later
	darkelf = {'good': ['archer', 'assassin', 'barbarian', 'beastfighter', 'chaosknight', 'druid', 'elementalist', 'farmer', 'healer', 'mindcrafter', 'monk', 'necromancer', 'paladin', 'priest', 'ranger', 'weaponsmith', 'wizard'], 'bad': ['fighter'], 'middle': ['bard', 'duelist', 'merchant', 'thief']}
	drakeling = {'good': ['beastfighter', 'farmer', 'mindcrafter', 'thief', 'fighter', 'paladin', 'chaosknight', 'monk', 'assassin', 'duelist', 'healer', 'priest', 'weaponsmith', 'wizard'], 'bad': ['merchant'], 'middle': ['druid', 'elementalist', 'necromancer', 'archer', 'barbarian', 'bard', 'ranger']}
	dwarf = {'good': ['assassin', 'barbarian', 'beastfighter', 'chaosknight', 'duelist', 'farmer', 'fighter', 'healer', 'mindcrafter', 'monk', 'paladin', 'ranger', 'thief', 'weaponsmith', 'priest', 'wizard'], 'bad': ['merchant'], 'middle': ['archer', 'bard', 'druid', 'elementalist', 'necromancer']}
	gnome = {'good': ['archer', 'assassin', 'bard', 'beastfighter', 'chaosknight', 'druid', 'duelist', 'elementalist', 'farmer', 'healer', 'monk', 'necromancer', 'paladin', 'priest', 'ranger', 'thief', 'weaponsmith', 'wizard'], 'bad': ['fighter', 'merchant'], 'middle': ['barbarian', 'mindcrafter']}
	grayelf = {'good': ['archer', 'barbarian', 'bard', 'beastfighter', 'chaosknight', 'druid', 'duelist', 'elementalist', 'farmer', 'healer', 'mindcrafter', 'monk', 'necromancer', 'paladin', 'priest', 'ranger', 'weaponsmith', 'wizard'], 'bad': ['merchant', 'thief'], 'middle': ['assassin', 'fighter']}
	highelf = {'good': ['archer', 'assassin', 'barbarian', 'chaosknight', 'duelist', 'elementalist', 'healer', 'paladin', 'priest', 'ranger', 'thief', 'weaponsmith'], 'bad': ['beastfighter', 'farmer', 'fighter', 'merchant', 'monk'], 'middle': ['bard', 'druid', 'mindcrafter', 'necromancer', 'wizard']}
	human = {'good': ['archer', 'assassin', 'barbarian', 'beastfighter', 'chaosknight', 'druid', 'duelist', 'elementalist', 'farmer', 'healer', 'mindcrafter', 'monk', 'necromancer', 'paladin', 'priest', 'ranger', 'weaponsmith', 'wizard'], 'bad': ['merchant'], 'middle': ['fighter', 'thief']}
	hurthling = {'good': ['archer', 'assassin', 'beastfighter', 'chaosknight', 'duelist', 'elementalist', 'farmer', 'healer', 'mindcrafter', 'monk', 'ranger', 'thief', 'weaponsmith'], 'bad': ['fighter', 'merchant', 'necromancer', 'priest', 'wizard'], 'middle': ['barbarian', 'bard', 'druid', 'paladin']}
	mistelf = {'good': ['wizard', 'priest', 'druid', 'elementalist', 'necromancer', 'paladin', 'barbarian', 'chaosknight', 'weaponsmith', 'assassin', 'duelist', 'farmer', 'healer', 'mindcrafter', 'monk'], 'bad': ['merchant'], 'middle': ['thief', 'archer', 'bard', 'beastfighter', 'fighter', 'ranger']}
	orc = {'good': ['archer', 'assassin', 'barbarian', 'beastfighter', 'chaosknight', 'duelist', 'farmer', 'fighter', 'healer', 'monk', 'paladin', 'priest', 'ranger', 'thief', 'weaponsmith'], 'bad': ['bard', 'druid', 'elementalist', 'mindcrafter', 'necromancer'], 'middle': ['merchant', 'wizard']}
	ratling = {'good': ['archer', 'assassin', 'beastfighter', 'chaosknight', 'duelist', 'farmer', 'fighter', 'healer', 'monk', 'ranger', 'thief', 'weaponsmith'], 'bad': ['merchant'], 'middle': ['barbarian', 'bard', 'druid', 'elementalist', 'mindcrafter', 'necromancer', 'paladin', 'priest', 'wizard']}
	troll = {'good': ['healer', 'barbarian', 'farmer', 'fighter', 'assassin', 'monk', 'ranger', 'thief', 'weaponsmith', 'archer', 'chaosknight', 'priest'], 'bad': ['merchant', 'mindcrafter', 'necromancer', 'bard', 'druid'], 'middle': ['beastfighter', 'elementalist', 'paladin', 'wizard', 'duelist']}

	races = {'darkelf' : darkelf, 'drakeling' : drakeling, 'dwarf' : dwarf, 'gnome' : gnome, 'grayelf' : grayelf, 'highelf' : highelf, 'human' : human, 'hurthling' : hurthling, 'mistelf' : mistelf, 'orc' : orc, 'ratling' : ratling, 'troll' : troll}

	archer = {'good': ['darkelf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'orc', 'ratling', 'troll'], 'middle': ['drakeling', 'dwarf', 'mistelf'], 'bad': []}
	assassin = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'highelf', 'human', 'hurthling', 'mistelf', 'orc', 'ratling', 'troll'], 'middle': ['grayelf'], 'bad': []}
	barbarian = {'good': ['darkelf', 'dwarf', 'grayelf', 'highelf', 'human', 'mistelf', 'orc', 'troll'], 'middle': ['drakeling', 'gnome', 'hurthling', 'ratling'], 'bad': []}
	bard = {'good': ['gnome', 'grayelf'], 'middle': ['darkelf', 'drakeling', 'dwarf', 'highelf', 'hurthling', 'mistelf', 'ratling'], 'bad': ['human', 'orc', 'troll']}
	beastfighter = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'human', 'hurthling', 'orc', 'ratling'], 'middle': ['mistelf', 'troll'], 'bad': ['highelf']}
	chaosknight = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'mistelf', 'orc', 'ratling', 'troll'], 'middle': [], 'bad': []}
	druid = {'good': ['darkelf', 'gnome', 'grayelf', 'human', 'mistelf'], 'middle': ['drakeling', 'dwarf', 'highelf', 'hurthling', 'ratling'], 'bad': ['orc', 'troll']}
	duelist = {'good': ['drakeling', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'mistelf', 'orc', 'ratling'], 'middle': ['darkelf', 'troll'], 'bad': []}
	elementalist = {'good': ['darkelf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'mistelf'], 'middle': ['drakeling', 'dwarf', 'ratling', 'troll'], 'bad': ['orc']}
	farmer = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'human', 'hurthling', 'mistelf', 'orc', 'ratling', 'troll'], 'middle': [], 'bad': ['highelf']}
	fighter = {'good': ['drakeling', 'dwarf', 'orc', 'ratling', 'troll'], 'middle': ['grayelf', 'human', 'mistelf'], 'bad': ['darkelf', 'gnome', 'highelf', 'hurthling']}
	healer = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'mistelf', 'orc', 'ratling', 'troll'], 'middle': [], 'bad': []}
	merchant = {'good': [], 'middle': ['darkelf', 'orc'], 'bad': ['drakeling', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'mistelf', 'ratling', 'troll']}
	mindcrafter = {'good': ['darkelf', 'drakeling', 'dwarf', 'grayelf', 'human', 'hurthling', 'mistelf'], 'middle': ['gnome', 'highelf', 'ratling'], 'bad': ['orc', 'troll']}
	monk = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'human', 'hurthling', 'mistelf', 'orc', 'ratling', 'troll'], 'middle': [], 'bad': ['highelf']}
	necromancer = {'good': ['darkelf', 'gnome', 'grayelf', 'human', 'mistelf'], 'middle': ['drakeling', 'dwarf', 'highelf', 'ratling'], 'bad': ['hurthling', 'orc', 'troll']}
	paladin = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'mistelf', 'orc'], 'middle': ['hurthling', 'ratling', 'troll'], 'bad': []}
	priest = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'mistelf', 'orc', 'troll'], 'middle': ['ratling'], 'bad': ['hurthling']}
	ranger = {'good': ['darkelf', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'orc', 'ratling', 'troll'], 'middle': ['drakeling', 'mistelf'], 'bad': []}
	thief = {'good': ['drakeling', 'dwarf', 'gnome', 'highelf', 'hurthling', 'orc', 'ratling', 'troll'], 'middle': ['darkelf', 'human', 'mistelf'], 'bad': ['grayelf']}
	weaponsmith = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'highelf', 'human', 'hurthling', 'mistelf', 'orc', 'ratling', 'troll'], 'middle': [], 'bad': []}
	wizard = {'good': ['darkelf', 'drakeling', 'dwarf', 'gnome', 'grayelf', 'human', 'mistelf'], 'middle': ['highelf', 'orc', 'ratling', 'troll'], 'bad': ['hurthling']}

	classes = {'archer' : archer, 'assassin' : assassin, 'barbarian' : barbarian, 'bard': bard, 'beastfighter' : beastfighter, 'chaosknight' : chaosknight, 'druid' : druid, 'duelist' : duelist, 'elementalist' : elementalist, 'farmer' : farmer, 'fighter' : fighter, 'healer' : healer, 'merchant' : merchant, 'mindcrafter' : mindcrafter, 'monk' : monk, 'necromancer' : necromancer, 'paladin' : paladin, 'priest' : priest, 'ranger' : ranger, 'thief' : thief, 'weaponsmith' : weaponsmith, 'wizard' : wizard}

	starsigns = {'raven' : ['bard'], 
	'book' : ['mistelf', 'highelf', 'grayelf', 'darkelf', 'paladin', 'drakeling', 'darkelf', 'hurthling', 'orc', 'troll', 'dwarf', 'assassin', 'archer', 'barbarian', 'beastfighter', 'duelist', 'elementalist', 'farmer', 'fighter', 'healer', 'merchant', 'mindcrafter', 'monk', 'ranger', 'thief', 'weaponsmith' ],
	'wand' : ['wizard', 'grayelf', 'drakeling', 'gnome', 'human'],
	'unicorn' : ['chaosknight', 'darkelf', 'orc', 'troll', 'dwarf', 'highelf', 'hurthling'],
	'salamander' : ['elementalist', 'necromancer'],
	'dragon' : ['fighter', 'assassin', 'barbarian', 'beastfighter', 'chaosknight', 'duelist', 'farmer', 'monk', 'paladin', 'ranger', 'thief', 'weaponsmith'],
	'sword' : ['drakeling', 'darkelf', 'hurthling', 'orc', 'troll', 'fighter', 'assassin', 'barbarian', 'beastfighter', 'chaosknight', 'duelist', 'farmer', 'monk', 'paladin', 'ranger', 'thief', 'weaponsmith'],
	'falcon' : ['wizard', 'priest', 'druid', 'necromancer', 'mindcrafter', 'elementalist', 'paladin', 'healer', 'bard', 'merchant', 'gnome', 'hurthling', 'darkelf', 'orc', 'troll'],
	'cup' : ['wizard', 'troll', 'priest', 'grayelf', 'gnome', 'hurthling', 'druid', 'necromancer', 'mindcrafter', 'orc', 'drakeling', 'darkelf'],
	'candle' : ['troll', 'chaosknight', 'archer', 'assassin', 'barbarian', 'bard', 'farmer', 'fighter', 'merchant', 'mindcrafter', 'thief', 'necromancer', 'weaponsmith', 'mistelf', 'grayelf', 'darkelf', 'highelf'],
	'wolf' : ['wizard', 'priest', 'druid', 'necromancer', 'mindcrafter', 'elementalist', 'paladin', 'healer', 'dwarf', 'orc', 'troll'],
	'tree' : ['wizard', 'priest', 'druid', 'necromancer', 'mindcrafter', 'elementalist', 'paladin', 'healer']
	}
	return races, classes, starsigns

def adjustStars():
	races, classes, starsigns = resetValues()
	month = ''
	verboseMsg = ''
	while month not in starsigns.keys():
		month = input("\nWhat month is it?\n\n" + ', '.join(starsigns.keys()).title() + "\n").lower()


		#nudge probabilities
	for item in starsigns[month]: #wizard, #mindcrafter
		verbosePart = [[],[]]
		for key in races.keys(): #darkelf, dwarf, 
			if item in races[key]['middle']: #wizard in darkelf['middle']
				races[key]['good'].append(races[key]['middle'].pop(races[key]['middle'].index(item))) #darkelf['good'].append(darkelf['middle'].pop(races[darkelf['middle'].index(wizard)))
				verbosePart[0].append(key) #darkelf
			elif item in races[key]['bad']:
				races[key]['middle'].append(races[key]['bad'].pop(races[key]['bad'].index(item)))
				verbosePart[1].append(key)

		for key in classes.keys():
			if item in classes[key]['middle']:
				classes[key]['good'].append(classes[key]['middle'].pop(classes[key]['middle'].index(item)))
				verbosePart[0].append(key)
			elif item in classes[key]['bad']:
				classes[key]['middle'].append(classes[key]['bad'].pop(classes[key]['bad'].index(item)))
				verbosePart[1].append(key)

		if verbosePart[0] or verbosePart[1]:
			verboseMsg += item.title() + ': ' #wizard
		if verbosePart[0]:
			verboseMsg += "Moved from bad to middle in %s. " % (', '.join(verbosePart[0]))
		if verbosePart[1]:
			verboseMsg += "Moved from middle to good in %s. " % (', '.join(verbosePart[1]))
		verboseMsg += '\n'
	if verbose:
		print(verboseMsg)
	return races, classes

def createCharacter(even,odd): #even is chosen evenly with random.choice, odd is chosen to suit even
	verboseMsg = ''
	result = ''
	evenType = random.choice(list(even.keys())) #grayelf, #fighter
	oddType = ""
	dice = random.random() # float between 0 and 1
	verboseMsg += "Dice: %s.\n" % str(round(dice,3))
	evenGood = even[evenType]['good']
	evenMiddle = even[evenType]['middle']
	evenBad = even[evenType]['bad']
	evenWorse = []
	evenBetter = []
	spread = 0
	for key in even[evenType]:
		if even[evenType][key]:
			spread+=1
	if spread == 3: # we have good, middle, and bad items
		badRatio = min(0.1, len(evenBad)/len(odd))
		middleRatio = min(0.3, len(evenMiddle)/len(odd))
		goodRatio = 1 - badRatio - middleRatio
		verboseMsg += "All categories. Bad: %s items, %s percent chance each. Middle: %s items, %s percent chance each. Good: %s items, %s percent chance each.\n" % (
			str(len(evenBad)), 
			str(round(100*badRatio/len(evenBad),1)), 
			str(len(evenMiddle)), 
			str(round(100*middleRatio/len(evenMiddle),1)),
			str(len(evenGood)), 
			str(round(100*goodRatio/len(evenGood),1))
			)
	
	elif spread==2: #we have a better and a worse option
		if not evenBad:
			verboseMsg += "No bad. "
			evenBetter = evenGood
			evenWorse = evenMiddle
		elif not evenMiddle:
			verboseMsg += "No middle. "
			evenBetter = evenGood
			evenWorse = evenBad
		else:
			verboseMsg += "No good. "
			evenBetter = evenMiddle
			evenWorse = evenBad
		badRatio = min(0.25, len(evenWorse)/len(odd))
		goodRatio = max(0.75, len(evenBetter)/len(odd)) # equivalent to 1-badRatio
		verboseMsg += "Worse: %s items, %s percent chance each, Better: %s items %s percent chance each." % (
			str(len(evenWorse)), 
			str(round(100*badRatio/len(evenWorse),1)), 
			str(len(evenBetter)), 
			str(round(100*goodRatio/len(evenBetter),1))
			)
	else: #spread=1
		for key in even[evenType]:
			if even[evenType][key]:
				verboseMsg = "All %s. %s items, equal chance of each\n" % (key, str(len(even[evenType][key])))
				evenBetter = even[evenType][key]
				goodRatio = 1
				badRatio = -1
				break

	if dice <= badRatio:
		oddType = random.choice(evenBad or evenWorse)
	elif dice >= 1- goodRatio: 
		oddType = random.choice(evenGood or evenBetter)
	elif middleRatio:
		oddType = random.choice(evenMiddle)

	if verbose:
		print(verboseMsg)

	if len(even) < len(odd): # there are fewer races than classes and race should always be displayed first.
		result = evenType + ' ' + oddType
	else:
		result = oddType + ' ' + evenType

	return result

def again():
	yes = input("\nDo you want to generate another character? Y/n ")
	if yes[0].upper() == "Y":
		mainThread()
	else:
		print("Bye!")
		exit()

def mainThread():
	races, classes = adjustStars()
	firstPair = createCharacter(races,classes)
	secondPair = createCharacter(classes,races)

	print("\nHow about a %s or a %s?\n" % (firstPair, secondPair))
	again()


mainThread()