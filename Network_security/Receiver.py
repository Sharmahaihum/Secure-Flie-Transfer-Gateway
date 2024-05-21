import gradio as gr
import socket
import hashlib
import json

def start_server():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Data received: {data}")
    data_array = json.loads(data)
    encrypted_message = data_array[0]
    received_hash = data_array[1]
    client_socket.close()
    decrypted_message = dcry(encrypted_message)
    computed_hash = verify_hash(decrypted_message)
    print("Computed Hash:", computed_hash)
    if computed_hash == received_hash:
        return decrypted_message, True
    else:
        return decrypted_message, False

def verify_hash(data):
    md_object = hashlib.sha512(data.encode("utf-8"))
    md = md_object.hexdigest()
    return md

def dcry(data1):
    array = 'abcdefghijklmnopqrstuvwxyz'
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

def xor_encrypt(inputs):
    outputdata, check = start_server()
    file_path = "output.txt"
    with open(file_path, "w") as file:
        file.write(outputdata)
    return file_path, check

def lan():
    iface = gr.Interface(
        fn=xor_encrypt,
        inputs="text",
        outputs=["file", "text"],
        live=True,
        title="Secure data/file transfer System",
        description="Transfer file securely"
    )
    iface.launch(share=True)

lan()
