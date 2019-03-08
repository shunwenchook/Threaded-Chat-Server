# Threaded-Chat-Server
A python based chat server that allows for communication of users across different systems

Design
The program is a basic chat system, where two programs are capable of communicating with each other. These programs can also take in inputs and send them between themselves. Our program was based on the lab work, and then additional functions were added.
Functions
Encryption
When a message is sent the server can determine whether the message was completely sent without any changes to it. This is done by the sha224 encryption algorithm, which hashes the user’s message. The server then hashes the received message, and compares the hashed data to the client’s encrypted message and then determines if the message is complete and unchanged.

Pinging
The program is capable of pinging the server, which results in the server sending the message “pong” to the person, as well as displaying the amount of time it took the server to respond.

User Names
When a user enters the chat, he or she is prompted to input a username. The chat is capable of displaying the name of a user with the username command.

Displaying Time
A user is capable of asking the server to display the current time with the “time” command.
The server then shows the current day of the week, date and hour.

Total Messages
By typing in the command “total”, the user will receive a message from the server, saying how many messages were sent between the users.


 
Implementation
Encryption
When the user puts in an input in the input program c.py, the hashlib is used to hash the message.

hash = hashlib.sha224(text).hexdigest()

Our program uses the SHA224 hash algorithm to convert the text input into a secure hash. the hexdigest() method returns the digest of strings containing hexadecimal digits.

output = '<cmd>message:'+text+'-'+hash+'</cmd>' 

The hash code is then put in a string with the command, message, together with the initial text input. The string output is then passed to the s.sendall() method to send the command to the listener program, s.py. The s.py program receives the command and passes it to the paserInput() method where it determines what method to be called according to the command.

elif "message" in command:
            parseMessage(command)


Since the word “message” was in the command, parseMessage() is called with the command as the parameter. The method strips down the the <cmd> tag and the the message, leaving only the hash code. The method hashes the message again with the same method and compares the hash code.

keyvaluepair = command[8:len(command)]

An if statement checks if the hash code matches and prints a message if it does.

 
Ping
When the ping command is inputted in the input progra, c.py.  An If statement is called that starts a timer for the message pong to come back from the s.py program.

if "ping" in text:
    # start the timer
    startTime = time.time()
    print "ping start time " + str(startTime)

The parseInput() method is then called which then calls the pong() method.

def pong():
    print "sending pong"
    conn.send("pong")

The pong() method sends the string, pong, back to the c.py program. 

if "pong" in response:
    print "stop timer"
    stopTime = time.time()
    print "stop time" + str(stopTime)
    totalTime = stopTime - startTime
    print "total time" + str(totalTime)

Once pong is returned back to the c.py program. The program stops the time and prints the time it took for the program to respond back to the c.py program.
User name
The programs starts by asking the user what is his/her username

print "Please input username:"
username = raw_input()

The username is then inserted in a command holder that is then passed to the s.py program.

if "username" in text:
    output = '<cmd>username='+username+'</cmd>'

In the s.py program, an if statement calls in the printUsername() method with the command as a the parameter which contains the username.

elif "username" in command:
            printUsername(command)
The printUsername() method cuts down the command section of the string and just takes the username and prints it back to the user.

Displaying Time
The displayTime() method in the s.py program, uses the gmtime and strftime library to get time information for the program.

def displayTime():
    time = strftime("The server time is %a, %d %b %Y %H.%M.%S +0000", gmtime())
    conn.send(time);

The strftime() method gets the current time and sends it back to the user.

Total Messages

The manageConnection() method adds the command to the buffer each time a command is passed to the s.py, program. The totalBuffer() method retrieves the buffer from the manageConnection() method and counts it using the count() method. The count method counts how many times a colon, :, is passed to it

def totalBuffer():
    global buffer
    count = buffer.count(':')
    conn.send('There are '+ str(count)+' messages in the buffer')

 
Visual representation
Users establishes connections by running the c.py program. The program will first ask for a username input followed by a command input. The server, s.py, program then determines what command was called and calls the methods accordingly. 
