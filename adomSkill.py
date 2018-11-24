#!/usr/bin/python
# Helps you decide which skills to upgrade, pointing you towards useful skills that you can
# increase by a large number of points

import os, readline, textwrap
TerminalHeight, TerminalWidth = os.popen('stty size', 'r').read().split()

skillUsefulness = {'ale' : 9, 'ath' : 9, 'dod' : 9, 'fin' : 9, 'fir' : 9, 'foo' : 9, 'hea' : 9, 'litsp' : 9, 'consp' : 9, 'nec' : 9, 'ste' : 9, \
    'arc' : 8, 'bac' : 8, 'dett' : 8, 'fle' : 8, 'her' : 8, 'picl' :8, 'picp' : 8, 'swi' : 8, 'tac' :8, \
    'clisp' : 7, 'coo' : 7, 'dis' : 7, 'smi' :7, \
    'deti' : 6, 'ven' : 6, \
    'alc' : 5, 'gar' : 5, 'hag' : 5, 'musb' : 5, 'lit' :5, \
    'two' : 4, 'gem' : 4, 'cou' : 4, 'cli' : 4, 'con' :4, \
    'mus' : 3, 'sur' : 3, \
    'bri' : 2, 'min' : 2, \
    'app' : 1, 'law' : 1, 'lis' : 1, 'met' : 1, 'woo' : 1 \
}

SkillTable = 'ALChemy, ALErtness, APPraisal, ARChery, ATHletics, BACkstabbing, BRIdgebuilding, CLImbing, CLImbingSPellcasters, CONcentration, CONconcentrationSPellcasters, COOking, COUrage, DETectItemstatus, DETectTraps, DISarm traps, DODge, FINd weakness, FIRst aid, FLEtchery, FOOd preservation, GARdening, GEMology, HAGgling, HEAling, HERbalism, LAW, LIStening, LITeracy, LITeracySPellcasters, METallurgy, MINing, MUSic, MUSicBards, NECromancy, PICkLocks, PICkPockets, SMIthing, STEalth, SURvival, SWImming, TACtics, TWOweaponcombat, VENtriloquism, WOOdcraft'

print("\tspellcasters: use litsp, clisp, and consp\n\tbards: use musb\n\teveryone: dett (traps), deti (items)")

skills = {}

def updateskills():
    newSkill = input("enter letter, skill, new value as CSV: ")
    # accepts 'a, ale, 20', '"a", "ale", "20"', 'a,ale,20', etc.
    letter, skill, newvalue = newSkill.split(',')
    letter = letter.strip(' "\'').lower()
    skill = skill.strip(' "\'').lower()
    newvalue = int(newvalue)
    skills[letter] = skillUsefulness[skill]*newvalue
    pairs = list(zip(skills.values(), skills.keys()))
    pairs.sort(reverse=True) # highest values first
    print(pairs)
    short = ""
    for letter in pairs:
        short += letter[1]
    print(short)

while (True):
    try:
        updateskills()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        print(textwrap.fill(SkillTable,int(TerminalWidth)) + '\n')
