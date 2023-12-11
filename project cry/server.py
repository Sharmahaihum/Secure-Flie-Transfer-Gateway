import socket
import random as rand

def start_server():
    host = '127.0.0.1'  
    port = 12345         
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        check = int(client_socket.recv(1024).decode("utf-8"))
        if check == 1:
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received data: {data}")
            response, key = work(data)
            client_socket.send(f"{response} Key: {key}".encode('utf-8'))
            client_socket.close()
        elif check == 2:
            data1 = client_socket.recv(1024).decode('utf-8')
            key = int(client_socket.recv(1024).decode('utf-8'))
            response = work2(data1,key)
            client_socket.send(response.encode('utf-8'))
            client_socket.close()

def ecry(data):
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = []
    z = 1
    key = rand.randrange(101,1000)
    for i in range(len(array)):
        alpha.append((array[i], z))
        z += 1
    sentence = data
    words = sentence.split()
    encrypted_words = []
    for word in words:
        add = []
        final = []
        result = []
        for char in word:
            for i in range(len(alpha)):
                if alpha[i][0] == char:
                    add.append(alpha[i][1])
        for i in range(len(add)):
            final.append((add[i] + key) % 26)
        for i in range(len(final)):
            for j in range(len(alpha)):
                if final[i] == alpha[j][1]:
                    result.append(alpha[j][0])
        encrypted_words.append("".join(result))
    encrypted_sentence = " ".join(encrypted_words)
    return encrypted_sentence, key

def dcry(data1, key):
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = []
    z = 1
    for i in range(len(array)):
        alpha.append((array[i], z))
        z += 1
    sentence = data1
    key = key
    words = sentence.split()
    decrypted_words = []
    for word in words:
        add = []
        final = []
        result = []
        for char in word:
            for i in range(len(alpha)):
                if alpha[i][0] == char:
                    add.append(alpha[i][1])
        for i in range(len(add)):
            final.append((add[i] - key) % 26)
        for i in range(len(final)):
            for j in range(len(alpha)):
                if final[i] == alpha[j][1]:
                    result.append(alpha[j][0])
        decrypted_words.append("".join(result))

    decrypted_sentence = " ".join(decrypted_words)
    return decrypted_sentence

def work(data):
    return ecry(data)

def work2(data1, key):
    return dcry(data1, key)

if __name__ == "__main__":
    start_server()
