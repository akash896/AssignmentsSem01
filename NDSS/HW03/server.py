import hmac

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

def send_message_to_client(c, client_shared_secret):
   s_to_c_message = input("Enter essage for Client")
   h = hmac.new(str(client_shared_secret[0]).encode(), s_to_c_message.encode(), hashlib.sha256)
   hash = str(h.hexdigest())
   print("message = ", s_to_c_message, " \n hash = ", hash)
   message_hash = s_to_c_message + hash
   c.send(message_hash.encode())

def check_server_message(c, client_shared_secret):
   c_to_s_message = c.recv(1024).decode()
   hash = c_to_s_message[-64:]
   message = c_to_s_message[0:len(c_to_s_message) - 64]
   calculated_h = hmac.new(str(client_shared_secret[0]).encode(), message.encode(), hashlib.sha256)
   calculated_hash = calculated_h.hexdigest()
   if calculated_hash == hash:
      print("message C->S = ", message, "\n hash = ", hash)
      print("C to S message SUCCESSFULLY transferred ####################################")
   else:
      print("Client to server MESSAGE is NOT CORRECT")


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
   client_public_key = tuple(int(k) for k in c.recv(1024).decode()[1:-1].split(", "))
   print("Client Public key = ", client_public_key)
    # creating the shared secret
   client_shared_secret = scalar_mult(server_Secret_Key, client_public_key)
   print("### Client shared secret = ", client_shared_secret)

   send_message_to_client(c, client_shared_secret)
   check_server_message(c, client_shared_secret)


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