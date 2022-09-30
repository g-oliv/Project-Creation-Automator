#!/bin/sh

BASEDIR=$(dirname "$0")

new() {

    OUT=$(python "$BASEDIR"/createProject.py $@)

    if [ $? ]; then
        VISIBILITY=$OUT
        gh repo create "$1" --"$VISIBILITY" --clone
        cd "$1"
        touch README.md
        git add . && git commit -a -m "Initial Commit"
        git push -u origin main
    fi

}
