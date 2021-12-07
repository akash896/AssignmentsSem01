
import socket               # Import socket module

########################################### CLIENT ###########################################################################

s = socket.socket()             # Creating a socket object
host = socket.gethostname()     # Getting local machine name
port = 12345                    # Assign a port for connection
s.connect((host, port))         # requesting server for connection
print ("Server says => ", s.recv(1024).decode())    #printing message received from server
s.close()                       # closing the connection