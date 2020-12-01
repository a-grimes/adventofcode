#!/usr/bin/python3

import os

DAY = "DAY N"

class DayAnswer:
    def __init__(self, aLines):
        self.fileLines = aLines
        # part 1 and part 2 data stores

    def part1(self, aArgList):
        for line in self.fileLines:
            if not line:
                continue
            line = line.strip()
            # part 1 logic

    def part2(self, aArgList):
        for line in self.fileLines:
            if not line:
                continue
            line = line.strip()
            # part 2 logic

    def giveAnswers(self):
        print (DAY)
        print (" Part 1 : {}".format())
        print (" Part 2 : {}".format())

def Answer():
    inputFileName = __file__.replace(".py", ".input")
    if not os.path.isfile(inputFileName):
        print ("Input file ({}) does not exist.".format(inputFileName))
    inputFile = open(inputFileName, 'r') 
    lines = inputFile.readlines()
    inputFile.close()
    
    day = DayAnswer(lines)
    
    day.part1([])
    day.part2([])

    day.giveAnswers()

# if run stand-alone
if __name__ == '__main__':
    Answer()
