#!/bin/sh

for file in $2/*.in; do
    output=${file%.in}.out

    if [[ $1 == *.exe ]]; then
        cat <(./$1 < $file) > $output
    elif [[ $1 == *.py ]]; then
        cat <(python3 $1 < $file) > $output
    fi
    
done