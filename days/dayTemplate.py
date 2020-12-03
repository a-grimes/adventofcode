#!/usr/bin/python3

import os

DAY = "DAY <>"

def PrepareList(aList):
    # handle additional list preparation/manipulation
    # ex: numList = [int(item) for item in aList]
    return aList

def PrintAnswers(aPart1, aPart2):
    print (DAY)
    print ("  Part 1:  {}".format(aPart1))
    print ("  Part 2:  {}".format(aPart2))

def Answer(aList):
    part1 = "?"
    part2 = "?"

    # DO IT



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
