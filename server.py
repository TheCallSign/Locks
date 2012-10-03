#!/usr/bin/python
#Name: Locks - Main Server Program for LockOn
#FileName: server.py
import BaseHTTPServer, CoreHTTPServer
import sys, socket, SocketServer, threading, os
import urlparse
from time import asctime
from filetool import UserConfig
__version__ = "0.4.1"
__all__ = ["LocksWebServer"] 


# TODO:
# Comments in config.txt
# Change config.txt to config.ini
# (This can wait) 4 Faster. And handling more connections
 

""" 
Locks Web Server

Locks Web Server but now has dropped some components 
(such as the cmd, map maker and the logger tool)



Author: Beyonder


 """

class locksHandler(CoreHTTPServer.SimpleHTTPRequestHandler):
    __base = BaseHTTPServer.BaseHTTPRequestHandler
    __base_handle = __base.handle
    server_version = "Locks/" + __version__

    def handle(self):
        (ip, port) =  self.client_address
        self.__base_handle()
        
        
class ThreadingHTTPServer (SocketServer.ThreadingMixIn,
                           BaseHTTPServer.HTTPServer):
    def __init__ (self, server_address, RequestHandlerClass, logger=None):
        BaseHTTPServer.HTTPServer.__init__ (self, server_address,
                                            RequestHandlerClass)


def exit(ext):
    sys.exit(ext)
	
def main(server_class=BaseHTTPServer.HTTPServer, handler_class=locksHandler):
    version = __version__
    print "Starting Locks Web Server..."
    ConfigFile = UserConfig()
    doc_root = ConfigFile.doc_root
    port = ConfigFile.port
    if port < 1024:
        loginname = os.geteuid()
        if loginname == 0:
            pass
        else:
            print '[!]You have to be root to listen on ports under 1024.'
            sys.exit(1)
    local_hostname = socket.gethostname ()
    server_address = ('127.0.0.1', port)
    httpd = ThreadingHTTPServer(server_address, handler_class)
    try:
        os.chdir(doc_root) #Change to doc_root for security
        currdir = os.curdir
    except OSError:
        os.mkdir(doc_root)
        os.chdir(doc_root)
        currdir = os.curdir
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    httpd.daemon_threads = True	
    server_thread.start()
    print 'Listening on port: {}'.format(port)
    try:    
        while 1:
            raw_input()
    except:
        print '\nExiting'


if __name__ == "__main__":
    exit(main ())
