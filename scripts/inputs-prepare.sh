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
