import socket

################################# SERVER ##################################################

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Assign same port for connection.
s.bind((host, port))        # Bind to the port number
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from client with address = ', addr)
   c.send('Thank you for connecting'.encode()) #sending message to client

   c.close()               # closing the connecton