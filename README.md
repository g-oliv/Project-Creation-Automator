# Project Creation Workflow Automator

#### This project automates the project creation workflow

It replaces my typical workflow

```
gh repo create NewProject --clone

cd NewProject

touch README.md

git add . && git commit -a -m "Initial Commit"

git push -u origin main
```

with
```
create NewProject
```

It makes use of GitHub cli to create a remote repo and clone it. \
There is the option to choose repo visibility, with default as **_public_**
```commandline
gh repo create NewProject --private --clone
```


