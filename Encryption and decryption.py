from Crypto.Cipher import AES as AS
import hashlib


'''
PART 3
Encryption and decryption using ASE algorithm
ASE 
Encryptor
Create a function that receives a string as an argument and encrypts it using a constant key of your choice.
Write your choice of encrypting algorithm
a. The function receives a string
b. The function returns a string that has been encrypted
Decrypter
Create a function that receives an encrypted string as an argument and decrypts it using a constant key of
your choice. It should reverse the encryptor
a. The function receives a string that has been encrypted
b. The function returns a string after decrypting it.
Create a function that uses the encryptor and the function from part 1 to connect to an open port and send
an encrypted string. 
'''
#This function will genarat a key to encrypt and decrypt
def genarating_key():
    # The lenght of the password impact the key--> longger password is better
    # We need to encode it to make it to bytes
    my_secret = 'brownskingirl'.encode()
    # standart lenght key is 16/24/32
    # use hash to get the correct lenght of the key
    key = hashlib.sha3_256(my_secret).digest()
    # create the mode --> block chipher mode
    mode = AS.MODE_CBC
    # vector need to be 16b --> help to randomize the ciphertxt
    IV = "This is an IV256".encode()
    cipher = AS.new(key, mode, IV)
    return cipher

# This function will encrypt a mssagee to ciphertext
def encrypt(msg):
    cipher = genarating_key()
    cnt = 0
    org_msg = msg
    #The msg need to 16b so we will add a padding to her if it is not 16b
    while len(msg) % 16 != 0:
        msg = msg + " "
    encrypted_msg = cipher.encrypt(msg.encode())
    return encrypted_msg

# Decrypt to plaintext
def decrypt(enc_str):
    cipher = genarating_key()
    print(enc_str)
    decrypt_msg = cipher.decrypt(enc_str)

    return decrypt_msg.decode()

# In this function we encrypt the paylod and send it to tcp_flow function
def send_encrypted_message(ip,port,msg):
    enc_msg=encrypt(msg)
    #method from other project
    #tcp_flow(ip,port,enc_msg)
