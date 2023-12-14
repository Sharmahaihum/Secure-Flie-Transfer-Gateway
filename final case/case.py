import random as r
import gradio as  gr
def ecry(plaintext):
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = []
    z = 1
    key = r.randrange(1,10)
    for i in range(len(array)):
        alpha.append((array[i], z))
        z += 1
    # Creating hehe
    sentence=plaintext
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
    print(encrypted_sentence)
    return encrypted_sentence,key


def dcry():
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = []
    z = 1
    for i in range(len(array)):
        alpha.append((array[i], z))
        z += 1
    # Creating hehe
    sentence = input("Enter sentence: ")
    key = int(input("Enter Key value: "))
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
def file_sentence(plaintext):
    encrypted_sentence,key=ecry(plaintext)
    file_path = "output.txt"
    with open(file_path, "w") as file:
        file.write(encrypted_sentence)
    return file_path,key



#Gradio 
def xor_encrypt(input_file):
    # Read 
    with open(input_file.name, 'r') as f:
        plaintext = f.read()
    output_file_name,key=file_sentence(plaintext)
    #output 
    return output_file_name, key

def lan():
    iface = gr.Interface(
    fn=xor_encrypt,
    inputs="file",
    outputs=["file", "text"],
    live=True,
    title="File Encryption System",
    description="Encrypt a file using XOR encryption with a random key."
)

    iface.launch(share=True)
    
# Driver command line

if __name__ == "__main__":
    lan()
    
