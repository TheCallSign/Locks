#!/usr/bin/python
#Name: File Tool - File I/O Tool for Locks Web Server
#FileName: filetool.py
__version__ = "0.1.1"
__all__ = ["FileTool"] 
""" 
File Tool

Tool for reading and managing files with Locks (0.3.0)

"""

import os
import sys

class ReadErrorPage():
    """Read error pages """
    def Error404(self):
        pass
        
class UserConfig():
    """Config file """
    
    def MakeConfig(self):
        template = 'DocRoot=www\nErr404=Error404.html\nNoIndexError=NoIndex.html\nPort=9000'
        config = open('config.txt', 'r+')
        config.write(template)
        config.close()
        
    def ReadConfig(self): #XXX: Need to make sure what actual option it is returning value for.
        config = open('config.txt', 'r')
        returnlist = []
        for line in config:
            [x, y] = line.split('=')
            returnlist.append(y)
        config.close()
        return returnlist # Return values in the format: Doc_root, Err404, NoIndex, Port



