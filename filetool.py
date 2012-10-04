#!/usr/bin/python
#Name: File Tool - File I/O Tool for Locks Web Server
#FileName: filetool.py
__version__ = "0.2.4"
__all__ = ["FileTool"] 
""" 
File Tool

Tools for managing files, colors and more! For Locks.

"""

import os
import sys

class ReadErrorPage():
    """Read error pages """
    poweredby =  'Powered by Locks <i>(0.3.0)</i> (By: Core 4 The Lan Team)'
    def ErrorPage(self, path, error):
        try:
            f = open('../'+path, 'rb')
            htmlpage = []
            for lines in f:
                htmlpage.append(lines)
            f.close
            return htmlpage
        
        except IOError: # got to get rid of this
            if error == 404: # Error: 404
                print 'IOError'
                f = open('../'+path, 'w')
                f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
                f.write('\n<!-- This File was automaticly generated by Locks Web Server-->\n')
                f.write('\n<!-- Produced by Core 4 The Lan-->\n')
                f.write('<html>\n<title>Error: 404 File Not Found</title>\n')
                f.write('<body>\n<h2>Error 404</h2>\n<h3>File Not Found</h3>\n')
                f.write('<p>Sorry, but the file you were looking for does not seem exist here.</p>\n')
                f.write('<p>Please do not become upset and send <b>Robots</b> to extermanate us...</p>\n')
                f.write('<p>You can always google it. :P</p>')
                f.write('\n<hr>\n<p>{}</p></body></html>'.format(self.poweredby))
                f.close()
                return f
            if error == 0: # No Index
                f = open('../'+path, 'w')
                f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
                f.write('\n<!-- This File was automaticly generated by Locks Web Server-->\n')
                f.write('\n<!-- Produced by Core 4 The Lan-->\n')
                f.write('<html>\n<title>Index?</title>\n')
                f.write('<body>\n<h2>Non-Existant Index</h2>\n')
                f.write('<h3>No index here...</h3>\n')
                f.write('<p>Soz, the person in charge of maintaining the Web Site\'s Content Side</p>\n')
                f.write('<p>of the server, cannot keep up with his workload (as you can see) and</p>\n')
                f.write('<p>has not made a index page for this directory. <b>Instead</b> <i>I</i> </p>\n')
                f.write('<p>(The writer of this software - Locks - The best Web Server Software out</p>\n') 
                f.write('<p>there at the moment*) has to program this server to generate this page</p>\n')
                f.write('<p>and <u>therefore</u> <b>LAGGING</b> this Extremly <i>Fast</i> Server. </p>\n')
                f.write('</br>\n<p>*and best of all - It\'s writen in '\
                '<a href=http://www.python.org>Python</a></p>')
                f.write('\n<hr>\n<p>{}</p></body></html>'.format(self.poweredby))
                f.close()
                
        
        
class UserConfig():
    """Config file """
    def __init__(self): 
        config = open('config.ini', 'r+b')
        returnlist = []
        for line in config: 
            if line[0] == '#':
                pass
            elif line [0] == '\n':
                pass
            else:
                try:
                    y = line.strip()
                    [x, z] = y.split('=')
                except:
                    print bcolors.red + '[!]Error: ' + 'There is something weird about the Config file: ' + bcolors.blue + '{}'.format(line)
                    sys.exit(1)
                returnlist.append(z)
        config.close()
        self.doc_root = returnlist[0]
        self.err404   = returnlist[1]
        self.noindex  = returnlist[2]
        self.port     = int(returnlist[3]) #Port needs to be interger
        
    def MakeConfig(self):
        template = '# Config File for Locks Web Server \n# Produced by: The Core 4 the Lan Team\n' \
        '\n# DocumentRoot. Where your website is. Default is \'www\'' \
        '\nDocRoot=www\n' \
        '\n# Custom error pages for Error 404 (File not Found) and if there is no index.html in a directory.'\
        '\nErr404=error404.html' \
        '\nAutomaticIndex=noindex.html\n' \
        '\n# Port for Locks to listen on.' \
        '\nPort=9000'
        
        config = open('config.txt', 'r+')
        config.write(template)
        config.close()
        
class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    endc = '\033[0m'
    
    def disable(self):
        purple = '\033[95m'  # Purple
        blue = '\033[94m'  # Blue
        green = '\033[92m' # Green
        yellow = '\033[93m' # Yellow
        red = '\033[91m'    # Red
        white = '\033[0m'     # White
        endc = '\033[0m'
        


