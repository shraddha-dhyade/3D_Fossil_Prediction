#!/usr/bin/env bash


cd species_2/

#for d in *; do
 #echo $d
 #echo '{$d}+.obj'

#done
var a
shopt -s dotglob
find * -prune -type d | while IFS= read -r d; do
    echo "$d"
    cd $d
    ls
    a=$d'.obj'
    echo $a
    ../../binvox $a
    cd ../
done