#!/bin/sh

TIME_MAX=0
MEMORY_MAX=0

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
    time_s=$(( (end-start)/(10**6) ))
    printf "%.3fs\n\n" $(( $time_s ))e-3

    if (( "$time_s" > "$TIME_MAX" )); then
        TIME_MAX=$(( $time_s ))
        TIME_MAX_NAME=$( basename $test )
    fi
done

printf "All tests passed!\n\n"
printf "Max time: %.3fs\n" $(( TIME_MAX ))e-3
printf "Test name: %s\n\n" $TIME_MAX_NAME
