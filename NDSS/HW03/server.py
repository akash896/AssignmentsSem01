import socket
import hashlib
################################# SERVER ##################################################
sha256_hash = hashlib.sha256()

def start_server():
   s = socket.socket()         # Create a socket object
   host = socket.gethostname() # Get local machine name
   port = 12345                # Assign same port for connection.
   s.bind((host, port))        # Bind to the port number
   s.listen(5)                 # Now wait for client connection.
   c, addr = s.accept()  # Establish connection with client.
   print('Got connection from client with address = ', addr)
   c.send('Thank you for connecting, Now you can send REQUESTS'.encode())  # sending message to client
   while True:
      c_to_s = c.recv(1024).decode()
      print("Client says = ", c_to_s)
      if c_to_s == "bye":
         print("Closing connection as Client says bye\n")
         c.close()               # closing the connecton
         break
      message = input("input message for Client \n")
      c.send(message.encode())
      if message == "bye":
         c.close()


if __name__ == '__main__':
   start_server()