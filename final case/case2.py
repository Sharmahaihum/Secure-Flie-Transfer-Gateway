import random as r
import gradio as  gr

def dcry(plaintext,integer_input):
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = []
    z = 1
    for i in range(len(array)):
        alpha.append((array[i], z))
        z += 1
    # Creating hehe
    sentence = plaintext
    key = integer_input
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

#file to sentence 
def file_sentence(plaintext,integer_input):
    encrypted_sentence=dcry(plaintext,integer_input)
    file_path = "output.txt"
    with open(file_path, "w") as file:
        file.write(encrypted_sentence)
    return file_path



#Gradio 
def xor_encrypt(input_file,integer_input):
    # Read 
    with open(input_file.name, 'r') as f:
        plaintext = f.read()
    output_file_name=file_sentence(plaintext,integer_input)
    #output 
    return output_file_name

def process_files(integer_input,input_file):
    if input_file is not None and integer_input is not None:
        output_file = xor_encrypt(input_file,integer_input)
        return output_file
    
def lan():
    
    iface = gr.Interface(
    fn=process_files,
    inputs=[
        gr.Number(label="Enter Integer", default=10, min=1, max=100, step=1),
        gr.File(label="Upload File")
    ],
    outputs=gr.File(label="Download Output"),
    live=True,
)

    iface.launch(share=True)
    
# Driver command line

if __name__ == "__main__":
    lan()
    
