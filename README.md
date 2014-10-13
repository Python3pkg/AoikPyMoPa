# AoikPyMoPa
Find a Python module's file paths. Have considered Implicit Namespace Packages introduced in [PEP 420](http://legacy.python.org/dev/peps/pep-0420/) since [Python 3.3](https://docs.python.org/3/whatsnew/3.3.html#pep-420-implicit-namespace-packages). Handy for debugging tricky importing problems.

Tested working with:
- Windows  
- Python: 2.1+, 3.0+

[Package on PyPI](https://pypi.python.org/pypi/AoikPyMoPa)

## Contents
- [How to install](#how-to-install)
  - [Install via pip](#install-via-pip)
  - [Install via download](#install-via-download)
- [How to use](#how-to-use)
  - [Find the command](#find-the-command)
  - [Run the command](#run-the-command)
- [How to read the funny source code](#how-to-read-the-funny-source-code)

## How to install
### Install via pip
Run
```
pip install AoikPyMoPa
```
or
```
pip install git+https://github.com/AoiKuiyuyou/AoikPyMoPa
```

### Install via download
Alternatively download this [single file](/src/aoikpymopa/aoikpmp.py).

Note installing this way you do not get the executable file that pip creates for you.

## How to use
### Find the command
After the [installation](#how-to-install), a command named **aoikpmp** should be available on your console.

### Run the command
Run without argument to show usage: 
```
aoikpmp
```
```
Usage: aoikpmp PYTHON.MODULE.NAME
```

Run for a file module
```
aoikpmp os
```
```
D:\Software\Dev\Lang\Python\2\dst\lib\os.pyc
```

Run for a built-in module
```
aoikpmp sys
```
```
Module |sys| seems to have no file. Is it a built-in?
```

Run for an Implicit Namespace Package introduced in [PEP 420](http://legacy.python.org/dev/peps/pep-0420/) since [Python 3.3](https://docs.python.org/3/whatsnew/3.3.html#pep-420-implicit-namespace-packages)
```
#/ Windows
SET PYTHONPATH=D:\Python\dir1;D:\Python\dir2

#/
aoikpmp an_implicit_namespace_package
```
```
D:\Python\dir1\an_implicit_namespace_package
D:\Python\dir2\an_implicit_namespace_package
```

Run for a non-existent module
```
aoikpmp a_nonexistent_module
```
```
Module |a_nonexistent_module| can not be imported.
```

Run for a broken module
```
aoikpmp a_broken_module
```
```
Module |a_broken_module| has had errors when being imported:
---
Traceback (most recent call last):
  File "D:\Software\Dev\Lang\Python\2\dst\lib\site-packages\aoikpymopa\aoikpmp.py", line 53, in main
    __import__(mod_name)
  File "D:\Software\Dev\Lang\Python\2\dst\lib\site-packages\a_broken_module.py", line 1, in <module>
    assert False
AssertionError
---
```

## How to read the funny source code
For developers interested in reading the source code,  
Here is a flowchart ([.png](/doc/dev/main.png?raw=true), [.svg](/doc/dev/main.svg?raw=true), or [.graphml](/doc/dev/main.graphml?raw=true)) that has recorded key steps of the program.  
![Image](/doc/dev/main.png?raw=true)

The flowchart is produced using free graph editor [yEd](http://www.yworks.com/en/products_yed_download.html).

If you want to copy the text in the graph, it's recommended to download the [.svg](/doc/dev/main.svg?raw=true) file and open it locally in your browser. (For security reason, Github has disabled rendering of SVG images on the page.)

The meaning of the shapes in the flowchart should be straightforward.  
One thing worth mentioning is isosceles trapezium means sub-steps.

The most useful feature of the flowchart is, for each step in it,
there is a 7-character ID.  
This ID can be used to locate (by text searching) the code that implements a step.  
This mechanism has two merits:

1. It has provided **precise** (locating precision is line-level)
  and **fast** (text searching is fast) mapping from doc to code, which is
  very handy for non-trivial project.

  Without it you have to rely on developers' memory to recall the code locations (*Will you recall them after several months, precise and fast?*).

2. It has provided **precise** (unique ID) and **concise** (7-character long) names
  for each steps of a program, which is very handy for communicating between
  members of a development team.

  Without it describing some steps of a program between team members tends to be unclear.
