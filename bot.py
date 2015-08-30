#/usr/bin/python2
import socket
import subprocess
import urllib
import sys
import random
import time
import platform
import os

def bot_nick():
    randnum = random.randrange(1,100)
    return randnum
	
# IRC Settings
x = bot_nick()
server = "irc.freenode.net" #Server goes here      
channel = "#loldays" # Channel to connect to goes here (all channels require a # infront of their name)
botnick = ("Zer0Day" + str(x)) # The bot's name will be Zer0Day followed by the IP Address of the machine it's calling from.

def sayHello(text):
        '''
            Name: sayHello
            Purpose: Awaits the text "Hi" and responds with "Hello Commands, lovely day is it not?".
                     This servers as an "are you alive?" message.
            Return: Text in IRC chat.
       
        '''
        if text.find(':Hi') !=-1: #you can change !hi to whatever you want
            t = text.split(':Hi') #you can change t and to :)
            to = t[1].strip() #this code is for getting the first word after !hi
            irc.send('PRIVMSG '+channel+' :Hello Commander, lovely day is it not?' + '\r\n')
	
def goodnight(text):
        '''
            Name: goodnight
            Purpose: Awaits the text "goodnight and goodluck" to shutdown the Bot.
        '''
        if text.find(":goodnight and good luck") !=-1: #you can change !hi to whatever you want
            t = text.split(":goodnight and good luck") #you can change t and to :)
            to = t[1].strip() #this code is for getting the first word after !hi
            sys.exit()
		
if __name__ == "__main__":
    '''
        Main function that connects to IRC server and awaits commands to be issued.
        This should be moved to a few functions or a class to better configure the bot.
    '''
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Defines the socket
    irc.connect((server, 6667))                                                         #connects to the server
    irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n") #user authentication
    irc.send("NICK "+ botnick +"\n")                            #sets nick
    irc.send("PRIVMSG nickserv :iNOOPE\r\n")    # Auth
    irc.send("JOIN "+ channel +"\n")        # Join the channel specified above
                                    
    while 1:    #puts Bot in a loop constantly waiting to receive text.
            text=irc.recv(4096)  #receive the text
            lines = text.split("\n")

            if text.find('PING') != -1:                          # Check if 'PING' is found (part of the IRC RFC)
                    irc.send('PONG ' + text.split() [1] + '\r\n') # Returns 'PONG' back to the server (prevents pinging out!) Also part of the IRC RFC.
            elif text.find("PRIVMSG " + botnick): # For private messaging individual bots.
                    #Custom commands
                    sayHello(text)
                    goodnight(text)
            else:
            #Custom commands
                    sayHello(text)
                    goodnight(text)
