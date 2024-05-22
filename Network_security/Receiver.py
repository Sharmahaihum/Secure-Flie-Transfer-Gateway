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
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = {char: idx for idx, char in enumerate(array, start=1)}
    key = 7
    decrypted_sentence = []
    for word in data1.split():
        encrypted_word = []
        for char in word:
            if char.isalpha():
                char_lower = char.lower()
                encrypted_char = (alpha[char_lower] - key) % 26
                encrypted_word.append(array[encrypted_char - 1].upper() if char.isupper() else array[encrypted_char - 1])
            else:
                encrypted_word.append(char)
        decrypted_sentence.append("".join(encrypted_word))
    decrypted_sentence = " ".join(decrypted_sentence)
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
