import socket
import gradio as gr
import random
def start_client(plaintext):
    host = '127.0.0.1'  
    port = 12345        
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = plaintext
    client_socket.send(message.encode('utf-8'))
    client_socket.close()


def ecry(data):
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = {char: idx for idx, char in enumerate(array, start=1)}
    key = 7
    encrypted_words = []
    for word in data.split():
        encrypted_word = []
        for char in word:
            if char.isalpha():
                char_lower = char.lower()
                encrypted_char = (alpha[char_lower] + key) % 26
                encrypted_word.append(array[encrypted_char - 1].upper() if char.isupper() else array[encrypted_char - 1])
            else:
                encrypted_word.append(char)
        encrypted_words.append("".join(encrypted_word))
    encrypted_sentence = " ".join(encrypted_words)
    start_client(encrypted_sentence)

    
def xor_encrypt(input_file):
    # Read 
    with open(input_file.name, 'r') as f:
        plaintext = f.read()
    ecry(plaintext)
    #output 
    output="Message deliverd Successfully"
    return output




def lan():
    iface = gr.Interface(
    fn=xor_encrypt,
    inputs="file",
    outputs=["text"],
    live=True,
    title="Secure data/file transed System",
    description="Transfer file securely"
)

    iface.launch(share=True)
    
# Driver command line

if __name__ == "__main__":
    lan()