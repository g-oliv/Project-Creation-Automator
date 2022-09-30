# Project Creation Workflow Automator

#### This project automates the typical project creation workflow

It replaces my typical workflow:

```
gh repo create NewProject --clone

cd NewProject

touch README.md

git add . && git commit -a -m "Initial Commit"

git push -u origin main
```

with:
```
new MyNewProject
```
\
It makes use of [GitHub cli ](https://cli.github.com/) to create a remote repo and clone it. \
There is the option to choose remote repo visibility,
```
new MyNewProject private
```
which sets it as either private or public, with default as **_public_**.

## Install
1. Clone the repo 
2. Open .zshrc or .bashrc in your editor, depending on your shell
3. Add the following at the end of the file and replace with the path to the repo clone

```
source /<YOUR-PATH>/ProjectCreationAutomator/createProject.sh
```

