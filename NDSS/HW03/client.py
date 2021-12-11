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