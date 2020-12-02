#!/usr/bin/python3

import os

DAY = "DAY 1"

def PrepareList(aList):
    numList = [int(item) for item in aList]
    return numList

def PrintAnswers(aPart1, aPart2):
    print (DAY)
    print ("  Part 1:  {}".format(aPart1))
    print ("  Part 2:  {}".format(aPart2))

def Answer(aList):
    # part 1
    part1 = "?"
    for item in aList:
        if ((2020-item) in aList):
            part1 = item * (2020-item)
        for item2 in aList:
            if ((2020-item-item2) in aList):
                part2 = item * item2 * (2020-item-item2)
    
    # part 2
    # part2 = "?"

    PrintAnswers(part1, part2)
    
def Main():
    inputFileName = __file__.replace(".py", ".input")
    if not os.path.isfile(inputFileName):
        print ("Input file ({}) does not exist.".format(inputFileName))
        return
    with open(inputFileName, 'r') as fh:
        lines = [line.strip() for line in fh]
    
    # Prepare line list (as necessary)
    numList = PrepareList(lines)
    # Part 1/2 function call(s)
    Answer(numList)

# if run stand-alone
if __name__ == '__main__':
    Main()
