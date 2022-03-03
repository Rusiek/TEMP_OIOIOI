#!/bin/sh

for file in $2/*.in; do
    start=`date +%s%N`
    test=${file%.in}.out

    if      [[ $1 == *.exe ]];  then
        diff -bsq $test <(./$1 < $file) || break
    elif    [[ $1 == *.py ]];   then
        diff -bsq $test <(python3 $1 < $file) || break
    elif    [[ $1 == *.c ]];    then
        printf "Use .exe file instead of .c file!\n"
    elif    [[ $1 == *.cpp ]];  then
        printf "Use .exe file instead of .cpp file!\n"
    fi

    end=`date +%s%N`
    printf "%.3f%s\n\n" $(((end-start)/(10**6)))e-3 s
done