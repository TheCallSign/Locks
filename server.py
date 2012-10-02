#!/usr/bin/python
#Name: Locks - Main Server Program for LockOn
#FileName: server.py
import BaseHTTPSe1rver, CoreHTTPServer
import sys, socket, SocketServer, threading, os
import urlparse
from time import asctime
__version__ = "0.3.0"
__all__ = ["LocksServer"] 
DOC_ROOT = './www'
PORT = 80

# TODO:
# 1 Add config.txt file to read options from (That is PORT, DOC_ROOT, and more to come)
# 2 Want to add the 404 error and no index error 
# to be custom pages that the user makes
# 4 Faster. And handling more connections
 

""" 
Locks Web Server

Locks Web Server but now has dropped some components 
(such as the cmd, map maker and the logger tool)

Author: Beyonder

CHANGELOG:

01/10/2012: Striped it down just to the core (Possiably even better now that it doesn't have all that extra stuff...

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
    doc_root = DOC_ROOT
    port = PORT
    local_hostname = socket.gethostname ()
    server_address = ('127.0.0.1', port)    
    httpd = ThreadingHTTPServer(server_address, handler_class)
    try:
        os.chdir(doc_root)
        currdir = os.curdir
    except OSError:
        os.mkdir(doc_root)
	os.chdir(doc_root)
        currdir = os.curdir
        print 'Done.\n'
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    httpd.daemon_threads = True	
    server_thread.start()
    extstat = None
    try:    
        while 1:
            raw_input()
    except:
        print 'Exiting'


if __name__ == "__main__":
    exit(main ())
