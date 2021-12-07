
import socket               # Import socket module
import hashlib
########################################### CLIENT ###########################################################################
sha256_hash = hashlib.sha256()

def start_client():
    s = socket.socket()             # Creating a socket object
    host = socket.gethostname()     # Getting local machine name
    port = 12345                    # Assign a port for connection
    s.connect((host, port))         # requesting server for connection
    print("Server says => ", s.recv(1024).decode())  # printing message received from server
    while True:
        message = input("Write message to be sent to server\n")
        s.send(message.encode())
        if message == "bye":
            s.close()
        s_to_c = s.recv(1024).decode()
        print("Server says = ", s_to_c)
        if s_to_c == "bye":
            print("Closing connection as Server says bye\n")
            s.close()                       # closing the connection
            break

if __name__ == '__main__':
    start_client()