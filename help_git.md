=============================================================================
#///  GRAFIC INTERFACE
git
tig
gitk
git log --graph
git log --graph --all --abbrev-commit
=============================================================================
#///  INFO OF MY ACCOUNT

user.name=Javier Quesada Reyes
user.email=xavier53348@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
=============================================================================
#/// CREATE VIRTUAL ENVAIROMENT

$ python3 -m venv .venv
$ source .venv/bin/activate
=============================================================================
#///  RUN ONE TIME
$ git config --global user.name "Javier Quesada Reyes"
$ git config --global user.email xavier53348@gmail.com

$ git config --global core.editor subl
$ git config --list
$ git config user.name
$ git help <comando>
=============================================================================
#///  START GIT PROYECT

$ git init
touch .gitignore             # <=== IGNORE
=============================================================================
#///  ONE EXEMPLE GIT IGNORE .gitignore:

# a comment – this is ignored
*.a       # no .a files
!lib.a    # but do track lib.a, even though you're ignoring .a files above
/TODO     # only ignore the root TODO file, not subdir/TODO
build/    # ignore all files in the build/ directory
doc/*.txt # ignore doc/notes.txt, but not doc/server/arch.txt
=============================================================================
#///  RENAME ADD REMOVE RESTORE

$ git mv  README.txt README  # <=== RENAME
$ git add README             # <=== ADD
$ git rm  README.txt         # <=== REMOVE
$ git rm --cached <file>     # <=== REMOVE
$ git restore --staged <file># <=== RESTORE
$ git commit -m 'COMMENT'    # <=== UPDATE
=============================================================================
#///  ADD AND UPDATE GIT

$ git add README test.rb LICENSE
$ git add .
$ git add -A                 # <=== USE THIS
$ git commit -m 'COMMENT'    # <===
$ git commit -a -m 'COMMENT' # <=== es un add y commit al mismo tiempo
=============================================================================
#///  CREATE A NEW BRANCH AND CHANGE BETWEEN BRANCHS

$ git branch                 # <=== SABER las ramas git branch --no-merged
$ git branch testing         # <=== CREAMOS la nueva rama TESTING   pro [git branch features/menu_phone]
$ git checkout testing       # <=== NOS MOVEMOS de la rama master que es por defecto a la rama testing
$ git checkout -b testing    # <=== es branch and checkout <== creamos y apuntamos a la rama
=============================================================================
#///  MERGE BRANCHS

$ git checkout master        # <=== NOS MOVEMOS la rama master
$ git merge testing          # <=== FUCIONAMOS  la rama que queremos
$ git branch -d testing      # <=== BORRAMOS    la rama testing

$ git checkout master        # <=== NOS MOVEMOS la rama master y centramos en ese archivo
$ git checkout --patch testing file.py # <=== de la rama testing mege fiel.py

=============================================================================
#///  mergetool GRAFICS INTERFACE

$ git mergetool
=============================================================================
#///  LOGS AND INFO

$ git status
$ git reflog

$ git shortlog                                      # <===
$ git log --pretty=oneline                          # <===
$ git log --pretty=reference                        # <===
$ git log --stat                                    # <=== ****

$ git log
$ git log --pretty=format:"%h - %an, %ar : %s"
=============================================================================
#///  REMOVE LOGS
$ git -rf .git
$ git init

$ git reflog expire --expire=now --all
$ git gc --aggressive --prune=all

===================================== MARK DOWN =============================
#///

# Big title H1
## MEDIUM title H2
### NORMAL title H3
#### Big title H4
##### Big title H5
###### Big title H6


pip install mkdos <==== instalacion de documentacion


<!-- words -->

*italic*
**bold**
~~strike_text~~

<!-- list unorder -->
* this is a
* list unorder
    * sub list unorder

<!-- list order -->
1. this is a
2. list unorder

<!-- link -->
[button](http://exemple.com)
[button](http://exemple.com 'custom title')


> this is a cite

` simple code print('hello')`
```python
multy line code
    print('hello')
```

<!-- table -->
| item 1 | item 2 |
|--------|--------|
|exemple | exemple|

<!-- imagen -->
![viual studio logo](http://place.logo.imagen)
![viual studio logo](imagen.png 'title of the imagen')