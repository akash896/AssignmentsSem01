import hmac
import os

from secp256k1 import curve,scalar_mult
import random
import socket               # Import socket module
import hashlib
########################################### CLIENT ###########################################################################
client_Secret_Key = ""
client_Public_Key = ""
server_public_key = ""

def generate_asymmetric_keys():
    global client_Public_Key, client_Secret_Key
    client_Secret_Key = random.randrange(1, curve.n)
    client_Public_Key = scalar_mult(client_Secret_Key, curve.g)



def check_server_message(s, server_shared_secret):
    s_to_c_message = s.recv(1024).decode()
    hash = s_to_c_message[-64:]
    message = s_to_c_message[0:len(s_to_c_message)-64]
    calculated_h1 = hmac.new(str(server_shared_secret[0]).encode(), message.encode(), hashlib.sha256)
    calculated_hash1 = calculated_h1.hexdigest()
    appended_message_hash1 = message + calculated_hash1
    print("\n Message part S=>C = \n", message, "\n MAC1 \n", calculated_hash1)
    calculated_h2 = hmac.new(str(server_shared_secret[1]).encode(), appended_message_hash1.encode(), hashlib.sha256)
    calculated_hash2 = calculated_h2.hexdigest()
    if calculated_hash2 == hash:
        print("\n message S=>C = \n", message, "\n calculated_MAC2 = \n", calculated_hash2)
        print("\nS to C message SUCCESSFULLY transferred ####################################\n")
    else:
        print("\n message S=>C = \n", message, "\n calculated_MAC2 = \n", calculated_hash2)
        print("server to client MESSAGE is NOT CORRECT")



def send_message_to_server(s, server_shared_secret):
    c_to_s_message = input("Enter essage for Server")
    h1 = hmac.new(str(server_shared_secret[0]).encode(), c_to_s_message.encode(), hashlib.sha256)
    hash1 = str(h1.hexdigest())
    message_plus_hash1 = c_to_s_message + hash1
    print("\n C=> S message = \n", c_to_s_message, "\n MAC1 = \n ", hash1)
    h2 = hmac.new(str(server_shared_secret[1]).encode(), message_plus_hash1.encode(), hashlib.sha256)
    hash2 = str(h2.hexdigest())
    message_plus_hash2 = c_to_s_message + hash2
    print("\n C=> S message + MAC1 = \n", message_plus_hash1, "\n MAC2 = \n ", hash2)
    print("\n Final message sent from C=> S = \n", message_plus_hash2)
    s.send(message_plus_hash2.encode())



def start_client():
    s = socket.socket()             # Creating a socket object
    host = socket.gethostname()     # Getting local machine name
    port = 12345                    # Assign a port for connection
    s.connect((host, port))         # requesting server for connection

    # receiving public key from server
    global server_public_key
    server_public_key = s.recv(1024).decode()
    # server_public_key = int.from_bytes(s.recv(1024), "big")
    print("Server public key = ", server_public_key)

    # sending client public key to server
    s.send(str(client_Public_Key).encode())

    # creating shared secret
    print(type(server_public_key[0]))
    s_Kp = tuple(int(k) for k in server_public_key[1:-1].split(", "))
    print(s_Kp)
    print(type(s_Kp[0]))
    server_shared_secret = scalar_mult(int(client_Secret_Key), s_Kp)
    print("### Server shared secret is = ", server_shared_secret)

    check_server_message(s, server_shared_secret)
    send_message_to_server(s, server_shared_secret)






    # print("Server says => ", s.recv(1024).decode())  # printing message received from server
    # while True:
    #     message = input("Write message to be sent to server\n")
    #     s.send(message.encode())
    #     if message == "bye":
    #         s.close()
    #     s_to_c = s.recv(1024).decode()
    #     print("Server says = ", s_to_c)
    #     if s_to_c == "bye":
    #         print("Closing connection as Server says bye\n")
    #         s.close()                       # closing the connection
    #         break

if __name__ == '__main__':
    generate_asymmetric_keys()
    print("Client Public key = ", client_Public_Key)
    print("Client secret key = ", client_Secret_Key)
    start_client()