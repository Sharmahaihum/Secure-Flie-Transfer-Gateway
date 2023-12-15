import gradio as gr
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
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received data: {data}")
        response=work(data)
        client_socket.close()
        return response


def dcry(data1):
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = {char: idx for idx, char in enumerate(array, start=1)}
    key = 7
    decrypted_words = []
    for word in data1.split():
        decrypted_word = []
        for char in word:
            if char.isalpha():
                decrypted_char = (alpha[char] - key) % 26
                decrypted_word.append(array[decrypted_char - 1])
            else:
                decrypted_word.append(char)
        decrypted_words.append("".join(decrypted_word))
    decrypted_sentence = " ".join(decrypted_words)
    return decrypted_sentence


def work(data):
    return dcry(data)

def xor_encrypt(inputs):
    outputdata=start_server()
    #outputfile_path
    file_path = "output.txt"
    with open(file_path, "w") as file:
        file.write(outputdata)
    return file_path




def lan():
    iface = gr.Interface(
    fn=xor_encrypt,
    inputs="text",
    outputs=["file"],
    live=True,
    title="Secure data/file transed System",
    description="Transfer file securely"
    )
    iface.launch(share=True)
    
# Driver command line
lan()