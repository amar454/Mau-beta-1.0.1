# Mau-beta-1.0.
Description:
  shell imitation made in python
Commands:
    echo: ARGS,             returns ARGS as plain text

    quit,                   quits command line

    refresh,                clears the screen

    ls: &[SETTINGS]: &OPT:,  lists the current directories files, and subdirectories. If param OPT is filled it will list OPT's files and subdirectories, will return FileNotFoundError if OPT isn't a real directory under the root directory

    cat: FILE,              will print out a FILE's contents

    nset: OPTION: NAME,     will change the name of option if option is a nml system name

    cset: OPTION: NAME,     will change OPTION consoles colored text, with, will throw error is NAME isn't a valid termcolor color.

    cd: DIR                 will change the working directory to DIR if dir is a directory
Tip:
    Type (command) --help for more help with each command
