#!/usr/bin/python3.8
import sys

from termcolor import colored

from app.ceditbeta.main import *
from msys.lib.cd import *
from msys.lib.cset import cset
from msys.lib.echo import *
from msys.lib.ls import *
from msys.lib.nset import *
from msys.lib.pathdif import *
from msys.lib.quit import quitf
from msys.lib.refresh import refresh
from msys.lib.cat import cat
from msys.lib.mkdir import *
from msys.lib.mkfile import *
from msys.lib.posixnt import *

"""
MAU is a linux imitation made in python
Amar Djulovic & others
2020
"""
rootDir = os.path.dirname(os.path.abspath(__file__))
posixorlinux = posixfinder()
def printE(strs):
    return print(strs, end='')


class Finder:
    def __init__(self, command):
        self.command = command
        self.commandList = command.split()
        self.keywords = {'echo', 'ls', 'quit', 'exit', 'math', 'help', 'cd', 'nset', 'refresh', 'cset', 'open', 'cedit',
                         'cat', 'mkdir', 'mkfile'}

    def mFinder(self):
        # checks for valid keywords, a sort of tokenization system.
        # guides the program to each functions
        # calls command files.
        try:
            if self.commandList[0] in self.keywords:
                pass
        except IndexError:
            return None
        if self.commandList[0] in self.keywords:
            tk = self.commandList[0]
            if tk == 'echo':
                return echo(self.commandList)
            elif tk == 'cset':
                return cset(commandList=self.commandList, rootDir=os.path.dirname(os.path.abspath(__file__)), posixbool=posixorlinux)
            elif tk == 'quit':
                return quitf()
            elif tk == 'refresh':
                if posixorlinux:
                    system('clear')
                else:
                    system('cls')
                os.execv(__file__, sys.argv)
            elif tk == 'nset':
                return nsmain(self.commandList, posixorlinux)
            elif tk == 'help':
                with open(r'doc/help.txt') as f:
                    print(f.read())
                    f.close()
                return None
            elif tk == 'ls':
                return ls(self.commandList, docDir=r'doc', rootDir=os.path.dirname
                (os.path.abspath(__file__)),posixfinder=posixorlinux)
            elif tk == 'cd':
                return cd(commandList=self.commandList, currpathname=currPath, rootDir=os.path.dirname
                (os.path.abspath(__file__)))
            elif tk == 'cat':
                return cat(self.commandList, os.path.dirname
                (os.path.abspath(__file__)))
            elif tk == 'mkfile':
                return mkfile(commandList=self.commandList, rootDir=rootDir)
            elif tk == 'mkdir':
                return mkdirMain(commandList=self.commandList, rootDir=rootDir)
            elif tk == 'cedit':
                pass


        else:
            return print(f'{self.commandList[0]}: command not found')


if __name__ == '__main__':
    system('clear')
    with open(r'msys/nml/username' if posixorlinux else r'msys\nml\username') as f:
        userName = f.read()
        f.close()
    with open(r'msys/nml/computername' if posixorlinux else r'msys\nml\computername') as f:
        computerName = f.read()
        f.close()
    with open(r'msys/nml/consolecolor.txt' if posixorlinux else r'msys\nml\consolecolor.txt') as f:
        c_colorsList = f.read().split('\n')

    while True:
        currPath = os.getcwd()
        userInput = input(
            colored(f'{userName}@{computerName}', c_colorsList[0],
                    attrs=['bold']) + ':' + colored(replaceHome(text=currPath, rootDir=os.path.dirname
            (os.path.abspath(__file__))), c_colorsList[1]) + '% ')
        Finder(userInput).mFinder()
