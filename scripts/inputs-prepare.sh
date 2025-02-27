#!/bin/bash 

rm -rf tmp/
mkdir tmp/

find inputs/linux/ -name "*.h" > tmp/filelist.txt
find inputs/linux/ -name "*.c" >> tmp/filelist.txt

cat tmp/filelist.txt | while read line
do
    mkdir -p tmp/$(dirname $line)
done

find inputs/linux/ -name "*.h" -exec cp {} tmp/{} \;
find inputs/linux/ -name "*.c" -exec cp {} tmp/{} \;

rm /tmp/tokens.txt
cat tmp/filelist.txt | while read line
do
    echo "Tokenizing $line"
    current_file="tmp/$line"
    cat $current_file >> tmp/corpus.txt
done

head -n 1000000 tmp/corpus.txt > tmp/corpus-reduced.txt
