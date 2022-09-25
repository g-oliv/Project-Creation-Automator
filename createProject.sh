#!/bin/sh

function new() {
    out=$(python createProject.py $@)

if [ $? ]
then
    visibility=$out
    echo $visibility
    gh repo create $1 --$visibility --clone
    cd $1
    touch README.md
    git add . && git commit -a -m "Initial Commit"
    git push -u origin main
fi
}
