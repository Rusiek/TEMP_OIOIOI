for file in $2/*.in; do
    output=${file%.in}.out
    cat <(./$1 < $file) > $output
done