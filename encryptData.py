from cryptography.fernet import Fernet
import rsa


def Encryption(message):
    # open the symmetric key file
    skey = open('messageKey.key', 'rb')
    key = skey.read()

    # create the cipher
    cipher = Fernet(key)

    # encrypt the data
    encrypted_data = cipher.encrypt(bytes(message, 'utf-8'))
    edata = open('EncryptedFile', 'wb')
    edata.write(encrypted_data)

    # open the public key file
    pkey = open('publicKey.key', 'rb')
    pkdata = pkey.read()

    # load the file
    pubkey = rsa.PublicKey.load_pkcs1(pkdata)

    # encrypt the symmetric key file with the public key
    encrypted_key = rsa.encrypt(key, pubkey)

    ekey = open('encryptedMessageKey', 'wb')
    ekey.write(encrypted_key)
