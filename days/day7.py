#!/usr/bin/python3

'''
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
'''

import os
import re

DAY = "DAY 7"

myBag = "shiny gold"
bagDict = {} # global
masterFind = 0
part1 = 0
part2 = 0

def PrepareList(aList):
    # handle additional list preparation/manipulation
    # ex: numList = [int(item) for item in aList]
    return aList

def PrintAnswers(aPart1, aPart2):
    print (DAY)
    print ("  Part 1:  {}".format(aPart1))
    print ("  Part 2:  {}".format(aPart2))

def BagCounter1000(aBag):
    global masterFind
    
    if aBag == myBag:
        masterFind += 1
    
    if aBag in bagDict.keys():
        if isinstance(bagDict[aBag][0], list):
            for subBag in bagDict[aBag]:
                BagCounter1000(subBag[1])    
        else:
            BagCounter1000(bagDict[aBag][1])

def BagCounter2000(aCount, aBag):
    global part2
    
    if aBag in bagDict.keys():
        if isinstance(bagDict[aBag][0], list):
            for subBag in bagDict[aBag]:
                part2 += int(subBag[0])*aCount
                BagCounter2000(int(subBag[0])*aCount, subBag[1])
        else:
            part2 += int(subBag[0])*aCount
            BagCounter2000(int(bagDict[aBag][0])*aCount, bagDict[aBag][1])

def Answer(aList):

    # DO IT
    mainBagRegex = "^([\w\s]+)\sbags\scontain"
    subBagRegex = "(\d)+\s([\w\s]+)\sbag"
    
    # build main bag / sub bag dictionary
    for line in aList:
        mainBagMatch = re.search(mainBagRegex, line.strip())
        for subBagMatch in re.finditer(subBagRegex, line.strip()):
            if mainBagMatch[1] not in bagDict.keys():
                bagDict[mainBagMatch[1]] = [[subBagMatch[1], subBagMatch[2]]]
            else:
                bagDict[mainBagMatch[1]].append([subBagMatch[1], subBagMatch[2]])
    
    # count against bagDict database
    global masterFind, part1
    for mainBag in bagDict.keys():
        BagCounter1000(mainBag)
        if mainBag == myBag:
            part1 -= 1
        if masterFind:
            part1 += 1
            masterFind = 0
        
    BagCounter2000(1, myBag)
    #

    PrintAnswers(part1, part2)
    
def Main():
    inputFileName = __file__.replace(".py", ".input")
    if not os.path.isfile(inputFileName):
        print ("Input file ({}) does not exist.".format(inputFileName))
        return
    with open(inputFileName, 'r') as fh:
        lines = [line.strip() for line in fh]
    
    # Prepare line list (as necessary)
    modList = PrepareList(lines)
    # Part 1/2 function call(s)
    Answer(modList)

# if run stand-alone
if __name__ == '__main__':
    Main()
