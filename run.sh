#!/usr/bin/bash

if [ $# -ne 1 ]; then
    echo "Rerun with a selected day: ./run.sh <day>"
    exit
fi

dayPy="days/day$1.py"
dayInput="days/day$1.input"

if [ -f $dayPy ] && [ -f $dayInput ]; then
    python3 $dayPy $dayInput
else
    echo "Day $1 files do not exist"
fi