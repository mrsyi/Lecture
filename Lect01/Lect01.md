# SicunStudio2017

#### Preface: Symbols and Fonts Regulation

- Emoji:
  - :x:: **PLZ**! Don't you ever listen to this!
  - :thumbsdown:: Don't use this, unless there no a second way
  - :question:: It depends...
  - :thumbsup:: **Always** take this piece of advice while you can
- Font:
  - **HEAVY UPPERCASE**: Pay attention to these words!
  - **E**mphasized **C**apitalized **L**etters: Helps you to memorize the terms
  - *Italicized* : Technical terms
  - `code`: Coding terms
  - star at the end\*: Try 'em out!
  - ~~deleted~~: Deleted lines


## Lecture 01

### Few words on National-Day Homework

- IDE / Text Editor Choice
  - `notepad` (Win default text editor) :thumbsdown:
    - GB2312 and UTF-8
    - CRLF
  - MS Office :x:
  - Atom, SumblimeText, VisualStudio Code :thumbsup:
  - Notepad++: :question: for it's ugliness
- Usage of CSS Framework :question:


----------------------------------------------------------------

### Git & CLI


#### CLI

_CLI, i.e. Command Line Interface_

To use `git` like a pro, CLI tricks are neccessary!  

Fortunately, CLI commands are **EASY** to read and write!  
*Commands* are just like *imperative sentences* in natural language, which consists of *Verb* and *Object*, sometimes *Modifiers* if neccessary.  

Examples\*:  
- `cd TARGET_DIR`: **C**hange working **D**irectory to **TARGET_DIR**
- `mkdir DIR_NAME`: **M**a**K**e **DIR**ectory, named **DIR_NAME** (under *current working directory* by default)
  - `-p` flag: make **P**arent directory if it does not exist
- ...  


#### System File Structure

- Linux\*:
  - `/`: root directory
  - `/home/<USER>/`: home directory of each user, namely `<USER>`
  - `/usr/`: **U**nix **S**oftware **R**esources
  - `/usr/bin/`: common binary executables, like `gcc`, `nmcli`
  - ...  
- WinNT (system installed under `C:\`):
  - `C:\`: system partition, like `/`
  - `C:\User\<USER>`: like `/home/<USER>`
  - `C:\System\` *(?)* : like `/usr/`
  - ...

##### Surfing your file system\*

- the `cd` (**C**hange **D**irectory) command
- Relative path:
  - `./`: current directory
  - `../`: parent directory

##### How to open a image using Google Chrome\*

Use **U**niform **R**esource **I**dentifier: `file://<PATH_TO_FILE>`  

- Linux: `file:///home/smdsbz/Desktop/ESL.pdf`
- WinNT: `file://C:\User\smdsbz\Desktop\PEP8%20Style%20Guide.mhtml`


Use the skills you've just learned in this section in coding, when:
- referencing to a **LOCAL** file resource:
  - some `url_for()` function provided by template renderers, like `Flask` :thumbsup:
  - relative path: starting with the `.` :question:
  - absolute path: starting with `/` (or `[A-Z]:\` on WinNT) :thumbsdown:
    - Users should **NOT** know details about your server's configuration
    - It leads to considerable amount of re-coding work when you distribute your service to a server, whose system's file structure is unknown
- ...


#### Git\*

_`git` is a CLI tool-set for version control_  
_repo is the short term for repository_

##### 1. Create a new *repository* on [GitHub.com](https://github.com)
- Initialize your repo with a `README.md`
  - Put documentations of your project in `README.md`, so other people visiting your repo will see it
- `.gitignore`
  - Your `git` will ignore the files with the suffixes listed in `.gitignore`, so they won't be uploaded to code server, e.g:
    - `.exe`: compiled binaries / executables
    - `__pycache__/`: python cache directory
    - `.so` / `.dll`: shared objects
- `LICENCE`
  - How your work can be referenced by other people
    - MIT, GNU GPL, Apache

##### 2. Hack! Hack! Hack!

##### 3. Upload your code to your repo on GitHub.com

Your changes made on your source code files can have the following 4 statuses:
- changes not commited
- changes added to version control system
- changes prepared to be commited
- uploaded to GitHub.com

`git` heads-up:
- `git status`: check what's not added to v.c.s.
- `git add *`: **add** `*` (everything) to v.c.s, like a quick back-up
- `git commit -m 'my messages'`: prepare your changes to be **commit**ed
  - `-m` flag: **M**essage, otherwise `git` will open a text editor
- `git push`: upload (**push**) commits to GitHub.com

##### 4. RETURN to Step 2, 'till job done

------------------------------------------------------------

### A Simple Webpage, sur place!\*

- basic html
- basic `<link>` css

------------------------------------------------------------

### Assignment

Five-in-a-Row (presented via HTML, CSS, JS)
