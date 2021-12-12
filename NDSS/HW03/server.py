import hmac
import timeit
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
   s_to_c_message = input("Enter message S=> C :  \n")
   h = hmac.new(str(client_shared_secret[0]).encode(), s_to_c_message.encode(), hashlib.sha256)
   hash1 = str(h.hexdigest())
   print("S->C message = ", s_to_c_message, " \n MAC1 = ", hash1)
   message_hash1 = s_to_c_message + hash1 # message + MAC(message, key[0])
   print("Message + MAC1 = \n", message_hash1)

   #calculate MAC using 2nd shared secret
   h = hmac.new(str(client_shared_secret[1]).encode(), message_hash1.encode(), hashlib.sha256)
   hash2 = str(h.hexdigest())
   print("S->C message + MAC1 = ", message_hash1, " \n MAC2 = ", hash2)
   message_hash2 = s_to_c_message + hash2  # message + MAC(message + MAC(message, key[0]), key[1])
   print("Final Message transferred from S => C = \n", message_hash2)
   c.send(message_hash2.encode()) #sending message appended to dual MAC

def check_server_message(c, client_shared_secret):
   c_to_s_message = c.recv(1024).decode()
   print("\n Message received from CLIENT = ", c_to_s_message)
   hash = c_to_s_message[-64:]
   message = c_to_s_message[0:len(c_to_s_message) - 64]
   calculated_h1 = hmac.new(str(client_shared_secret[0]).encode(), message.encode(), hashlib.sha256)
   calculated_hash1 = calculated_h1.hexdigest()
   print("\n message part C->S = \n", message, "\n MAC1 = \n", calculated_hash1)
   message_plus_hash1 = message + calculated_hash1

   calculated_h2 = hmac.new(str(client_shared_secret[1]).encode(), message_plus_hash1.encode(), hashlib.sha256)
   calculated_hash2 = calculated_h2.hexdigest()
   print("message C->S + MAC1 = \n", message_plus_hash1, "\n MAC2 = \n", calculated_hash2)

   if calculated_hash2 == hash:
      print("\n message C->S = \n", message, "\n final MAC2 = \n", calculated_hash2)
      print("#################   C => S message SUCCESSFULLY transferred   ####################################")
   else:
      print("\n message C->S = \n", message, "\n final MAC2 = \n", calculated_hash2)
      print("############   Client to server MESSAGE is NOT CORRECT   ##############################")


def start_server():
   s = socket.socket()         # Create a socket object
   host = socket.gethostname() # Get local machine name
   port = 12345                # Assign same port for connection.
   s.bind((host, port))        # Bind to the port number
   s.listen(5)                 # Now wait for client connection.
   c, addr = s.accept()  # Establish connection with client.

   start = timeit.timeit()
   generate_asymmetric_keys()
   print("Server Public key = ", server_Public_Key)
   print("Server secret key = ", server_Secret_Key)

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
   end = timeit.timeit()
   print("TIME taken to generate shared secret in server side = ",end - start)




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
   start_server()