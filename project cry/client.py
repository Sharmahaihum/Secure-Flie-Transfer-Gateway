import socket

def start_client(decision):
    host = '127.0.0.1'  
    port = 12345        
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(str(decision).encode('utf-8'))
    if decision == 1:
        message = input("Enter a message:")
        client_socket.send(message.encode('utf-8'))
        # Receive 
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Encrypted message from server: {response}")
    elif decision == 2:
        message = input("Enter a message:")
        client_socket.send(message.encode('utf-8'))
        key = int(input("Enter a key:"))
        client_socket.send(str(key).encode('utf-8'))
        # Receive 
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Decrypted message from server: {response}")
    client_socket.close()

if __name__ == "__main__":
    print("Welcome to Jimin Encryption and Decryption")
    print("****************************************************************")
    decision = int(input("Enter 1 for encryption, 2 for decryption:"))
    start_client(decision)
