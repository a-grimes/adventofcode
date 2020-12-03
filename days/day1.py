#!/usr/bin/python3

'''
--- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

'''

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
