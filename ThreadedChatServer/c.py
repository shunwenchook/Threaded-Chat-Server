
# Echo client program
import socket
import hashlib
import time

HOST = '127.0.0.1'    # The remote host
PORT = 50007          # The same port as used by the server



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print "Please input username:"
username = raw_input()


print "type input:"

text = raw_input()
if "ping" in text:
    # start the timer
    startTime = time.time()
    print "ping start time " + str(startTime)

# <cmd>message:hello there - a</cmd>

hash = hashlib.sha224(text).hexdigest()

output = '<cmd>message:'+text+'-'+hash+'</cmd>' #holder for the command


# when we send data to the server, we are using a colon
# at the end of a sentence to mark the end of the current sentence
# later when the input comes back, we will then be breaking the input
# into individual parts using the colon : to separate the lines
if "ping" in text:
    output = "<cmd>ping</cmd>"
    
if "username" in text:
    output = '<cmd>username='+username+'</cmd>'

if "time" in text:
    output = '<cmd>time</cmd>'
   
if "total" in text:
    output = '<cmd>total</cmd>'
   
s.sendall(output + ":")

data = s.recv(80000)

# breaking apart the data we get back.
response = data.split(':')

for x in response:
    print "Response:" + str(x)
    
if "pong" in response:
    print "stop timer"
    stopTime = time.time()
    print "stop time" + str(stopTime)
    totalTime = stopTime - startTime
    print "total time" + str(totalTime)
    
    
s.close()
