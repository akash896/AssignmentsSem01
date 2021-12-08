from secp256k1 import curve,scalar_mult
import random
import socket
import hashlib

################################# SERVER ##################################################
server_Secret_Key = ""
server_Public_Key = ""
client_public_key = ""

def generate_asymmetric_keys():
    global server_Public_Key, server_Secret_Key
    server_Secret_Key = random.randrange(1, curve.n)
    server_Public_Key = scalar_mult(server_Secret_Key, curve.g)

def start_server():
   s = socket.socket()         # Create a socket object
   host = socket.gethostname() # Get local machine name
   port = 12345                # Assign same port for connection.
   s.bind((host, port))        # Bind to the port number
   s.listen(5)                 # Now wait for client connection.
   c, addr = s.accept()  # Establish connection with client.
   print('Got connection from client with address = ', addr)

   # sending server public key to client
   c.send(str(server_Public_Key).encode())
   # receiving public key from client
   global client_public_key
   client_public_key = c.recv(1024).decode()
   print("Client Public key = ", client_public_key)
    # creating the shared secret
   client_shared_secret = scalar_mult(server_Secret_Key, client_public_key)
   print("Server shared secret = ", client_shared_secret)




   # c.send('Thank you for connecting, Now you can send REQUESTS'.encode())  # sending message to client
   # while True:
   #    c_to_s = c.recv(1024).decode()
   #    print("Client says = ", c_to_s)
   #    if c_to_s == "bye":
   #       print("Closing connection as Client says bye\n")
   #       c.close()               # closing the connecton
   #       break
   #    message = input("input message for Client \n")
   #    c.send(message.encode())
   #    if message == "bye":
   #       c.close()


if __name__ == '__main__':
   generate_asymmetric_keys()
   print("Server Public key = ", server_Public_Key)
   print("Server secret key = ", server_Secret_Key)
   start_server()
